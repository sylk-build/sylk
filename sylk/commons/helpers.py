# Copyright (c) 2023 sylk.build

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from collections import defaultdict
import logging
from ntpath import join
import os
import re
import subprocess
from typing import List, Literal
from sylk import __version__, config
from sylk.commons import file_system

from sylk.commons import errors, pretty
from sylk.commons.modules.google import google
from sylk.commons.protos.sylk.SylkEnum.v2 import SylkEnum_pb2
from sylk.commons.protos.sylk.SylkMessage.v2 import SylkMessage_pb2
from sylk.commons.resources import generate_package, generate_service
from sylk.commons.errors import SylkCoderError, SylkValidationError
from sylk.commons.file_system import check_if_file_exists, join_path
from sylk.commons.protos.sylk.Sylk.v2 import Sylk_pb2 as SylkCore
from sylk.commons.protos.sylk.SylkField.v1 import SylkField_pb2
from sylk.commons.protos.sylk.SylkCommons.v1 import SylkCommons_pb2

from itertools import groupby
from google.protobuf.struct_pb2 import Value
from google.protobuf.json_format import ParseDict, MessageToDict, MessageToJson
from google.protobuf import text_format, descriptor_pool, message_factory
from google.protobuf.any_pb2 import Any
from google.protobuf.timestamp_pb2 import Timestamp
from google.protobuf.descriptor_pb2 import FileDescriptorProto, DESCRIPTOR as ProtobufDescriptor

from platform import platform
from inquirer import errors as inquirerErrors

import concurrent.futures

from sylk.commons.sylk import SylkTree

log = logging.getLogger("sylk.cli.main")

_WELL_KNOWN_PY_IMPORTS = [
    "from google.protobuf.timestamp_pb2 import Timestamp",
    "from typing import Iterator",
]

_WELL_KNOWN_TS_IMPORTS = [
    "import { \n\thandleUnaryCall,\n\thandleClientStreamingCall,\n\thandleServerStreamingCall,\n\thandleBidiStreamingCall,\n\tsendUnaryData,\n\tServerDuplexStream,\n\tServerReadableStream,\n\tServerUnaryCall,\n\tServerWritableStream,\n\tstatus,\n\tUntypedHandleCall,\n\tMetadata,\n\tInterceptor,\n\tcredentials\n } from '@grpc/grpc-js';",
    "import { ServiceError } from '../../utils/error';",
    "import { ApiType } from '../../utils/interfaces';",
]

_WELL_KNOWN_TS_CLIENT_IMPORTS = [
    "import { \n\thandleUnaryCall\n\t,ClientUnaryCall\n\t,ClientReadableStream,\n\thandleClientStreamingCall,\n\thandleServerStreamingCall,\n\thandleBidiStreamingCall,\n\tsendUnaryData,\n\tServerDuplexStream,\n\tServerReadableStream,\n\tServerUnaryCall,\n\tServerWritableStream,\n\tstatus,\n\tUntypedHandleCall,\n\tMetadata,\n\tInterceptor,\n\tcredentials,\n\tChannelCredentials,\n\tServiceError as _service_error\n } from '@grpc/grpc-js';",
    "import { promisify } from 'util';",
    "import { Observable } from 'rxjs';",
]

_WELL_KNOWN_GO_IMPORTS = ['"context"', '"io"', '"google.golang.org/grpc/metadata"']

_FIELD_TYPES = Literal[
    "TYPE_UINT64",
    "TYPE_UINT32",
    "TYPE_INT32",
    "TYPE_INT64",
    "TYPE_STRING",
    "TYPE_BOOL",
    "TYPE_MESSAGE",
    "TYPE_ENUM",
    "TYPE_DOUBLE",
    "TYPE_FLOAT",
    "TYPE_BYTE",
]
_FIELD_LABELS = Literal["LABEL_OPTIONAL", "LABEL_REPEATED"]
_EXTENSIONS_TYPE = Literal[
    "FileOptions", "MessageOptions", "FieldOptions", "ServiceOptions", "MethodOptions"
]

_OPEN_BRCK = "{"
_CLOSING_BRCK = "}"


def parse_version_component(full_name: str) -> dict or None:
    full_name = full_name.replace("/", ".")
    if full_name:
        segments = full_name.split(".")

        pattern = r"^v(\d+)(alpha|beta)?(\d+)?$"

        for segment in segments:
            regex = re.compile("[@!#$%^&*()<>?/\|}{~:]")
            # Pass the string in search
            # method of regex object.
            if regex.search(segment) is not None:
                raise SylkValidationError(
                    "package", "package name cannot hold any special characters"
                )

            match = re.match(pattern, segment)

            if match:
                version = int(match.group(1))
                channel = match.group(2)
                release = int(match.group(3)) if match.group(3) else None
                return {"version": version, "channel": channel, "release": release}

        # if segments[-1][0] == "v":
        #     regex = r"^v(\d+)?$"
        #     match = re.match(regex, segments[-1])
        #     if match is None:
        #         pretty.print_warning(
        #             "seems like you tried to pass version component that is not valid -> {}\nversion component must follow these rules:\n\t- Start with a lower case 'v'\n\t- Followed by a decimal number\n\t- Optionaly can have a 'channel' from the following: 'alpha' | 'beta'\n\t- Optionaly specify 'release' with decimal number".format(
        #                 segments[-1]
        #             )
        #         )

    return None


def to_camel_case(string):
    words = re.findall(r"[A-Z]?[a-z0-9]+|[A-Z]+(?![a-z])", string)
    return words[0].lower() + "".join(word.title() for word in words[1:])


def check_if_under_project():
    return check_if_file_exists(join_path(os.getcwd(), "sylk.json"))


def SylkJsonCacheToMessage(path) -> SylkCore.SylkJson:
    data = open(path, "rb").read()  # read file as string
    msg = SylkJson()
    msg.ParseFromString(data)


def SylkJsonToMessage(sylk_json, validate: bool = False) -> SylkCore.SylkJson:
    if validate:
        pass
        # pretty.print_info("Validating sylk.json", True)
        # assert(sylk_json.get('project') is not None)
        # assert(sylk_json.get('config') is not None)
        # assert(sylk_json.get('packages') is not None)
        # assert(sylk_json.get('services') is not None)
        # for p in sylk_json.get('packages'):
        #     pkg = sylk_json.get('packages')[p]
        #     reorder = []
        #     index = 0
        #     for m in pkg.get('messages'):
        #         dependency_in_pkg = next((f for f in m.get('fields') if f.get('messageType') is not None),None)

        #         reorder.append(index)
        #         if dependency_in_pkg is not None:
        #             if pkg.get('package') in dependency_in_pkg.get('messageType'):
        #                 pretty.print_error(dependency_in_pkg)
        #                 pretty.print_info(reorder,True,"{0} / {1}".format(index,max(reorder)))
        #                 if index > max(reorder):
        #                     reorder = [x+1 for x in reorder]
        #                     reorder[index] = max(reorder) -1
        #                 else:
        #                     reorder[index] = index +1
        #             else:
        #                 if index >= reorder[index]:
        #                     reorder = [x+1 for x in reorder]

        #                 reorder[index] = index
        #         else:
        #             reorder[index] = max(reorder) +1
        #         pretty.print_info(dependency_in_pkg,True)
        #         pretty.print_info(reorder,True,"After changes")

        #         index += 1
        #     reorder = [x-1 for x in reorder]
        #     mylist = [pkg.get('messages')[i] for i in reorder]
        #     pkg['messages'] = mylist

        #     pretty.print_info(mylist,True,"Last step")
        #     sylk_json['packages'][p] = pkg
        #     pretty.print_info(sylk_json['packages'][p],True,"Package After Change step")

    return ParseDict(sylk_json, SylkCore.SylkJson())


class SylkProject:
    """sylk top level object that defines the required meta data properties."""

    def __init__(
        self,
        sylk_json_path: str,
        project_name: str,
        domain: str,
    ) -> None:
        """Parses a fields into a :module:`sylk.commons.protos.sylk_pb2.Project` representation.

        Parameters
        ----------
            sylk_json_path (str): Absoulute path of sylk JSON file.
            project_name (str): A project name, can include hyphens or
                 underscores but not blank spaces.
            domain (Str): A company domain name,
                it is not the full domain your company holds
                for e.x all `sylk.build` projects are inputed on gRPC
                as `sylk` without any suffix or prefix.
        """


class SylkField:
    """sylk field level object that defines the required meta data properties."""

    def __init__(
        self,
        name,
        type: _FIELD_TYPES,
        label: _FIELD_LABELS,
        message_type=None,
        enum_type=None,
        extensions=None,
        description=None,
        key_type=None,
        value_type=None,
        oneof_fields=[],
    ) -> None:
        """Parses a fields into a :module:`sylk.commons.protos.sylk.FieldDescriptor` representation.

        Parameters
        ----------
            name (str): A field name, `MUST` not include blank space and hyphens.
            type (:module:`sylk.commons.helpers._FIELD_TYPES`): One of the available field types.
            label (:module:`sylk.commons.helpers._FIELD_LABELS`): One of the available labels,
                `LABEL_REPEATED` - will compile generated class field as array / list type
            message_type (str): `MUST` be included when field type is `TYPE_MESSAGE` and should be
                passed as full name for the message the field represent.
            enum_type (str): Same as `message_type` field just with enums binding.
            extensions (dict): A dict value for extensions of field.
            description (str):  A field description.
        """

        self._name = name
        self._field_type = type
        self._label = label
        self._message_type = message_type
        self._enum_type = enum_type
        self._extensions = extensions
        self._description = description
        self._key_type = key_type
        self._value_type = value_type
        self._oneof_fields = oneof_fields

    def setName(self, name):
        self._name = name

    def setType(self, type):
        self._field_type = type

    def setLabel(self, label):
        self._label = label

    def setMessageType(self, message_type):
        self._message_type = message_type

    def to_dict(self):
        temp = {}
        self._validate()
        for k in dict(self.__dict__):
            if k == "_extensions":
                if dict(self.__dict__)[k] is not None:
                    temp[k[1:]] = {}
                    for j in dict(self.__dict__)[k]:
                        if isinstance(dict(self.__dict__)[k][j], str):
                            temp[k[1:]][j] = Value(
                                string_value=dict(self.__dict__)[k][j]
                            )
                        elif isinstance(dict(self.__dict__)[k][j], int) or isinstance(
                            dict(self.__dict__)[k][j], float
                        ):
                            temp[k[1:]][j] = Value(
                                number_value=dict(self.__dict__)[k][j]
                            )
                        elif isinstance(dict(self.__dict__)[k][j], bool):
                            temp[k[1:]][j] = Value(bool_value=dict(self.__dict__)[k][j])
                        else:
                            if isinstance(dict(self.__dict__)[k][j], Value):
                                temp[k[1:]][j] = dict(self.__dict__)[k][j]
                            else:
                                pretty.print_warning("Not supported extension type !")
            else:
                temp[k[1:]] = dict(self.__dict__)[k]

        return temp

    def _validate(self):
        if self._field_type == "TYPE_ENUM":
            if self._enum_type is None:
                pretty.print_error(
                    f"Field {self._name} missing enum type and is configured as 'TYPE_ENUM'"
                )
                exit(1)
        elif self._field_type == "TYPE_MESSAGE":
            if self._message_type is None:
                pretty.print_error(
                    f"Field {self._name} missing enum type and is configured as 'TYPE_MESSAGE'"
                )
                exit(1)

    @property
    def name(self):
        return self._name

    @property
    def field_type(self):
        return self._field_type

    @property
    def label(self):
        return self._label

    @property
    def message_type(self):
        return self._message_type


class SylkRPC:
    """sylk RPC level object that defines the required meta data properties."""

    def __init__(
        self,
        name,
        in_type,
        out_type,
        client_stream=False,
        server_stream=False,
        description=None,
    ) -> None:
        """Parses a fields into a :module:`sylk.commons.protos.sylk.MethodDescriptor` representation.

        Parameters
        ----------
            name (str): A RPC name, `MUST` not include blank space and hyphens.
            in_type (str): Full name for message to be used as input type for the new RPC.
            out_type (str):  Full name for message to be used as output type for the new RPC.
            client_stream (bool): If client stream is available to this RPC, Defaulted to False.
            server_stream (bool): If sever stream is available to this RPC, Defaulted to False.
            description (str): Description for the RPC mainly used for client generated docs.
        """
        self._name = name
        self._input_type = in_type
        self._output_type = out_type
        self._client_stream = client_stream
        self._server_stream = server_stream
        self._description = description

    def to_tuple(self):
        return (
            self._name,
            [
                (self._client_stream, self._input_type),
                (self._server_stream, self._output_type),
            ],
            self._description,
        )


class SylkService:
    """sylk service level object that defines the required meta data properties."""

    def __init__(
        self,
        name,
        methods: List[SylkRPC] = [],
        dependencies: List[str] = [],
        description=None,
        extensions=None,
    ) -> None:
        """Parses a fields into a :module:`sylk.commons.protos.sylk.ServiceDescriptor` representation.

        Parameters
        ----------
            name (str): A service name, `MUST` not include blank space and hyphens.
            methods (:module:`List[sylk.commons.helpers.SylkRPC]`): A list of RPC methods.
            dependencies (List[str]): List of service dependencies (Other packages).
            description (str): A service description.
        """
        self._name = name
        self._methods = methods
        self._dependencies = dependencies
        self._description = description
        self._extensions = extensions

    def to_tuple(self):
        rpcs = []
        for rpc in self._methods:
            rpcs.append(rpc.to_tuple())
        return self._name, rpcs, self._dependencies, self._description, self._extensions

    @property
    def name(self):
        return self._name


class SylkMessage:
    """sylk message level object that defines the required meta data properties."""

    def __init__(
        self,
        name,
        fields: List[SylkField] = None,
        description: str = None,
        extension_type: _EXTENSIONS_TYPE = None,
        extensions=None,
        domain=None,
    ) -> None:
        """Parses a fields into a :module:`sylk.commons.protos.sylk.Descriptor` representation.

        Parameters
        ----------
            name (str): A message name, `MUST` not include blank space and hyphens.
            fields (:module:`List[sylk.commons.helpers.SylkField]`): A list of message fields.
            description (str): A message description.
            extension_type (:module:`sylk.commons.protos.sylk.Options`): A message extension option.
        """
        self._name = name
        self._fields = fields
        self._description = description
        self._extension_type = extension_type
        self._extensions = extensions
        self._domain = domain

    def setFields(self, fields: List[SylkField]):
        self._fields = fields

    def to_tuple(self):
        if self._fields is None:
            raise SylkValidationError("Message", "Message must hold atleast 1 field !")

        f_array = []
        for f in self._fields:
            f_array.append(f.to_dict())

        return (
            self._name,
            f_array,
            self._description,
            self._extension_type,
            self._extensions,
            self._domain,
        )

    @property
    def name(self):
        return self._name


class SylkEnumValue:
    """sylk enum value level object that defines the required meta data properties."""

    def __init__(self, name: str, number: int, description: str = None) -> None:
        """Parses a fields into a :module:`sylk.commons.protos.sylk.EnumValue` representation.

        Parameters
        ----------
            name (str): A enum key.
            number (int): A enum value.
        """
        self._name = name
        self._number = number
        self._description = description

    def setName(self, name):
        self._name = name

    def setNumber(self, type):
        self._number = type

    def setDescription(self, type):
        self._description = type

    def to_dict(self):
        temp = {}
        for k in dict(self.__dict__):
            temp[k[1:]] = dict(self.__dict__)[k]
        return temp

    @property
    def name(self):
        return self._name

    @property
    def number(self):
        return self._number


class SylkEnum:
    """sylk enum level object that defines the required meta data properties."""

    def __init__(
        self,
        name,
        enum_values: List[SylkEnumValue] = [],
        description: str = "",
        domain=None,
    ) -> None:
        """Parses a fields into a :module:`sylk.commons.protos.sylk.Enum` representation.

        Parameters
        ----------
            name (str): A enum name.
            enum_values (:module:`List[sylk.commons.helpers.SylkEnumValue]`): A list of enum values.
        """
        self._name = name
        self._enum_values = enum_values
        self._description = description
        self._domain = domain

    def to_tuple(self):
        enums_values = []
        for ev in self._enum_values:
            enums_values.append(ev.to_dict())
        return self._name, enums_values, self._description, self._domain

    @property
    def name(self):
        return self._name


class SylkContext:
    def __init__(self, sylk_context):
        self._sylk_context = sylk_context
        self._parse_context()

    def _parse_context(self):
        self._files = self._sylk_context.get("files")

    def get_rpc(self, service, name):
        svc = None
        if self._files is not None and len(self._files) > 0:
            svc = next(
                (
                    svc
                    for svc in self._files
                    if svc["file"].split("/")[-1].split(".")[0] == service
                ),
                None,
            )
            if svc is not None:
                for rpc in svc["methods"]:
                    if rpc["name"] == name:
                        return rpc
            else:
                return svc

    def new_rpc(self, service, context, suffix="py"):
        file = next(
            (
                file
                for file in self._files
                if file.get("file") == f"./services/{service}.{suffix}"
            ),
            None,
        )
        if file is not None:
            file.get("methods").append(context)

    def edit_rpc(self, service, name, new_context):
        rpc = self.get_rpc(service, name)
        rpc["code"] = new_context["code"]
        rpc["type"] = new_context["type"]
        rpc["name"] = new_context["name"]

    def set_rpc_code(self, service, name, code):
        rpc = self.get_rpc(service, name)
        rpc["code"] = code
        rpc["type"] = "rpc"

    def get_functions(self, service):
        if self._files is not None:
            svc = next(
                (
                    svc
                    for svc in self._files
                    if svc["file"].split("/")[-1].split(".")[0] == service
                ),
                None,
            )
            funcs = []
            if svc is not None:
                for func in svc["methods"]:
                    if func["type"] != "rpc":
                        funcs.append(func)
                return funcs
            else:
                return svc

    def set_method_code(self, service, name, code):
        file = next((f for f in self._files if service in f["file"]), None)
        if file is not None:
            method = next((m for m in file["methods"] if m["name"] == name), None)
            if method is None:
                file["methods"].insert(0, {"name": name, "code": code, "type": "func"})
            else:
                method["code"] = code

    def dump(self):
        return self._sylk_context

    @property
    def files(self):
        return self._files


class SylkPackage:
    """sylk package level object that defines the required meta data properties."""

    def __init__(
        self,
        name,
        messages: List[SylkMessage] = [],
        enums: List[SylkEnum] = [],
        extensions=None,
        domain=None,
    ):
        """Parses a fields into a :module:`sylk.commons.protos.sylk_pb2.PackageDescriptor` representation.

        Parameters
        ----------
            name (str): A package name.
            messages (List[:module:`sylk.commons.helpers.SylkMessage`]): A list of package messages.
            enums (List[:module:`sylk.commons.helpers.SylkEnum`]): A list of package enums.
        """
        self._name = name
        self._messages = messages
        self._enums = enums
        self._extensions = extensions
        self._domain = domain

    def to_tuple(self):
        messages = []
        enums = []
        for e in self._enums:
            enums.append(e.to_tuple())
        for m in self._messages:
            messages.append(m.to_tuple())
        return self._name, messages, enums, self._extensions, self._domain

    @property
    def name(self):
        return self._name


class SylkJson:
    def __init__(self, sylk_json):
        self._sylk_json = sylk_json

        self._parse_json()
        self._parse_proto_tree()
        self._parse_protobuf_messages()

    def _parse_protobuf_messages(self):
        proto = FileDescriptorProto()
        ProtobufDescriptor.CopyToProto(proto)
        self._pb_messages = message_factory.GetMessages([proto],descriptor_pool.Default())

    def _topological_sort(self,packages):
        def dfs(package, visited, stack):
            if self.packages.get(package) is not None:
                visited.add(package)
                for dependency in [dep for dep in self.packages.get(package,{}).get('dependencies',[]) if 'google.' not in dep]:
                    if dependency not in visited and dependency not in self.packages[package].get('package'):
                        dfs(dependency.replace('.','/'), visited, stack)
                if package not in stack:
                    stack.append(package)

        visited = set()
        stack = []

        for package in packages:
            if package not in visited:
                dfs(package, visited, stack)
        return stack

    def _parse_proto_tree(self):
        self._proto_tree = SylkTree(self.domain,self.project.get('name'))
        self._proto_tree.load_module(google())

        def _process_enum(self,enum,inline:str = None):
            enm_name = enum.get('name')
            inline = f'{inline}.' if inline is not None else ''
            enm_path = pkg_path + '.' + inline + enm_name
            self._proto_tree.add_node(enm_path,'enum',enum)
            if enum.get('values') is not None:
                for v in enum.get('values'):
                    self._proto_tree.add_node(enm_path + '.' + v.get('name'),'value',v)

        def _process_msg(self, msg, inline: str = None):
            msg_name = msg.get('name')
            inline = '' if inline is None else inline+'.'
            msg_path = pkg_path + '.' + inline + msg_name
            self._proto_tree.add_node(msg_path,'message',m)
            if msg.get('inlines') is not None:
                for inline in msg.get('inlines'):
                    if inline.get('type') == 'enum':
                        _process_enum(self,inline,msg.get('name'))
                    else:
                        _process_msg(self, inline, msg.get('name'))
            if msg.get('fields') is not None:
                for f in msg.get('fields'):
                    self._proto_tree.add_node(msg_path + '.' + f.get('name'),'field',f)
                    if f.get('fieldType') == "TYPE_ENUM":
                        self._proto_tree.add_field_reference(msg_path, f.get('name'), f.get('enumType'))
                    elif f.get('fieldType') == "TYPE_MESSAGE":
                        self._proto_tree.add_field_reference(msg_path, f.get('name'), f.get('messageType'))
                    elif f.get('fieldType') == "TYPE_MAP":
                        if f.get('valueType') == "TYPE_ENUM":
                            self._proto_tree.add_field_reference(msg_path, f.get('name'), f.get('enumType'))
                        elif f.get('valueType') == "TYPE_MESSAGE":
                            self._proto_tree.add_field_reference(msg_path, f.get('name'), f.get('messageType'))
                    elif f.get('fieldType') == "TYPE_ONEOF":
                        for oneof in f.get('oneofFields'):
                            if oneof.get('fieldType') == "TYPE_ENUM":
                                self._proto_tree.add_field_reference(msg_path+'.'+f.get('name'), oneof.get('name'), oneof.get('enumType'))
                            elif oneof.get('fieldType') == "TYPE_MESSAGE":
                                self._proto_tree.add_field_reference(msg_path+'.'+f.get('name'), oneof.get('name'), oneof.get('messageType'))

        if self.packages is not None:
            for pkg in self._topological_sort(self.packages):
                p = self.packages[pkg]
                pkg_path = p.get('package')
                self._proto_tree.add_node(pkg_path,'package',p)

                if p.get('enums') is not None:
                    for e in p.get('enums'):
                        _process_enum(self,e)
                if p.get('messages') is not None:
                    sorted = self._proto_tree.resolve_dependency_order(p.get('messages'))
                    for m in sorted:
                        _process_msg(self,m)
                        
                if p.get('services') is not None:
                    for s in p.get('services'):
                        svc_name = s.get('name')
                        svc_path = pkg_path + '.' + svc_name
                        self._proto_tree.add_node(svc_path,'service',s)
                        if s.get('methods') is not None:
                            for r in s.get('methods'):
                                self._proto_tree.add_node(svc_path + '.' + r.get('name'),'method',r)
                                self._proto_tree.add_method_reference(svc_path + '.' + r.get('name'), r.get('inputType'))
                                self._proto_tree.add_method_reference(svc_path + '.' + r.get('name'), r.get('outputType'))


    def _parse_json(self):
        self._organization = self._sylk_json.get("organization")
        self._domain = (
            self._organization.get("domain")
            if self._organization is not None
            and self._organization.get("domain") is not None
            else "sylk"
        )
        self._config = self._sylk_json.get("configs")
        self._root_protos = self._config.get("protoBasePath")
        self._project = self._sylk_json.get("project")
        self._packages = self._sylk_json.get("packages")
        self._services = self.flat_services()
        self._path = self._sylk_json.get("project").get("uri")
        self._sylk_version = self._sylk_json.get("sylkVersion")

    def flat_services(self):
        temp_services = []
        if self.packages:
            for p in self.packages:
                pkg = self.packages[p]
                if pkg.get("services"):
                    for s in pkg.get("services"):
                        temp_services.append(s)
        return temp_services

    def get_service(self, full_name, json=True):
        name = full_name.split(".")[-1]
        if json:
            try:
                pkg = self.get_package(".".join(full_name.split(".")[:-1]), json)
                filtered_svc = [s for s in pkg["services"] if s.get("name") == name]
                return filtered_svc[0] if filtered_svc else None
            except Exception:
                return None
        else:
            pkg = self.get_package(".".join(full_name.split(".")[:-1]))
            filtered_svc = [s for s in pkg["services"] if s.get("name") == name]
            if filtered_svc:
                svc = filtered_svc[0]
                depend = svc.get("dependencies")
                description = svc.get("description")
                methods = svc.get("methods")
                extensions = svc.get("extensions")
                return generate_service(
                    self.path,
                    full_name,
                    self.get_server_language(),
                    depend if depend is not None else [],
                    description,
                    methods if methods is not None else [],
                    extensions=extensions,
                    sylk_json=self._sylk_json,
                )
            else:
                return None

    def get_path(self, full_name, tag: str = None):
        paths = "/".join(full_name.split("."))
        temp_path = f"{self._root_protos}/{paths}"
        if (
            self._packages.get(temp_path)
            is not None
            # or self.get_service().get(temp_path) is not None
        ):
            return temp_path
        else:
            raise SylkValidationError(
                "Resource",
                "Sylk Resource Path {} not found.".format(
                    temp_path,
                ),
            )

    def get_package(self, full_name, json=True):
        ver = parse_version_component(full_name=full_name)
        pkg_path = "/".join(full_name.split("."))
        if json:
            if self._packages.get(pkg_path) is None:
                raise SylkValidationError(
                    "Package", "Sylk Package {} not found".format(full_name)
                )
            else:
                return self._packages[pkg_path]
        else:

            pkg = self._packages.get(pkg_path)
            if pkg is not None:
                depend = pkg.get("dependencies")
                msgs = pkg.get("messages")
                enums = pkg.get("enums")
                services = pkg.get("services")
                return generate_package(
                    self.path,
                    pkg.get("package"),
                    dependencies=depend if depend is not None else [],
                    messages=msgs if msgs is not None else [],
                    enums=enums if enums is not None else [],
                    services=services if services is not None else [],
                    sylk_json=self,
                    version=ver,
                    extensions=pkg.get('extensions')
                )
            else:
                raise SylkValidationError(
                    "package",
                    "package '{}' is not found under '{}' project".format(
                        pkg_path, self.project.get("name")
                    ),
                )

    def get_enum(self, full_name):
        parent = self._resolve_path_backwards(full_name)
        enums = parent.get("enums") if parent.get("enums") is not None else []
        if len(enums) > 0:
            return next(
                (m for m in enums if m["name"] == full_name.split(".")[-1]), None
            )
        else:
            return None

    def _resolve_path_backwards(self, path):
        parts = path.split(".")
        current_path = ""
        for i in range(len(parts), 0, -1):
            current_path = ".".join(parts[:i])
            current_full_path = current_path.replace(".", "/")
            if current_full_path in self._packages:
                return self._packages[current_full_path]
        return None

    def get_well_known_message(self, key):
        if key == "google.protobuf.MessageOptions":
            return {
                "fullName": key,
                "name": key.split(".")[-1],
                "fields": [
                    {
                        "name": "message_set_wire_format",
                        "index": 1,
                        "fieldType": "TYPE_BOOL",
                        "label": "LABEL_OPTIONAL",
                    },
                    {
                        "name": "no_standard_descriptor_accessor",
                        "index": 2,
                        "fieldType": "TYPE_BOOL",
                        "label": "LABEL_OPTIONAL",
                    },
                    {
                        "name": "deprecated",
                        "index": 3,
                        "fieldType": "TYPE_BOOL",
                        "label": "LABEL_OPTIONAL",
                    },
                ],
            }

    def get_message(self, full_name):
        parent = self._resolve_path_backwards(full_name)
        if parent is not None:
            msgs = parent.get("messages") if parent.get("messages") is not None else []
            if len(msgs) > 0:
                return next(
                    (m for m in msgs if m["name"] == full_name.split(".")[-1]), None
                )
        return None

    def get_rpc(self, full_name):
        svc = [s for s in self.services if s["fullName"] == full_name]
        if svc:
            rpcs = svc[0].get("methods")
            if rpcs is not None:
                return next(
                    (r for r in rpcs if r["name"] == full_name.split(".")[-1]), None
                )
        return None

    def get_server_language(self):
        return self.project.get("server").get("language").lower()

    def get_extensions(
        self,
        extensions_type: Literal[
            "FieldOptions",
            "MessageOptions",
            "ServiceOptions",
            "FileOptions",
            "MethodOptions",
        ] = None,
    ):
        extensions = []
        if self.packages is not None:
            for p in self.packages:
                pkg = self.packages[p]
                msgs = pkg.get("messages")
                if msgs is not None:
                    for m in msgs:
                        ext_type = m.get("extensionType")
                        if ext_type is not None:
                            if (
                                extensions_type is not None
                                and extensions_type == ext_type
                            ):
                                extensions.append(m)
                            else:
                                extensions.append(m)
        return extensions

    def get_extended_fields(self, message_full_name: str):
        """This function should be used when trying to iterate a specific message fields options

        Args
        ----
            message_full_name - Full valid name for the message we want to get fields that are extended

        Returns
        -------
            A list of fields under passed message that holds an extension value
        """
        list_fields = None
        temp_msg = self.get_message(message_full_name)

        if temp_msg is not None:
            list_fields = [
                f for f in temp_msg.get("fields") if f.get("extensions") is not None
            ]

        return list_fields

    def get_extended_messages(self, package: str, extension: str = None):
        """This function should be used when trying to iterate a specific package message options

        Args
        ----
            package - valid name for the package we want to get fields that are extended
            extension - Optional full name that filter the message extension accordingly must be the extension message full name

        Returns
        -------
            A list of messages under passed package that holds an extension value
        """
        list_msgs = None
        temp_pkg = self.get_package(package)

        if temp_pkg is not None:
            if temp_pkg.get("messages") is not None:
                list_msgs = [
                    m
                    for m in temp_pkg.get("messages")
                    if m.get("extensions") is not None
                    and (
                        extension in m.get("extensions")
                        if extension is not None
                        else True
                    )
                ]

        return list_msgs

    def get_extended_services(self, extension: str = None):
        """This function should be used when trying to iterate a specific service options

        Args
        ----
            extension - Optional full name that filter the message extension accordingly must be the extension message full name

        Returns
        -------
            A list of services under the whole project that holds an extension value
        """
        list_pkgs = []

        for svc in self.services:
            temp_pkg = self.services[svc]

            if temp_pkg.get("extensions") is not None:
                if extension is not None:
                    if extension in temp_pkg.get("extensions"):
                        list_pkgs.append(temp_pkg)
                else:
                    list_pkgs.append(temp_pkg)

        return list_pkgs

    def get_extended_packages(self, extension: str = None):
        """This function should be used when trying to iterate a specific package message options

        Args
        ----
            extension - Optional full name that filter the message extension accordingly must be the extension message full name

        Returns
        -------
            A list of packages under the whole project that holds an extension value
        """
        list_pkgs = []

        for p in self.packages:
            temp_pkg = self.packages[p]

            if temp_pkg.get("extensions") is not None:
                if extension is not None:
                    if extension in temp_pkg.get("extensions"):
                        list_pkgs.append(temp_pkg)
                else:
                    list_pkgs.append(temp_pkg)

        return list_pkgs

    def is_language(self, language: str):
        if self.project.get("server").get("language") == language:
            return True
        else:
            for c in list(
                map(lambda c: c.get("language"), self.project.get("clients"))
            ):
                if c == language:
                    return True

        return False

    def get_service_dependencies(self, service):
        deps = []
        service_node = self._proto_tree._find_node(service,self._proto_tree.root)
        svc_deps = [ref for ref in self._proto_tree.get_references(service)]
        files = self._proto_tree._get_file_paths(svc_deps)
        for f in files:
            if service_node.properties.get('tag') != f.split('/')[-1].split('.')[0]:
                deps.append(f'import "{f}";')
        return deps

    def get_message_dependencies(self, message_name):
        deps = []
        if "google.protobuf." in message_name:
            for t, msgs in _WellMap:
                if message_name.split(".")[-1] in msgs:
                    import_path = 'import "google/protobuf/{}.proto";'.format(t)
                    deps.append(import_path)
                    break
        else:
            refs = self._proto_tree.get_references(message_name)
            files = self._proto_tree._get_file_paths(refs)
            for f in files:
                import_path = 'import "{}";'.format(
                    f
                )
                deps.append(import_path)
            # print(message_name,refs,'->',files)
            # msg = self.get_message(message_name)
            # pkg = self._resolve_path_backwards(message_name)
            # for f in msg.get("fields"):
            #     if f.get("fieldType") == "TYPE_MESSAGE":
            #         dep_msg = self.get_message(f.get("messageType"))
            #         if pkg.get("package") not in f.get("messageType"):
            #             dep_pkg = self._resolve_path_backwards(f.get("messageType"))
            #             if pkg.get("package") not in f.get("messageType") or (
            #                 dep_msg.get("tag") is not None
            #                 and dep_msg.get("tag") != msg.get("tag")
            #             ):
            #                 file_name = (
            #                     dep_msg.get("tag")
            #                     if dep_msg.get("tag") is not None
            #                     else dep_pkg.get("name")
            #                 )
            #                 import_path = 'import "{}/{}.proto";'.format(
            #                     dep_pkg.get("package").replace(".", "/"), file_name
            #                 )
            #                 if import_path not in deps:
            #                     deps.append(import_path)
            #         elif dep_msg.get("tag") != msg.get("tag"):
            #             file_name = (
            #                 dep_msg.get("tag")
            #                 if dep_msg.get("tag") is not None
            #                 else pkg.get("name")
            #             )
            #             import_path = 'import "{}/{}.proto";'.format(
            #                 pkg.get("package").replace(".", "/"), file_name
            #             )
            #             if import_path not in deps:
            #                 deps.append(import_path)
            #     if f.get("fieldType") == "TYPE_ENUM":
            #         dep_enm = self.get_enum(f.get("enumType"))
            #         if pkg.get("package") not in f.get("enumType"):
            #             dep_pkg = self._resolve_path_backwards(f.get("enumType"))
            #             if pkg.get("package") not in f.get("enumType") or (
            #                 dep_enm.get("tag") is not None
            #                 and dep_enm.get("tag") != msg.get("tag")
            #             ):
            #                 file_name = (
            #                     dep_enm.get("tag")
            #                     if dep_enm.get("tag") is not None
            #                     else dep_pkg.get("name")
            #                 )
            #                 import_path = 'import "{}/{}.proto";'.format(
            #                     dep_pkg.get("package").replace(".", "/"), file_name
            #                 )
            #                 if import_path not in deps:
            #                     deps.append(import_path)
            #         elif dep_enm.get("tag") != msg.get("tag"):
            #             file_name = (
            #                 dep_enm.get("tag")
            #                 if dep_enm.get("tag") is not None
            #                 else pkg.get("name")
            #             )
            #             import_path = 'import "{}/{}.proto";'.format(
            #                 pkg.get("package").replace(".", "/"), file_name
            #             )
            #             if import_path not in deps:
            #                 deps.append(import_path)
        return deps

    @property
    def code_base_path(self):
        return self._config.get('codeBasePath') if self._config.get('codeBasePath') is not None else ''

    @property
    def domain(self):
        """str: Project domain."""
        return self._domain

    @property
    def project(self):
        """:obj:`dict` Project dictionary."""
        return self._project

    @property
    def services(self):
        """:obj:`List[dict]` Project domain."""
        return self._services

    @property
    def packages(self):
        return self._packages

    @property
    def path(self):
        return self._path

    @property
    def sylk_version(self):
        return self._sylk_version


def load_sylk_json(path: str):
    SYLK_JSON = file_system.rFile(path, json=True)
    SYLK_JSON = SylkJson(sylk_json=SYLK_JSON)
    return SYLK_JSON


def proto_struct_to_dict(proto_struct):
    result = {}
    for key, value in proto_struct.fields.items():
        if value.HasField("null_value"):
            result[key] = None
        elif value.HasField("number_value"):
            result[key] = value.number_value
        elif value.HasField("string_value"):
            result[key] = value.string_value
        elif value.HasField("bool_value"):
            result[key] = bool(value.bool_value)
        elif value.HasField("struct_value"):
            result[key] = proto_struct_to_dict(value.struct_value)
        elif value.HasField("list_value"):
            result[key] = [proto_struct_to_dict(v) if v.HasField("struct_value") else v for v in value.list_value.values]
    return result

def to_snake_case(s):
    # Insert an underscore before all uppercase letters, then make lowercase
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', s)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class SylkProtoFile:
    def __init__(self, file_name, package, sylk_json: SylkJson = None, is_tag: bool = False) -> None:
        self._file_name = file_name
        self._package = package
        self._is_tag = is_tag
        self._sylk_json = sylk_json
        self._file_path = self._set_file_path()

    def _set_file_path(self):
        pkg_path = self._package.package.replace(".", "/")
        return f"{file_system.join_path(self._sylk_json.path, self._sylk_json._root_protos, pkg_path, self._file_name)}.proto"

    def write_license(self):
        if self._sylk_json._config.get('license') is not None:
            return f"{self._sylk_json._config.get('license')}\n"
        
        else:
            return ''


    def get_metadata(self):
        pkg_path = self._package.package.replace(".", "/")
        base_protos = self._sylk_json._root_protos +'/' if self._sylk_json._root_protos is not None and self._sylk_json._root_protos != '' else ''
        file_ver = parse_version_component(self._package.package.split('.')[-1])
        if file_ver is not None:
            file_ver = f";{self._package.name}v{file_ver.get('version')}{file_ver.get('channel') if file_ver.get('channel') is not None else ''}{file_ver.get('release') if file_ver.get('release') is not None else ''}"
        else:
            file_ver = ''

        metadata = []
        # Workaround for weave command integration: We check if 'goPackage' option is existing on project level
        # If its not and the project uses go we must verify that the override of goPackage option is existing
        # On the package level as an extension
        must_override_go = False
        if self._sylk_json.is_language("go") and self._sylk_json.project.get('goPackage') is None:
            must_override_go = True
        for k in self._package.extensions.keys():
            # TODO move to a defind protobuf message
            if k == 'files':
                d = proto_struct_to_dict(self._package.extensions[k])
                for file_name in d.keys():
                    if file_name == self._file_name:
                        # Check if goPackage must be provided within the extensions
                        if must_override_go and 'goPackage' not in d[file_name].keys():
                            raise errors.SylkProtoError("Must define go_package option on proto file, it seems like you using go in your project but havent specified a project level package")
                        elif 'goPackage' not in d[file_name].keys() and self._sylk_json.is_language("go"):
                            metadata.append('option go_package = "{}/{}services/{}{}{}";'.format(
                                self._sylk_json.project.get('goPackage'),
                                self._sylk_json.code_base_path + '/' if self._sylk_json.code_base_path is not None and self._sylk_json.code_base_path != '' else '',
                                base_protos,
                                pkg_path,
                                file_ver
                            ))
                        for file_opt in d[file_name]:
                            metadata.append('option {} = "{}";'.format(to_snake_case(file_opt), d[file_name][file_opt]))
        
        # Forcing the existance of goPackage when go is in use at the project
        if self._sylk_json.is_language("go") and len(metadata) == 0:
            metadata.append('option go_package = "{}/{}services/{}{}{}";'.format(
                self._sylk_json.project.get('goPackage'),
                self._sylk_json.code_base_path + '/' if self._sylk_json.code_base_path is not None else '',
                base_protos,
                pkg_path,
                file_ver
            ))
        metadata = '\n'.join(metadata)
        # go_package = f'\noption go_package = "{self._sylk_json.project.get("goPackage")}/services/{base_protos}{pkg_path}{file_ver}";' if self._sylk_json.project.get("goPackage") is not None else ''
        return "\npackage {};\n\n{}".format(self._package.package,metadata)

    def get_imports(self):
        dependencies = []
        # print(self._file_path)
        current_file_path = self._file_path.split(join_path(self._sylk_json.path,self._sylk_json._root_protos))[1]
        if self._file_name != self._package.name or self._is_tag == True:
            refs = []
            msgs = [m.full_name for m in self._package.messages if m.tag == self._file_name]
            enms = [e.full_name for e in self._package.enums if e.tag == self._file_name]
            svcs = [s.full_name for s in self._package.services if s.tag == self._file_name]
            refs = msgs + enms + svcs
            file_refs = []
            for m in msgs:
                deps = self._sylk_json.get_message_dependencies(m)
                for d in deps:
                    if d not in dependencies and current_file_path.lstrip('/') not in d:
                        dependencies.append(d)
            for s in svcs:
                deps = self._sylk_json.get_service_dependencies(s)
                for d in deps:
                    if d not in dependencies and  current_file_path.lstrip('/') not in d:
                        dependencies.append(d)
            # for i in refs:
            #     references = self._sylk_json._proto_tree.get_references(i)
            #     for r in references:
            #         if r not in file_refs:
            #             file_refs.append(r)
            # files = self._sylk_json._proto_tree._get_file_paths(file_refs)
            # for f in files:
            #     # current_file = self._package.package.replace('.','/') + '/' + self._file_name + '.proto'
            #     imp_path = f'import "{f}";'
            #     if imp_path not in dependencies and f != current_file_path:
            #         dependencies.append(imp_path)
             
            # for m in msgs:
            #     deps = self._sylk_json.get_message_dependencies(m.full_name)
            #     for d in deps:
            #         if d not in dependencies:
            #             dependencies.append(d)
            # for s in svcs:
            #     deps = self._sylk_json.get_service_dependencies(s)
            #     for d in deps:
            #         if d not in dependencies:
            #             dependencies.append(d)

        else:
            msgs = [m.full_name for m in self._package.messages if m.tag == "" or m.tag == self._file_name]
            enms = [e.full_name for e in self._package.enums if e.tag == "" or e.tag == self._file_name]
            svcs = [s.full_name for s in self._package.services if s.tag == "" or s.tag == self._file_name]
            
            for m in msgs:
                deps = self._sylk_json.get_message_dependencies(m)
                for d in deps:
                    if d not in dependencies and current_file_path.lstrip('/') not in d:
                        dependencies.append(d)
            for s in svcs:
                deps = self._sylk_json.get_service_dependencies(s)
                for d in deps:
                    if d not in dependencies and  current_file_path.lstrip('/') not in d:
                        dependencies.append(d)

        return "\n\n" + "\n".join(dependencies) if len(dependencies) > 0 else ""

    def get_services(self):
        temp_svcs = []
        if self._file_name != self._package.name:
            svcs = [s for s in self._package.services if s.tag == self._file_name]
        else:
            svcs = [s for s in self._package.services if s.tag == "" or s.tag == self._file_name]
        
        for s in svcs:
            methods = []
            for rpc in s.methods:
                in_stream = "stream " if rpc.client_streaming == True else ""
                out_stream = "stream " if rpc.server_streaming == True else ""
                format_desc =  rpc.description.split('\n') if rpc.description.split('\n')[-1]!='' else rpc.description.split('\n')[:-1]
                if format_desc is not None and len(format_desc) > 0:
                    methods.append("\t// {}".format('// '.join(format_desc)))
                methods.append(
                    "\trpc {} ({}{}) returns ({}{});".format(
                        rpc.name, in_stream, rpc.input_type, out_stream, rpc.output_type
                    )
                )
            methods = "\n".join(methods)

            format_desc =  s.description.split('\n') if s.description.split('\n')[-1]!='' else s.description.split('\n')[:-1]
            if format_desc is not None and len(format_desc) > 0:
                temp_svcs.append("// {}".format('// '.join(format_desc)))
            temp_svcs.append(
                "service {0} {2}\n{1}\n{3}".format(
                    s.name, methods, _OPEN_BRCK, _CLOSING_BRCK
                )
            )
        return "\n\n" + "\n".join(temp_svcs) if len(temp_svcs) > 0 else ""

    def get_messages(self):
        temp_msgs = []

        def _process_field(self,f,inline=False):
            inline_fields = []

            field_label = (
                ""
                if (
                    f.label == SylkField_pb2.LABEL_OPTIONAL
                    or f.label == SylkField_pb2.DEFAULT_SYLKFIELDLABELS
                )
                else "repeated "
            )
            field_type = (
                SylkField_pb2.SylkFieldTypes.Name(f.field_type)
                .split("_")[1]
                .lower()
                if f.field_type
                not in [
                    SylkField_pb2.TYPE_MESSAGE,
                    SylkField_pb2.TYPE_ENUM,
                    SylkField_pb2.TYPE_MAP,
                    SylkField_pb2.TYPE_ONEOF,
                ]
                else f.message_type
                if f.field_type == SylkField_pb2.TYPE_MESSAGE
                else f.enum_type
                if f.field_type == SylkField_pb2.TYPE_ENUM
                else "map<{}, {}>".format(
                    SylkField_pb2.SylkFieldTypes.Name(f.key_type)
                    .split("_")[1]
                    .lower(),
                    SylkField_pb2.SylkFieldTypes.Name(f.value_type)
                    .split("_")[1]
                    .lower()
                    if f.value_type
                    not in [SylkField_pb2.TYPE_MESSAGE, SylkField_pb2.TYPE_ENUM]
                    else f.message_type
                    if f.value_type == SylkField_pb2.TYPE_MESSAGE
                    else f.enum_type,
                )
                if f.field_type == SylkField_pb2.TYPE_MAP
                else "oneof"
            )

            field_extensions = ""
            field_opts = []
            if f.extensions is not None:
                for ext in f.extensions:
                    ext_data = proto_struct_to_dict(f.extensions.get(ext))
                    for k in ext_data:
                        val = ext_data[k]
                        if isinstance(val, (bool)):
                            if val:
                                val = "true"
                            else:
                                val = "false"
                        field_opts.append(f"{k} = {val}")

            field_opts = ',\n\t\t'.join(field_opts)
            format_desc =  f.description.split('\n') if f.description.split('\n')[-1]!='' else f.description.split('\n')[:-1]
            if inline == False and len(format_desc)>0:
                fields.append(
                    "\t// {}".format(
                        '\n\t//'.join(format_desc)
                    )
                )
            elif len(format_desc)>0:
                inline_fields.append(
                    "\t// {}".format(
                       '\n\t//'.join(format_desc)
                    )
                )

            if f.field_type == SylkField_pb2.TYPE_ONEOF:
                oneofs = []
                for oneof in f.oneof_fields:

                    oneof_field_type = (
                        SylkField_pb2.SylkFieldTypes.Name(oneof.field_type)
                        .split("_")[1]
                        .lower()
                        if oneof.field_type
                        not in [
                            SylkField_pb2.TYPE_MESSAGE,
                            SylkField_pb2.TYPE_ENUM,
                        ]
                        else oneof.message_type
                        if oneof.field_type == SylkField_pb2.TYPE_MESSAGE
                        else oneof.enum_type
                        if oneof.field_type == SylkField_pb2.TYPE_ENUM
                        else "map<{}, {}>".format(
                            SylkField_pb2.SylkFieldTypes.Name(oneof.key_type)
                            .split("_")[1]
                            .lower(),
                            SylkField_pb2.SylkFieldTypes.Name(oneof.value_type)
                            .split("_")[1]
                            .lower()
                            if oneof.value_type
                            not in [SylkField_pb2.TYPE_MESSAGE, SylkField_pb2.TYPE_ENUM]
                            else oneof.message_type
                            if oneof.value_type == SylkField_pb2.TYPE_MESSAGE
                            else oneof.enum_type,
                        )
                        if oneof.field_type == SylkField_pb2.TYPE_MAP
                        else "NONE"
                    )
                    oneof_field_extensions = ""
                    format_desc = oneof.description.split('\n') if oneof.description.split('\n')[-1]!='' else oneof.description.split('\n')[:-1]
                    if format_desc is not None and len(format_desc) > 0:
                        oneofs.append(
                            "{}\t\t// {}".format(
                                '\t' if inline == True else '' , '\n\t\t//'.join(format_desc)
                            )
                        )
                    oneofs.append(
                        "{}\t\t{} {} = {}{};".format(
                           '\t' if inline == True else '' ,oneof_field_type, oneof.name, oneof.index, oneof_field_extensions
                        )
                    )
                    field_extensions = '{\n'+'\n'.join(oneofs)+'\n\t}'
                if inline == False:
                    fields.append(
                        "\t{} {} {};".format(
                            field_type, f.name, field_extensions
                        )
                    )
                else:
                    inline_fields.append(
                        "\t{} {} {};".format(
                            field_type, f.name, field_extensions
                        )
                    )
            else:
                if len(field_opts)>0:
                    field_extensions = f" [{field_opts}]"

                if inline == False:
                    fields.append(
                       "\t{}{} {} = {}{};".format(
                        field_label, field_type, f.name, f.index, field_extensions
                        )
                    )
                else:
                    inline_fields.append(
                        "\t{}{} {} = {}{};".format(
                        field_label, field_type, f.name, f.index, field_extensions
                        )
                    )
            return inline_fields

        def _process_inline(self, inline, temp_inlines,level=1):
            if 'SylkMessage' in inline.type_url:
                msg = SylkMessage_pb2.SylkMessage()
                inline.Unpack(msg)
                inline_fields = []
                for f in msg.fields:
                    inline_fields = inline_fields + _process_field(self,f,True)
                format_desc =  msg.description.split('\n') if msg.description.split('\n')[-1]!='' else msg.description.split('\n')[:-1]
                if format_desc is not None and len(format_desc) > 0:
                    temp_inlines.append("\n{}// {}".format('\t'*level,'\n//'.join(format_desc)))
                nested_inline_tmp = []
                for nested_inline in msg.inlines:
                   _process_inline(self,nested_inline,nested_inline_tmp,level+1)
                temp_inlines.append(
                    "{6}message {0} {3}{1}\n{6}{2}\n{6}{4}\n".format(
                        msg.name, '\n'+"\n".join(nested_inline_tmp) if len(nested_inline_tmp) >0 else '' ,"\n".join(inline_fields), _OPEN_BRCK, _CLOSING_BRCK, msg.full_name,'\t'* level
                    )
                )
            else:
                enm = SylkEnum_pb2.SylkEnum()
                inline.Unpack(enm)
                values = "\n\t".join(self._process_enum(enm))
                format_desc =  enm.description.split('\n') if enm.description.split('\n')[-1]!='' else enm.description.split('\n')[:-1]
                if format_desc is not None and len(format_desc) > 0:
                    temp_inlines.append("\n{}// {}".format('\t'*level,'\n//'.join(format_desc)))
                temp_inlines.append(
                    "{5}enum {0} {2}\n{5}{1}\n{5}{3}\n".format(
                        enm.name, values, _OPEN_BRCK, _CLOSING_BRCK, enm.full_name, '\t'*level
                    )
                )
            return temp_inlines

        if self._file_name != self._package.name or self._is_tag == True:
            msgs = [m for m in self._package.messages if m.tag == self._file_name]
        else:
            msgs = [m for m in self._package.messages if m.tag == "" or m.tag == self._file_name]
        for m in msgs:
            fields = []
            temp_inlines = []
            for inline in m.inlines:
                temp_inlines=_process_inline(self,inline,temp_inlines)

            for f in m.fields:
                _process_field(self,f)
            temp_inlines = "\n".join(temp_inlines)
            fields = "\n".join(fields)
            format_desc =  m.description.split('\n') if m.description.split('\n')[-1]!='' else m.description.split('\n')[:-1]
            if format_desc is not None and len(format_desc) > 0:
                temp_msgs.append("\n// {}".format('\n//'.join(format_desc)))
            else:
                temp_msgs.append("")

            msg_opts = []
            
            if m.extensions is not None:
                for ext in m.extensions:
                    pb_message = self._sylk_json._pb_messages.get(ext)
                    ext_data = proto_struct_to_dict(m.extensions.get(ext))
                    for k in ext_data:
                        if pb_message:
                            ext_field = next((f for f in pb_message.DESCRIPTOR.fields if f.name == k),None)

                        val = ext_data[k]
                        if isinstance(val, (bool)):
                            if val:
                                val = "true"
                            else:
                                val = "false"
                        msg_opts.append(f"\toption {k} = {val};\n")

            msg_opts = '\n'+''.join(msg_opts)
            temp_msgs.append(
                "message {0} {4}{1}{2}\n{3}\n{5}".format(
                    m.name, msg_opts, temp_inlines, fields, _OPEN_BRCK, _CLOSING_BRCK
                )
            )
        return "\n" + "\n".join(temp_msgs) if len(temp_msgs) > 0 else ""
    
    def _process_enum(self,e):
        values = []
        for v in sorted(e.values, key=lambda x: x.number):
            format_desc =  v.description.split('\n') if v.description.split('\n')[-1]!='' else v.description.split('\n')[:-1]
            if format_desc is not None and len(format_desc) > 0:
                values.append('\t// {}'.format('// '.join(format_desc)))
            values.append('\t{} = {};'.format(v.name, v.number))
        return values
    
    def get_enums(self):
        temp_enums = []
        if self._file_name != self._package.name or self._is_tag == True:
            enums = [e for e in self._package.enums if e.tag == self._file_name]
        else:
            enums = [e for e in self._package.enums if e.tag == "" or e.tag == self._file_name]
        for e in enums:
            values = "\n".join(self._process_enum(e))
            format_desc =  e.description.split('\n') if e.description.split('\n')[-1]!='' else e.description.split('\n')[:-1]
            if format_desc is not None and len(format_desc) > 0:
                temp_enums.append("\n// {}".format('\n//'.join(format_desc)))    
            else:
                temp_enums.append("")
            temp_enums.append(
                "enum {0} {2}\n{1}\n{3}".format(
                    e.name, values, _OPEN_BRCK, _CLOSING_BRCK
                )
            )
        return "\n\n" + "\n".join(temp_enums) if len(temp_enums) > 0 else ""

    def to_str(self):
        return f'{self.write_license()}// Generated by sylk.build\nsyntax = "proto3";\n{self.get_metadata()}{self.get_imports()}{self.get_services()}{self.get_messages()}{self.get_enums()}'


class SylkProto:
    def __init__(
        self,
        name,
        imports=[],
        package=None,
        services=[],
        messages=[],
        enums=[],
        description=None,
        extensions=None,
        sylk_json: SylkJson = None,
        tags=None,
    ):
        self._name = name
        self._imports = imports
        self._package = package
        self._messages = messages
        self._enums = enums
        self._services = services
        self._description = description
        self._extensions = extensions
        self._sylk_json = sylk_json
        self._tags = tags
        self._files = []

    def write_files(self):
        self.generate_files()
        for path, content in self._files:
            file_system.wFile(
                file_system.join_path(
                    self._sylk_json.path, self._sylk_json._root_protos, path
                ),
                content,
                True,
                False,
                True,
            )

    def write_imports(self, tag=None):
        temp_imports = []
        if tag is None:
            tag = ""
        svcs = [s for s in self._services if s.tag == tag]
        msgs = [m for m in self._messages if m.tag == tag]
        enms = [e for e in self._enums if e.tag == tag]
        for svc in svcs:
            for rpc in svc.methods:
                if self._package not in rpc.input_type or rpc.input_type in [
                    m.full_name for m in self._messages if m.tag != tag
                ]:
                    msg = self._sylk_json.get_message(rpc.input_type)
                    pkg = self._sylk_json._resolve_path_backwards(rpc.input_type)
                    imp_path = "/".join(pkg.get("package").split("."))
                    imp_file = (
                        pkg.get("name") if msg.get("tag") is None else pkg.get("name")
                    )
                    temp_imports.append(f'\nimport "{imp_path}/{imp_file}.proto";')
                if self._package not in rpc.output_type or rpc.output_type in [
                    m.full_name for m in self._messages if m.tag != tag
                ]:
                    msg = self._sylk_json.get_message(rpc.output_type)
                    pkg = self._sylk_json._resolve_path_backwards(rpc.output_type)
                    imp_path = "/".join(pkg.get("package").split("."))
                    imp_file = (
                        pkg.get("name") if msg.get("tag") is None else pkg.get("name")
                    )
                    if f'\nimport "{imp_path}/{imp_file}.proto";' not in temp_imports:
                        temp_imports.append(f'\nimport "{imp_path}/{imp_file}.proto";')
        for msg in msgs:
            # Message fields
            for f in [
                f
                for f in msg.fields
                if f.field_type == SylkField_pb2.SylkFieldTypes.TYPE_MESSAGE
            ]:
                if self._package not in f.message_type or f.message_type in [
                    m.full_name for m in self._messages if m.tag != tag
                ]:
                    msg = self._sylk_json.get_message(rpc.input_type)
                    pkg = self._sylk_json._resolve_path_backwards(rpc.input_type)
                    imp_path = "/".join(pkg.get("package").split("."))
                    imp_file = (
                        pkg.get("name") if msg.get("tag") is None else pkg.get("name")
                    )
                    temp_imports.append(f'\nimport "{imp_path}/{imp_file}.proto";')
                if self._package not in rpc.output_type or rpc.output_type in [
                    m.full_name for m in self._messages if m.tag != tag
                ]:
                    msg = self._sylk_json.get_message(rpc.output_type)
                    pkg = self._sylk_json._resolve_path_backwards(rpc.output_type)
                    imp_path = "/".join(pkg.get("package").split("."))
                    imp_file = (
                        pkg.get("name") if msg.get("tag") is None else pkg.get("name")
                    )
                    if f'\nimport "{imp_path}/{imp_file}.proto";' not in temp_imports:
                        temp_imports.append(f'\nimport "{imp_path}/{imp_file}.proto";')

        if self._imports is not None:
            for imp in self._imports:
                if "google.protobuf" in imp:
                    for msgs in self._messages:
                        for f in [
                            f.message_type
                            for f in msgs.fields
                            if f.field_type == SylkField_pb2.TYPE_MESSAGE
                        ]:
                            for t, msgs in _WellMap:
                                if f.split(".")[-1] in msgs:
                                    well_known = imp.replace(".", "/")
                                    temp_imports.append(f'\nimport "{well_known}/{t}";')
                                    break
                else:
                    try:
                        dep_pkg = self._sylk_json.get_package(imp, False)
                        imp_path = imp.replace(".", "/")
                        for msgs in self._messages:
                            for f in [
                                f.message_type
                                for f in msgs.fields
                                if f.field_type == SylkField_pb2.TYPE_MESSAGE
                                and imp in f.message_type
                            ]:
                                tags = self._tags.get(imp)
                                if tags is not None:
                                    temp_imports.append(
                                        f'\nimport "{imp_path}/{tags.get(f.message_type)}";'
                                    )
                                else:
                                    temp_imports.append(
                                        f'\nimport "{imp_path}/{dep_pkg.name}.proto";'
                                    )

                        # temp_imports.append(f'\nimport "imp/{imp_file}";')
                    except SylkValidationError as e:
                        print(e)
                        # pretty.print_warning(e)
                        # pretty.print_success(
                        #     "Importing {} Service into {} Service".format(
                        #         self._sylk_json.get_service(imp).get("name"), self._name
                        #     )
                        # )
            options = next(
                (
                    m
                    for m in self._messages
                    if m.extension_type is not SylkCommons_pb2.DEFAULT_SYLKEXTENSIONS
                ),
                None,
            )
            if (
                options is not None
                and '\nimport "google/protobuf/descriptor.proto";' not in temp_imports
            ):
                temp_imports.append('\nimport "google/protobuf/descriptor.proto";')
            return "".join(temp_imports)
        else:
            return "".join(temp_imports)

    def write_package(self):
        if self._package is not None:
            if self._extensions is not None:
                temp_extensions = []
                for ext_key in self._extensions:
                    ext_value = self._extensions[ext_key]
                    extension_type = self._sylk_json.get_message(
                        ".".join(ext_key.split(".")[:4])
                    )
                    extensions_package = parse_extension_to_proto(
                        "FileOptions",
                        extension_type,
                        ext_key,
                        ext_value,
                        self._sylk_json,
                    )
                    temp_extensions.append(extensions_package)
                joined_extensions = "\n".join(temp_extensions)
                return f"\n\npackage {self._package};\n\n// Sylk.build Package Extensions\n{joined_extensions}"
            else:
                return f"\n\npackage {self._package};"
        else:
            svc_package = self._service.get("fullName")
            return f"\n\npackage {svc_package};"

    def write_service(self, services):
        tmp_services = []
        for s in services:
            rpcs = []

            if s.extensions is not None:
                for ext in s.extensions:
                    ext_msg = self._sylk_json.get_message(ext)

                    temp_svc_ext = parse_extension_to_proto(
                        "ServiceOptions",
                        ext_msg,
                        ext,
                        s.extensions[ext],
                        self._sylk_json,
                    )

                    rpcs.append(temp_svc_ext)

            for m in s.methods:
                rpc_name = m.name
                msg_name_in = m.input_type
                msg_name_out = m.output_type

                description = m.description

                stream_in = (
                    "stream "
                    if m.client_streaming is not None and m.client_streaming == True
                    else ""
                )
                stream_out = (
                    "stream "
                    if m.server_streaming is not None and m.server_streaming == True
                    else ""
                )

                rpcs.append(
                    f"// {description}\n\trpc {rpc_name} ({stream_in}{msg_name_in}) returns ({stream_out}{msg_name_out});"
                )
            rpcs = "\n\t".join(rpcs)
            desc = (
                f"// {self._description}\n"
                if self._description is not None
                else ""
            )
            tmp_services.append(
                f"{desc}service {self._name} {_OPEN_BRCK}\n\t{rpcs}\n{_CLOSING_BRCK}"
            )

        return "".join(tmp_services)

    def write_messages(self, messages):
        if len(messages) > 0:
            msgs = []
            for m in messages:
                msg_name = m.name
                msg_full_name = m.full_name
                fields = []
                # Adding MessageOptions
                if m.extensions is not None:
                    for ext_key in m.extensions:
                        if "google.protobuf" in ext_key:
                            fields.append(
                                "{}".format(
                                    parse_extension_to_proto(
                                        "MessageOptions",
                                        self._sylk_json.get_well_known_message(ext_key),
                                        ext_key,
                                        m.extensions[ext_key],
                                        self._sylk_json,
                                    )
                                )
                            )
                        else:
                            ext_msg = self._sylk_json.get_message(ext_key)
                            if ext_msg is None:
                                raise SylkValidationError(
                                    "FieldOptions",
                                    f'Field Option [{ext}] specified for : "{ext_key}", is invalid !',
                                )
                            fields.append(
                                "{}".format(
                                    parse_extension_to_proto(
                                        "MessageOptions",
                                        ext_msg,
                                        ext_key,
                                        m.extensions[ext_key],
                                        self._sylk_json,
                                    )
                                )
                            )
                m_desc = m.description
                ext_type = m.extension_type
                for f in m.fields:
                    fLabel = (
                        ""
                        if f.label == SylkField_pb2.LABEL_OPTIONAL
                        else "{0} ".format(
                            SylkField_pb2.SylkFieldLabels.Name(f.label)
                            .split("_")[-1]
                            .lower()
                        )
                    )
                    f_type = (
                        SylkField_pb2.SylkFieldTypes.Name(f.field_type)
                        .split("_")[-1]
                        .lower()
                    )
                    if f_type == "message":
                        f_type = f.message_type
                    elif f_type == "enum":
                        f_type = f.enum_type
                    elif f_type == "map":
                        key_type = (
                            SylkField_pb2.SylkFieldTypes.Name(f.key_type)
                            .split("_")[-1]
                            .lower()
                            if f.key_type is not None and f.key_type != -1
                            else None
                        )
                        value_type = (
                            SylkField_pb2.SylkFieldTypes.Name(f.value_type)
                            .split("_")[-1]
                            .lower()
                            if f.value_type != "TYPE_MESSAGE"
                            and f.value_type != "TYPE_ENUM"
                            else f.message_type
                            if f.value_type == "TYPE_MESSAGE"
                            else f.enum_type
                            if f.value_type == "TYPE_ENUM"
                            else None
                        )
                        if value_type is None:
                            pretty.print_error(
                                "Value type for 'map' is not valid ! {0}".format(
                                    f.value_type
                                )
                            )
                        else:
                            f_type = "map<{0}, {1}>".format(key_type, value_type)
                    elif f_type == "oneof":
                        field_name = f.name
                        oneof_fields = []

                        for oneof_field in f.oneof_fields:
                            if oneof_field.field_type == "TYPE_MESSAGE":
                                oneof_field_type = oneof_field.message_type
                            elif oneof_field.field_type == "TYPE_ENUM":
                                oneof_field_type = oneof_field.enum_type
                            else:
                                oneof_field_type = (
                                    SylkField_pb2.SylkFieldTypes.Name(
                                        oneof_field.field_type
                                    )
                                    .split("_")[-1]
                                    .lower()
                                )

                            oneof_field_name = oneof_field.name
                            oneof_field_index = (
                                oneof_field.index
                                if oneof_field.index is not None
                                else 1
                            )
                            oneof_fields.append(
                                f"\n\t\t{oneof_field_type} {oneof_field_name} = {oneof_field_index};"
                            )
                        oneof_fields = "".join(oneof_fields)
                        f_type = f"oneof {field_name} {_OPEN_BRCK}\n{oneof_fields}\n\t{_CLOSING_BRCK}"

                    f_name = f.name
                    f_index = int(f.index)
                    fOptions = []
                    if f.extensions is not None:
                        for ext in f.extensions:
                            list_names = ext.split(".")
                            ext_msg = None

                            if len(list_names) > 2:
                                if ".".join(list_names[:3]) == self._package:
                                    ext_msg = next(
                                        (
                                            m
                                            for m in self._messages
                                            if m.name == list_names[3]
                                        ),
                                        None,
                                    )
                            else:
                                ext_msg = next(
                                    (
                                        m
                                        for m in self._messages
                                        if m.name == ext.split(".")[0]
                                    ),
                                    None,
                                )
                            if ext_msg is None:
                                ext_msg = self._sylk_json.get_message(
                                    ".".join(ext.split(".")[:-1])
                                )
                                if ext_msg is None:
                                    raise SylkValidationError(
                                        "FieldOptions",
                                        f'Field Option [{ext}] specified for : "{f_name}", is invalid !',
                                    )

                            temp_field_extension_test = parse_extension_to_proto(
                                "FieldOptions",
                                ext_msg,
                                ext,
                                f.extensions[ext],
                                self._sylk_json,
                            )
                            fOptions.append(temp_field_extension_test)

                        fOptions = ",\n\t\t".join(fOptions)
                    fOptions = (
                        f" [\n\t\t{fOptions}\n\t]"
                        if len(fOptions) > 1
                        else f"[{fOptions}]"
                        if len(fOptions) == 1
                        else ""
                    )
                    f_desc = f.description
                    f_fullname = f.full_name
                    if (
                        ext_type == "FieldOptions"
                        or ext_type == "FileOptions"
                        or ext_type == "MessageOptions"
                        or ext_type == "ServiceOptions"
                        or ext_type == "MethodOptions"
                    ):
                        f_desc = (
                            f"// {f_desc}\n\t\t"
                            if f_desc is not None
                            else ""
                        )
                    else:
                        f_desc = (
                            f"// {f_desc}\n\t"
                            if f_desc is not None
                            else ""
                        )
                    if f.field_type == "TYPE_ONEOF":
                        fields.append(f"{f_desc}{f_type}")
                    else:
                        fields.append(
                            f"{f_desc}{fLabel}{f_type} {f_name} = {f_index}{fOptions};"
                        )

                if ext_type == "FieldOptions":
                    fields = "\n\t\t".join(fields)
                    msgs.append(
                        f"\n// {m_desc}\nmessage {msg_name} {_OPEN_BRCK}\n\textend google.protobuf.FieldOptions {_OPEN_BRCK}\n\t\t{fields}\n\t{_CLOSING_BRCK}\n{_CLOSING_BRCK}\n"
                    )
                elif ext_type == "MessageOptions":
                    fields = "\n\t\t".join(fields)
                    msgs.append(
                        f"\n// {m_desc}\nmessage {msg_name} {_OPEN_BRCK}\n\textend google.protobuf.MessageOptions {_OPEN_BRCK}\n\t\t{fields}\n\t{_CLOSING_BRCK}\n{_CLOSING_BRCK}\n"
                    )
                elif ext_type == "FileOptions":
                    fields = "\n\t\t".join(fields)
                    msgs.append(
                        f"\n// {m_desc}\nmessage {msg_name} {_OPEN_BRCK}\n\textend google.protobuf.FileOptions {_OPEN_BRCK}\n\t\t{fields}\n\t{_CLOSING_BRCK}\n{_CLOSING_BRCK}\n"
                    )
                elif ext_type == "ServiceOptions":
                    fields = "\n\t\t".join(fields)
                    msgs.append(
                        f"\n// {m_desc}\nmessage {msg_name} {_OPEN_BRCK}\n\textend google.protobuf.ServiceOptions {_OPEN_BRCK}\n\t\t{fields}\n\t{_CLOSING_BRCK}\n{_CLOSING_BRCK}\n"
                    )
                elif ext_type == "MethodOptions":
                    fields = "\n\t\t".join(fields)
                    msgs.append(
                        f"\n// {m_desc}\nmessage {msg_name} {_OPEN_BRCK}\n\textend google.protobuf.MethodOptions {_OPEN_BRCK}\n\t\t{fields}\n\t{_CLOSING_BRCK}\n{_CLOSING_BRCK}\n"
                    )
                else:
                    fields = "\n\t".join(fields)
                    msgs.append(
                        f"\n// {m_desc}\nmessage {msg_name} {_OPEN_BRCK}\n\t{fields}\n{_CLOSING_BRCK}\n"
                    )

            msgs = "\n".join(msgs)
            return msgs
        else:
            return ""

    def write_enums(self, enums):
        if enums is not None:
            tmp_enums = []
            for e in enums:
                enum_name = e.name
                enum_full_name = e.full_name
                values = []
                for v in e.values:
                    value_name = v.name
                    value_number = 0 if v.number is None else v.number
                    v_desc = v.description
                    values.append(
                        f"// {v_desc}\n\t{value_name} = {int(value_number)};"
                    )
                values = "\n\t".join(values)
                e_desc = e.description
                tmp_enums.append(
                    f"// {e_desc}\nenum {enum_name} {_OPEN_BRCK}\n\t{values}\n{_CLOSING_BRCK}\n"
                )
            return "\n".join(tmp_enums)

        else:
            return ""

    def to_str(self):
        return self.__str__()

    def generate_files(self):
        options = []
        options = "\n".join(options)
        # if self._sylk_json.project.get("goPackage") is not None:
        #     options.append(
        #         '// Go package name\noption go_package = "{}{}";\n'.format(
        #             self._sylk_json.project.get("goPackage"),
        #             "/services/protos/{0}/{1}/{2};{3}".format(
        #                 domain, name, ver, name + ver
        #             ),
        #         )
        #     )

        for t in self._tags:
            svcs = [s for s in self._services if s.tag == t]
            msgs = [m for m in self._messages if m.tag == t]
            enms = [e for e in self._enums if e.tag == t]
            self._files.append(
                (
                    self._package.replace(".", "/") + "/" + t + ".proto",
                    f'// sylk.build Generated proto DO NOT EDIT\nsyntax = "proto3";{self.write_package()}{self.write_imports(t)}\n\n{options}{self.write_service(svcs)}{self.write_messages(msgs)}{self.write_enums(enms)}',
                )
            )
        svcs = [s for s in self._services if s.tag == "" or s.tag == pkg_name]
        msgs = [m for m in self._messages if m.tag == ""  or m.tag == pkg_name]
        enms = [e for e in self._enums if e.tag == "" or e.tag == pkg_name]

        if len(enms) > 0 or len(msgs) > 0 or len(svcs) > 0:
            ver = parse_version_component(self._package)
            if ver:
                pkg_name = self._package.split(".")[-2].lower()
            else:
                pkg_name = self._package.split(".")[-1].lower()

            self._files.append(
                (
                    self._package.replace(".", "/") + "/" + pkg_name + ".proto",
                    f'// sylk.build Generated proto DO NOT EDIT\nsyntax = "proto3";{self.write_package()}{self.write_imports()}\n\n{options}{self.write_service(svcs)}{self.write_messages(msgs)}{self.write_enums(enms)}',
                )
            )


class SylkClientPy:
    """A helper class to write 'Python' language clients for sylk.build project services"""

    def __init__(
        self,
        project_package,
        services=None,
        packages=None,
        context: SylkContext = None,
        config=None,
        pre_data=None,
        sylk_json: SylkJson = None
    ):
        self._services = services
        self._project_package = project_package
        self._context = context
        self._packages = packages
        self._config = config
        self._pre_data = pre_data
        self._sylk_json = sylk_json

    def __str__(self):
        return f"{self.write_imports()}\n{self.write_client_wrapper()}\n\n{self.write_services_classes()}"

    def write_client_wrapper(self):
        if self._pre_data is not None:
            client_options = self._pre_data.get("client_options")
            client_options = "\n\t".join(
                list(
                    map(
                        lambda opt: '("{}", {}),'.format(opt[0], opt[1]), client_options
                    )
                )
            )
        sylk_version = __version__.__version__
        sylk_global_auth_key = None
        return f"\n# For available channel options in python visit https://github.com/grpc/grpc/blob/v1.46.x/include/grpc/impl/codegen/grpc_types.h\n_CHANNEL_OPTIONS = ({client_options})\n\n# Global metadata\n_METADATA = (('sylk-version','{sylk_version}'),)\n\n# Global auth key that will be verified by sylk client\n_GLOBAL_AUTH_KEY = {sylk_global_auth_key}\n\n# Generated thanks to [sylk.build](https://www.sylk.build)\n"

    def init_stubs(self):
        stubs = []
        for svc in self._services:
            svc_name = svc.split("/")[-1].split(".")[0]
            svc_ver = svc.split("/")[-2]
            stubs.append(
                f"self.{svc_name}{svc_ver}Stub = {svc_name}{svc_ver}Service.{svc_name}Stub(channel)"
            )

        return "\n\t\t".join(stubs)

    def init_wrapper(self):
        if self._config is not None:
            host = self._config.get("host")
            port = self._config.get("port")

        else:
            host = "localhost"
            port = 44880
        init_func = f"def __init__(self, host=\"{host}\", port={port}, timeout=10, log_level='ERROR'):\n\t\tlogging.root.setLevel(log_level)\n\t\tself._sylk_global_auth_key = _GLOBAL_AUTH_KEY\n\t\tchannel = grpc.insecure_channel('{_OPEN_BRCK}0{_CLOSING_BRCK}:{_OPEN_BRCK}1{_CLOSING_BRCK}'.format(host, port),_CHANNEL_OPTIONS)\n\t\ttry:\n\t\t\tgrpc.channel_ready_future(channel).result(timeout=timeout)\n\t\texcept grpc.FutureTimeoutError:\n\t\t\tlogging.error('Timed out: Server seems to be offline. Verify your connection configs.')\n\t\t\tsys.exit(1)\n\t\t{self.init_stubs()}"
        return init_func

    
    def write_imports(self):
        adding_protos_module_path = f'# Adding protos module path if needed\n\
script_dir = os.path.dirname(os.path.abspath(__file__))\n\
proto_module = os.path.join(script_dir, "{self._sylk_json._root_protos}")\n\
if proto_module not in sys.path:\n\
    # Insert the protos modules path at the beginning of sys.path (to give it higher priority)\n\
    sys.path.insert(0, proto_module)'
        imports = [
            "from typing import Tuple, Iterator, Any",
            "import grpc",
            "import os",
            "import sys",
            adding_protos_module_path,
            "from functools import partial",
            # "from sylk.commons.interceptors import sylk_client_pre_rpc, SylkSimpleAuth",
            "import logging",
        ]

        files =  self._sylk_json._proto_tree.get_all_file_paths()
        for mod in files:
            mod_path = '.'.join(mod.split('/')[:-1])
            mod_name = mod.split('/')[-1].split('.')[0]
            ver = self._sylk_json._proto_tree._parse_version_component(mod_path)
            code_base_path = '' if self._sylk_json.code_base_path is None or self._sylk_json.code_base_path == '' else f'{self._sylk_json.code_base_path}.'
            
            if ver is not None:
                version = mod_path.split('.')[-1]
            else:
                version = ''
            if mod_path.split('.')[0] != self._sylk_json._proto_tree.root.name:
                base_protos = code_base_path

                imports.append(f"from {mod_path} import {mod_name}_pb2" )
            else:
                base_protos = f'.{code_base_path}{self._sylk_json._root_protos}.' if self._sylk_json._root_protos is not None and self._sylk_json._root_protos != '' else f'.{code_base_path}'
                imports.append(f"from {base_protos}{mod_path} import {mod_name}_pb2 as {mod_name}_{version}, {mod_name}_pb2_grpc as {mod_name}_{version}_grpc" )

        # Pre data parsing
        if self._pre_data is not None:
            if self._pre_data.get("imports") is not None:
                for imp in self._pre_data.get("imports"):
                    if imp not in imports:
                        imports.append(imp)

        return "\n".join(imports)

    def write_services_classes(self):
        defualt_port = self._sylk_json._config.get('port')
        if self._services is not None:
            svcs = []
            for svc in self._services:
                rpcs = []
                svc_pkg = self._sylk_json._proto_tree.get_parent(svc.get('fullName'))
                
                svc_ver = parse_version_component(svc.get("fullName"))
                svc_name = svc.get("name")
                formatted_version = ''
                if svc_ver is not None:
                    svc_pkg_name = svc_pkg.full_path.split('.')[-2] if svc.get('tag') is None else svc.get('tag')
                    formatted_version = "v{}".format(svc_ver.get("version"))
                    if svc_ver.get("channel") is not None:
                        formatted_version += svc_ver.get("channel")
                        if svc_ver.get("release") is not None:
                            formatted_version += svc_ver.get("release")
                else:
                    svc_pkg_name = svc_pkg.full_path.split('.')[-1] if svc.get('tag') is None else svc.get('tag')
                for rpc in svc.get("methods"):
                    rpc_name = rpc["name"]
                    description = (
                        rpc.get("description")
                        if rpc.get("description") is not None
                        else ""
                    )
                    rpc_in_type = rpc["inputType"].split(".")[-1]
                    if "google.protobuf" in rpc["inputType"]:
                        pb_pkg = rpc["inputType"].split(".")[-1].lower()
                        rpc_in_type = f"{pb_pkg}_pb2.{rpc_in_type}"
                    else:
                        rpc_in_pkg = self._sylk_json._proto_tree.get_parent(rpc["inputType"])
                        rpc_in_type_pkg = self._sylk_json._proto_tree._get_file_paths([rpc["inputType"]])
                        rpc_in_type_pkg = rpc_in_type_pkg[0].split('/')[-1].split('.')[0]
                        ver = self._sylk_json._proto_tree._parse_version_component(rpc["inputType"])
                        if ver is not None:
                            rpc_in_type_over = rpc_in_pkg.full_path.split(".")[-1]
                        else:
                            rpc_in_type_over = ""
                        rpc_in_type = (
                            f"{rpc_in_type_pkg}_{rpc_in_type_over}.{rpc_in_type}"
                        )
                   
                    rpc_out_type = rpc["outputType"].split(".")[-1]
                    if "google.protobuf" in rpc["outputType"]:
                        pb_pkg = rpc["outputType"].split(".")[-1].lower()
                        rpc_out_type = f"{pb_pkg}_pb2.{rpc_out_type}"
                    else:
                        rpc_out_pkg = self._sylk_json._proto_tree.get_parent(rpc["outputType"])
                        rpc_out_type_pkg = self._sylk_json._proto_tree._get_file_paths([rpc["outputType"]])
                        rpc_out_type_pkg = rpc_out_type_pkg[0].split('/')[-1].split('.')[0]
                        ver = self._sylk_json._proto_tree._parse_version_component(rpc["outputType"])
                        if ver is not None:
                            rpc_out_type_over = rpc_out_pkg.full_path.split(".")[-1]
                        else:
                            rpc_out_type_over = ""
                        rpc_out_type = (
                            f"{rpc_out_type_pkg}_{rpc_out_type_over}.{rpc_out_type}"
                        )
                    in_open_type = (
                        "Iterator["
                        if rpc.get("clientStreaming") is not None
                        and rpc.get("clientStreaming") == True
                        else ""
                    )
                    in_close_type = (
                        "]"
                        if rpc.get("clientStreaming") is not None
                        and rpc.get("clientStreaming") == True
                        else ""
                    )
                    out_open_type = (
                        "Iterator["
                        if rpc.get("serverStreaming") is not None
                        and rpc.get("serverStreaming") == True
                        else ""
                    )
                    out_close_type = (
                        "]"
                        if rpc.get("serverStreaming") is not None
                        and rpc.get("serverStreaming") == True
                        else ""
                    )
                    if svc_ver is not None:
                        rpcs.append(
                            f'\n\tdef {rpc_name}_WithCall(self, request: {in_open_type}{rpc_in_type}{in_close_type}, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[{out_open_type}{rpc_out_type}{out_close_type}, Any]:\n\t\t"""sylk - {description} Returns: RPC output and a call object"""\n\n\t\treturn self.{svc_name}_{formatted_version}_stub.{rpc_name}.with_call(request,metadata=metadata)'
                        )
                        rpcs.append(
                            f'\n\tdef {rpc_name}(self, request: {in_open_type}{rpc_in_type}{in_close_type}, metadata: Tuple[Tuple[str,str]] = _METADATA) -> {out_open_type}{rpc_out_type}{out_close_type}:\n\t\t"""sylk - {description}"""\n\n\t\treturn self.{svc_name}_{formatted_version}_stub.{rpc_name}(request,metadata=metadata)'
                        )
                    else:
                        rpcs.append(
                            f'\n\tdef {rpc_name}_WithCall(self, request: {in_open_type}{rpc_in_type}{in_close_type}, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[{out_open_type}{rpc_out_type}{out_close_type}, Any]:\n\t\t"""sylk - {description} Returns: RPC output and a call object"""\n\n\t\treturn self.{svc_name}_{formatted_version}_stub.{rpc_name}.with_call(request,metadata=metadata)'
                        )
                        rpcs.append(
                            f'\n\tdef {rpc_name}(self, request: {in_open_type}{rpc_in_type}{in_close_type}, metadata: Tuple[Tuple[str,str]] = _METADATA) -> {out_open_type}{rpc_out_type}{out_close_type}:\n\t\t"""sylk - {description}"""\n\n\t\treturn self.{svc_name}_{formatted_version}_stub.{rpc_name}(request,metadata=metadata)'
                        )
                rpcs = "\n\n\t".join(rpcs)
                if svc_ver is not None:
                    svcs.append(
                        f"\nclass {svc_name}_{formatted_version}:\n\t\"\"\"\n\tservice class generated by sylk.build\n\n\tFile: {svc.get('fullName')}\n\tService: {svc_name}\n\tVersion: {formatted_version}\n\t\"\"\"\n\n\tdef __init__(self,channel: grpc.ChannelCredentials = None, client_opt = {_OPEN_BRCK}{_CLOSING_BRCK}):\n\t\tlogging.root.setLevel(client_opt.get('log_level','ERROR'))\n\t\tif channel is None:\n\t\t\tself.channel = grpc.insecure_channel('{_OPEN_BRCK}0{_CLOSING_BRCK}:{_OPEN_BRCK}1{_CLOSING_BRCK}'.format(client_opt.get('host','localhost'), client_opt.get('port',{defualt_port})),_CHANNEL_OPTIONS)\n\t\t\ttry:\n\t\t\t\tgrpc.channel_ready_future(self.channel).result(timeout=client_opt.get('timeout',10))\n\t\t\texcept grpc.FutureTimeoutError:\n\t\t\t\tlogging.error('Timedout: server seems to be offline. verify your connection configs.')\n\t\t\t\tsys.exit(1)\n\t\telse:\n\t\t\tself.channel = channel\n\t\tself.{svc_name}_{formatted_version}_stub = {svc_pkg_name}_{formatted_version}_grpc.{svc_name}Stub(self.channel)\n{rpcs}"
                    )
                else:
                    svcs.append(
                        f"\nclass {svc_name}:\n\t\"\"\"\n\tservice class generated by sylk.build\n\n\tFile: {svc}\n\tService: {svc_name}\n\tVersion: {formatted_version}\n\t\"\"\"\n\n\tdef __init__(self,channel: grpc.ChannelCredentials = None, client_opt = {_OPEN_BRCK}{_CLOSING_BRCK}):\n\t\tlogging.root.setLevel(client_opt.get('log_level','ERROR'))\n\t\tif channel is None:\n\t\t\tself.channel = grpc.insecure_channel('{_OPEN_BRCK}0{_CLOSING_BRCK}:{_OPEN_BRCK}1{_CLOSING_BRCK}'.format(client_opt.get('host','localhost'), client_opt.get('port',{defualt_port})),_CHANNEL_OPTIONS)\n\t\t\ttry:\n\t\t\t\tgrpc.channel_ready_future(self.channel).result(timeout=client_opt.get('timeout',10))\n\t\t\texcept grpc.FutureTimeoutError:\n\t\t\t\tlogging.error('Timedout: server seems to be offline. verify your connection configs.')\n\t\t\t\tsys.exit(1)\n\t\telse:\n\t\t\tself.channel = channel\n\t\tself.{svc_name}_{formatted_version}_stub = {svc_pkg_name}_{formatted_version}_grpc.{svc_name}Stub(self.channel)\n{rpcs}"
                    )
            svcs = "\n\n".join(svcs)
        return "".join(svcs)


class SylkServicePy:
    """A helper class to write 'Python' language services for sylk.build project services"""

    def __init__(
        self,
        project_package,
        name,
        imports=[],
        service=None,
        package=None,
        messages=[],
        enums=[],
        context: SylkContext = None,
        sylk_json: SylkJson = None,
    ):
        self._name = name
        self._imports = imports
        self._service = service
        self._project_package = project_package
        self._context = context
        self._sylk_json = sylk_json
        self._service_name = self._name.split("/")[-1].split(".")[0]
        self._service_path = ".".join(self._name.split("/")[:-1])

    def write_imports(self):
        list_d = list(map(lambda i: i, _WELL_KNOWN_PY_IMPORTS))

        parent = self._sylk_json._proto_tree.get_parent(self._service.get('fullName'))
        refs = self._sylk_json._proto_tree.get_parents_refs([self._service.get('fullName')])
        
        deps = self._sylk_json._proto_tree.get_references(self._service.get('fullName'))
       
        pkg_ver = self._sylk_json._proto_tree._parse_version_component(parent.full_path)
        if pkg_ver is not None:
            pkg_name = parent.full_path.split('.')[-2]
        else:
            pkg_name = parent.name
        module_name = pkg_name if self._service.get('tag') is None and self._service.get('tag') != '' else self._service.get('tag')
        base_protos = self._sylk_json._root_protos.replace('/','.')
        code_base_path = '' if self._sylk_json.code_base_path is None or self._sylk_json.code_base_path == '' else f'{self._sylk_json.code_base_path}.'

        for d in deps:
            if d.split('.')[0] == self._sylk_json._proto_tree.root.name:
                root = self._sylk_json._proto_tree.root
                dep_parent = self._sylk_json._proto_tree.get_parent(d)
                base_path = f'{code_base_path}services.' if self._sylk_json._root_protos is None or self._sylk_json._root_protos == '' else f'{code_base_path}services.{base_protos}.'
                msg_dep =self._sylk_json._proto_tree._find_node(d,root) 
                if parse_version_component(dep_parent.full_path) is not None:
                    temp_name = dep_parent.full_path.split('.')[-2]
                else:
                    temp_name = dep_parent.name
                dep_mod_name = temp_name if msg_dep.properties.get('tag') is None or msg_dep.properties.get('tag') == '' else msg_dep.properties.get('tag')
                imp_path = f"from {base_path}{dep_parent.full_path} import {dep_mod_name}_pb2_grpc, {dep_mod_name}_pb2"
            else:
                root = self._sylk_json._proto_tree.proto_modules[d.split('.')[0]].root
                dep_parent = self._sylk_json._proto_tree.proto_modules[d.split('.')[0]].get_parent(d)
                msg_dep =self._sylk_json._proto_tree._find_node(d,root) 
                if parse_version_component(dep_parent.full_path) is not None:
                    temp_name = dep_parent.full_path.split('.')[-2]
                else:
                    temp_name = dep_parent.name
                dep_mod_name = temp_name if msg_dep.properties.get('tag') is None or msg_dep.properties.get('tag') == '' else msg_dep.properties.get('tag')
                imp_path = f"from {dep_parent.full_path} import {dep_mod_name}_pb2"
            if imp_path not in list_d:
                list_d.append(
                    imp_path
                )
        
        base_path = f'{code_base_path}services.' if self._sylk_json._root_protos is None or self._sylk_json._root_protos == '' else f'{code_base_path}services.{base_protos}.'
        imp_path = f"from {base_path}{parent.full_path} import {module_name}_pb2_grpc, {module_name}_pb2"
        if imp_path not in list_d:
            list_d.append(
                    f"from {base_path}{parent.full_path} import {module_name}_pb2_grpc, {module_name}_pb2"
                )
        list_d = "\n".join(list_d)
        return f"{list_d}"
        

    def write_class(self):
        rpcs = []
        svc_node = self._sylk_json._proto_tree.get_parent(self._service.get('fullName'))
        ver = self._sylk_json._proto_tree._parse_version_component(self._service.get('fullName'))
        if ver is not None:
            pkg_name = svc_node.full_path.split('.')[-2]
        else:
            pkg_name = svc_node.full_path.split('.')[-1]
        mod_name = self._service.get('tag') if self._service.get('tag') is not None else pkg_name

        if self._context is not None:
            functions = self._context.get_functions(self._name)
            if functions is not None:
                for func in functions:
                    func_code = func["code"]
                    rpcs.append(f"\t# @skip @@sylk - DO NOT REMOVE\n{func_code}")

        for rpc in self._service.get("methods"):
            rpc_name = rpc.get("name")
            if "google.protobuf." in rpc.get("inputType"):
                in_mod_name = rpc.get("inputType").split(".")[-1].lower()
            else:
                files = self._sylk_json._proto_tree._get_file_paths([rpc.get("inputType")])
                in_mod_name = files[0].split('/')[-1].split('.')[0]
            rpc_in_name = rpc.get("inputType").split(".")[-1]
            if "google.protobuf." in rpc.get("outputType"):
                out_mod_name = rpc.get("outputType").split(".")[-1].lower()
            else:
                files = self._sylk_json._proto_tree._get_file_paths([rpc.get("outputType")])
                out_mod_name = files[0].split('/')[-1].split('.')[0]
            rpc_out_name = rpc.get("outputType").split(".")[-1]
            rpc_type_in = rpc.get("clientStreaming")
            rpc_type_out = rpc.get("serverStreaming")

            open_in_type = (
                "Iterator[" if rpc_type_in is not None and rpc_type_in == True else ""
            )
            closing_in_type = (
                "]" if rpc_type_in is not None and rpc_type_in == True else ""
            )

            open_out_type = (
                "Iterator[" if rpc_type_out is not None and rpc_type_out == True else ""
            )
            close_out_type = (
                "]" if rpc_type_out is not None and rpc_type_out == True else ""
            )
            code = ""
            if self._context is not None:
                code = self._context.get_rpc(self._name, rpc_name)
                if code is not None:
                    code = code.get("code")
                else:
                    if self._sylk_json is not None:
                        fields = []
                        msg = self._sylk_json.get_message(rpc.get("outputType"))
                        for f in msg.get("fields"):
                            fields.append("{0}=None".format(f.get("name")))
                    fields = ",".join(fields)
                    if rpc_type_out:
                        out_prototype = f"\t\t# responses = [{out_mod_name}_pb2.{rpc_out_name}({fields})]\n\t\t# for res in responses:\n\t\t#    yield res\n"
                    else:
                        out_prototype = f"\t\t# response = {out_mod_name}_pb2.{rpc_out_name}({fields})\n\t\t# return response\n"
                    code = (
                        f"{out_prototype}\n\t\tsuper().{rpc_name}(request, context)\n\n"
                    )
            else:
                if self._sylk_json is not None:
                    fields = []
                    msg = self._sylk_json.get_message(rpc.get("outputType"))
                    if msg is not None:
                        for f in msg.get("fields"):
                            fields.append("{0}=None".format(f.get("name")))
                fields = ",".join(fields)
                if rpc_type_out:
                    out_prototype = f"\t\t# responses = [{out_mod_name}_pb2.{rpc_out_name}({fields})]\n\t\t# for res in responses:\n\t\t#    yield res\n"
                else:
                    out_prototype = f"\t\t# response = {out_mod_name}_pb2.{rpc_out_name}({fields})\n\t\t# return response\n"
                code = f"{out_prototype}\n\t\tsuper().{rpc_name}(request, context)\n\n"
            rpcs.append(
                f"\t# @rpc @@sylk - DO NOT REMOVE\n\tdef {rpc_name}(self, request: {open_in_type}{in_mod_name}_pb2.{rpc_in_name}{closing_in_type}, context: grpc.ServicerContext) -> {open_out_type}{out_mod_name}_pb2.{rpc_out_name}{close_out_type}:\n{code}"
            )
        rpcs = "".join(rpcs)
        return f"class {self._service_name}({mod_name}_pb2_grpc.{self._service_name}Servicer):\n\n{rpcs}"

    def to_str(self):
        return self.__str__()

    def __str__(self):
        return f'"""sylk.build service implemantation for -> {self._name}"""\nimport grpc\n{self.write_imports()}\n\n{self.write_class()}'


class SylkServiceTs:
    """A helper class to write 'Typescript' language services for sylk.build project services"""

    def __init__(
        self,
        project_package,
        name,
        imports=[],
        service=None,
        package=None,
        messages=[],
        enums=[],
        context: SylkContext = None,
        sylk_json: SylkJson = None,
    ):
        self._name = name
        self._imports = imports
        self._service = service
        self._project_package = project_package
        self._context = context
        self._sylk_json = sylk_json
        self._import_name = self._name.split("/")[-1].split(".")[0]
        self._import_path = (
            "/".join(self._name.split("/")[:-1]) + "/" + self._import_name
        )

    def write_imports(self):
        list_d = list(map(lambda i: i, _WELL_KNOWN_TS_IMPORTS))
        parent = self._sylk_json._proto_tree.get_parent(self._service.get('fullName'))
        refs = self._sylk_json._proto_tree.get_parents_refs([self._service.get('fullName')])
        
        deps = self._sylk_json._proto_tree.get_references(self._service.get('fullName'))
       
        pkg_ver = self._sylk_json._proto_tree._parse_version_component(parent.full_path)
        if pkg_ver is not None:
            pkg_name = parent.full_path.split('.')[-2]
        else:
            pkg_name = parent.name
        module_name = pkg_name if self._service.get('tag') is None and self._service.get('tag') != '' else self._service.get('tag')
        base_protos = self._sylk_json._root_protos.replace('/','.')
        for d in list(set(deps)):

            if d.split('.')[0] == self._sylk_json._proto_tree.root.name:
                root = self._sylk_json._proto_tree.root
                dep_parent = self._sylk_json._proto_tree.get_parent(d)
                
                base_path = '../../' if self._sylk_json._root_protos is None or self._sylk_json._root_protos == '' else f'../../{base_protos}/'
                msg_dep =self._sylk_json._proto_tree._find_node(d,root) 
                if parse_version_component(dep_parent.full_path) is not None:
                    temp_name = dep_parent.full_path.split('.')[-2]
                else:
                    temp_name = dep_parent.name
                dep_mod_name = temp_name if msg_dep.properties.get('tag') is None or msg_dep.properties.get('tag') == '' else msg_dep.properties.get('tag')
                imp_path = f"import * as {dep_mod_name} from '{base_path}{dep_parent.full_path.replace('.','/')}/{dep_mod_name}';"
                # f"from {base_path}{dep_parent.full_path} import {dep_mod_name}_pb2_grpc, {dep_mod_name}_pb2"
            else:
                root = self._sylk_json._proto_tree.proto_modules[d.split('.')[0]].root
                dep_parent = self._sylk_json._proto_tree.proto_modules[d.split('.')[0]].get_parent(d)
                msg_dep =self._sylk_json._proto_tree._find_node(d,root) 
                base_path = '../../' if self._sylk_json._root_protos is None or self._sylk_json._root_protos == '' else f'../../{base_protos}/'
                if parse_version_component(dep_parent.full_path) is not None:
                    temp_name = dep_parent.full_path.split('.')[-2]
                else:
                    temp_name = dep_parent.name
                dep_mod_name = temp_name if msg_dep.properties.get('tag') is None or msg_dep.properties.get('tag') == '' else msg_dep.properties.get('tag')
                imp_path = f"import * as {dep_mod_name} from '{base_path}{dep_parent.full_path.replace('.','/')}/{dep_mod_name}';"
            if imp_path not in list_d:
                list_d.append(
                    imp_path
                )
        base_path = '../../' if self._sylk_json._root_protos is None or self._sylk_json._root_protos == '' else f'../../{base_protos}/'
        imp_path = f"import {_OPEN_BRCK} {self._service.get('name')}Service {_CLOSING_BRCK} from '{base_path}{parent.full_path.replace('.','/')}/{module_name}';"
        if imp_path not in list_d:
            list_d.append(
                    imp_path
                )
        list_d = "\n".join(list_d)
        return f"{list_d}"

        # if self._imports is not None:
        #     pkg = self._sylk_json.get_package(
        #         self._service.get("name"),
        #         version=self._service.get("fullName").split(".")[-1],
        #         json=False,
        #     )
        #     list_d.append(
        #         f"import {_OPEN_BRCK} {self._import_name}Server, {self._import_name}Service {_CLOSING_BRCK} from '../../{self._import_path}';"
        #     )
        #     for d in self._imports:
        #         if "google.protobuf." in d:
        #             pass
        #             # wellknown_message = d.split('.')[-1]
        #             # list_d.append(f'from google.protobuf import {wellknown_message.lower()}_pb2')
        #         else:
        #             name = d.split(".")[1]
        #             d_name = "{0}".format(name)
        #             d_ver = d.split(".")[-1]
        #             pkg = "/".join(
        #                 self._sylk_json.get_path(
        #                     d.split(".")[0], d.split(".")[1], d.split(".")[2]
        #                 ).split("/")[:-1]
        #             )
        #             list_d.append(
        #                 f"import * as {d_name}{d_ver} from '../../{pkg}/{d_name}';"
        #             )

        #     list_d = "\n".join(list_d)
        #     return f"{list_d}"
        # else:
        #     pkg = self._sylk_json.get_package(
        #         self._service.get("name"),
        #         version=self._service.get("fullName").split(".")[-1],
        #         json=False,
        #     )
        #     msgs = []
        #     for m in pkg.messages:
        #         msgs.append(m.name)
        #     msgs = ", ".join(msgs)
        #     list_d.append(
        #         f"import {_OPEN_BRCK} {self._import_name}Server, {self._import_name}Service, {msgs} {_CLOSING_BRCK} from '../../{self._import_path}';"
        #     )
        #     list_d = "\n".join(list_d)
        #     return f"{list_d}"

    def write_class(self):
        rpcs = []
        svc_node = self._sylk_json._proto_tree.get_parent(self._service.get('fullName'))
        ver = self._sylk_json._proto_tree._parse_version_component(self._service.get('fullName'))
        if ver is not None:
            pkg_name = svc_node.full_path.split('.')[-2]
        else:
            pkg_name = svc_node.full_path.split('.')[-1]
        mod_name = self._service.get('tag') if self._service.get('tag') is not None else pkg_name
        if self._context is not None:
            functions = self._context.get_functions(self._name)
            if functions is not None:
                for func in functions:
                    func_code = func["code"]
                    rpcs.append(f"\t// @skip @@sylk - DO NOT REMOVE\n{func_code}")

        for rpc in self._service.get("methods"):
            rpc_name = rpc.get("name")
            # rpc_in_pkg = rpc.get("inputType").split(".")[1]
            # rpc_in_pkg_ver = rpc.get("inputType").split(".")[2]
            # Case the service holds the messages we remove the prefix of package
            # since the service imports pb generated classes and grpc classes from single a file
            if "google.protobuf." in rpc.get("inputType"):
                in_mod_name = rpc.get("inputType").split(".")[-1].lower()
            else:
                files = self._sylk_json._proto_tree._get_file_paths([rpc.get("inputType")])
                in_mod_name = files[0].split('/')[-1].split('.')[0]
            
            rpc_in_name = rpc.get("inputType").split(".")[-1]
            # Same as we done for inputs prefixes we do for output prefixes
            if "google.protobuf." in rpc.get("outputType"):
                out_mod_name = rpc.get("outputType").split(".")[-1].lower()
            else:
                files = self._sylk_json._proto_tree._get_file_paths([rpc.get("outputType")])
                out_mod_name = files[0].split('/')[-1].split('.')[0]
            rpc_out_name = rpc.get("outputType").split(".")[-1]
            rpc_type_in = (
                rpc.get("clientStreaming")
                if rpc.get("clientStreaming") is not None
                else False
            )
            rpc_type_out = (
                rpc.get("serverStreaming")
                if rpc.get("serverStreaming") is not None
                else False
            )

            handleType = "handleUnaryCall"
            args = f"call: ServerUnaryCall<{in_mod_name}.{rpc_in_name}, {out_mod_name}.{rpc_out_name}>,\n\t\tcallback: sendUnaryData<{out_mod_name}.{rpc_out_name}>"

            if rpc_type_in and rpc_type_out:
                handleType = "handleBidiStreamingCall"
                args = f"call: ServerDuplexStream<{in_mod_name}.{rpc_in_name}, {out_mod_name}.{rpc_out_name}>"
            elif rpc_type_in and rpc_type_out == False:
                handleType = "handleClientStreamingCall"
                args = f"call: ServerReadableStream<{in_mod_name}.{rpc_in_name}, {out_mod_name}.{rpc_out_name}>,\n\t\tcallback: sendUnaryData<{out_mod_name}.{rpc_out_name}>"
            elif rpc_type_in == False and rpc_type_out:
                handleType = "handleServerStreamingCall"
                args = f"call: ServerWritableStream<{in_mod_name}.{rpc_in_name}, {out_mod_name}.{rpc_out_name}>"
            code = ""
            if self._context is not None:
                code = self._context.get_rpc(self._name, rpc_name)
                if code is not None:
                    code = code.get("code")
            temp_name = rpc_name[0].lower() + rpc_name[1:]
            rpcs.append(
                f"\t// @rpc @@sylk - DO NOT REMOVE\n\tpublic {temp_name}: {handleType}<{in_mod_name}.{rpc_in_name}, {out_mod_name}.{rpc_out_name}> = (\n\t\t{args}\n\t) => {_OPEN_BRCK}\n{code}\n\t{_CLOSING_BRCK}\n"
            )
        rpcs = "".join(rpcs)
        return f"\nclass {self._import_name} implements {mod_name}.{self._import_name}Server, ApiType<UntypedHandleCall> {_OPEN_BRCK}\n\t[method: string]: any;\n\n{rpcs}\n\n{_CLOSING_BRCK}\n\nexport {_OPEN_BRCK}\n\t{self._import_name},\n\t{self._import_name}Service\n{_CLOSING_BRCK};"

    def to_str(self):
        return self.__str__()

    def __str__(self):
        return f"{self.write_imports()}\n{self.write_class()}"


class SylkClientTs:
    """A helper class to write 'Typescript' language clients for sylk.build project services"""

    def __init__(
        self,
        project_package,
        services=None,
        packages=None,
        context: SylkContext = None,
        config=None,
        pre_data=None,
        sylk_json: SylkJson = None
    ):
        self._services = services
        self._project_package = project_package
        self._context = context
        self._packages = packages
        self._config = config
        self._pre_data = pre_data
        self._sylk_json = sylk_json

    def __str__(self):
        return f"{self.write_imports()}\n{self.write_client_wrapper()}\n\n{self.write_services_classes()}"

    def write_client_exports(self):
        pkgs_list = []
        clients_list = []
        for key in self._packages:
            pkg = self._packages[key].get("name")
            pkgs_list.append(pkg)
        pkgs_list = ",\n\t".join(pkgs_list)
        for key in self._services:
            svc_name = key.split("/")[-1].split(".")[0]
            clients_list.append(f"{svc_name}Client")

        # Pre data parsing
        if self._pre_data is not None:
            if self._pre_data.get("exports") is not None:
                for exp in self._pre_data.get("exports"):
                    if exp not in clients_list:
                        clients_list.append(exp)

        clients_list = ",\n\t".join(clients_list)
        return f"export {_OPEN_BRCK}\n\t{pkgs_list},\n\t{clients_list}\n{_CLOSING_BRCK}"

    def write_client_wrapper(self):
        client_options = self._pre_data.get("client_options")
        client_options = "\n\t".join(
            list(map(lambda opt: '"{}": {},'.format(opt[0], opt[1]), client_options))
        )

        # Parsing pre data
        before_init = ""
        interceptors = []

        if self._pre_data:
            if self._pre_data.get("before_init") is not None:
                before_init = self._pre_data.get("before_init")
            if self._pre_data.get("interceptors") is not None:
                interceptors = self._pre_data.get("interceptors")

        interceptors = ", ".join(interceptors)
        return f'\n{before_init}\nconst interceptorsProviders: Interceptor[] = [{interceptors}]\nconst _DEFAULT_OPTION = {_OPEN_BRCK}\n\t{client_options}\n{_CLOSING_BRCK}\n\n/**\n * Generated thanks to [sylk.build](https://www.sylk.build)\n */\nexport interface SylkClientOpts {_OPEN_BRCK}\n\thost: string;\n\tport: number;\n\tmetadata: Metadata;\n\tchannelCreds: ChannelCredentials\n{_CLOSING_BRCK}\nconst DEFAULT_CLIENT_OPTS: SylkClientOpts = {_OPEN_BRCK}\n\thost: "localhost",\n\tport: 44880,\n\tmetadata: new Metadata(),\n\tchannelCreds: credentials.createInsecure()\n{_CLOSING_BRCK}\n'

    def init_stubs(self, svc):
        stubs = []
        temp_stubs = {}
        if self._pre_data is not None:
            if self._pre_data.get("stubs") is not None:
                temp_stubs = self._pre_data.get("stubs")

        svc_name = svc.get("name")
        svc_ver = parse_version_component(svc.get('fullName'))
        if svc_ver is not None:
            svc_ver = f"v{svc_ver.get('version')}{svc_ver.get('channel') if svc_ver.get('channel') is not None else ''}{svc_ver.get('release') if svc_ver.get('release') is not None else ''}"
        else:
            svc_ver = ""
        if svc.get('name') in temp_stubs:
            stub = temp_stubs[svc.get('name')]
            stub_target = (
                stub.get("target")
                if stub.get("target") is not None
                else "${_OPEN_BRCK}this.host{_CLOSING_BRCK}:${_OPEN_BRCK}this.port{_CLOSING_BRCK}"
            )
            stub_creds = (
                stub.get("creds")
                if stub.get("creds") is not None
                else "credentials.createInsecure()"
            )
            stub_opts = (
                stub.get("opts") if stub.get("opts") is not None else "_DEFAULT_OPTION"
            )
            stubs.append(
                f"this.{svc_name}{svc_ver}Client = new {svc_name}{svc_ver}Client(`{stub_target}`, {stub_creds}, {stub_opts});"
            )
        else:
            stubs.append(
                f"this.{svc_name}{svc_ver}Client = new {svc_name}{svc_ver}Client(`${_OPEN_BRCK}this.host{_CLOSING_BRCK}:${_OPEN_BRCK}this.port{_CLOSING_BRCK}`, <ChannelCredentials>channelCreds,_DEFAULT_OPTION);"
            )

        return "\n\t\t".join(stubs)

    def args_stubs(self, svc):
        svc_name = svc.get('name')
        svc_ver = parse_version_component(svc.get('fullName'))
        if svc_ver is not None:
            svc_ver = f"v{svc_ver.get('version')}{svc_ver.get('channel') if svc_ver.get('channel') is not None else ''}{svc_ver.get('release') if svc_ver.get('release') is not None else ''}"
        else:
            svc_ver = ""
        return f"private readonly {svc_name}{svc_ver}Client: {svc_name}{svc_ver}Client;"

    def init_wrapper(self, svc):
        if self._config is not None:
            host = self._config.get("host")
            port = self._config.get("port")

        else:
            host = "localhost"
            port = 44880
        sylk_version = __version__.__version__
        init_func = f"constructor(opts: SylkClientOpts) {_OPEN_BRCK}\n\t\tconst {_OPEN_BRCK} host, metadata, port, channelCreds {_CLOSING_BRCK} = {_OPEN_BRCK}...DEFAULT_CLIENT_OPTS, ...opts{_CLOSING_BRCK}\n\t\tthis.host = host;\n\t\tthis.port = port;\n\t\tthis.metadata = metadata;\n\t\tthis.metadata.add('sylk-version','{sylk_version}');\n\t\t{self.init_stubs(svc)}\n\t{_CLOSING_BRCK}\n\n\tprivate readonly metadata: Metadata;\n\tprivate readonly host: string;\n\tprivate readonly port: number;\n\t{self.args_stubs(svc)}"
        return init_func

    def write_imports(self):

        list_d = list(map(lambda i: i, _WELL_KNOWN_TS_CLIENT_IMPORTS))
        for svc in self._services:
            parent = self._sylk_json._proto_tree.get_parent(svc.get('fullName'))
            refs = self._sylk_json._proto_tree.get_parents_refs([svc.get('fullName')])
            
            deps = self._sylk_json._proto_tree.get_references(svc.get('fullName'))
        
            pkg_ver = self._sylk_json._proto_tree._parse_version_component(parent.full_path)
            if pkg_ver is not None:
                pkg_ver = f'v{pkg_ver.get("version")}{pkg_ver.get("channel") if pkg_ver.get("channel") is not None else ""}{pkg_ver.get("release") if pkg_ver.get("release") is not None else ""}'
                pkg_name = parent.full_path.split('.')[-2]
            else:
                pkg_ver = ''
                pkg_name = parent.name
            module_name = pkg_name if svc.get('tag') is None and svc.get('tag') != '' else svc.get('tag')
            base_protos = self._sylk_json._root_protos.replace('/','.')
            for d in list(set(deps)):

                if d.split('.')[0] == self._sylk_json._proto_tree.root.name:
                    root = self._sylk_json._proto_tree.root
                    dep_parent = self._sylk_json._proto_tree.get_parent(d)
                    
                    base_path = './' if self._sylk_json._root_protos is None or self._sylk_json._root_protos == '' else f'./{base_protos}/'
                    msg_dep =self._sylk_json._proto_tree._find_node(d,root) 
                    dep_mode_ver = parse_version_component(dep_parent.full_path)
                    if dep_mode_ver is not None:
                        dep_mode_ver = f'v{dep_mode_ver.get("version")}{dep_mode_ver.get("channel") if dep_mode_ver.get("channel") is not None else ""}{dep_mode_ver.get("release") if dep_mode_ver.get("release") is not None else ""}'
                        temp_name = dep_parent.full_path.split('.')[-2]
                    else:
                        dep_mode_ver = ''
                        temp_name = dep_parent.name
                    dep_mod_name = temp_name if msg_dep.properties.get('tag') is None or msg_dep.properties.get('tag') == '' else msg_dep.properties.get('tag')
                    imp_path = f"import * as {dep_mod_name}{dep_mode_ver} from '{base_path}{dep_parent.full_path.replace('.','/')}/{dep_mod_name}';"
                    # f"from {base_path}{dep_parent.full_path} import {dep_mod_name}_pb2_grpc, {dep_mod_name}_pb2"
                else:
                    root = self._sylk_json._proto_tree.proto_modules[d.split('.')[0]].root
                    dep_parent = self._sylk_json._proto_tree.proto_modules[d.split('.')[0]].get_parent(d)
                    msg_dep =self._sylk_json._proto_tree._find_node(d,root) 
                    base_path = './' if self._sylk_json._root_protos is None or self._sylk_json._root_protos == '' else f'./{base_protos}/'
                    dep_mode_ver = parse_version_component(dep_parent.full_path)
                    if dep_mode_ver is not None:
                        dep_mode_ver = f'v{dep_mode_ver.get("version")}{dep_mode_ver.get("channel") if dep_mode_ver.get("channel") is not None else ""}{dep_mode_ver.get("release") if dep_mode_ver.get("release") is not None else ""}'
                        temp_name = dep_parent.full_path.split('.')[-2]
                    else:
                        dep_mode_ver = ''
                        temp_name = dep_parent.name
                    dep_mod_name = temp_name if msg_dep.properties.get('tag') is None or msg_dep.properties.get('tag') == '' else msg_dep.properties.get('tag')
                    imp_path = f"import * as {dep_mod_name}{dep_mode_ver} from '{base_path}{dep_parent.full_path.replace('.','/')}/{dep_mod_name}';"
                if imp_path not in list_d:
                    list_d.append(
                        imp_path
                    )
                base_path = './' if self._sylk_json._root_protos is None or self._sylk_json._root_protos == '' else f'./{base_protos}/'
                imp_path = f"import {_OPEN_BRCK} {svc.get('name')}Service, {svc.get('name')}Client as {svc.get('name')}{pkg_ver}Client  {_CLOSING_BRCK} from '{base_path}{parent.full_path.replace('.','/')}/{module_name}';"
                if imp_path not in list_d:
                    list_d.append(
                            imp_path
                        )
        # Pre data parsing
        if self._pre_data is not None:
            if self._pre_data.get("imports") is not None:
                for imp in self._pre_data.get("imports"):
                    if imp not in list_d:
                        list_d.append(imp)
        list_d = "\n".join(list_d)
        return list_d

    def write_services_classes(self):
        if self._services is not None:
            svcs = []
            for svc in self._services:
                svc_name = svc.get("name")
                svc_ver = parse_version_component(svc.get('fullName'))
                if svc_ver is not None:
                    svc_ver = f"v{svc_ver.get('version')}{svc_ver.get('channel') if svc_ver.get('channel') is not None else ''}{svc_ver.get('release') if svc_ver.get('release') is not None else ''}"
                else:
                    svc_ver = ""
                rpcs = []
                for rpc in svc.get("methods",[]):
                    rpc_name = rpc["name"]
                    rpc_in_pkg = self._sylk_json._proto_tree.get_parent(rpc["inputType"])
                    rpc_in_type_pkg = self._sylk_json._proto_tree._get_file_paths([rpc["inputType"]])
                    rpc_in_type_pkg = rpc_in_type_pkg[0].split('/')[-1].split('.')[0]
                    rpc_in_type = rpc["inputType"].split(".")[-1]
                    if rpc_in_type_pkg != "protobuf":
                        rpc_in_ver = self._sylk_json._proto_tree._parse_version_component(rpc["inputType"])
                        if rpc_in_ver is not None:
                            rpc_in_type_pkg_ver = rpc_in_pkg.full_path.split(".")[-1]
                        else:
                            rpc_in_type_pkg_ver = ""
                        rpc_in_type = (
                            f"{rpc_in_type_pkg}{rpc_in_type_pkg_ver}.{rpc_in_type}"
                        )
                    rpc_out_pkg = self._sylk_json._proto_tree.get_parent(rpc["outputType"])
                    rpc_out_type_pkg = self._sylk_json._proto_tree._get_file_paths([rpc["outputType"]])
                    rpc_out_type_pkg = rpc_out_type_pkg[0].split('/')[-1].split('.')[0]
                    rpc_out_type = rpc["outputType"].split(".")[-1]
                    rpc_out_ver = self._sylk_json._proto_tree._parse_version_component(rpc["outputType"])
                    if rpc_out_type_pkg != "protobuf":
                        rpc_out_ver = self._sylk_json._proto_tree._parse_version_component(rpc["outputType"])
                        if rpc_out_ver is not None:
                            rpc_out_type_pkg_ver = rpc_out_pkg.full_path.split(".")[-1]
                        else:
                            rpc_out_type_pkg_ver = ""
                        rpc_out_type = (
                            f"{rpc_out_type_pkg}{rpc_out_type_pkg_ver}.{rpc_out_type}"
                        )
                    rpc_output_type = (
                        rpc.get("serverStreaming")
                        if rpc.get("serverStreaming") is not None
                        else False
                    )
                    rpc_input_type = (
                        rpc.get("clientStreaming")
                        if rpc.get("clientStreaming") is not None
                        else False
                    )

                    rpc_type = (
                        "Unary"
                        if rpc_output_type == False and rpc_input_type == False
                        else "Client Stream"
                        if rpc_input_type == True and rpc_output_type == False
                        else "Server Stream"
                        if rpc_input_type == False and rpc_output_type == True
                        else "Bidi Stream"
                    )

                    rpc_description = rpc.get("description")
                    return_type_overload = (
                        "ClientUnaryCall"
                        if rpc_output_type == False and rpc_input_type == False
                        else f"ClientDuplexStream<{rpc_in_type}, {rpc_out_type}>"
                        if rpc_output_type == True and rpc_input_type == True
                        else f"ClientReadableStream<{rpc_out_type}>"
                        if rpc_output_type == True and rpc_input_type == False
                        else f"ClientWritableStream<{rpc_in_type}>"
                        if rpc_output_type == False and rpc_input_type == True
                        else "any"
                    )
                    return_type = (
                        f"Promise<{rpc_out_type}>"
                        if rpc_output_type == False
                        else f"Observable<{rpc_out_type}>"
                    )
                    temp_rpc_name = rpc_name[0].lower() + rpc_name[1:]
                    temp_rpc_name = to_camel_case(temp_rpc_name)
                    rpc_impl = (
                        f"if (callback === undefined) {_OPEN_BRCK}\n\t\t\treturn promisify<{rpc_in_type}, Metadata, {rpc_out_type}>(this.{svc_name}{svc_ver}Client.{temp_rpc_name}.bind(this.{svc_name}{svc_ver}Client))({rpc_in_type}.fromJSON(request), metadata);\n\t\t{_CLOSING_BRCK} else {_OPEN_BRCK}\n\t\t return this.{svc_name}{svc_ver}Client.{temp_rpc_name}({rpc_in_type}.fromJSON(request), metadata, callback);\n\t\t{_CLOSING_BRCK}"
                        if rpc_output_type == False and rpc_input_type == False
                        else f"return this.{svc_name}{svc_ver}Client.{temp_rpc_name}(metadata);"
                        if rpc_output_type == True and rpc_input_type == True
                        else f"if (callback === undefined) {_OPEN_BRCK}\n\t\t\tcallback = (_error:_service_error | null , _response:{rpc_out_type}) => {_OPEN_BRCK}if (_error) throw _error; return _response{_CLOSING_BRCK}\n\t\t{_CLOSING_BRCK}\n\t\treturn this.{svc_name}{svc_ver}Client.{temp_rpc_name}(metadata, callback);"
                        if rpc_output_type == False and rpc_input_type == True
                        else f"return new Observable(subscriber => {_OPEN_BRCK}\n\t\tconst stream = this.{svc_name}{svc_ver}Client.{temp_rpc_name}({rpc_in_type}.fromJSON(request), metadata);\n\t\t\tstream.on('data', (res: {rpc_out_type}) => {_OPEN_BRCK}\n\t\t\t\tsubscriber.next(res)\n\t\t\t{_CLOSING_BRCK}).on('end', () => {_OPEN_BRCK}\n\t\t\t\tsubscriber.complete()\n\t\t\t{_CLOSING_BRCK}).on('error', (err: any) => {_OPEN_BRCK}\n\t\t\t\tsubscriber.error(err)\n\t\t\t\tsubscriber.complete()\n\t\t\t{_CLOSING_BRCK});\n\t\t{_CLOSING_BRCK})"
                    )
                    # Client streaming
                    if rpc_output_type == False and rpc_input_type == True:
                        description = f"/**\n\t* @method {svc_name}.{rpc_name}\n\t* @description {rpc_description}\n\t* @kind {rpc_type}\n\t* @param metadata Metadata\n\t*/"
                        rpcs.append(
                            f"\n\t{description}\n\tpublic {rpc_name}(metadata?: Metadata): {return_type};\n\tpublic {rpc_name}(metadata: Metadata, callback: (error: _service_error | null, response: {rpc_out_type}) => void): {return_type_overload};\n\tpublic {rpc_name}(metadata: Metadata = this.metadata, callback?: (error: _service_error | null, response: {rpc_out_type}) => void): {return_type_overload} | {return_type} {_OPEN_BRCK}\n\t\t{rpc_impl}\n\t{_CLOSING_BRCK}"
                        )
                    # Bidi stream
                    elif rpc_output_type == True and rpc_input_type == True:
                        description = f"/**\n\t* @method {svc_name}.{rpc_name}\n\t* @description {rpc_description}\n\t* @kind {rpc_type}\n\t* @param request {rpc_in_type}\n\t* @param metadata Metadata\n\t*/"
                        rpcs.append(
                            f"\n\t{description}\n\tpublic {rpc_name}(metadata: Metadata = this.metadata): {return_type_overload} {_OPEN_BRCK}\n\t\t{rpc_impl}\n\t{_CLOSING_BRCK}"
                        )
                    # Unary
                    else:
                        description_0 = f"/**\n\t* @method {svc_name}.{rpc_name}\n\t* @description {rpc_description}\n\t* @kind {rpc_type}\n\t* @param request {rpc_in_type}\n\t* @param metadata Metadata\n\t* @returns {return_type}\n\t*/"
                        description_1 = f"/**\n\t* @method {svc_name}.{rpc_name}\n\t* @description {rpc_description}\n\t* @kind {rpc_type}\n\t* @param request {rpc_in_type}\n\t* @param metadata Metadata\n\t* @param callback A callback function to be excuted once the server responds with {rpc_out_type}\n\t* @returns {return_type_overload}\n\t*/"

                        rpcs.append(
                            f"\n\t{description_0}\n\tpublic {rpc_name}(request: {rpc_in_type}, metadata?: Metadata): {return_type};\n\t{description_1}\n\tpublic {rpc_name}(request: {rpc_in_type}, metadata: Metadata, callback: (error: _service_error | null, response: {rpc_out_type}) => void): {return_type_overload};\n\tpublic {rpc_name}(request: {rpc_in_type}, metadata: Metadata = this.metadata, callback?: (error: _service_error | null, response: {rpc_out_type}) => void): {return_type_overload} | {return_type} {_OPEN_BRCK}\n\t\t{rpc_impl}\n\t{_CLOSING_BRCK}"
                        )

                rpcs = "\n\n\t".join(rpcs)
                svcs.append(
                    f"export class {svc_name}{svc_ver.upper()} {_OPEN_BRCK}\n\t{self.init_wrapper(svc)}\n{rpcs}\n{_CLOSING_BRCK}"
                )
            svcs = "\n".join(svcs)
        return "".join(svcs)


class SylkClientJs:
    """A helper class to write 'Javascript' language clients for sylk.build project services"""

    def __init__(
        self,
        project_package,
        services=None,
        packages=None,
        context: SylkContext = None,
        config=None,
        pre_data=None,
    ):
        self._services = services
        self._project_package = project_package
        self._context = context
        self._packages = packages
        self._config = config
        self._pre_data = pre_data
        self._proto_paths = []

    def __str__(self):
        return f"{self.write_imports()}\n{self.write_services_namespaces()}\n{self.write_client_wrapper()}\n\n\t{self.write_services_classes()}\n{_CLOSING_BRCK}\n{self.write_client_exports()}"

    def write_client_exports(self):
        pkgs_list = []
        clients_list = []
        # for key in self._packages:
        #     pkg = self._packages[key].get('name')
        #     pkgs_list.append(pkg)
        # pkgs_list = ',\n\t'.join(pkgs_list)
        # for key in self._services:
        #     clients_list.append(key+'Client')

        # Pre data parsing
        if self._pre_data is not None:
            if self._pre_data.get("exports") is not None:
                for exp in self._pre_data.get("exports"):
                    if exp not in clients_list:
                        clients_list.append(exp)

        clients_list = ",\n\t".join(clients_list)
        return (
            f"module.exports = {_OPEN_BRCK}\n\t{self._project_package}\n{_CLOSING_BRCK}"
        )

    def write_services_namespaces(self):
        svcs = []
        for svc in self._services:
            svc_methods = []
            for method in svc["methods"]:
                rpc_name = method["name"]
                rpc_in_type_pkg = method["inputType"].split(".")[1]
                rpc_in_type = method["inputType"].split(".")[-1]
                rpc_in_type = f"{rpc_in_type_pkg}.{rpc_in_type}"
                rpc_out_type_pkg = method["outputType"].split(".")[1]
                rpc_out_type = method["outputType"].split(".")[-1]
                rpc_out_type = f"{rpc_out_type_pkg}.{rpc_out_type}"
                rpc_output_type = (
                    method.get("serverStreaming")
                    if method.get("serverStreaming") is not None
                    else False
                )
                rpc_input_type = (
                    method.get("clientStreaming")
                    if method.get("clientStreaming") is not None
                    else False
                )

                rpc_type = (
                    "Unary"
                    if rpc_output_type == False and rpc_input_type == False
                    else "Client Stream"
                    if rpc_input_type == True and rpc_output_type == False
                    else "Server Stream"
                    if rpc_input_type == False and rpc_output_type == True
                    else "Bidi Stream"
                )
                return_type_overload = (
                    "ClientUnaryCall"
                    if rpc_output_type == False and rpc_input_type == False
                    else f"ClientDuplexStream<{rpc_in_type}, {rpc_out_type}>"
                    if rpc_output_type == True and rpc_input_type == True
                    else f"ClientReadableStream<{rpc_out_type}>"
                    if rpc_output_type == True and rpc_input_type == False
                    else f"ClientWritableStream<{rpc_in_type}>"
                    if rpc_output_type == False and rpc_input_type == True
                    else "any"
                )
                temp_rpc_name = rpc_name[0].lower() + rpc_name[1:]
                rpc_impl = (
                    f"if (callback === undefined) {_OPEN_BRCK}\n\t\t\treturn new Promise((resolve,reject) => {_OPEN_BRCK}\n\t\t\tclient.{temp_rpc_name}.bind(client)(request, metadata, (err,res) => {_OPEN_BRCK}\n\t\t\t\tif(err) reject(err);\n\t\t\t\telse {_OPEN_BRCK}\n\t\t\t\t\tresolve(res);\n\t\t\t\t\t{_CLOSING_BRCK}\n\t\t\t\t{_CLOSING_BRCK});\n\t\t\t\t{_CLOSING_BRCK})\n\t\t{_CLOSING_BRCK} else {_OPEN_BRCK}\n\t\t return client.{temp_rpc_name}(request, metadata, callback);\n\t\t{_CLOSING_BRCK}"
                    if rpc_output_type == False and rpc_input_type == False
                    else f"return client.{temp_rpc_name}(metadata);"
                    if rpc_output_type == True and rpc_input_type == True
                    else f"if (callback === undefined) {_OPEN_BRCK}\n\t\t\tcallback = (_error, _response) => {_OPEN_BRCK}if (_error) throw _error; return _response{_CLOSING_BRCK}\n\t\t{_CLOSING_BRCK}\n\t\treturn client.{temp_rpc_name}(metadata, callback);"
                    if rpc_output_type == False and rpc_input_type == True
                    else f"return new Observable(subscriber => {_OPEN_BRCK}\n\t\tconst stream = client.{temp_rpc_name}({rpc_in_type}.fromJSON(request), metadata);\n\t\t\tstream.on('data', (res) => {_OPEN_BRCK}\n\t\t\t\tsubscriber.next(res)\n\t\t\t{_CLOSING_BRCK}).on('end', () => {_OPEN_BRCK}\n\t\t\t\tsubscriber.complete()\n\t\t\t{_CLOSING_BRCK}).on('error', (err) => {_OPEN_BRCK}\n\t\t\t\tsubscriber.error(err)\n\t\t\t\tsubscriber.complete()\n\t\t\t{_CLOSING_BRCK});\n\t\t{_CLOSING_BRCK})"
                )
                # Client streaming
                if rpc_output_type == False and rpc_input_type == True:
                    svc_methods.append(
                        f"{rpc_name}: (client, metadata = this.metadata, callback = undefined) => {_OPEN_BRCK}\n\t\t{rpc_impl}\n\t{_CLOSING_BRCK}"
                    )
                # Bidi stream
                elif rpc_output_type == True and rpc_input_type == True:
                    svc_methods.append(
                        f"{rpc_name}: (client, metadata = this.metadata) => {_OPEN_BRCK}\n\t\t{rpc_impl}\n\t{_CLOSING_BRCK}"
                    )
                # Unary
                else:
                    svc_methods.append(
                        f"{rpc_name}: (client, request, metadata = this.metadata, callback = undefined) => {_OPEN_BRCK}\n\t\t{rpc_impl}\n\t{_CLOSING_BRCK}"
                    )

            svc_methods = ",\n\t".join(svc_methods)
            svcs.append(
                f"const {svc}Service = {_OPEN_BRCK}\n\t{svc_methods}\n{_CLOSING_BRCK}"
            )
            return "\n\n".join(svcs)

    def write_client_wrapper(self):
        client_options = self._pre_data.get("client_options")
        client_options = "\n\t".join(
            list(map(lambda opt: '"{}": {},'.format(opt[0], opt[1]), client_options))
        )

        # Parsing pre data
        before_init = ""
        interceptors = []

        if self._pre_data:
            if self._pre_data.get("before_init") is not None:
                before_init = self._pre_data.get("before_init")
            if self._pre_data.get("interceptors") is not None:
                interceptors = self._pre_data.get("interceptors")
        # proto_paths = ','.join(self._proto_paths)
        interceptors = ", ".join(interceptors)
        if self._config is not None:
            host = self._config.get("host")
            port = self._config.get("port")

        else:
            host = "localhost"
            port = 44880
        return f'\n{before_init}\nconst interceptorsProviders = [{interceptors}]\nconst _DEFAULT_OPTION = {_OPEN_BRCK}\n\t{client_options}\n{_CLOSING_BRCK}\n\nconst protoDefinitions = protoLoader.loadSync(\n\t[...PROTO_PATHS],\n\t{_OPEN_BRCK}\n\t\tincluderDirs: [`${_OPEN_BRCK}__dirname{_CLOSING_BRCK}`],\n\t\tkeepCase:true,\n\t\tlongs: String,\n\t\tenums: String,\n\t\tdefaults: true,\n\t\toneofs: true,\n\t{_CLOSING_BRCK}\n);\nconst protos = grpc.loadPackageDefinition(protoDefinitions);\nconst defaultClientOptions = {_OPEN_BRCK}\n\thost: "{host}",\n\tport: {port},\n\tmetadata: new grpc.Metadata(),\n\tglobalInterceptors: []\n{_CLOSING_BRCK};\n\n/**\n * Generated thanks to [sylk.build](https://www.sylk.build)\n */\nclass {self._project_package} {_OPEN_BRCK}\n\n\t{self.init_wrapper()}'

    def init_stubs(self):
        stubs = []
        temp_stubs = {}
        if self._pre_data is not None:
            if self._pre_data.get("stubs") is not None:
                temp_stubs = self._pre_data.get("stubs")
        for svc in self._services:
            if svc.get('fullName') in temp_stubs:
                stub = temp_stubs[svc]
                stub_target = (
                    stub.get("target")
                    if stub.get("target") is not None
                    else "${_OPEN_BRCK}this.host{_CLOSING_BRCK}:${_OPEN_BRCK}this.port{_CLOSING_BRCK}"
                )
                stub_creds = (
                    stub.get("creds")
                    if stub.get("creds") is not None
                    else "credentials.createInsecure()"
                )
                stub_opts = (
                    stub.get("opts")
                    if stub.get("opts") is not None
                    else "_DEFAULT_OPTION"
                )
                stubs.append(
                    f"this._{svc}Client = new {svc}Client(`{stub_target}`, {stub_creds}, {stub_opts});"
                )
            else:
                stubs.append(
                    f"this._{svc}Client = new protos.{svc}(`${_OPEN_BRCK}this.host{_CLOSING_BRCK}:${_OPEN_BRCK}this.port{_CLOSING_BRCK}`, grpc.credentials.createInsecure());"
                )

        return "\n\t\t".join(stubs)

    def args_stubs(self):
        stubs = []
        for svc in self._services:
            stubs.append(f"_{svc}Client;")

        return "\n\t".join(stubs)

    def init_wrapper(self):
        sylk_version = __version__.__version__
        init_func = f"constructor(options = {_OPEN_BRCK}{_CLOSING_BRCK}) {_OPEN_BRCK}\n\t\tconst {_OPEN_BRCK} host, port, metadata, globalInterceptors {_CLOSING_BRCK} = {_OPEN_BRCK} ...defaultClientOptions, ...options {_CLOSING_BRCK};\n\t\tthis.host = host;\n\t\tthis.port = port;\n\t\tthis.metadata = metadata;\n\t\tthis.metadata.add('sylk-version','{sylk_version}');\n\t\tthis.globalInterceptors = globalInterceptors;\n\t\t{self.init_stubs()}\n\t{_CLOSING_BRCK}\n\n\tmetadata;\n\thost;\n\tport;\n\t{self.args_stubs()}"
        return init_func

    def write_imports(self):
        imports = [
            "let grpc = require('@grpc/grpc-js');",
            "let protoLoader = require('@grpc/proto-loader');",
            "const { compose } = require('lodash/fp');",
            "const { clientMethodWrapper, clientRetries } = require('./utils/interceptors');",
        ]
        proto_paths = []
        for svc in self._services:
            proto_paths.append(
                f"`${_OPEN_BRCK}__dirname{_CLOSING_BRCK}/protos/{svc}/v1/{svc}.proto`"
            )
        for pkg in self._packages:
            pkg_name = pkg.split("/")[-1].split(".")[0]
            pkg_version = pkg.split("/")[1]
            proto_paths.append(
                f"`${_OPEN_BRCK}__dirname{_CLOSING_BRCK}/protos/{pkg_name}/{pkg_version}/{pkg_name}.proto`"
            )
        proto_paths = ",\n\t".join(proto_paths)
        imports.append(f"const PROTO_PATHS = [{proto_paths}\n];")

        # Pre data parsing
        if self._pre_data is not None:
            if self._pre_data.get("imports") is not None:
                for imp in self._pre_data.get("imports"):
                    if imp not in imports:
                        imports.append(imp)

        return "\n".join(imports)

    def write_services_classes(self):
        if self._services is not None:
            rpcs = []
            for svc in self._services:
                for rpc in svc["methods"]:
                    rpc_name = rpc["name"]
                    rpc_in_type_pkg = rpc["inputType"].split(".")[1]
                    rpc_in_type = rpc["inputType"].split(".")[-1]
                    rpc_in_type = f"{rpc_in_type_pkg}.{rpc_in_type}"
                    rpc_out_type_pkg = rpc["outputType"].split(".")[1]
                    rpc_out_type = rpc["outputType"].split(".")[-1]
                    rpc_out_type = f"{rpc_out_type_pkg}.{rpc_out_type}"
                    rpc_output_type = (
                        rpc.get("serverStreaming")
                        if rpc.get("serverStreaming") is not None
                        else False
                    )
                    rpc_input_type = (
                        rpc.get("clientStreaming")
                        if rpc.get("clientStreaming") is not None
                        else False
                    )

                    rpc_type = (
                        "Unary"
                        if rpc_output_type == False and rpc_input_type == False
                        else "Client Stream"
                        if rpc_input_type == True and rpc_output_type == False
                        else "Server Stream"
                        if rpc_input_type == False and rpc_output_type == True
                        else "Bidi Stream"
                    )

                    rpc_description = rpc.get("description")
                    return_type_overload = (
                        "ClientUnaryCall"
                        if rpc_output_type == False and rpc_input_type == False
                        else f"ClientDuplexStream<{rpc_in_type}, {rpc_out_type}>"
                        if rpc_output_type == True and rpc_input_type == True
                        else f"ClientReadableStream<{rpc_out_type}>"
                        if rpc_output_type == True and rpc_input_type == False
                        else f"ClientWritableStream<{rpc_in_type}>"
                        if rpc_output_type == False and rpc_input_type == True
                        else "any"
                    )
                    return_type = (
                        f"Promise" if rpc_output_type == False else f"Observable"
                    )
                    temp_rpc_name = rpc_name[0].lower() + rpc_name[1:]
                    rpc_impl = f"return compose(\n\t\t\tclientMethodWrapper, clientRetries, ...this.globalInterceptors\n\t\t)({svc}Service.{rpc_name})(this._{svc}Client,request,metadata,callback)"
                    # Client streaming
                    if rpc_output_type == False and rpc_input_type == True:
                        description = f"/**\n\t* @method {svc}.{rpc_name}\n\t* @description {rpc_description}\n\t* @kind {rpc_type}\n\t* @param metadata Metadata\n\t*/"
                        rpcs.append(
                            f"\n\t{description}\n\t{rpc_name}(metadata = this.metadata, callback = undefined) {_OPEN_BRCK}\n\t\t{rpc_impl}\n\t{_CLOSING_BRCK}"
                        )
                    # Bidi stream
                    elif rpc_output_type == True and rpc_input_type == True:
                        description = f"/**\n\t* @method {svc}.{rpc_name}\n\t* @description {rpc_description}\n\t* @kind {rpc_type}\n\t* @param request {rpc_in_type}\n\t* @param metadata Metadata\n\t*/"
                        rpcs.append(
                            f"\n\t{description}\n\t{rpc_name}(metadata = this.metadata) {_OPEN_BRCK}\n\t\t{rpc_impl}\n\t{_CLOSING_BRCK}"
                        )
                    # Unary
                    else:
                        # description_0 = f'/**\n\t* @method {svc}.{rpc_name}\n\t* @description {rpc_description}\n\t* @kind {rpc_type}\n\t* @param request {rpc_in_type}\n\t* @param metadata Metadata\n\t* @returns {return_type}\n\t*/'
                        description_1 = f"/**\n\t* @method {svc}.{rpc_name}\n\t* @description {rpc_description}\n\t* @kind {rpc_type}\n\t* @param request {rpc_in_type}\n\t* @param metadata Metadata\n\t* @param callback A callback function to be excuted once the server responds with {rpc_out_type}\n\t* @returns {return_type_overload}\n\t*/"

                        rpcs.append(
                            f"\n\t{description_1}\n\t{rpc_name}(request, metadata = this.metadata, callback = undefined) {_OPEN_BRCK}\n\t\t{rpc_impl}\n\t{_CLOSING_BRCK}"
                        )

            rpcs = "\n\n\t".join(rpcs)
        return "".join(rpcs)


class SylkClientGo:
    """A helper class to write 'Go' language clients for sylk.build project services"""

    def __init__(
        self,
        project_package,
        services=None,
        packages=None,
        context: SylkContext = None,
        config=None,
        sylk_json: SylkJson = None,
        pre_data=None
    ):
        self._services = services
        self._project_package = project_package
        self._context = context
        self._packages = packages
        self._config = config
        self._sylk_json = sylk_json
        for s in self._services:
            svc_name = s.get('name')
            svc_code = f"{self.write_imports(s)}{self.write_struct(s)}{self.write_new(s)}{self.write_methods(s)}"
            svc_ver = parse_version_component(s.get('fullName'))
            if svc_ver is not None:
                svc_ver = f"v{svc_ver.get('version')}{svc_ver.get('channel') if svc_ver.get('channel') is not None else ''}{svc_ver.get('release') if svc_ver.get('release') is not None else ''}"
                file_system.wFile(
                    file_system.join_path(
                        sylk_json.path,
                        self._sylk_json.code_base_path,
                        "clients",
                        "go",
                        svc_name,
                        svc_ver,
                        f"{svc_name}.go",
                    ),
                    svc_code,
                    overwrite=True,
                    force=True,
                )
            else:
                file_system.wFile(
                    file_system.join_path(
                        self._sylk_json.path,
                        self._sylk_json.code_base_path,
                        "clients",
                        "go",
                        svc_name,
                        f"{svc_name}.go",
                    ),
                    svc_code,
                    overwrite=True,
                    force=True,
                )

    def _camelize_string(self,s):
        words = s.split('_')
        return words[0][0].upper() + words[0][1:] + ''.join(word.title() for word in words[1:])


    def write_imports(self, s):
        list_of_services = ["// Importing services"]
        list_of_packages = ["// Importing packages"]

        files = self._sylk_json._proto_tree.get_all_file_paths()
        imports = []
        go_package_path = self._sylk_json.project.get("goPackage")
        code_base_path = self._sylk_json.code_base_path + '/' if self._sylk_json.code_base_path is not None and self._sylk_json.code_base_path != '' else ''
        for mod in files:
            mod_path = '.'.join(mod.split('/')[:-1])
            mod_name = mod.split('/')[-1].split('.')[0]
            ver = self._sylk_json._proto_tree._parse_version_component(mod_path)
            if ver is not None:
                version = mod_path.split('.')[-1]
            else:
                mod_path = '.'.join(mod.split('/')[:-1])+'.'+self._camelize_string(mod.split('/')[-1].split('.')[0])
                version = ''
            if mod_path.split('.')[0] != self._sylk_json._proto_tree.root.name:
                base_protos = ''
                root = self._sylk_json._proto_tree.proto_modules[mod_path.split('.')[0]].root
                dep_parent = self._sylk_json._proto_tree.proto_modules[mod_path.split('.')[0]].get_parent(mod_path)
                msg_dep =self._sylk_json._proto_tree._find_node(mod_path,root) 
                if msg_dep is not None:
                    if parse_version_component(dep_parent.full_path) is not None:
                        temp_name = msg_dep.full_path.split('.')[-2]
                    else:
                        temp_name = msg_dep.name
                    dep_mod_name = temp_name if msg_dep.properties.get('tag') is None or msg_dep.properties.get('tag') == '' else msg_dep.properties.get('tag')
                    if "google.protobuf" in mod_path:
                        imp_path = f'{dep_mod_name}pb "google.golang.org/protobuf/types/known/{dep_mod_name}pb"'
                        if imp_path not in imports:
                            imports.append(imp_path)
                    else:
                        imp_path = f'"{base_protos}{mod_path.replace(".","/")}"' 
                        if imp_path not in imports:
                            imports.append(imp_path)
            else:
                base_protos = f'{self._sylk_json._root_protos}/' if self._sylk_json._root_protos is not None and self._sylk_json._root_protos != '' else ''
                imp_path = f'"{go_package_path}/{code_base_path}services/{base_protos}{mod_path.replace(".","/")}"' 
                if imp_path not in imports:
                    imports.append(imp_path)

        # svc_domain = self._services[s].get("fullName").split(".")[0]
        svc_name = s.get("name")
        svc_ver = parse_version_component(s.get("fullName"))
        if svc_ver is not None:
            svc_ver = f'v{svc_ver.get("version")}{svc_ver.get("channel") if svc_ver.get("channel") is not None else ""}{svc_ver.get("release") if svc_ver.get("release") is not None else ""}'
        else:
            svc_ver = ''
        # svc_path = '{4} "{0}/services/protos/{1}/{2}/{3}"'.format(
        #     self._sylk_json.project.get("goPackage"),
        #     svc_domain,
        #     svc_name,
        #     svc_ver,
        #     svc_name + svc_ver,
        # )
        # list_of_services.append(svc_path)
        # if s.get("dependencies") is not None:
        #     for dep in s.get("dependencies"):
        #         if "google.protobuf" in dep:
        #             dep_name = dep.split(".")[-1].lower()
        #             list_of_services.append(
        #                 f'{dep_name}pb "google.golang.org/protobuf/types/known/{dep_name}pb"'
        #             )

        # for p in self._packages:
        #     pkg_domain = self._packages[p].get("package").split(".")[0]
        #     pkg_name = self._packages[p].get("package").split(".")[1]
        #     pkg_ver = self._packages[p].get("package").split(".")[2]
        #     pkg_path = '{4} "{0}/services/protos/{1}/{2}/{3}"'.format(
        #         self._sylk_json.project.get("goPackage"),
        #         pkg_domain,
        #         pkg_name,
        #         pkg_ver,
        #         pkg_name + pkg_ver,
        #     )
        #     if pkg_path not in list_of_services:
        #         list_of_packages.append(pkg_path)
        #     if self._packages[p].get("dependencies") is not None:
        #         for dep in self._packages[p].get("dependencies"):
        #             if "google.protobuf" in dep:
        #                 dep_name = dep.split(".")[-1].lower()
        #                 list_of_packages.append(
        #                     f'{dep_name}pb "google.golang.org/protobuf/types/known/{dep_name}pb"'
        #                 )

        _sylk_conn_builder = '\tsylkChannel "{}/{}clients/go/utils"'.format(
            self._sylk_json.project.get("goPackage"),
            code_base_path
        )
        _default_imports = [
            '"fmt"',
            '"io"',
            '"context"',
            '"log"',
            '"time"',
            '"google.golang.org/grpc"',
            '"google.golang.org/grpc/credentials/insecure"',
            '"google.golang.org/grpc/metadata"',
            "\n",
            _sylk_conn_builder,
            "\n\t".join(list_of_services),
            "\n\t".join(list_of_packages),
            "\n\t".join(imports)
        ]

        return "package {}\n\nimport (\n\t{}\n)".format(
            svc_name + svc_ver, "\n\t".join(_default_imports)
        )

    # def write_types(self):
    #     struct_values = []
    #     for p in self._sylk_json.packages:
    #         temp_pkg = self._sylk_json.packages[p]

    #         if temp_pkg.get('messages'):
    #             for m in temp_pkg.get('messages'):
    #                 msg_name = m.get('name')
    #                 msg_go_name = msg_name[0].upper() + msg_name[1:]
    #                 struct_values.append('{} {}.{}'.format(msg_go_name,m.get('fullName').split('.')[1],msg_go_name))

    #         if temp_pkg.get('enums'):
    #             for e in temp_pkg.get('enums'):
    #                 enm_name = e.get('name')
    #                 enm_go_name = enm_name[0].upper() + enm_name[1:]
    #                 struct_values.append('{} {}.{}'.format(enm_go_name,m.get('fullName').split('.')[1],enm_go_name))

    #     struct_values = '\n\t'.join(struct_values)
    #     return '\n\ntype (\n\t{2}\n{1}\n'.format(_OPEN_BRCK,_CLOSING_BRCK,struct_values)

    def write_struct(self, s):
        client_options = [
            "host string // Host name should be a valid ip or domain",
            "port int // Port that been served by the host",
            "dialOpts []grpc.DialOption // Connection dial options",
            "callOpts []grpc.CallOption // Connection call options",
            "md metadata.MD // Global metadata",
            "ctx context.Context // Global context",
            "conn *grpc.ClientConn // A client connection object",
        ]
        s_name = s.get('name')
        temp_svc = (
            s_name[0].upper()
            + s_name[1:]
        )
        temp_lower_svc = s_name.lower()
        svc_name = s_name
        svc_ver = parse_version_component(s.get('fullName'))
        if svc_ver is not None: 
            svc_ver = f"v{svc_ver.get('version')}{svc_ver.get('channel') if svc_ver.get('channel') is not None else ''}{svc_ver.get('release') if svc_ver.get('release') is not None else ''}"
            pkg_name = s.get('fullName').split('.')[-3]
        else:
            pkg_name = s.get('fullName').split('.')[-2]
            svc_ver = ''
        client_options.append(f"{temp_lower_svc} {pkg_name}{svc_ver}.{temp_svc}Client")
        return "\n\n// '{0}' represents the project services facing client side\ntype {0} struct {1}\n\t{2}\n{3}\n\n".format(
            svc_name, _OPEN_BRCK, "\n\t".join(client_options), _CLOSING_BRCK
        )

    def write_new(self, s):
        _list_of_services_clients = []
        _temp_svc_list = []
        _list_of_client_opts = [
            "host string",
            "port int",
            "dialOpts []grpc.DialOption",
            "callOpts []grpc.CallOption",
            "md metadata.MD",
            "ctx context.Context",
        ]
        _list_of_client_opts_none_types = []

        for i in _list_of_client_opts:
            _list_of_client_opts_none_types.append(i.split()[0])

        svc_name = s.get('name')
        temp_service = svc_name[0].upper() + svc_name[1:]
        svc_ver = parse_version_component(s.get('fullName'))
        if svc_ver is not None: 
            pkg_name = s.get('fullName').split('.')[-3]
            svc_ver = f"v{svc_ver.get('version')}{svc_ver.get('channel') if svc_ver.get('channel') is not None else ''}{svc_ver.get('release') if svc_ver.get('release') is not None else ''}"
        else:
            pkg_name = s.get('fullName').split('.')[-2]
            svc_ver = ''
        _list_of_services_clients.append(
            "{0}Client := {1}{3}.New{2}Client(conn)".format(
                svc_name.lower(), pkg_name, temp_service, svc_ver
            )
        )
        _temp_svc_list.append("{0}Client".format(svc_name.lower()))

        _new_client_init = [
            "\n\n\tif len(dialOpts) == 0 {\n\t\tdialOpts = DefaultDialOpts\n\t}",
            '\n\n\tif host == "" {}\n\t\thost = DefaultHost\n\t{}'.format(
                _OPEN_BRCK, _CLOSING_BRCK
            ),
            "\n\n\tif port == 0 {}\n\t\tport = DefaultPort\n\t{}".format(
                _OPEN_BRCK, _CLOSING_BRCK
            ),
            "\n\n\tif md == nil {0}\n\t\tmd = DefaultMetadata\n\t{1} else {0}\n\t\tmd = metadata.Join(md, DefaultMetadata)\n\t{1}".format(
                _OPEN_BRCK, _CLOSING_BRCK
            ),
            "\n\n\tif ctx == nil {}\n\t\tctx = DefaultCtx\n\t{}".format(
                _OPEN_BRCK, _CLOSING_BRCK
            ),
            "\n\tctx = metadata.NewOutgoingContext(ctx, md)",
            "\n\n\tlog.SetFlags(log.Lshortfile + log.Ltime)",
            "\n\n\tconnBuilder := sylkChannel.GrpcConnBuilder{}{}".format(
                _OPEN_BRCK, _CLOSING_BRCK
            ),
            "\n\n\tconnBuilder.WithContext(ctx)",
            "\n\tconnBuilder.WithOptions(dialOpts...)",
            '\n\t// Dailing to client target\n\tconn, err := connBuilder.GetConn(fmt.Sprintf("%s:%d", host, port))',
            '\n\tif err != nil {}\n\t\tlog.Fatalf("fail to dial: %v", err)\n\t{}'.format(
                _OPEN_BRCK, _CLOSING_BRCK
            ),
            "\n",
            "\n\t".join(_list_of_services_clients),
            "\n\tc := &{0}{1}{2}, conn, {3}{4}".format(
                svc_name,
                _OPEN_BRCK,
                ", ".join(_list_of_client_opts_none_types),
                ", ".join(_temp_svc_list),
                _CLOSING_BRCK,
            ),
            "\n\treturn c",
        ]
        default_client = "// Default returns the standard client used by the project-level services RPC's.\nfunc Defualt() *{} {} return std {}".format(
            svc_name, _OPEN_BRCK, _CLOSING_BRCK
        )
        return '// Initalize default constants\n\nvar (\n\tDefaultMsgSize  = 1024 * 1024 * 50 // Max Recv / Send message 50MB as default\n\tDefaultHost = "localhost"\n\tDefaultPort = 44880\n\tDefaultDialOpts = []grpc.DialOption{2}\n\t\tgrpc.WithTransportCredentials(insecure.NewCredentials()),\n\t\tgrpc.WithDefaultCallOptions(\n\t\t\tgrpc.MaxCallRecvMsgSize(DefaultMsgSize),\n\t\t\tgrpc.MaxCallSendMsgSize(DefaultMsgSize)),\n\t{4}\n\tDefaultCallOpts = []grpc.CallOption{2}{4}\n\tDefaultMetadata = metadata.Pairs("sylk-version","{6}",)\n\tDefaultCtx = context.Background()\n\tstd = New(DefaultHost, DefaultPort, DefaultDialOpts, DefaultCallOpts, DefaultMetadata, DefaultCtx)\n)\n\n{5}\n// Create new client stub\nfunc New({0}) *{1} {2}\n{3}\n{4}'.format(
            ", ".join(_list_of_client_opts),
            svc_name,
            _OPEN_BRCK,
            "".join(_new_client_init),
            _CLOSING_BRCK,
            default_client,
            __version__.__version__,
        )

    def write_methods(self, s):
        list_of_rpcs = []
        svc = s
        svc_name = s.get('name')
        for r in svc.get("methods"):
            root = self._sylk_json._proto_tree.root
            if r.get("inputType").split('.')[0] != root.name:
                root = self._sylk_json._proto_tree.proto_modules[r.get("inputType").split('.')[0]].root

            ref_node = self._sylk_json._proto_tree._find_node(r.get("inputType"),root)
            ref_node_parent = self._sylk_json._proto_tree.get_parent(ref_node.full_path)
            pkg_ver = parse_version_component(ref_node_parent.full_path)
            if pkg_ver is not None:
                ref_node_parent = self._sylk_json._proto_tree.get_parent(ref_node_parent.full_path)
                rpc_msg_in_pkg = ref_node_parent.name + f'v{pkg_ver.get("version")}{pkg_ver.get("channel") if pkg_ver.get("channel") is not None else ""}{pkg_ver.get("release") if pkg_ver.get("release") is not None else ""}'
            else:
                rpc_msg_in_pkg = ref_node_parent.full_path.split('.')[-1]
            
            rpc_msg_input_type = (
                r.get("inputType").split(".")[-1][0].upper()
                + r.get("inputType").split(".")[-1][1:]
            )
            if "google.protobuf" in r.get("inputType"):
                well_known = r.get("inputType").split(".")[-1].lower()
                rpc_msg_in_pkg = f"{well_known}pb"
            root= self._sylk_json._proto_tree.root
            if r.get("outputType").split('.')[0] != root.name:
                root = self._sylk_json._proto_tree.proto_modules[r.get("outputType").split('.')[0]].root
            ref_node = self._sylk_json._proto_tree._find_node(r.get("outputType"),root)
            ref_node_parent = self._sylk_json._proto_tree.get_parent(ref_node.full_path)
            pkg_ver = parse_version_component(ref_node_parent.full_path)
            if pkg_ver is not None:
                ref_node_parent = self._sylk_json._proto_tree.get_parent(ref_node_parent.full_path)
                rpc_msg_out_pkg = ref_node_parent.name + f'v{pkg_ver.get("version")}{pkg_ver.get("channel") if pkg_ver.get("channel") is not None else ""}{pkg_ver.get("release") if pkg_ver.get("release") is not None else ""}'
            else:
                rpc_msg_out_pkg = ref_node_parent.full_path.split('.')[-1]
            
            rpc_msg_output_type = (
                r.get("outputType").split(".")[-1][0].upper()
                + r.get("outputType").split(".")[-1][1:]
            )
            if "google.protobuf" in r.get("outputType"):
                well_known = r.get("outputType").split(".")[-1].lower()
                rpc_msg_out_pkg = f"{well_known}pb"
            rpc_client_stream = (
                r.get("clientStreaming")
                if r.get("clientStreaming") is not None
                else False
            )
            rpc_server_stream = (
                r.get("serverStreaming")
                if r.get("serverStreaming") is not None
                else False
            )
            rpc_name = r.get("name")[0].upper() + r.get("name")[1:]
            # Unary
            if rpc_server_stream == False and rpc_client_stream == False:
                list_of_rpcs.append(
                    '\n\n// [sylk.build] - {10}.{1}\n// Description: {9}\n// Read: https://www.sylk.build/docs/go/unary-call\nfunc (c *{0}) {1}(message *{2}.{3}) (*{7}.{8}, metadata.MD, metadata.MD) {4}\n\tlog.Printf("Calling {1} %v", message)\n\n\tctx, cancel := context.WithTimeout(c.ctx, 10*time.Second)\n\n\tdefer cancel()\n\n\tvar header, trailer metadata.MD\n\n\tresponse, err := c.{5}.{1}(ctx, message, grpc.Header(&header), grpc.Trailer(&trailer))\n\n\tif err != nil {4}\n\t\tlog.Printf("Client call {1} failed: %v", err)\n\t{6}\n\n\treturn response, header, trailer\n{6}'.format(
                        svc_name,
                        rpc_name,
                        rpc_msg_in_pkg,
                        rpc_msg_input_type,
                        _OPEN_BRCK,
                        svc_name.lower(),
                        _CLOSING_BRCK,
                        rpc_msg_out_pkg,
                        rpc_msg_output_type,
                        r.get("description"),
                        s.get('fullName'),
                    )
                )
            # Client stream
            elif rpc_client_stream == True and rpc_server_stream == False:
                list_of_rpcs.append(
                    '\n\n// [sylk.build] - {10}.{1}\n// Description: {9}\n// Read: https://www.sylk.build/docs/go/client-stream\nfunc (c *{0}) {1}(messages []*{2}.{3}) *{7}.{8} {4}\n\tlog.Printf("Calling {1} %v", messages)\n\n\tctx, cancel := context.WithTimeout(c.ctx, 10*time.Second)\n\n\tdefer cancel()\n\n\tstream, err := c.{5}.{1}(ctx)\n\n\tif err != nil {4}\n\t\tlog.Printf("Client call {1} failed: %v", err)\n\t{6}\n\n\tfor _, message := range messages {4}\n\t\tif err := stream.Send(message); err != nil {4}\n\t\t\tlog.Printf("Client sending message %v stream failed: %v", message, err)\n\t\t{6}\n\t{6}\n\tresponse, err := stream.CloseAndRecv()\n\tif err != nil {4}\n\t\tlog.Printf("Client stream failed on getting response: %v", err)\n\t{6}\n\n\treturn response\n{6}'.format(
                        svc_name,
                        rpc_name,
                        rpc_msg_in_pkg,
                        rpc_msg_input_type,
                        _OPEN_BRCK,
                        svc_name.lower(),
                        _CLOSING_BRCK,
                        rpc_msg_out_pkg,
                        rpc_msg_output_type,
                        r.get("description"),
                        s.get('fullName'),
                    )
                )
            # Server stream
            elif rpc_client_stream == False and rpc_server_stream == True:
                list_of_rpcs.append(
                    '\n\n// sylk.build - {10}.{1}\n// Description: {9}\n// Read: https://www.sylk.build/docs/go/server-stream\nfunc (c *{0}) {1}(message *{2}.{3}, serverStream chan<- *{7}.{8}, done chan struct{4}{6}) {4}\n\tlog.Printf("Calling {1} %v", message)\n\n\tctx, cancel := context.WithTimeout(c.ctx, 10*time.Second)\n\n\tdefer cancel()\n\n\tstream, err := c.{5}.{1}(ctx, message)\n\n\tif err != nil {4}\n\t\tlog.Printf("Client call {1} failed: %v", err)\n\t{6}\n\n\tdefer stream.CloseSend()\n\tfor {4}\n\t\tselect {4}\n\t\tcase <-done:\n\t\t\treturn\n\t\tdefault:\n\t\t\tpayload, err := stream.Recv()\n\t\t\tif err != nil {4}\n\t\t\t\tlog.Fatalf("Failed to recieve data: %v", err)\n\t\t\t{6}\n\n\t\t\t// Send the recieved paylod to the main goroutine via the serverStream channel\n\t\t\tserverStream <- payload\n\t\t{6}\n\t{6}\n{6}'.format(
                        svc_name,
                        rpc_name,
                        rpc_msg_in_pkg,
                        rpc_msg_input_type,
                        _OPEN_BRCK,
                        svc_name.lower(),
                        _CLOSING_BRCK,
                        rpc_msg_out_pkg,
                        rpc_msg_output_type,
                        r.get("description"),
                        s.get('fullName'),
                    )
                )
            # BidiStream
            elif rpc_client_stream and rpc_server_stream:
                list_of_rpcs.append(
                    '\n\n// sylk.build - {10}.{1}\n// Description: {9}\n// Read: https://www.sylk.build/docs/go/bidi-stream\nfunc (c *{0}) {1}(messages []*{2}.{3}) []*{7}.{8} {4}\n\tlog.Printf("Calling {1} %v", message)\n\n\tctx, cancel := context.WithTimeout(c.ctx, 10*time.Second)\n\n\tdefer cancel()\n\n\tstream, err := c.{5}.{1}(ctx)\n\n\tif err != nil {4}\n\t\tlog.Printf("Client call {1} failed: %v", err)\n\t{6}\n\n\tvar listResponses []*{7}.{8}\n\n\twaitc := make(chan struct{4}{6})\n\n\tgo func() {4}\n\t\tfor {4}\n\t\t\t{8}, err := stream.Recv()\n\t\t\tif err == io.EOF {4}\n\t\t\t\tclose(waitc)\n\t\t\t\tbreak\n\t\t\t{6}\n\t\t\tif err != nil {4}\n\t\t\t\tlog.Printf("Client call {1} stream message failed: %v", err)\n\t\t\t{6}\n\t\t\tlistResponses = append(listResponses, {8})\n\t\t{6}\n\t{6}()\n\tfor _, message := range messages {4}\n\t\tif err := stream.Send(message); err != nil {4}\n\t\t\tlog.Printf("Client.{1} stream.Send(%v) failed: %v", message, err)\n\t\t{6}\n\t{6}\n\tstream.CloseSend()\n\t<-waitc\n\treturn listResponses\n{6}'.format(
                        svc_name,
                        rpc_name,
                        rpc_msg_in_pkg,
                        rpc_msg_input_type,
                        _OPEN_BRCK,
                        svc_name.lower(),
                        _CLOSING_BRCK,
                        rpc_msg_out_pkg,
                        rpc_msg_output_type,
                        r.get("description"),
                        s.get('fullName'),
                    )
                )

        return "\n\n".join(list_of_rpcs)


class SylkServiceGo:
    """A helper class to write 'Go' language services for sylk.build project services"""

    def __init__(
        self,
        project_package,
        name,
        imports=[],
        service=None,
        package=None,
        messages=[],
        enums=[],
        context: SylkContext = None,
        sylk_json: SylkJson = None,
    ):
        self._name = name
        self._imports = imports
        self._service = service
        self._project_package = project_package
        self._context = context
        self._sylk_json = sylk_json
        self._service_name = self._name.split("/")[-1].split(".")[0]
        self._service_path = ".".join(self._name.split("/")[:-1])

    def write_imports(self):
        list_d = list(map(lambda i: i, _WELL_KNOWN_GO_IMPORTS))
        parent = self._sylk_json._proto_tree.get_parent(self._service.get('fullName'))
        refs = self._sylk_json._proto_tree.get_parents_refs([self._service.get('fullName')])
        code_base_path = self._sylk_json.code_base_path +'/' if self._sylk_json.code_base_path is not None and self._sylk_json.code_base_path != '' else ''
        deps = self._sylk_json._proto_tree.get_references(self._service.get('fullName'))
       
        pkg_ver = self._sylk_json._proto_tree._parse_version_component(parent.full_path)
        if pkg_ver is not None:
            pkg_ver = f'v{pkg_ver.get("version")}{pkg_ver.get("channel","") if pkg_ver.get("channel","") is not None else ""}{pkg_ver.get("release","") if pkg_ver.get("release","") is not None else ""}'
            pkg_name = parent.full_path.split('.')[-2]
        else:
            pkg_ver = ''
            pkg_name = parent.name
        module_name = pkg_name if self._service.get('tag') is None and self._service.get('tag') != '' else self._service.get('tag')
        base_protos = self._sylk_json._root_protos.replace('/','.')
        go_package_name = self._sylk_json.project.get("goPackage")
        
        for d in deps:
            if d.split('.')[0] == self._sylk_json._proto_tree.root.name:
                root = self._sylk_json._proto_tree.root
                dep_parent = self._sylk_json._proto_tree.get_parent(d)
                base_path = f'{go_package_name}/{code_base_path}services/' if self._sylk_json._root_protos is None or self._sylk_json._root_protos == '' else f'{go_package_name}/{code_base_path}services/{base_protos}/'
                msg_dep =self._sylk_json._proto_tree._find_node(d,root) 
                dep_mod_version = parse_version_component(dep_parent.full_path)
                if dep_mod_version is not None:
                    channel = dep_mod_version.get("channel","") if dep_mod_version.get("channel") is not None else ''
                    release = dep_mod_version.get("release","") if dep_mod_version.get("release") is not None else ''
                    dep_mod_version = f'v{dep_mod_version.get("version")}{channel}{release}'
                    temp_name = dep_parent.full_path.split('.')[-2]
                else:
                    temp_name = dep_parent.name
                    dep_mod_version = ''
                dep_mod_name = temp_name if msg_dep.properties.get('tag') is None or msg_dep.properties.get('tag') == '' else msg_dep.properties.get('tag')
                imp_path = f'{dep_mod_name}{dep_mod_version} "{base_path}{dep_parent.full_path.replace(".","/")}"'
            else:
                root = self._sylk_json._proto_tree.proto_modules[d.split('.')[0]].root
                dep_parent = self._sylk_json._proto_tree.proto_modules[d.split('.')[0]].get_parent(d)
                msg_dep =self._sylk_json._proto_tree._find_node(d,root) 
                dep_parent_version = parse_version_component(dep_parent.full_path)
                if dep_parent_version is not None:
                    channel = dep_mod_version.get("channel","") if dep_mod_version.get("channel") is not None else ''
                    release = dep_mod_version.get("release","") if dep_mod_version.get("release") is not None else ''
                    dep_mod_version = f'v{dep_mod_version.get("version")}{channel}{release}'
                    temp_name = dep_parent.full_path.split('.')[-2]
                else:
                    temp_name = dep_parent.name
                    dep_parent_version = ""
                dep_mod_name = temp_name if msg_dep.properties.get('tag') is None or msg_dep.properties.get('tag') == '' else msg_dep.properties.get('tag')
                imp_path = f'{dep_mod_name}{dep_parent_version} "{dep_parent.full_path.replace(".","/")}"'
                if 'google.protobuf' in dep_parent.full_path:
                    imp_path = f'{dep_mod_name}pb "google.golang.org/protobuf/types/known/{dep_mod_name}pb"'
            if imp_path not in list_d:
                list_d.append(
                    imp_path
                )
        base_path = f'{go_package_name}/{code_base_path}services/' if self._sylk_json._root_protos is None or self._sylk_json._root_protos == '' else f'{go_package_name}/{code_base_path}services/{base_protos}/'
        imp_path = f'{module_name}{pkg_ver} "{base_path}{parent.full_path.replace(".","/")}"'
        
        if imp_path not in list_d:
            list_d.append(
                    imp_path
                )
        list_d.append(f'"{go_package_name}/{code_base_path}services/utils"')
        list_d = "\n".join(list_d)
        return f"{list_d}"
        # # 
        # if self._imports is not None:
        #     go_package_name = self._sylk_json.project.get("goPackage")
        #     name = self._name.split("/")[-1].split(".")[0]
        #     path = "/".join(self._name.split("/")[:-1])
        #     ver = self._name.split("/")[-2]
        #     list_d.append(f'{name}{ver} "{go_package_name}/services/{path}"')
        #     list_d.append(f'"{go_package_name}/services/utils"')

        #     for d in self._imports:
        #         if "google.protobuf." in d:
        #             name = d.split(".")[-1]
        #             d_name = "{0}".format(name).lower()
        #             list_d.append(
        #                 f'"google.golang.org/protobuf/types/known/{d_name}pb"'
        #             )
        #         else:
        #             name = d.split(".")[1]
        #             d_name = "{0}".format(name)
        #             d_path = self._sylk_json.get_path(
        #                 d.split(".")[0], d.split(".")[1], d.split(".")[2]
        #             )
        #             path = "/".join(d_path.split("/")[:-1])
        #             d_ver = d.split(".")[2]
        #             list_d.append(
        #                 f'{d_name}{d_ver} "{go_package_name}/services/{path}"'
        #             )

        #     list_d = "\n\t".join(list_d)
        #     return f"{list_d}"
        # else:
        #     # When service is standalone we need to make sure that the defaults packages are imported
        #     go_package_name = self._sylk_json.project.get("goPackage")
        #     name = self._name.split("/")[-1].split(".")[0]
        #     path = "/".join(self._name.split("/")[:-1])
        #     ver = self._name.split("/")[-2]
        #     list_d.append(f'{name}{ver} "{go_package_name}/services/{path}"')
        #     list_d = "\n\t".join(list_d)
        #     return f"{list_d}"

    def write_struct(self):
        ver = parse_version_component(self._service.get('fullName'))
        if ver is not None:
            ver = f'v{ver.get("version")}{ver.get("channel") if ver.get("channel") is not None else ""}{ver.get("release") if ver.get("release") is not None else ""}'
        else:
            ver = ''
        name = self._name
        temp_name = name[0].capitalize() + name[1:]
        ver = parse_version_component(self._service.get('fullName'))
        if ver is not None:
            ver = f'v{ver.get("version")}{ver.get("channel") if ver.get("channel") is not None else ""}{ver.get("release") if ver.get("release") is not None else ""}'
            svc_name = self._service.get('fullName').split('.')[-3] + ver
        else:
            svc_name = self._service.get('fullName').split('.')[-2]
        dep_mod_name = svc_name if self._service.get('tag') is None or self._service.get('tag') == '' else self._service.get('tag')

        return "type {0} struct {1}\n\t{3}.Unimplemented{0}Server\n{2}".format(
            temp_name, _OPEN_BRCK, _CLOSING_BRCK, dep_mod_name
        )

    def write_methods(self):
        name = self._name.split("/")[-1].split(".")[0]
        temp_name = name[0].capitalize() + name[1:]
        list_of_rpcs = []
        for rpc in self._service.get("methods"):
            rpc_temp_name = rpc.get("name")[0].capitalize() + rpc.get("name")[1:]
            rpc_output_type = (
                rpc.get("serverStreaming")
                if rpc.get("serverStreaming") is not None
                else False
            )
            rpc_input_type = (
                rpc.get("clientStreaming")
                if rpc.get("clientStreaming") is not None
                else False
            )
            rpc_input_name = rpc.get("inputType").split(".")[-1]
            if "google.protobuf." in rpc.get("inputType"):
                rpc_input_package_name = "{0}pb".format(
                    rpc.get("inputType").split(".")[-1]
                ).lower()
            else:
                ver = parse_version_component(rpc.get("inputType"))
                ref_node = self._sylk_json._proto_tree.get_parent(rpc.get("inputType"))
                if ver is not None:
                    ver = f'v{ver.get("version")}{ver.get("channel") if ver.get("channel") is not None else ""}{ver.get("release") if ver.get("release") is not None else ""}'
                    pkg_name = ref_node.full_path.split('.')[-2]
                else:
                    pkg_name = ref_node.name
                    ver = ''
                dep_mod_name = pkg_name if ref_node.properties.get('tag') is None or ref_node.properties.get('tag') == '' else ref_node.properties.get('tag')
                rpc_input_package_name = (
                    dep_mod_name
                    + ver
                )
            rpc_output_name = rpc.get("outputType").split(".")[-1]
            if "google.protobuf." in rpc.get("outputType"):
                rpc_output_package_name = "{0}pb".format(
                    rpc.get("outputType").split(".")[-1]
                ).lower()
            else:
                ver = parse_version_component(rpc.get("outputType"))
                ref_node = self._sylk_json._proto_tree.get_parent(rpc.get("outputType"))
                if ver is not None:
                    ver = f'v{ver.get("version")}{ver.get("channel") if ver.get("channel") is not None else ""}{ver.get("release") if ver.get("release") is not None else ""}'
                    pkg_name = ref_node.full_path.split('.')[-2]
                else:
                    pkg_name = ref_node.name
                    ver = ''
                dep_mod_name = pkg_name if ref_node.properties.get('tag') is None or ref_node.properties.get('tag') == '' else ref_node.properties.get('tag')
                rpc_output_package_name = (
                    dep_mod_name
                    + ver
                )
            temp_go_rpc_input_name = rpc_input_name[0].capitalize() + rpc_input_name[1:]
            temp_go_rpc_output_name = (
                rpc_output_name[0].capitalize() + rpc_output_name[1:]
            )
            rpc_description = rpc.get("description")

            # Unary
            if rpc_output_type == False and rpc_input_type == False:
                list_of_rpcs.append(
                    "\n".join(
                        [
                            f"\n\n// [sylk.build] - {name}.{rpc_temp_name} - {rpc_description}",
                            f"func ({name}Servicer *{temp_name}) {rpc_temp_name}(ctx context.Context, {rpc_input_name} *{rpc_input_package_name}.{temp_go_rpc_input_name}) (response *{rpc_output_package_name}.{temp_go_rpc_output_name}, err error) {_OPEN_BRCK}",
                            f'\tprintLog("{rpc_temp_name}",ctx, {rpc_input_name})',
                            f"\treturn &{rpc_output_package_name}.{temp_go_rpc_output_name}{_OPEN_BRCK}{_CLOSING_BRCK}, nil",
                            f"{_CLOSING_BRCK}",
                        ]
                    )
                )
            # Client stream
            elif rpc_input_type == True and rpc_output_type == False:
                list_of_rpcs.append(
                    "\n".join(
                        [
                            f"\n\n// [sylk.build] - {name}.{rpc_temp_name} - {rpc_description}",
                            f"func ({name}Servicer *{temp_name}) {rpc_temp_name}(stream {rpc_output_package_name}.{temp_name}_{rpc_temp_name}Server) (err error) {_OPEN_BRCK}",
                            f'\tprintLog("{rpc_temp_name}",stream.Context(), nil)',
                            f"\tfor {_OPEN_BRCK}",
                            f"\t\tclientStreamRequest, err := stream.Recv()",
                            f"\t\tif err == io.EOF {_OPEN_BRCK}",
                            f'\t\t\tutils.ErrorLogger.Printf("[{rpc_temp_name}] Client stream closed.")',
                            f"\t\t\tbreak",
                            f"\t\t{_CLOSING_BRCK}",
                            f"\t\tif err != nil {_OPEN_BRCK}",
                            f"\t\t\tutils.ErrorLogger.Printf(\"[{rpc_temp_name}] Client stream Request error: '%v'.\", err)",
                            f"\t\t\treturn stream.SendAndClose(&{rpc_output_package_name}.{temp_go_rpc_output_name}{_OPEN_BRCK}{_CLOSING_BRCK})",
                            f"\t\t{_CLOSING_BRCK}",
                            f"\t\t// Do something with incoming object",
                            f"\t\tutils.InfoLogger.Printf(\"[{rpc_temp_name}] Request received: '%v'.\", clientStreamRequest)",
                            f"\t{_CLOSING_BRCK}",
                            f"\treturn stream.SendAndClose(&{rpc_output_package_name}.{temp_go_rpc_output_name}{_OPEN_BRCK}{_CLOSING_BRCK})",
                            f"{_CLOSING_BRCK}",
                        ]
                    )
                )
            # Server stream
            elif rpc_input_type == False and rpc_output_type == True:
                list_of_rpcs.append(
                    "\n".join(
                        [
                            f"\n\n// [sylk.build] - {name}.{rpc_temp_name} - {rpc_description}",
                            f"func ({name}Servicer *{temp_name}) {rpc_temp_name}({rpc_input_name} *{rpc_input_package_name}.{temp_go_rpc_input_name}, stream {rpc_output_package_name}.{temp_name}_{rpc_temp_name}Server) (err error) {_OPEN_BRCK}",
                            f'\tprintLog("{rpc_temp_name}",stream.Context(), nil)',
                            f"\t// Do loop for responses",
                            f"\treturn nil",
                            f"{_CLOSING_BRCK}",
                        ]
                    )
                )
            # BidiStream
            elif rpc_input_type and rpc_output_type:
                list_of_rpcs.append(
                    "\n".join(
                        [
                            f"\n\n// [sylk.build] - {name}.{rpc_temp_name} - {rpc_description}",
                            f"func ({name}Servicer *{temp_name}) {rpc_temp_name}(stream {name}Servicer.{temp_name}_{rpc_temp_name}Server) (err error) {_OPEN_BRCK}",
                            f'\tprintLog("{rpc_temp_name}",stream.Context(), nil)',
                            f"\tfor {_OPEN_BRCK}",
                            f"\t\tbidirectionalStreamRequest, err := stream.Recv()",
                            f"\t\tif err == io.EOF {_OPEN_BRCK}",
                            f'\t\t\tutils.ErrorLogger.Printf("[{rpc_temp_name}] Client stream closed.")',
                            f"\t\t\tbreak",
                            f"\t\t{_CLOSING_BRCK}",
                            f"\t\tif err != nil {_OPEN_BRCK}",
                            f"\t\t\tutils.ErrorLogger.Printf(\"[{rpc_temp_name}] Client stream Request error: '%v'.\", err)",
                            f"\t\t\treturn stream.Send(&{rpc_output_package_name}.{temp_go_rpc_output_name}{_OPEN_BRCK}{_CLOSING_BRCK})",
                            f"\t\t{_CLOSING_BRCK}",
                            f"\t\t// Do something with incoming object",
                            f"\t\tutils.InfoLogger.Printf(\"[{rpc_temp_name}] Request received: '%v'.\", bidirectionalStreamRequest)",
                            f"\t\tstream.Send(&{rpc_output_package_name}.{temp_go_rpc_output_name}{_OPEN_BRCK}{_CLOSING_BRCK})",
                            f"\t{_CLOSING_BRCK}",
                            "\treturn nil",
                            f"{_CLOSING_BRCK}",
                        ]
                    )
                )

        return "\n".join(list_of_rpcs)

    def write_log_func(self):
        return f'func printLog(name string, ctx context.Context, message interface{_OPEN_BRCK}{_CLOSING_BRCK}) {_OPEN_BRCK}\n\
\tcontextMetadata, _ := metadata.FromIncomingContext(ctx)\n\
\tutils.InfoLogger.Printf("[%s] Got RPC request: %v", name, message)\n\
\tutils.DebugLogger.Printf("[%s] Metadata: %v", name, contextMetadata)\n\
{_CLOSING_BRCK}'

    def to_str(self):
        return self.__str__()

    def __str__(self):
        name = self._name.split("/")[-1].split(".")[0]
        temp_svc_name = name[0].capitalize() + name[1:]
        return f"package {temp_svc_name}\n\nimport (\n\t{self.write_imports()}\n)\n\n{self.write_struct()}\n{self.write_methods()}\n\n{self.write_log_func()}"


class SylkServiceJs:
    """A helper class to write 'Typescript' language services for sylk.build project services"""

    def __init__(
        self,
        project_package,
        name,
        imports=[],
        service=None,
        package=None,
        messages=[],
        enums=[],
        context: SylkContext = None,
        sylk_json: SylkJson = None,
    ):
        self._name = name
        self._imports = imports
        self._service = service
        self._project_package = project_package
        self._context = context
        self._sylk_json = sylk_json

    def write_imports(self):
        return ""

    def write_class(self):
        rpcs = []
        if self._context is not None:
            functions = self._context.get_functions(self._name)
            if functions is not None:
                for func in functions:
                    func_code = func["code"]
                    rpcs.append(f"\t// @skip @@sylk - DO NOT REMOVE\n{func_code}")
        methods_exports = []
        methods_functions = []
        for rpc in self._service.get("methods"):
            rpc_name = rpc.get("name")
            args = f"call, callback"

            # if rpc_type_in and rpc_type_out:
            #     handleType = 'handleBidiStreamingCall'
            #     args = f'call, {rpc_out_pkg}.{rpc_out_name}>'
            # elif rpc_type_in and rpc_type_out == False:
            #     handleType = 'handleClientStreamingCall'
            #     args = f'call: ServerReadableStream<{rpc_in_pkg}.{rpc_in_name}, {rpc_out_pkg}.{rpc_out_name}>,\n\t\tcallback: sendUnaryData<{rpc_out_pkg}.{rpc_out_name}>'
            # elif rpc_type_in == False and rpc_type_out:
            #     handleType = 'handleServerStreamingCall'
            #     args = f'call: ServerWritableStream<{rpc_in_pkg}.{rpc_in_name}, {rpc_out_pkg}.{rpc_out_name}>'
            code = ""
            if self._context is not None:
                code = self._context.get_rpc(self._name, rpc_name)
                if code is not None:
                    code = code.get("code")
            temp_name = rpc_name[0].lower() + rpc_name[1:]
            methods.append(temp_name)
            rpcs.append(
                f"\t// @rpc @@sylk - DO NOT REMOVE\nconst {temp_name} = function({args}) {_OPEN_BRCK}\n\t\n\n{_CLOSING_BRCK}\n\n"
            )
            # rpcs.append(
            # f'\t// @rpc @@sylk - DO NOT REMOVE\n\t{temp_name}= ({args}) => {_OPEN_BRCK}\n{code}\n\t{_CLOSING_BRCK}\n')
        rpcs = "".join(rpcs)
        methods = ",\n\t".join(methods_exports)
        return (
            f"\n{rpcs}\n\nmodule.exports = {_OPEN_BRCK}\n\t{methods}\n{_CLOSING_BRCK};"
        )

    def to_str(self):
        return self.__str__()

    def __str__(self):
        return f"{self.write_imports()}\nconst protoDefinitions = protoLoader.loadSync(\n\t[...PROTO_PATHS],\n\t{_OPEN_BRCK}\n\t\tincluderDirs: [`${_OPEN_BRCK}__dirname{_CLOSING_BRCK}`],\n\t\tkeepCase:true,\n\t\tlongs: String,\n\t\tenums: String,\n\t\tdefaults: true,\n\t\toneofs: true,\n\t{_CLOSING_BRCK}\n);\nconst protos = grpc.loadPackageDefinition(protoDefinitions);{self.write_class()}"


def parse_code_file(file_content, seperator="@rpc"):
    log.debug(f"Parsing code file | seperator : {seperator}")
    # temp_lines = []
    # for lines in :
    #     drop_lines = False
    #     for line in lines:
    #         print(line)
    #         if nag in line:
    #             drop_lines = True

    #     if drop_lines == False:
    #         temp_lines.append(lines)

    return [
        list(g) for k, g in groupby(file_content, key=lambda x: seperator not in x) if k
    ][1:]


def validation(answers, current):
    if len(current) == 0:
        raise inquirerErrors.ValidationError(
            current, reason="Resource name must not be blank"
        )
    if len(re.findall("\s", current)) > 0:
        raise inquirerErrors.ValidationError(
            current, reason="Resource name must not include blank spaces"
        )
    if len(re.findall("-", current)) > 0:
        raise inquirerErrors.ValidationError(
            current,
            reason="Resource name must not include hyphens, underscores are allowed",
        )
    return True


def field_exists_validation(new_field, fields, msg):
    if new_field in fields:
        raise errors.SylkProtoError(
            "Message", f"Field {new_field} already exits under {msg}"
        )
    return True


def float_value_validate(answers, current):
    try:
        float(current)
    except Exception:
        raise inquirerErrors.ValidationError(
            current, reason="Value must be valid float type"
        )
    return True


def int_value_validate(answers, current):
    try:
        int(current)
    except Exception:
        raise inquirerErrors.ValidationError(
            current, reason="Value must be valid integer type"
        )
    return True


def enum_value_validate(answers, current):
    try:
        int(current)
    except Exception:
        raise errors.ValidationError(
            current, reason="Enum Value MUST be an integer value"
        )
    return True


# def send_analytic_event(args):
#     stub = sylkanalytics()
#     ts = Timestamp()
#     ts.GetCurrentTime()
#     temp_args = []
#     if hasattr(args, '__dict__'):
#         for k in args.__dict__:
#             temp_args.append(str((k,args.__dict__[k])))
#     else:
#         temp_args = [str((k, v)) for k, v in args.items()]
#     hostname=socket.gethostname()
#     # pretty.print_info(temp_args)
#     try:
#         stub.PublishCLIEvent(
#         SylkAnalytics_pb2.CLIEvent(
#             version=__version__.__version__,
#             ts=ts,
#             args=temp_args,
#             os=platform() if hasattr(config,'token') == False else config.token.split(':')[0],
#             user_id='UNKNWON:'+hostname if hasattr(config,'token') == False else config.token+':'+hostname
#             ))
#     except Exception as e:
#         pretty.print_warning(e)

_BUILTINS_TEMPLATES = Literal[
    "@sylk/Blank",
    "@sylk/SamplePy",
    "@sylk/SampleTs",
    "@sylk/PubSubTs",
    "@sylk/HelloWorldPy",
    "@sylk/HelloWorldTs",
]


def attach_template(ARCHITECT, template: _BUILTINS_TEMPLATES):
    if template != "@sylk/Blank":
        file_dir = os.path.dirname(__file__)
        template_domain_name = template.split("/")[0].split("@")[-1]
        template_name = template.split("/")[-1]
        pretty.print_note(
            file_dir
            + "/templates/{0}/{1}.template.py".format(
                template_domain_name, template_name
            )
        )
        os.chdir(ARCHITECT._path.split("sylk.json")[0])
        subprocess.run(
            [
                "python",
                file_dir
                + "/templates/{0}/{1}.template.py".format(
                    template_domain_name, template_name
                ),
                "--domain",
                ARCHITECT._domain,
                "--project-name",
                ARCHITECT._project_name,
            ]
        )


def parse_extension_to_proto(
    extension_type: Literal[
        "FileOptions",
        "MessageOptions",
        "FieldOptions",
        "ServiceOptions",
        "MethodOptions",
    ],
    extension_message,
    ext_key,
    ext_value,
    sylk_json,
):
    extension_value = None
    # Get current key to parse
    extension_field = next(
        (
            f
            for f in extension_message.get("fields")
            if f.get("name") == ext_key.split(".")[-1]
        ),
        None,
    )
    # Get type and label for the extension field
    type_ext = extension_field.get("fieldType").split("_")[-1].lower()
    label_ext = extension_field.get("label").split("_")[-1].lower()
    # Handle FileOptions extensions
    if extension_type == "FileOptions":
        if label_ext == "repeated":
            ext_values = []
            for v in ext_value:
                extension_value = parse_extension_value(
                    type_ext, v, sylk_json, extension_field
                )
                if extension_value is not None:
                    ext_values.append(f"option ({ext_key}) = {extension_value};")
            extension_value = "\n".join(ext_values)
        else:
            extension_value = parse_extension_value(
                type_ext, ext_value, sylk_json, extension_field
            )
            if extension_value is not None:
                extension_value = f"option {ext_key} = {extension_value};"

    elif extension_type == "MessageOptions":
        if label_ext == "repeated":
            pretty.print_error("Not supporting repeated MessageOptions")
            extension_value = ""
        else:
            extension_value = parse_extension_value(
                type_ext, ext_value, sylk_json, extension_field, 2
            )
            if extension_value is not None:
                extension_value = f"option ({ext_key}) = {extension_value};"

    elif extension_type == "FieldOptions":
        if label_ext == "repeated":
            pretty.print_error("Not supporting repeated FieldOptions")
            extension_value = ""
        else:
            extension_value = parse_extension_value(
                type_ext, ext_value, sylk_json, extension_field, 2
            )
            if extension_value is not None:
                extension_value = f"({ext_key}) = {extension_value}"
    elif extension_type == "ServiceOptions":
        if label_ext == "repeated":
            temp_value = []
            for v in ext_value:
                extension_value = parse_extension_value(
                    type_ext, v, sylk_json, extension_field, 2
                )
                if extension_value is not None:
                    temp_value.append(f"option ({ext_key}) = {extension_value};")

            extension_value = "\n\t".join(temp_value)
        else:
            extension_value = parse_extension_value(
                type_ext, ext_value, sylk_json, extension_field, 2
            )
            if extension_value is not None:
                extension_value = f"option ({ext_key}) = {extension_value};"
    elif extension_type == "MethodOptions":
        if label_ext == "repeated":
            pretty.print_error("Not supporting repeated MethodOptions")
            extension_value = ""
        else:
            extension_value = parse_extension_value(
                type_ext, ext_value, sylk_json, extension_field, 2
            )
            if extension_value is not None:
                extension_value = f"option ({ext_key}) = {extension_value};"

    else:
        raise errors.SylkValidationError(
            "Extension Type Error",
            "Extension of type {} is not valid !".format(extension_type),
        )
    return extension_value


def parse_extension_value(type, value, sylk_json: SylkJson, field=None, num_tabs=1):
    """
    This function serve as util for returning an extension proto value
    """
    if "int" in type:
        value = int(value)
    elif type == "float" or type == "double":
        value = float(value)
    elif type == "string":
        value = f'"{value}"'
    elif type == "bool":
        if value == 0:
            value = "false"
        elif value == 1:
            value = "true"
    elif type == "message":
        if field is not None:
            ext_msg = sylk_json.get_message(field.get("messageType"))
            temp_values = []
            for k in value:
                field_in_ext = next(
                    (f for f in ext_msg.get("fields") if f.get("name") == k), None
                )
                if field_in_ext is not None:
                    field_ext_in_type = (
                        field_in_ext.get("fieldType").split("_")[-1].lower()
                    )
                    parsed_value_field = parse_extension_value(
                        field_ext_in_type, value[k], sylk_json, field_in_ext
                    )
                    if parsed_value_field is not None:
                        temp_values.append("{} : {}".format(k, parsed_value_field))
            if num_tabs > 1:
                value = ",\n\t\t".join(temp_values)
                value = f"{_OPEN_BRCK}\n\t\t{value}\n\t{_CLOSING_BRCK}"
            else:
                value = ",\n\t".join(temp_values)
                value = f"{_OPEN_BRCK}\n\t{value}\n{_CLOSING_BRCK}"
    elif type == "enum":
        if isinstance(value, float) or isinstance(value, int):
            if value != 0:
                value = int(value)
            else:
                value = None
        else:
            if "UNKNOWN" not in value:
                value = value
            else:
                value = None

    return value


_WellKnowns = [
    "google.protobuf",
]

_WellMap = [
    ("struct.proto", ["Struct", "Value", "ListValue"]),
    ("any.proto", ["Any"]),
    ("field_mask.proto", ["FieldMask"]),
    ("empty.proto", ["Empty"]),
    ("duration.proto", ["Duration"]),
    ("timestamp.proto", ["Timestamp"]),
    (
        "descriptor.proto",
        ["FileOptions", "ServiceOptions", "MethodOptions", "MessageOptions"],
    ),
]


# Python class for topological sorting of a DAG
# Class to represent a graph
class Graph:
    def __init__(self, nodes, dependencies: bool = False):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.graph[None] = []

        if dependencies:
            for p in nodes:
                resource_name = (
                    p.get("package")
                    if p.get("package") is not None
                    else p.get("fullName")
                )

                if (
                    p.get("dependencies") is not None
                    and len(p.get("dependencies")) > 0
                    and True
                    not in list(map(lambda x: x in p.get("dependencies"), _WellKnowns))
                ):
                    for d in p.get("dependencies"):
                        self.addEdge(resource_name, d)
                else:
                    self.addEdge(resource_name, None)
        else:
            for m in nodes:
                list_of_msgs = []
                for f in m.get("fields"):
                    if (
                        f.get("messageType") is not None
                        and f.get("messageType") not in _WellKnowns
                    ):
                        list_of_msgs.append(f.get("messageType"))

                if len(list_of_msgs) > 0:
                    for msg in list_of_msgs:
                        self.addEdge(m.get("fullName"), msg)
                else:
                    self.addEdge(m.get("fullName"), None)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        visited = {}
        # Mark all the vertices as not visited
        for k in self.graph.keys():
            visited[k] = False
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in list(self.graph.keys()):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print contents of stack
        stack.remove(None)
        return stack


def read_to_parse_protos(file_paths):
    results = {}
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit file reading tasks to the thread pool
        file_reading_tasks = {
            executor.submit(file_system.read_file, file_path): file_path
            for file_path in file_paths
        }

        # Retrieve the results as they complete
        for future in concurrent.futures.as_completed(file_reading_tasks):
            file_path = file_reading_tasks[
                future
            ]  # Get the file path associated with the future
            try:
                file_contents = future.result()
                results[
                    file_path
                ] = file_contents  # Store the file contents in the dictionary
            except Exception as e:
                print(f"An error occurred while reading {file_path}: {e}")

    return results


def is_semver_less(semver1, semver2):
    if semver1 is None:
        return True

    def parse_semver(semver):
        major, minor, patch = map(int, semver.split("."))
        return major, minor, patch

    major1, minor1, patch1 = parse_semver(semver1)
    major2, minor2, patch2 = parse_semver(semver2)

    if major1 < major2:
        return True
    elif major1 > major2:
        return False

    if minor1 < minor2:
        return True
    elif minor1 > minor2:
        return False

    if patch1 < patch2:
        return True
    elif patch1 > patch2:
        return False

    return False
