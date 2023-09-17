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
import sys

from collections import defaultdict, deque
from typing import List
from sylk.architect import CommandMap, SylkArchitect
from sylk.cli import prompter
from sylk.cli.commands.build import build_protos
from sylk.commons import file_system, proto_comparison
from sylk.commons.helpers import SylkJson, parse_version_component, proto_struct_to_dict, to_snake_case
from sylk.commons.pretty import (
    print_error,
    print_info,
    print_success,
    print_warning,
    print_note,
)
from sylk.commons.proto_comparison import compare_proto_files, sylk_to_files
from grpc_tools import _protoc_compiler, protoc
import pkg_resources
from google.protobuf import descriptor_pb2
from google.protobuf.json_format import ParseDict, MessageToDict
from sylk.commons.protos.sylk.SylkEnum.v2 import SylkEnum_pb2
from sylk.commons.protos.sylk.SylkEnumValue.v1 import SylkEnumValue_pb2
from sylk.commons.protos.sylk.SylkField.v1 import SylkField_pb2
from sylk.commons.protos.sylk.SylkMessage.v2 import SylkMessage_pb2
from sylk.commons.protos.sylk.SylkMessage.v2.SylkMessage_pb2 import SylkMessage
from sylk.commons.protos.sylk.SylkMethod.v1 import SylkMethod_pb2
from sylk.commons.protos.sylk.SylkPackage.v2 import SylkPackage_pb2
from sylk.commons.protos.sylk.SylkPackage.v2.SylkPackage_pb2 import SylkPackage
from sylk.commons.protos.sylk.SylkService.v2 import SylkService_pb2
from google.protobuf.struct_pb2 import Struct, Value as pbValue
from google.protobuf.any_pb2 import Any
from google.protobuf.message import EncodeError
from google.protobuf.message_factory import GetMessages, GetMessageClassesForFiles
from google.protobuf.descriptor_pool import Default


def parse_file_descriptor_set(file_path):
    # Create an empty FileDescriptorSet
    file_descriptor_set = descriptor_pb2.FileDescriptorSet()

    # Read the serialized data
    with open(file_path, "rb") as file:
        file_descriptor_set.ParseFromString(file.read())

    return file_descriptor_set


def run_protoc(command_arguments):
    command_arguments = [argument.encode() for argument in command_arguments]
    return _protoc_compiler.run_main(command_arguments)


def get_description_for_message(
    message_index: int, source_code_info: descriptor_pb2.SourceCodeInfo
) -> str:
    # The path for messages is [4, message_index]
    path_for_message = [
        descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER,
        message_index,
    ]

    for location in source_code_info.location:
        if location.path == path_for_message:
            return location.leading_comments

    # Return empty string if no description found
    return ""


def get_description_for_enum(
    enum_index: int, source_code_info: descriptor_pb2.SourceCodeInfo
) -> str:
    # The path for enums is [4, enum_index]
    path_for_enum = [
        descriptor_pb2.FileDescriptorProto.ENUM_TYPE_FIELD_NUMBER,
        enum_index,
    ]

    for location in source_code_info.location:
        if location.path == path_for_enum:
            # Using leading_comments as the description. You can combine or choose between leading and trailing if needed.
            return location.leading_comments

    # Return empty string if no description found
    return ""


def get_description_for_service(
    service_index: int, source_code_info: descriptor_pb2.SourceCodeInfo
) -> str:
    # The path for services is [6, service_index]
    path_for_service = [
        descriptor_pb2.FileDescriptorProto.SERVICE_FIELD_NUMBER,
        service_index,
    ]

    for location in source_code_info.location:
        if location.path == path_for_service:
            return location.leading_comments

    # Return empty string if no description found
    return ""


def value_to_struct_val(obj) -> pbValue:
    """Convert a python native value to google.protobuf.Value."""
    if isinstance(obj, bool):
        return pbValue(bool_value=obj)
    elif isinstance(obj, float):
        return pbValue(number_value=obj)
    elif isinstance(obj, int):
        # Assuming int can be safely cast to float
        return pbValue(number_value=float(obj))
    elif isinstance(obj, str):
        return pbValue(string_value=obj)
    elif isinstance(obj, list):
        list_value = pbValue.list_value(values=[value_to_struct_val(i) for i in obj])
        return pbValue(list_value=list_value)
    elif isinstance(obj, dict):
        struct_value = pbValue(struct_value=convert_to_struct(obj))
        return pbValue(struct_value=struct_value)
    return pbValue(null_value=pbValue.null_value)


def convert_to_struct(data: dict) -> Struct:
    """Converts a dictionary to google.protobuf.Struct."""
    struct = Struct()
    for key, value in data.items():
        struct.fields[key].CopyFrom(value_to_struct_val(value))
    return struct


def parse_path_to_package(path: str):
    ver = parse_version_component(path.split(".")[-1])
    if ver is not None:
        pkg_name = ".".join(path.split(".")[:-2])
    else:
        pkg_name = ".".join(path.split(".")[:-1])
    return pkg_name


def parse_field_to_sylk_field(
    field_desc: descriptor_pb2.FieldDescriptorProto,
    message_desc: descriptor_pb2.DescriptorProto,
    message_full_path: str,
    file_desc: descriptor_pb2.FileDescriptorProto,
    sylk_package: SylkPackage_pb2.SylkPackage,
) -> SylkField_pb2.SylkField:
    sylk_field = SylkField_pb2.SylkField()
    sylk_field.name = field_desc.name
    sylk_field.full_name = f"{message_full_path}.{field_desc.name}"
    sylk_field.field_type = (
        field_desc.type
    )  # Assuming direct mapping; adjust if necessary
    sylk_field.index = field_desc.number
    sylk_field.label = SylkField_pb2.SylkFieldLabels.Name(field_desc.label)

    # Handling field type for enum or message
    if field_desc.type == descriptor_pb2.FieldDescriptorProto.TYPE_ENUM:
        # Use the full name of the referenced type
        sylk_field.enum_type = field_desc.type_name.lstrip(".")
        referenced_package = parse_path_to_package(field_desc.type_name.lstrip("."))
        if (
            referenced_package not in sylk_package.dependencies
            and referenced_package != file_desc.package
        ):
            sylk_package.dependencies.append(referenced_package)

    elif field_desc.type == descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE:
        # Use the full name of the referenced type
        sylk_field.message_type = field_desc.type_name.lstrip(".")
        referenced_package = parse_path_to_package(field_desc.type_name.lstrip("."))
        if (
            referenced_package not in sylk_package.dependencies
            and referenced_package != file_desc.package
        ):
            sylk_package.dependencies.append(referenced_package)
    
    # Check if it's a map type
    if (
        field_desc.type == descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE
        and field_desc.type_name.split('.')[-1]
        in [nested_type.name for nested_type in message_desc.nested_type]
    ):
        
        # Retrieve the nested message representing the map
        map_message = next(
            nested_type
            for nested_type in message_desc.nested_type
            if nested_type.name == field_desc.type_name.split('.')[-1]
        )
        if map_message.options.map_entry:
            # It's a map type
            key_field = map_message.field[0]  # Key type
            value_field = map_message.field[1]  # Value type
            sylk_field.key_type = key_field.type  # Assuming direct mapping for key type
            sylk_field.value_type = (
                value_field.type
            )  # Assuming direct mapping for value type
            sylk_field.field_type = SylkField_pb2.TYPE_MAP
            sylk_field.label = SylkField_pb2.LABEL_OPTIONAL
            if value_field.type == descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE:
                sylk_field.message_type = value_field.type_name.lstrip('.')
            
            elif value_field.type == descriptor_pb2.FieldDescriptorProto.TYPE_ENUM:
                sylk_field.enum_type = value_field.type_name.lstrip('.')
                sylk_field.ClearField('message_type')

            else:
                sylk_field.ClearField('message_type')

    # Check for oneof fields
    if field_desc.HasField("oneof_index"):
        oneof_descriptor = message_desc.oneof_decl[field_desc.oneof_index]
        oneof_field = SylkField_pb2.SylkOneOfField()
        oneof_field.name = oneof_descriptor.name
        # Add any other necessary mappings for oneof fields
        sylk_field.oneof_fields.append(oneof_field)

    msg_index = list(file_desc.message_type).index(message_desc)
    field_index = list(message_desc.field).index(field_desc)
    sylk_field.description = extract_description_for_field(file_desc.source_code_info, msg_index, field_index).strip()
    sylk_field.kind = "field"
    sylk_field.type = "descriptor"
    
    return sylk_field


def parse_file_opts(
    exts,
    file: descriptor_pb2.FileDescriptorProto
):
    file_opts = file.options
    if file_opts.go_package != '':
        new_file_opts = exts.get_or_create("files")
        new_file_opts.update({
            f"{file.name.split('/')[-1].split('.')[0]}" : MessageToDict(file_opts)
        })
    pass

def parse_descriptor_to_sylk_package(
    proto_set: descriptor_pb2.FileDescriptorSet,
    file: descriptor_pb2.FileDescriptorProto,
    sylk_package: SylkPackage_pb2.SylkPackage
) -> SylkPackage_pb2.SylkPackage:
    
    
    # Convert messages
    for idx, message in enumerate(file.message_type):
        if message.options.map_entry != True:
            sylk_message = parse_message_to_sylk_message(
                message, file.package, file.source_code_info, idx, file, sylk_package
            )
            sylk_message.tag = file.name.split("/")[-1].split(".")[0]
            sylk_package.messages.append(sylk_message)

    # Convert enums
    for idx, enum in enumerate(file.enum_type):
        sylk_enum = parse_enum_to_sylk_enum(
            enum, file.package, file.source_code_info, idx
        )
        sylk_enum.tag = file.name.split("/")[-1].split(".")[0]
        sylk_package.enums.append(sylk_enum)

    # Convert services
    for idx, service in enumerate(file.service):
        sylk_service = parse_service_to_sylk_service(
            service, file.package, file.source_code_info, idx
        )
        sylk_service.tag = file.name.split("/")[-1].split(".")[0]
        sylk_package.services.append(sylk_service)

    
    sylk_package.name = file.package.split('.')[-1] if parse_version_component(file.package.split('.')[-1]) is None else file.package.split('.')[-2]
    sylk_package.package = file.package
    
    parse_file_opts(sylk_package.extensions,file)
    
 
    # Here, other attributes like 'name', 'package', 'dependencies', etc. should also be set
    # for the sylk_package based on the properties of the 'file' and the 'proto_set'.
    # I'll omit those details for brevity.

    return sylk_package


def nested_type_to_any(
    nested_type,
    package,
    source_code_info,
    idx,
    file,
    sylk_package: SylkPackage_pb2.SylkPackage,
) -> Any:
    any_msg = Any()

    # Check if it's a message or an enum
    if nested_type.type == descriptor_pb2.FieldDescriptorProto.TYPE_MESSAGE:
        sylk_message = parse_message_to_sylk_message(
            nested_type, package, source_code_info, idx, file, sylk_package
        )
        try:
            any_msg.Pack(sylk_message)
            any_msg.type_url = "sylk.SylkMessage.v2.SylkMessage"
        except EncodeError:
            pass

    elif nested_type.type == descriptor_pb2.FieldDescriptorProto.TYPE_ENUM:
        sylk_enum = parse_enum_to_sylk_enum(nested_type)
        try:
            any_msg.Pack(sylk_enum)
            any_msg.type_url = "sylk.SylkEnum.v2.SylkEnum"
        except EncodeError:
            pass

    return any_msg

def parse_file_options_to_sylk_extensions(
    file_name: str,
    file_opts: descriptor_pb2.FileOptions,
    sylk_package: SylkPackage_pb2.SylkPackage
):
    extensions = {}
    temp_ext = Struct()
    files_exts = sylk_package.extensions.get_or_create('files')
    temp_ext.update({ **files_exts, f"{file_name}":  MessageToDict(file_opts)})
    extensions['files'] = temp_ext
    # files_exts.update({**files_exts, f"{file_name}": file_ext_struct})
    return extensions

def parse_field_options_to_sylk_extensions(
        field_opts: descriptor_pb2.FieldOptions
):
    extensions_map = {}
    extensions = {}
    extensions_map = MessageToDict(field_opts)
    if len(extensions_map.keys()) > 0:
        extensions["google.protobuf.FieldOptions"] = extensions_map
    return extensions


def parse_message_options_to_sylk_extensions(
    message_opts: descriptor_pb2.MessageOptions,
) -> dict:
    extensions_map = {}
    extensions = {}
    # Handling built-in options
    extensions_map = MessageToDict(message_opts)

    # Handling custom extensions (dynamic options)
    # Let's assume that the extensions are stored in the `uninterpreted_option` field of the options
    for option in message_opts.uninterpreted_option:
        # Building the extension's name from its components
        option_name = ".".join([name_part.name for name_part in option.name])

        if option.HasField("identifier_value"):
            extensions_map[option_name] = option.identifier_value
        elif option.HasField("positive_int_value"):
            extensions_map[option_name] = option.positive_int_value
        elif option.HasField("negative_int_value"):
            extensions_map[option_name] = option.negative_int_value
        elif option.HasField("double_value"):
            extensions_map[option_name] = option.double_value
        elif option.HasField("string_value"):
            extensions_map[option_name] = option.string_value
        elif option.HasField("aggregate_value"):
            extensions_map[option_name] = option.aggregate_value
        # Add other fields as necessary
    if len(extensions_map.keys()) > 0:
        extensions["google.protobuf.MessageOptions"] = extensions_map
    else:
        extensions = None
    return extensions


def dict_to_struct(data: dict) -> Struct:
    """
    Convert a Python dictionary into a protobuf Struct.
    """
    struct = Struct()

    for key, value in data.items():
        if isinstance(value, (str)):
            struct.fields[key].CopyFrom(pbValue(string_value=str(value)))
        elif isinstance(value, (bool)):
            struct.fields[key].CopyFrom(pbValue(bool_value=value))
        elif isinstance(value, (int, float)):
            struct.fields[key].CopyFrom(pbValue(number_value=value))
        # Handle other types as necessary, such as lists, nested dictionaries, etc.

    return struct

def set_sylk_extensions(sylk_any_resource, extensions_dict: dict):
    """
    Set the extensions property using a dictionary.
    """
    for key, value in extensions_dict.items():
        sylk_any_resource.extensions[key].CopyFrom(dict_to_struct(value))


def parse_message_to_sylk_message(
    message_desc: descriptor_pb2.DescriptorProto,
    package: str,
    source_code_info: descriptor_pb2.SourceCodeInfo,
    message_index: int,
    file_desc: descriptor_pb2.FileDescriptorProto,
    sylk_package: SylkPackage_pb2.SylkPackage,
) -> SylkMessage_pb2.SylkMessage:
    sylk_message = SylkMessage_pb2.SylkMessage()
    sylk_message.name = message_desc.name
    sylk_message.full_name = f"{package}.{message_desc.name}"
    
    # Parsing fields
    for field_desc in message_desc.field:
        
        sylk_field = parse_field_to_sylk_field(
            field_desc, message_desc, sylk_message.full_name, file_desc, sylk_package
        )
        field_opts = parse_field_options_to_sylk_extensions(field_desc.options)
        set_sylk_extensions(sylk_field, field_opts)

        sylk_message.fields.append(sylk_field)

    # Handling nested types (e.g., nested messages or enums)
    # TODO
    opts = parse_message_options_to_sylk_extensions(message_desc.options)
    if opts is not None:
        set_sylk_extensions(sylk_message, opts)
    # Handling protobuf options:
    for extension in message_desc.extension:
        # Assuming extension.name gives the full path for the option
        key = extension.name
        value = convert_to_struct(
            extension.options
        )  # Adjust this to wherever your option values are stored
        sylk_message.extensions[key] = value

    # Getting description from SourceCodeInfo
    sylk_message.description = get_description_for_message(
        message_index, source_code_info
    ).strip()

    sylk_message.type = "descriptor"
    sylk_message.kind = "message"
    return sylk_message


def parse_enum_to_sylk_enum(
    enum_desc: descriptor_pb2.EnumDescriptorProto,
    package: str,
    source_code_info: descriptor_pb2.SourceCodeInfo,
    enum_index: int,
) -> SylkEnum_pb2.SylkEnum:
    sylk_enum = SylkEnum_pb2.SylkEnum()

    # Setting the name directly
    sylk_enum.name = enum_desc.name

    # Constructing the full name
    sylk_enum.full_name = f"{package}.{enum_desc.name}"

    sylk_enum.type = "descriptor"
    sylk_enum.kind = "enum"

    # Parsing values
    for value_desc in enum_desc.value:
        sylk_value = (
            SylkEnumValue_pb2.SylkEnumValue()
        )  # Assuming SylkEnumValue structure is defined similarly
        sylk_value.full_name = f"{sylk_enum.full_name}.{value_desc.name}"
        sylk_value.name = value_desc.name
        sylk_value.index = value_desc.number
        sylk_value.number = value_desc.number
        sylk_value.type = "descriptor"
        sylk_value.kind = "enum_value"
        sylk_enum.values.append(sylk_value)

    sylk_enum.description = get_description_for_enum(enum_index, source_code_info).strip()

    return sylk_enum


def parse_service_to_sylk_service(
    service_desc: descriptor_pb2.ServiceDescriptorProto,
    package: str,
    source_code_info: descriptor_pb2.SourceCodeInfo,
    service_index: int,
) -> SylkService_pb2.SylkService:
    sylk_service = SylkService_pb2.SylkService()

    # Setting the name directly
    sylk_service.name = service_desc.name

    # Constructing the full name
    sylk_service.full_name = f"{package}.{service_desc.name}"

    # Parsing methods
    for method_desc in service_desc.method:
        sylk_method = SylkMethod_pb2.SylkMethod()
        sylk_method.name = method_desc.name
        sylk_method.input_type = method_desc.input_type[1:]
        sylk_method.output_type = method_desc.output_type[1:]
        sylk_service.methods.append(sylk_method)

    # Getting description from SourceCodeInfo
    sylk_service.description = get_description_for_service(
        service_index, source_code_info
    ).strip()

    return sylk_service


def adapt_descriptor_to_sylkpackage(
    proto_set: descriptor_pb2.FileDescriptorSet,
    existing_package: SylkPackage_pb2.SylkPackage,
    file: descriptor_pb2.FileDescriptorProto,
):
    ver = parse_version_component(file.package)
    if ver is not None:
        name = file.package.split(".")[-2]
    else:
        name = file.package.split(".")[-1]
    file_opts = parse_file_options_to_sylk_extensions(file_name=file.name.split('/')[-1].split('.')[0],file_opts=file.options,sylk_package=existing_package)
    sylk_package = SylkPackage_pb2.SylkPackage(
        name=name,
        package=file.package,
        messages=existing_package.messages,
        enums=existing_package.enums,
        services=existing_package.services,
        extensions=file_opts,
        description=existing_package.description,
        type="package",
    )
    deps = list(
        map(
            lambda x: {x: next((f for f in proto_set.file if f.name == x), None)},
            file.dependency,
        )
    )
    for f in list(map(lambda x: x[list(x.keys())[0]].package, deps)):
        sylk_package.dependencies.append(f)

    return sylk_package


def adapt_descriptor_to_sylkenum(
    descriptor: descriptor_pb2.EnumDescriptorProto,
    file: descriptor_pb2.FileDescriptorProto,
    enum_index,
    inline_name: str = None,
    inline_i: int = None
):
    """
    Adapts a protobuf enum descriptor object into a SylkEnum.

    Args:
        descriptor (object): The protobuf enum descriptor object.

    Returns:
        dict: A dictionary representation of the SylkEnum.
    """

    def convert_value(
        enum_name,
        value_descriptor: descriptor_pb2.EnumValueDescriptorProto,
        source_code: descriptor_pb2.SourceCodeInfo,
        enum_index,
        ev_index
    ):
        """Converts a field descriptor to a SylkEnumValue."""
        ev_desc = extract_description_for_enum_value(source_code, enum_index, ev_index)
        return {
            "index": value_descriptor.number
            if hasattr(value_descriptor, "number")
            else 1,
            "number": value_descriptor.number
            if hasattr(value_descriptor, "number")
            else 1,
            # "extensions": field_descriptor.extensions if hasattr(field_descriptor, 'extensions') else {},
            "full_name": enum_name + "." + value_descriptor.name,
            "kind": "enum_value",
            "description": ev_desc.strip() if ev_desc is not None else None,
            "name": value_descriptor.name if hasattr(value_descriptor, "name") else "",
            "type": "descriptor",
        }

    # Check if the message's file name (without extension) is different from the package name
    # Extract the file name (without extension) from the descriptor's file name
    file_name_without_extension = (
        file.name.split("/")[-1].split(".")[0] if hasattr(file, "name") else ""
    )
    # Extract all package components
    package_components = file.package.split(".") if hasattr(file, "package") else []

    # Check if the file name (without extension) is different from all package components
    tag = (
        file_name_without_extension
        if file_name_without_extension not in package_components
        else ""
    )
    enum_full_name = file.package + "." + descriptor.name
    if inline_name is not None:
        enum_full_name = inline_name + '.' + descriptor.name
    enum_values = []
    ev_index = 0
    for ev in descriptor.value:
        enum_values.append(convert_value(enum_full_name, ev, file.source_code_info, enum_index, ev_index))
        ev_index+=1
    
    sylk_enum = {
        "tag": tag,
        "values": enum_values,
        "kind": "enum",
        "description": extract_description_for_enum(file.source_code_info, enum_index, inline_i=inline_i if inline_name is not None else None).strip(),
        "type": "descriptor",
        "full_name": enum_full_name,
        # "extensions": descriptor.extensions if hasattr(descriptor, 'extensions') else {},
        # "uri": descriptor.uri if hasattr(descriptor, 'uri') else '',
        "name": descriptor.name if hasattr(descriptor, "name") else "",
        # "extension_type": {}  # Placeholder; populate if needed
    }

    return sylk_enum

def adapt_descriptor_to_sylkservice(
    descriptor: descriptor_pb2.ServiceDescriptorProto,
    file: descriptor_pb2.FileDescriptorProto,
    s_index,
):
    """
    Adapts a protobuf service descriptor object into a SylkService.

    Args:
        descriptor (object): The protobuf service descriptor object.

    Returns:
        dict: A dictionary representation of the SylkService.
    """

    def convert_rpc(
        service_name,
        rpc_descriptor: descriptor_pb2.MethodDescriptorProto,
        source_code: descriptor_pb2.SourceCodeInfo,
        s_index,
        r_index
    ):
        """Converts a field descriptor to a SylkField."""

        return {
            "full_name": service_name + "." + rpc_descriptor.name,
            "kind": "method",
            "description": extract_description_for_rpc(source_code, s_index, r_index).strip(),
            "name": rpc_descriptor.name if hasattr(rpc_descriptor, "name") else "",
            "type": "descriptor",
            "input_type": rpc_descriptor.input_type.lstrip('.'),
            "output_type": rpc_descriptor.output_type.lstrip('.'),
            "client_streaming": rpc_descriptor.client_streaming,
            "server_streaming": rpc_descriptor.server_streaming
        }
    
    # Check if the message's file name (without extension) is different from the package name
    # Extract the file name (without extension) from the descriptor's file name
    file_name_without_extension = (
        file.name.split("/")[-1].split(".")[0] if hasattr(file, "name") else ""
    )
    # Extract all package components
    package_components = file.package.split(".") if hasattr(file, "package") else []

    # Check if the file name (without extension) is different from all package components
    tag = (
        file_name_without_extension
        if file_name_without_extension not in package_components
        else ""
    )

    svc_full_name = file.package + "." + descriptor.name

    methods = []
    r_index = 0
    for r in descriptor.method:
        methods.append(convert_rpc(svc_full_name, r, file.source_code_info, s_index, r_index))
        r_index+=1

    sylk_message = {
        "tag": tag,
        "methods": methods,
        "type": "service",
        "description": extract_description_for_service(source_code_info=file.source_code_info, service_index=s_index).strip(),
        "full_name": svc_full_name,
        # "extensions": descriptor.extensions if hasattr(descriptor, 'extensions') else {},
        # "uri": descriptor.uri if hasattr(descriptor, 'uri') else '',
        "name": descriptor.name if hasattr(descriptor, "name") else "",
        # "extension_type": {}  # Placeholder; populate if needed
    }

    return sylk_message


def adapt_descriptor_to_sylkmessage(
    descriptor: descriptor_pb2.DescriptorProto,
    file: descriptor_pb2.FileDescriptorProto,
    m_index,
    inline_name: str = None,
    inline_i: int = None
):
    """
    Adapts a protobuf descriptor object into a SylkMessage.

    Args:
        descriptor (object): The protobuf descriptor object.

    Returns:
        dict: A dictionary representation of the SylkMessage.
    """

    def convert_field(
        message_name,
        file_descriptor: descriptor_pb2.FileDescriptorProto,
        message_description: descriptor_pb2.DescriptorProto,
        field_descriptor: descriptor_pb2.FieldDescriptorProto,
        m_index,
        f_index
    ):
        """Converts a field descriptor to a SylkField."""
        map_type = None
        label = field_descriptor.label
        message_type = field_descriptor.type_name.lstrip('.') if field_descriptor.type == field_descriptor.Type.TYPE_MESSAGE else None
        if field_descriptor.type == field_descriptor.Type.TYPE_MESSAGE:
            map_type = next((m for m in message_description.nested_type if m.options.map_entry and m.name == field_descriptor.type_name.split('.')[-1]),None)
            if map_type is not None:
                message_type = map_type.field[1].type_name.lstrip('.') if map_type.field[1].type == field_descriptor.Type.TYPE_MESSAGE else None
                label = SylkField_pb2.LABEL_OPTIONAL
        field_opts = parse_field_options_to_sylk_extensions(field_descriptor.options)
        return {
            "value_type": map_type.field[1].type if map_type is not None else None,
            "key_type": map_type.field[0].type if map_type is not None else None,
            "label": label,
            "index": field_descriptor.number
            if hasattr(field_descriptor, "number")
            else 1,
            "extensions": field_opts,
            "full_name": message_name + "." + field_descriptor.name,
            "kind": "field",
            "message_type": message_type,
            "field_type": field_descriptor.type if map_type is None else SylkField_pb2.TYPE_MAP
            if hasattr(field_descriptor, "type")
            else "",
            "enum_type": field_descriptor.type_name.lstrip('.') if field_descriptor.type == field_descriptor.Type.TYPE_ENUM else None,
            "description": extract_description_for_field(file_descriptor.source_code_info, m_index, f_index).strip(),
            "name": field_descriptor.name if hasattr(field_descriptor, "name") else "",
            # "oneof_fields": [],  # Placeholder; populate if needed
            # "uri": field_descriptor.uri if hasattr(field_descriptor, 'uri') else '',
            "type": "descriptor",
        }
    def convert_oneof_field(
        message_name,
        file_descriptor: descriptor_pb2.FileDescriptorProto,
        message_description: descriptor_pb2.DescriptorProto,
        field_descriptor: descriptor_pb2.FieldDescriptorProto,
        m_index,
    ):
        """Converts a field descriptor to a SylkField."""
        # field_opts = parse_field_options_to_sylk_extensions(field_descriptor.options)
        return {
            "label": SylkField_pb2.LABEL_OPTIONAL,
            "index": field_descriptor.number
            if hasattr(field_descriptor, "number")
            else 1,
            # "extensions": field_opts,
            "full_name": message_name + "." + field_descriptor.name,
            "kind": "oneof",
            "message_type": field_descriptor.type_name.lstrip('.') if field_descriptor.type == field_descriptor.Type.TYPE_MESSAGE else None,
            "field_type": field_descriptor.type 
            if hasattr(field_descriptor, "type")
            else "",
            "enum_type": field_descriptor.type_name.lstrip('.') if field_descriptor.type == field_descriptor.Type.TYPE_ENUM else None,
            # "description": extract_description_for_field(file_descriptor.source_code_info, m_index, f_index).strip(),
            "name": field_descriptor.name if hasattr(field_descriptor, "name") else "",
            # "oneof_fields": [],  # Placeholder; populate if needed
            # "uri": field_descriptor.uri if hasattr(field_descriptor, 'uri') else '',
            # "type": "descriptor",
        }

    # Check if the message's file name (without extension) is different from the package name
    # Extract the file name (without extension) from the descriptor's file name
    file_name_without_extension = (
        file.name.split("/")[-1].split(".")[0] if hasattr(file, "name") else ""
    )
    # Extract all package components
    package_components = file.package.split(".") if hasattr(file, "package") else []

    # Check if the file name (without extension) is different from all package components
    tag = (
        file_name_without_extension
        if file_name_without_extension not in package_components
        else ""
    )
    msg_full_name = file.package + "." + descriptor.name
    if inline_name is not None:
        msg_full_name = inline_name + '.' + descriptor.name

    fields = []
    inlines = []
    f_index = 0
    oneofs_groups = {}
    for f in descriptor.field:
        if f.HasField('oneof_index') and len(descriptor.oneof_decl) > 0:
            if oneofs_groups.get(descriptor.oneof_decl[f.oneof_index].name) is None:
                oneofs_groups[descriptor.oneof_decl[f.oneof_index].name] = []
            oneofs_groups[descriptor.oneof_decl[f.oneof_index].name].append(f)
        else:
            fields.append(convert_field(msg_full_name, file, descriptor, f, m_index, f_index))
        
        f_index+=1
        
    for oneof_field in oneofs_groups:
        oneofs_fields = []
        for oneof in oneofs_groups[oneof_field]:
            oneofs_fields.append(ParseDict(convert_oneof_field(msg_full_name+'.'+oneof_field, file, descriptor, oneof, m_index),SylkField_pb2.SylkOneOfField()))
        
        fields.append(MessageToDict(SylkField_pb2.SylkField(
            name=oneof_field,
            full_name=msg_full_name+'.'+oneof_field,
            description=None,
            index=f.number,
            label=SylkField_pb2.LABEL_OPTIONAL,
            type='descriptor',
            kind='field',
            oneof_fields=oneofs_fields,
            field_type=SylkField_pb2.TYPE_ONEOF
        )))

    inline_e_i = 0
    for e in descriptor.enum_type:
        adapted_inline = adapt_descriptor_to_sylkenum(e, file, m_index, msg_full_name, inline_e_i)
        any_inline = Any()
        any_inline.Pack(ParseDict(adapted_inline,SylkEnum_pb2.SylkEnum()))
        inlines.append(MessageToDict(any_inline))
        inline_e_i+=1

    if inline_i is None:
        inline_i = 0
    for m in descriptor.nested_type:
        if m.options.map_entry == False:
            adapted_inline = adapt_descriptor_to_sylkmessage(m,file,m_index, msg_full_name, inline_i)
            any_inline = Any()
            any_inline.Pack(ParseDict(adapted_inline,SylkMessage_pb2.SylkMessage()))
            inlines.append(MessageToDict(any_inline))
        inline_i+=1
    sylk_message = {
        "inlines": inlines,
        "tag": tag,
        "fields": fields,
        "kind": "message",
        "description": extract_description_for_message(source_code_info=file.source_code_info, message_index=m_index, inline=inline_i if inline_name is not None else None).strip(),
        "type": "descriptor",
        "full_name": msg_full_name,
        # "extensions":  if hasattr(descriptor, 'extensions') else {},
        # "uri": descriptor.uri if hasattr(descriptor, 'uri') else '',
        "name": descriptor.name if hasattr(descriptor, "name") else "",
        # "extension_type": {}  # Placeholder; populate if needed
    }
    return sylk_message


def value_diff(modified_field, last_state_field, path=""):
    diffs = []

    attributes = [
        "index",
        "extensions",
        "full_name",
        "kind",
        "description",
        "name",
        "number",
        "uri",
        "type",
    ]

    for attr in attributes:
        modified_attr = getattr(modified_field, attr, None)
        last_state_attr = getattr(last_state_field, attr, None)
        if (True if attr != 'description' else modified_attr.split(f'[{last_state_field.full_name}] - ')[1].strip() != last_state_attr if len(modified_attr.split(f'[{last_state_field.full_name}] - ')) > 1 else True) and (modified_attr != last_state_attr):
            if modified_attr is not None:
                diffs.append(f"+ {path}.{attr}: {modified_attr}")
            if last_state_attr is not None:
                diffs.append(f"- {path}.{attr}: {last_state_attr}")

    return diffs

def rpc_diff(modified_method, last_state_method, path=""):
    """
    Compare two SylkMethod objects and report the differences.

    Args:
        modified_method (SylkMethod): The modified SylkMethod object.
        last_state_method (SylkMethod): The SylkMethod object representing the last state.
        path (str): The current path in the comparison (used for reporting).

    Returns:
        list: A list of differences. Each difference is a string.
    """

    diffs = []

    attributes = [
        "extensions",
        "full_name",
        "kind",
        "input_type",
        "output_type",
        "description",
        "name",
        "client_streaming",
        "server_streaming",
    ]

    for attr in attributes:
        modified_attr = getattr(modified_method, attr, None)
        last_state_attr = getattr(last_state_method, attr, None)
        if modified_attr != last_state_attr:
            if modified_attr is not None:
                diffs.append(f"+ {path}.{attr}: {modified_attr}")
            if last_state_attr is not None:
                diffs.append(f"- {path}.{attr}: {last_state_attr}")

    return diffs

def field_diff(modified_field, last_state_field, path=""):
    """
    Compare two SylkField objects and report the differences.

    Args:
        modified_field (SylkField): The modified SylkField object.
        last_state_field (SylkField): The SylkField object representing the last state.
        path (str): The current path in the comparison (used for reporting).

    Returns:
        list: A list of differences. Each difference is a string.
    """

    diffs = []

    attributes = [
        "value_type",
        "key_type",
        "label",
        "index",
        "full_name",
        "kind",
        "message_type",
        "field_type",
        "enum_type",
        "description",
        "name",
        "oneof_fields",
        "uri",
        "type",
    ]

    for attr in attributes:
        modified_attr = getattr(modified_field, attr, None)
        last_state_attr = getattr(last_state_field, attr, None)
        if modified_attr != last_state_attr:
            if modified_attr is not None:
                diffs.append(f"+ {path}.{attr}: {modified_attr}")
            if last_state_attr is not None:
                diffs.append(f"- {path}.{attr}: {last_state_attr}")

    return diffs


def enum_diff(
    modified_sylk: SylkEnum_pb2.SylkEnum,
    last_state_sylk: SylkEnum_pb2.SylkEnum,
    path="",
    enum_line_index: int = 0,
    source_code_info=None,
    enm_i: int = 0,
    new_enum: bool = False,
    enm_schema: descriptor_pb2.EnumDescriptorProto = None
):
    diffs = []
    attr_diffs = []
    for attr in ["full_name", "tag", "description"]:
        modified_attr = getattr(modified_sylk, attr, None)
        last_state_attr = getattr(last_state_sylk, attr, None)
        if modified_attr != last_state_attr:
            if modified_attr is not None:
                attr_diffs.append(
                    {
                        # "line_number": enum_line_index,
                        "type": "+",
                        "diff": f"{path}.{attr}: {modified_attr}",
                    }
                )
            if last_state_attr is not None and new_enum == False:
                attr_diffs.append(
                    {
                        # "line_number": enum_line_index,
                        "type": "-",
                        "diff": f"{path}.{attr}: {last_state_attr}",
                    }
                )
    # If there are attribute differences, group them together
    if attr_diffs:
        diffs.extend(attr_diffs)

    # Check values
    values_diff = []
    for idx, (mod_value, last_value) in enumerate(
        zip(modified_sylk.values, last_state_sylk.values)
    ):
        field_line_num = extract_line_for_field(source_code_info, enm_i, idx)
        _field_diff = value_diff(mod_value, last_value)
        if len(_field_diff) > 0:
            values_diff.append(
                {
                    "field": f"{last_value.name}: ",
                    "line_number": field_line_num,
                    "diff": _field_diff,
                }
            )

    # Check if modified_sylk has more fields than last_state_sylk
    if len(modified_sylk.values) > len(last_state_sylk.values):
        for idx in range(len(last_state_sylk.values), len(modified_sylk.values)):
            diffs.append(
                {
                    "type": "+",
                    "line_number": None,
                    "diff": f"enum value at '{path}.values[{idx}]': {modified_sylk.values[idx].name} -> {modified_sylk.values[idx].number}",
                }
            )

    print(last_state_sylk.values)
    # Check if last_state_sylk has more fields than modified_sylk
    if len(modified_sylk.values) < len(last_state_sylk.values) and new_enum == False:
        for idx in range(len(modified_sylk.values), len(last_state_sylk.values)):
            diffs.append(
                {
                    "type": "-",
                    "line_number": None,
                    "diff": f"enum value at '{path}.values[{idx}]': {last_state_sylk.values[idx].name} -> {last_state_sylk.values[idx].number}",
                }
            )

    return {
        "message": f"{last_state_sylk.full_name}: line: {enum_line_index}",
        "diffs": diffs,
        "fields": values_diff,
    }

def message_diff(
    modified_sylk: SylkMessage,
    last_state_sylk: SylkMessage,
    path="",
    message_line_index: int = 0,
    source_code_info=None,
    msg_i: int = 0,
    new_message: bool = False,
    msg_schema: descriptor_pb2.DescriptorProto = None,
    file_desc: descriptor_pb2.FileDescriptorProto = None
):
    """
    Recursively compares two SylkMessage objects and reports the differences.

    Args:
        modified_sylk (SylkMessage): The modified SylkMessage object.
        last_state_sylk (SylkMessage): The SylkMessage object representing the last state.
        path (str): The current path in the comparison (used for reporting).

    Returns:
        list: A list of differences. Each difference is a string.
    """

    diffs = []

    # Check if the properties of both SylkMessage objects are the same
    attr_diffs = []
    for attr in ["full_name", "tag", "description"]:
        modified_attr = getattr(modified_sylk, attr, None)
        last_state_attr = getattr(last_state_sylk, attr, None)
        # print(attr, , f"{last_state_attr}")
        if modified_attr != last_state_attr:
            if modified_attr is not None:
                attr_diffs.append(
                    {
                        "type": "+",
                        "diff": f"{path}.{attr}: {modified_attr}",
                    }
                )
            if last_state_attr is not None and new_message == False:
                attr_diffs.append(
                    {
                        "type": "-",
                        "diff": f"{path}.{attr}: {last_state_attr}",
                    }
                )

    # If there are attribute differences, group them together
    if attr_diffs:
        diffs.extend(attr_diffs)

    extensions = MessageToDict(msg_schema.options)
    opt_i = 0
    for ext in extensions:
        if ext not in last_state_sylk.extensions.get(msg_schema.options.DESCRIPTOR.full_name,{}):
            msg_ext = next((field for field in descriptor_pb2.MessageOptions.DESCRIPTOR.fields if field.name == to_snake_case(ext)),None)
            import_line_numbers = None
            if msg_ext is not None:
                import_line_numbers = extract_line_for_message_option(file_desc.source_code_info, msg_i, msg_ext.number)
            ext_value = extensions[ext]
            diffs.append(
                    {
                        "type": "+",
                        "line_number": import_line_numbers,
                        "diff": f'\'{path}.options[{opt_i}]\': {to_snake_case(ext)} = {ext_value};',
                    }
                )
        opt_i += 1

    # Check fields
    field_diffs = []
    for idx, (mod_field, last_field) in enumerate(
        zip(modified_sylk.fields, last_state_sylk.fields)
    ):
        field_line_num = extract_line_for_field(source_code_info, msg_i, idx)
        _field_diff = field_diff(mod_field, last_field)
        if len(_field_diff) > 0:
            field_diffs.append(
                {
                    "field": f"{last_field.name}: ",
                    "line_number": field_line_num,
                    "diff": _field_diff,
                }
            )

    # Check if modified_sylk has more fields than last_state_sylk
    if len(modified_sylk.fields) > len(last_state_sylk.fields):
        for idx in range(len(last_state_sylk.fields), len(modified_sylk.fields)):
            diffs.append(
                {
                    "type": "+",
                    "diff": f"field at '{path}.fields[{idx}]': {modified_sylk.fields[idx].name} ({SylkField_pb2.SylkFieldTypes.Name(modified_sylk.fields[idx].field_type)})",
                }
            )

    # Check if last_state_sylk has more fields than modified_sylk
    if len(modified_sylk.fields) < len(last_state_sylk.fields) and new_message == False:
        for idx in range(len(modified_sylk.fields), len(last_state_sylk.fields)):
            diffs.append(
                {
                    "type": "-",
                    "diff": f"field at '{path}.fields[{idx}]': {last_state_sylk.fields[idx].name} ({SylkField_pb2.SylkFieldTypes.Name(last_state_sylk.fields[idx].field_type)})",
                }
            )

    return {
        "message": f"{last_state_sylk.full_name}: line: {message_line_index}",
        "diffs": diffs,
        "fields": field_diffs,
    }


def service_diff(
    modified_sylk: SylkService_pb2.SylkService,
    last_state_sylk: SylkService_pb2.SylkService,
    path="",
    service_line_index: int = 0,
    source_code_info=None,
    service_i: int = 0,
    new_svc: bool = False
):
    """
    Recursively compares two SylkService objects and reports the differences.

    Args:
        modified_sylk (SylkService): The modified SylkService object.
        last_state_sylk (SylkService): The SylkService object representing the last state.
        path (str): The current path in the comparison (used for reporting).

    Returns:
        list: A list of differences. Each difference is a string.
    """

    diffs = []

    # Check if the properties of both SylkMessage objects are the same
    attr_diffs = []
    for attr in ["full_name", "tag", "description", "type"]:
        modified_attr = getattr(modified_sylk, attr, None)
        last_state_attr = getattr(last_state_sylk, attr, None)
        if modified_attr != last_state_attr:
            if modified_attr is not None:
                attr_diffs.append(
                    {
                        "type": "+",
                        "diff": f"{path}.{attr}: {modified_attr}",
                    }
                )
            if last_state_attr is not None and new_svc == False:
                attr_diffs.append(
                    {
                        "type": "-",
                        "diff": f"{path}.{attr}: {last_state_attr}",
                    }
                )

    # If there are attribute differences, group them together
    if attr_diffs:
        diffs.extend(attr_diffs)

    # Check rpc's
    rpcs_diff = []
    for idx, (mod_rpc, last_rpc) in enumerate(
        zip(modified_sylk.methods, last_state_sylk.methods)
    ):
        rpc_line_num = extract_description_for_rpc(source_code_info, service_i, idx)
        _rpc_diff = rpc_diff(mod_rpc, last_rpc)
        if len(_rpc_diff) > 0:
            rpcs_diff.append(
                {
                    "field": f"{last_rpc.name}: ",
                    "line_number": rpc_line_num,
                    "diff": _rpc_diff,
                }
            )

    # Check if modified_sylk has more rpc's than last_state_sylk
    if len(modified_sylk.methods) > len(last_state_sylk.methods):
        for idx in range(len(last_state_sylk.methods), len(modified_sylk.methods)):
            diffs.append(
                {
                    "type": "+",
                    "diff": f"rpc at '{path}.methods[{idx}]': {modified_sylk.methods[idx].name}",
                }
            )

    # Check if last_state_sylk has more methods than modified_sylk
    if len(modified_sylk.methods) < len(last_state_sylk.methods) and new_svc == False:
        for idx in range(len(modified_sylk.methods), len(last_state_sylk.methods)):
            diffs.append(
                {
                    "type": "-",
                    "diff": f"rpc at '{path}.methods[{idx}]': {last_state_sylk.methods[idx].name}",
                }
            )

    return {
        "message": f"{last_state_sylk.full_name}: line: {service_line_index}",
        "diffs": diffs,
        "fields": rpcs_diff,
    }

def display_diffs(diff_structure, type):
    """
    Formats and displays differences in a git-diff style with separation between diffs and metadata of line position.
    """
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"
    output = []
    # Message header
    output.append(f"\n--- [{type}] {diff_structure['message']} ---")

    # Message diffs
    for diff in diff_structure["diffs"]:
        color = GREEN if diff["type"] == "+" else RED
        if "line_number" in diff and diff["line_number"]:
            output.append(f"@ line:{diff['line_number']}")
        output.append(f"{color}{diff['type']} {diff['diff']}{RESET}")
    # Fields diffs
    if len(diff_structure.get("fields", [])) > 0:
        output.append("\n\tfields diffs:")
    for field_diff in diff_structure.get("fields", []):
        output.append(f"\n\t--- {field_diff['field']} ---")
        for d in field_diff["diff"]:
            color = GREEN if d.startswith("+") else RED
            output.append(f"\t{color}{d}{RESET}")
    if len(output) == 1:
        output.append("* no changes.")
    return "\n".join(output)


def parse_locations(
    target_path, locations: List[descriptor_pb2.SourceCodeInfo.Location]
):
    """Iterate through all the location entries to find the matching path."""

    for location in locations:
        if location.path == target_path:
            # `span` typically contains [start_line, start_column, end_line, end_column].
            # We'll extract the start line.
            return location.span[0] + 1 if location.span else None
    return


def extract_line_for_service(
    source_code_info: descriptor_pb2.SourceCodeInfo, message_index: int
):
    """Extract line number for a service based on its index."""
    # Construct the path for the service based on its index.
    target_path = [
        descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER,
        message_index,
    ]
    line = parse_locations(target_path, source_code_info.location)
    return line

def extract_line_for_message(
    source_code_info: descriptor_pb2.SourceCodeInfo, message_index: int
):
    """Extract line number for a message based on its index."""
    # Construct the path for the message based on its index.
    target_path = [
        descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER,
        message_index,
    ]
    line = parse_locations(target_path, source_code_info.location)
    return line

def extract_description_for_enum(
    source_code_info: descriptor_pb2.SourceCodeInfo, enum_index: int,
    inline_i: int = None
):
    description = None
    if inline_i is not None:
        target_path = [
            descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER,
            enum_index,
            descriptor_pb2.DescriptorProto.ENUM_TYPE_FIELD_NUMBER,
            inline_i
        ]
    else:
        target_path = [
            descriptor_pb2.FileDescriptorProto.ENUM_TYPE_FIELD_NUMBER,
            enum_index,
        ]
    for loc in source_code_info.location:
        if loc.path == target_path:
            description = loc.leading_comments
            break
    return description

def extract_description_for_enum_value(
    source_code_info: descriptor_pb2.SourceCodeInfo, enum_index: int, ev_index: int
):
    description = None
    target_path = [
        descriptor_pb2.FileDescriptorProto.ENUM_TYPE_FIELD_NUMBER,
        enum_index,
        descriptor_pb2.EnumDescriptorProto.VALUE_FIELD_NUMBER,
        ev_index
    ]
    for loc in source_code_info.location:
        if loc.path == target_path:
            description = loc.leading_comments
            break
    return description

def extract_description_for_service(
    source_code_info: descriptor_pb2.SourceCodeInfo, service_index: int
):
    description = None
    target_path = [
        descriptor_pb2.FileDescriptorProto.SERVICE_FIELD_NUMBER,
        service_index,
    ]
    for loc in source_code_info.location:
        if loc.path == target_path:
            description = loc.leading_comments
            break
    return description

def extract_description_for_rpc(
    source_code_info: descriptor_pb2.SourceCodeInfo, service_index: int, r_index: int
):
    description = None
    target_path = [
        descriptor_pb2.FileDescriptorProto.SERVICE_FIELD_NUMBER,
        service_index,
        descriptor_pb2.ServiceDescriptorProto.METHOD_FIELD_NUMBER,
        r_index
    ]
    for loc in source_code_info.location:
        if loc.path == target_path:
            description = loc.leading_comments
            break
    return description

def extract_description_for_field(
    source_code_info: descriptor_pb2.SourceCodeInfo, message_index: int, f_index: int
):
    description = None
    target_path = [
        descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER,
        message_index,
        descriptor_pb2.DescriptorProto.FIELD_FIELD_NUMBER,
        f_index
    ]
    for loc in source_code_info.location:
        if loc.path == target_path:
            description = loc.leading_comments
            break
    return description

def extract_description_for_message(
    source_code_info: descriptor_pb2.SourceCodeInfo, message_index: int, inline: int = None
):
    description = None
    if inline is not None:
        target_path = [
            descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER,
            message_index,
            descriptor_pb2.DescriptorProto.NESTED_TYPE_FIELD_NUMBER,
            inline
        ]
    else:
        target_path = [
            descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER,
            message_index,
        ]
    for loc in source_code_info.location:
        if loc.path == target_path:
            description = loc.leading_comments
            break
    return description

def extract_line_for_message_option(
    source_code_info: descriptor_pb2.SourceCodeInfo, msg_i: int, option_i: int
):
    optionals = [
        # Utils
        [descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER, msg_i, descriptor_pb2.DescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.MessageOptions.DEPRECATED_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER, msg_i, descriptor_pb2.DescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.MessageOptions.MAP_ENTRY_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER, msg_i, descriptor_pb2.DescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.MessageOptions.MESSAGE_SET_WIRE_FORMAT_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER, msg_i, descriptor_pb2.DescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.MessageOptions.NO_STANDARD_DESCRIPTOR_ACCESSOR_FIELD_NUMBER],
    ]
    target = next((f for f in optionals if f[3] == option_i), None)
    if target is not None:
        line = parse_locations(target, source_code_info.location)
    else:
        line = None
    return line

def extract_line_for_file_option(
    source_code_info: descriptor_pb2.SourceCodeInfo, option_i: int
):
    optionals = [
        # C++
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.CC_ENABLE_ARENAS_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.CC_GENERIC_SERVICES_FIELD_NUMBER],
        # C#
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.CSHARP_NAMESPACE_FIELD_NUMBER],
        # PHP
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.PHP_CLASS_PREFIX_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.PHP_NAMESPACE_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.PHP_METADATA_NAMESPACE_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.PHP_GENERIC_SERVICES_FIELD_NUMBER],
        # Objective-C
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.OBJC_CLASS_PREFIX_FIELD_NUMBER],
        # Java
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.JAVA_GENERATE_EQUALS_AND_HASH_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.JAVA_GENERIC_SERVICES_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.JAVA_MULTIPLE_FILES_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.JAVA_OUTER_CLASSNAME_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.JAVA_PACKAGE_FIELD_NUMBER],
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.JAVA_STRING_CHECK_UTF8_FIELD_NUMBER],
        # Go
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.GO_PACKAGE_FIELD_NUMBER],
        # Swift
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.SWIFT_PREFIX_FIELD_NUMBER],
        # Python
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.PY_GENERIC_SERVICES_FIELD_NUMBER],
        # Ruby
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.RUBY_PACKAGE_FIELD_NUMBER],
        # Other utils
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.CODE_SIZE],
        [descriptor_pb2.FileDescriptorProto.OPTIONS_FIELD_NUMBER, descriptor_pb2.FileOptions.SPEED],
    ]
    target = next((f for f in optionals if f[1] == option_i), None)
    if target is not None:
        line = parse_locations(target, source_code_info.location)
    else:
        line = None
    return line

def extract_line_for_import(
    source_code_info: descriptor_pb2.SourceCodeInfo, dep_i: int
):
    """Extract line number for a import based on dependency index."""
    target_path = [descriptor_pb2.FileDescriptorProto.DEPENDENCY_FIELD_NUMBER, dep_i]
    line = parse_locations(target_path, source_code_info.location)
    return line


def extract_line_for_field(
    source_code_info: descriptor_pb2.SourceCodeInfo, msg_i, field_i: int
):
    """Extract line number for a field based on field index."""
    target_path = [
        descriptor_pb2.FileDescriptorProto.MESSAGE_TYPE_FIELD_NUMBER,
        msg_i,
        descriptor_pb2.DescriptorProto.FIELD_FIELD_NUMBER,
        field_i,
    ]
    line = parse_locations(target_path, source_code_info.location)
    return line


def extract_line_for_enum(source_code_info: descriptor_pb2.SourceCodeInfo, enum_i: int):
    """Extract line number for a field based on field index."""
    target_path = [descriptor_pb2.FileDescriptorProto.ENUM_TYPE_FIELD_NUMBER, enum_i]
    line = parse_locations(target_path, source_code_info.location)
    return line


def files_diff_add(new_files, proto_set: descriptor_pb2.FileDescriptorSet):
    file_diffs = []
    for f in new_files:
        diffs = []
        file = next((file for file in proto_set.file if file.name == f), None)
        if file is not None:
            s_index = 1
            for s in file.service:
                diffs.append(
                    {
                        "type": "+",
                        "diff": f"service at '.packages['{file.package}'].services[{s_index}]': {s.name}",
                    }
                )
                s_index += 1
            m_index = 0
            for m in file.message_type:
                msg_line_num = extract_line_for_message(file.source_code_info, m_index)

                diffs.append(
                    {
                        "type": "+",
                        "line_number": msg_line_num,
                        "diff": f"message at '.packages['{file.package}'].messages[{m_index}]': {m.name}",
                    }
                )
                f_index = 0
                for field in m.field:
                    diffs.append(
                        {
                            "type": "+",
                            "diff": f"field at '.packages['{file.package}'].messages[{m_index}].fields[{f_index}]': {field.name} -> {field.type}",
                        }
                    )
                    f_index += 1
                m_index += 1

            e_index = 0
            for e in file.enum_type:
                enum_line_num = extract_line_for_enum(file.source_code_info, e_index)

                diffs.append(
                    {
                        "type": "+",
                        "line_number": enum_line_num,
                        "diff": f"enum at '.packages['{file.package}'].enums[{e_index}]': {e.name}",
                    }
                )
                v_index = 0
                for v in e.value:
                    diffs.append(
                        {
                            "type": "+",
                            "diff": f"enum value at '.packages['{file.package}'].enums[{e_index}].values[{v_index}]': {v.name} -> {v.number}",
                        }
                    )
                    v_index += 1
                e_index += 1
        file_diffs.append({"message": f"Added file: {f}", "diffs": diffs})
    return file_diffs


def _run_protoc(protoc_args,new: bool = False):
    print_info(f"compiling protobuf{'' if new == False else ' new'} files...\n\n- Logs ------------------------")
    run_protoc(protoc_args)
    print("-------------------------------\n")


def package_diff(
    sylk_json: SylkJson,
    proto_set: descriptor_pb2.FileDescriptorSet,
    file_desc: descriptor_pb2.FileDescriptorProto,
    package_schema: SylkPackage_pb2.SylkPackage,
):
    deps = list(
        map(
            lambda x: {x: next((f for f in proto_set.file if f.name == x), None)},
            file_desc.dependency,
        )
    )

    dep_i = 0
    diffs = []
    extensions = MessageToDict(file_desc.options)
    exts = proto_struct_to_dict(package_schema.extensions.get('files'))
    file_exts = exts.get(file_desc.name.split('/')[-1].split('.')[0])
    opt_i = 0
    for new_ext in extensions:
        if file_exts is None or new_ext not in file_exts:
            field_ext = next((field for field in descriptor_pb2.FileOptions.DESCRIPTOR.fields if field.name == to_snake_case(new_ext)),None)
            import_line_numbers = None
            if field_ext is not None:
                import_line_numbers = extract_line_for_file_option(file_desc.source_code_info, field_ext.number)
            ext_value = extensions[new_ext]
            diffs.append(
                    {
                        "type": "+",
                        "line_number": import_line_numbers,
                        "diff": f'\'.options[{opt_i}]\': {to_snake_case(new_ext)} = "{ext_value}";',
                    }
                )
        opt_i += 1

    for d in file_desc.dependency:
        import_line_numbers = extract_line_for_import(file_desc.source_code_info, dep_i)
        for f in list(map(lambda x: x[list(x.keys())[0]].package, deps)):
            if f not in package_schema.dependencies:
                diffs.append(
                    {
                        "type": "+",
                        "line_number": import_line_numbers,
                        "diff": f"Added dependency at '.dependencies[{dep_i}]': {file_desc.dependency[dep_i]}",
                    }
                )
        dep_i += 1
    return {
        "message": f"{package_schema.package}:{file_desc.name.split('/')[-1]}",
        "diffs": diffs,
    }

def parse_message(
    message: descriptor_pb2.DescriptorProto,
    f: descriptor_pb2.FileDescriptorProto,
    pkg_schema: SylkPackage_pb2.SylkPackage,
    adapted_pkg: SylkPackage_pb2.SylkPackage,
    removed_msgs,
    sylk_json: SylkJson,
    architect: SylkArchitect,
    msg_i: int
):
    adapted = ParseDict(
        adapt_descriptor_to_sylkmessage(message, f, msg_i),
        SylkMessage(),
    )

    opts = parse_message_options_to_sylk_extensions(message.options)
    if opts is not None:
        ext = adapted.extensions.get_or_create("google.protobuf.MessageOptions")
        ext.update(opts.get('google.protobuf.MessageOptions'))
    msg_schema = next(
        (
            m
            for m in pkg_schema.messages
            if m.full_name == adapted.full_name
        ),
        {},
    )
    message_line_number = extract_line_for_message(
        f.source_code_info, msg_i
    )
    update_msg = False
    if len(removed_msgs) > 0 and msg_i in list(map(lambda x: x[0],removed_msgs)):
        update_msg = True
        rm_msg = next((m for m in removed_msgs if m[0] == msg_i),None)
        msg_schema = rm_msg[1]
        print_error(msg_schema.full_name,True,"message removal:")
        removed_msgs.remove(rm_msg)
    elif hasattr(msg_schema,'name') == False:
        msg_schema = SylkMessage()
    else:
        update_msg = True
    diffs = message_diff(
        adapted,
        msg_schema,
        message_line_index=message_line_number,
        source_code_info=f.source_code_info,
        msg_i=msg_i,
        new_message=update_msg==False,
        msg_schema=message,
        file_desc=f
    )
    if len(diffs) > 0:
        print(display_diffs(diffs, "message"))
        if len(msg_schema.name)>0:
            architect.ReplaceMessage(
                package_path=f.package,
                message_name=msg_schema.name,
                message=adapted,
            )
        else:
            fields = []
            for field in adapted.fields:
                fields.append(MessageToDict(field))
            architect.AddMessage(
                package=adapted_pkg,
                name=adapted.name,
                fields=fields,
                description=adapted.description,
                tag=adapted.tag,
                order_pkg=[
                    adapted_pkg.package,
                    *list(
                        map(
                            lambda x: x.replace(".", "/"),
                            sylk_json.packages.keys(),
                        )
                    ),
                ]
                if sylk_json.packages is not None
                else [adapted_pkg.package]
            )
    return diffs

def weave(args, sylk_json: SylkJson = None, architect: SylkArchitect = None):
    well_known_protos = pkg_resources.resource_filename("grpc_tools", "_proto")
    sylk_protos = pkg_resources.resource_filename("sylk", "_proto")
    removed_msgs = []
    removed_enms = []
    removed_svcs = []
    if sylk_json is not None:
        proto_compare, new_files = proto_comparison.compare_proto_files(
            sylk_json._root_protos, sylk_json
        )
        files = sylk_to_files(sylk_json)
        include_dirs = [
            "-I{}".format(well_known_protos),
            "-I{}".format(sylk_protos),
        ]
        protoc_args = [
            f"--proto_path={sylk_json._root_protos}/",
            f"-I./{sylk_json._root_protos}/",
            f"--descriptor_set_out=.sylk/descriptor.pb",
            "--include_source_info",
            "--include_imports",
            *list(files.keys()) + new_files,
        ] + include_dirs

        _run_protoc(protoc_args)
        diffs = []
        if len(proto_compare) > 0:

            if file_system.check_if_file_exists(".sylk/descriptor.pb"):
                files = parse_file_descriptor_set(".sylk/descriptor.pb")

                for f in files.file:
                    if f.name in proto_compare:
                        print_note(f"diff file: {f.name} [{f.package}]")
                        pkg_schema = sylk_json._sylk_json.get("packages", {}).get(
                            f.package.replace(".", "/")
                        )
                        if pkg_schema is None:
                            pkg_schema = {}
                        pkg_schema = ParseDict(pkg_schema, SylkPackage())
                        adapted_pkg = adapt_descriptor_to_sylkpackage(
                            files, pkg_schema, f
                        )
                        pkg_diffs = package_diff(
                            sylk_json,
                            proto_set=files,
                            file_desc=f,
                            package_schema=pkg_schema,
                        )
                        if len(pkg_diffs) > 0:
                            print(display_diffs(pkg_diffs, "package"))
                            architect.ReplacePackage(package=adapted_pkg)
                        
                        for i, svc in enumerate([s for s in pkg_schema.services if s.tag == f.name.split('/')[-1].split('.')[0] or (s.tag == '' and f.name.split('/')[-1].split('.')[0] == pkg_schema.name)]):
                            if svc.name not in list(map(lambda x: x.name, f.service)):
                                removed_svcs.append((i, svc))
    
                        svc_i = 0
                        for svc in f.service:
                            adapted = ParseDict(
                                adapt_descriptor_to_sylkservice(svc, f,svc_i),
                                SylkService_pb2.SylkService(),
                            )
                            svc_schema = next(
                                (
                                    s
                                    for s in pkg_schema.services
                                    if s.full_name == adapted.full_name
                                ),
                                {},
                            )

                            update_svc = False
                            

                            # if len(removed_svcs) > 0 and svc_i in list(map(lambda x: x[0],removed_svcs)):
                            #     update_svc = True
                            #     rm_svc = next((s for s in removed_svcs if s[0] == svc_i),None)
                            #     svc_schema = ParseDict(rm_svc[1],SylkService_pb2())
                            #     print_error(svc_schema.full_name,True,"service removal:")
                            #     removed_svcs.remove(rm_svc)
                            # elif hasattr(svc_schema,'name') == False:
                            #     svc_schema = SylkService_pb2.SylkService()
                            # print_note('[-/+] found the following diffs:\n\t '+'\n\t '.join())
                            svc_line_num = extract_line_for_service(
                                f.source_code_info, svc_i
                            )

                            if len(removed_svcs) > 0 and svc_i in list(map(lambda x: x[0],removed_svcs)):
                                rm_svc = next((m for m in removed_svcs if m[0] == svc_i),None)
                                svc_schema = rm_svc[1]
                                print_error(svc_schema.full_name,True,"service removal:")
                                removed_svcs.remove(rm_svc)
                            elif hasattr(svc_schema,'name') == False:
                                svc_schema = SylkService_pb2.SylkService()

                            diffs = service_diff(
                                modified_sylk=adapted,
                                last_state_sylk=svc_schema,
                                service_line_index=svc_line_num,
                                source_code_info=f.source_code_info,
                                service_i=svc_i,
                                new_svc=update_svc==False
                            )
                            if len(diffs) > 0:
                                print(display_diffs(diffs, "service"))
                                if len(pkg_schema.services) == 0:
                                    architect.AddService(
                                        name=adapted.name,
                                        dependencies=adapted.dependencies,
                                        description=adapted.description,
                                        extensions=adapted.extensions,
                                        methods=list(map(lambda r: MessageToDict(r), adapted.methods)),
                                        order_pkg=[
                                            adapted_pkg.package,
                                            *list(
                                                map(
                                                    lambda x: x.replace(".", "/"),
                                                    sylk_json.packages.keys(),
                                                )
                                            ),
                                        ]
                                        if sylk_json.packages is not None
                                        else [adapted_pkg.package],
                                        package=adapted_pkg,
                                        tag=adapted.tag
                                    )
                                else:
                                    architect.ReplaceService(
                                        service=adapted,
                                    )

                            svc_i += 1
                        msg_i = 0
                        for i, msg in enumerate([m for m in pkg_schema.messages if m.tag == f.name.split('/')[-1].split('.')[0] or (m.tag == '' and f.name.split('/')[-1].split('.')[0] == pkg_schema.name)]):
                            if msg.name not in list(map(lambda x: x.name, f.message_type)):
                                removed_msgs.append((i, msg))
                       
                        for message in f.message_type:
                            diffs = parse_message(
                                message=message,
                                adapted_pkg=adapted_pkg,
                                architect=architect,
                                f=f,
                                msg_i=msg_i,
                                pkg_schema=pkg_schema,
                                removed_msgs=removed_msgs,
                                sylk_json=sylk_json
                            )
                            msg_i += 1

                        for i, enm in enumerate([m for m in pkg_schema.enums if m.tag == f.name.split('/')[-1].split('.')[0] or (m.tag == '' and f.name.split('/')[-1].split('.')[0] == pkg_schema.name)]):
                            if enm.name not in list(map(lambda x: x.name, f.enum_type)):
                                removed_enms.append((i, enm))
                        enum_i = 0
                        for enum in f.enum_type:
                            adapted = ParseDict(
                                adapt_descriptor_to_sylkenum(enum, f, enum_i),
                                SylkEnum_pb2.SylkEnum(),
                            )
                            enm_schema = next(
                                (
                                    e
                                    for e in pkg_schema.enums
                                    if e.full_name == adapted.full_name
                                ),
                                {},
                            )
                            update_enm = False
                            if len(removed_enms) > 0 and enum_i in list(map(lambda x: x[0],removed_enms)):
                                update_enm = True
                                rm_enm = next((e for e in removed_enms if e[0] == enum_i),None)
                                enm_schema = ParseDict(rm_enm[1],SylkMessage())
                                print_error(enm_schema.full_name,True,"enum removal:")
                                removed_enms.remove(rm_enm)
                            elif hasattr(enm_schema,'name') == False:
                                enm_schema = SylkEnum_pb2.SylkEnum()
                            else:
                                update_enm = True

                            # enm_schema = ParseDict(enm_schema, SylkEnum_pb2.SylkEnum())
                            # print_note('[-/+] found the following diffs:\n\t '+'\n\t '.join())
                            enum_line_num = extract_line_for_enum(
                                f.source_code_info, enum_i
                            )
                            diffs = enum_diff(
                                adapted,
                                enm_schema,
                                enum_line_index=enum_line_num,
                                source_code_info=f.source_code_info,
                                enm_i=enum_i,
                                new_enum=update_enm==False
                            )
                            if len(diffs) > 0:
                                print(display_diffs(diffs, "enum"))
                                if len(enm_schema.name)>0:
                                    architect.ReplaceEnum(
                                        package_path=f.package,
                                        enum_name=enm_schema.name,
                                        enum=adapted,
                                    )
                                
                                else:
                                    values = []
                                    for ev in adapted.values:
                                        values.append(MessageToDict(ev))
                                    architect.AddEnum(
                                        adapted_pkg,
                                        adapted.name,
                                        values,
                                        tag=adapted.tag,
                                        order_pkg=[
                                            adapted_pkg.package,
                                            *list(
                                                map(
                                                    lambda x: x.replace(".", "/"),
                                                    sylk_json.packages.keys(),
                                                )
                                            ),
                                        ]
                                        if sylk_json.packages is not None
                                        else [adapted_pkg.package]
                                    )

                            enum_i += 1
            else:
                print_error(
                    "protoc failed, we cant save you proto schema.\nfirst fix your protobuf files, see details above."
                )
        elif len(new_files) == 0:
            print_info("no changes were made on protobuf from you current sylk schema")

        # Handle new files
        if len(new_files) > 0:

            if file_system.check_if_file_exists(".sylk/descriptor.pb"):
                files = parse_file_descriptor_set(".sylk/descriptor.pb")
                diffs = files_diff_add(new_files, files)
                package_to_files = {}
                unique_pkgs = list(set([tmp_file.package for tmp_file in files.file]))

                dependency_graph = defaultdict(list)
                for pkg in unique_pkgs:
                    for f in [tmp_f for tmp_f in files.file if tmp_f.package == pkg]:
                        # Dependency graph as an adjacency list.
                        # Key is the proto file, value is a list of files it depends on.
                        dependency_graph[f.name] = f.dependency

                # Perform topological sort
                # Create an in-degree dictionary
                in_degree = {node: 0 for node in dependency_graph}
                for dependencies in dependency_graph.values():
                    for dep in dependencies:
                        in_degree[dep] += 1

                # Initialize queue and result list
                queue = deque()
                result = []

                # Add nodes with in-degree 0 to the queue
                for node, degree in in_degree.items():
                    if degree == 0:
                        queue.append(node)

                # Perform the topological sort
                while queue:
                    current_node = queue.popleft()
                    result.append(current_node)

                    for neighbor in dependency_graph[current_node]:
                        in_degree[neighbor] -= 1
                        if in_degree[neighbor] == 0:
                            queue.append(neighbor)

                # Check if graph had cycles
                if len(result) != len(dependency_graph):
                    print_error("The graph contains a cycle. Topological sort is not possible.")


                # Step 1: Create a dictionary mapping .proto filenames back to their packages
                file_to_package = {}
                for package in unique_pkgs:
                    for dep_file in [tmp_f.name for tmp_f in files.file if tmp_f.package == package]:
                        file_to_package[dep_file] = package

                # Step 2: Create a list of packages in the order they should be resolved
                sorted_packages = []
                seen_packages = set()

                for file in result:
                    package = file_to_package.get(file)
                    if package is not None and package not in seen_packages:
                        sorted_packages.append(package)
                        seen_packages.add(package)


                for pkg in sorted_packages:
                    if pkg.split('.')[0] == sylk_json.domain: 
                        sylk_package = SylkPackage_pb2.SylkPackage()
                        for f in [tmp_f for tmp_f in files.file if tmp_f.package == pkg]:
                            sylk_package = parse_descriptor_to_sylk_package(files, f, sylk_package)

                        architect._sylk.execute(
                            CommandMap._ADD_RESOURCE,
                            {
                                "packages": {
                                    f"{sylk_package.package.replace('.','/')}": MessageToDict(
                                        sylk_package
                                    )
                                }
                            },
                            sorted_packages[::-1],
                        )

                if len(diffs) > 0:
                    for f_diff in diffs:
                        print(display_diffs(f_diff, "file"))
                    
                    # if args.dry_run == False:
                    #     confirm = prompter.ask_user_question(
                    #         questions=[
                    #             prompter.QConfirm(
                    #                 name="confirm",
                    #                 default=True,
                    #                 message="please confirm the weaving process for you schema",
                    #                 ignore=args.yes,
                    #             )
                    #         ]
                    #     )
                    #     if confirm.get("confirm") == True:
                    #         architect.Save()
                    #         print_success("Updated schema")

                    #         if args.build:
                    #             build_protos(sylk_json.path + "/sylk.json", args.yes)

                    # else:
                    #     print_note(
                    #         "dry run mode -> everything still remains the same..."
                    #     )
            else:
                print_error(
                    "protoc failed, we cant save you proto schema.\nfirst fix your protobuf files, see details above."
                )
        if len(removed_msgs) > 0 or len(removed_enms) > 0 or len(removed_svcs) > 0:
            print_error("make sure your not losing data with running 'sylk build --protos' before any manual change of proto code.",True,"Seems like you have done changes directly on sylk.json before using 'weave'")
            print_error("Following will be disregarded:\n\t- {}".format('\n\t- '.join([m[1].full_name for m in removed_msgs]+[e[1].full_name for e in removed_enms]+[s[1].full_name for s in removed_svcs])))
            if args.dry_run == False:
                confirm_unsaved_code_change = prompter.ask_user_question(
                    questions=[
                        prompter.QConfirm(
                            name="confirm",
                            default=True,
                            message="Disregard changes",
                            ignore=args.yes
                            or architect._unsaved_change == False,
                        )
                    ]
                )
                if confirm_unsaved_code_change.get("confirm") == False:
                    print_error("exiting weave process, must pass a valid confirmation")
                    exit(1)
                for rm_svc in removed_svcs:
                    architect.RemoveService(rm_svc[1].full_name)

        print("")
        if args.dry_run == False:
            if len(diffs) > 0:
                confirm = prompter.ask_user_question(
                    questions=[
                        prompter.QConfirm(
                            name="confirm",
                            default=True,
                            message="please confirm the weaving process for you schema",
                            ignore=args.yes
                            or architect._unsaved_change == False,
                        )
                    ]
                )
                if confirm.get("confirm") == True:
                    architect.Save()
                    print_success("Updated schema")

                    if args.build:
                        build_protos(sylk_json.path + "/sylk.json", args.yes)
        else:
            print_note("dry run mode -> everything still remains the same.")
        if file_system.check_if_file_exists(".sylk/descriptor.pb"):
            file_system.removeFile(".sylk/descriptor.pb")
        
    else:
        if getattr(args, "proto_path") is None:
            print_error(
                "cant weave proto files without specifyin the root proto directory with passing `--proto-path` argument"
            )
            exit(1)
