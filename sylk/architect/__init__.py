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

from enum import Enum
import logging
from sylk import __version__
from sylk.commons.errors import SylkProtoError
from sylk.commons.file_system import join_path
from sylk.commons.pretty import print_error, print_info, print_note

from sylk.commons.protos.sylk.SylkClient.v1 import SylkClient_pb2
from sylk.commons.protos.sylk.SylkServer.v1 import SylkServer_pb2
from sylk.commons.protos.sylk.SylkProject.v1 import SylkProject_pb2

from google.protobuf.json_format import MessageToDict
from sylk.commons.resources import (
    generate_enum,
    generate_message,
    generate_package,
    generate_project,
    generate_rpc,
    generate_service,
)

from sylk.architect.recievers import Builder
from sylk.architect.commands import (
    AddResource,
    EditResource,
    InitProject,
    Logger,
    RemoveResource,
    SetDomain,
)
from sylk.architect.invoker import Sylk

logging.basicConfig(
    level="INFO",
    format="%(asctime)s - [%(filename)10s] - %(funcName)10s() - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y%m%d-%H:%M%p",
)

def replace_object_element(array, target_object, new_object):
    for i, element in enumerate(array):
        if element == target_object:  # Using the '==' operator for object comparison
            array[i] = new_object
            break

class CommandMap(Enum):
    _REMOVE_RESOURCE = "RemoveResource"
    _EDIT_RESOURCE = "EditResource"
    _ADD_RESOURCE = "AddResource"
    _SET_DOMAIN = "SetDomain"
    _SET_CONFIG = "SetConfig"

class SylkArchitect:
    def __init__(
        self, path, domain="domain", project_name="project", save=None, base_protos="protos", format="json"
    ) -> None:
        logging.debug("Starting sylk build architect process")
        if "sylk.json" not in path:
            raise SylkProtoError(
                "sylk.json file path is not valid",
                "Make sure you pass in your architect class the right path to your sylk.json file",
            )
        self._path = path
        self._org_id = None
        self._project = None
        self._domain = domain
        self._project_name = project_name
        self._base_protos = base_protos
        self._builder = Builder()
        self._remove_resource = RemoveResource(self._builder)
        self._edit_resource = EditResource(self._builder)
        self._add_resource = AddResource(self._builder)
        self._logger = Logger(self._builder)
        self._set_domain = SetDomain(self._builder)
        self._format = format
        self._sylk = Sylk(self._path, save, self._format)
        self._sylk.registerCommand(CommandMap._REMOVE_RESOURCE, self._remove_resource)
        self._sylk.registerCommand(CommandMap._EDIT_RESOURCE, self._edit_resource)
        self._sylk.registerCommand(CommandMap._ADD_RESOURCE, self._add_resource)
        self._sylk.registerHook(CommandMap._ADD_RESOURCE, "log", self._logger)
        self._unsaved_change = False

    def SetDomain(self, domain):
        self._unsaved_change = True
        self._domain = domain
        self._sylk.execute(
            CommandMap._ADD_RESOURCE, {"organization": {"domain": domain}}, []
        )

    def SetOrgId(self, orgId):
        self._unsaved_change = True
        self._org_id = orgId
        self._sylk.execute(CommandMap._ADD_RESOURCE, {"organization": {"orgId": orgId}}, [])

    def SetConfig(self, config):
        self._unsaved_change = True
        self._sylk.execute(CommandMap._ADD_RESOURCE, {"configs": config}, [])

    def SetSylkVersion(self):
        self._unsaved_change = True
        self._sylk.execute(
            CommandMap._ADD_RESOURCE, {"sylkVersion": __version__.__version__}, []
        )

    def AddProject(
        self,
        name=None,
        server_language=SylkServer_pb2.SylkServerLanguages.Name(SylkServer_pb2.python),
        clients=[],
    ) -> SylkProject_pb2.SylkProject:
        self._unsaved_change = True
        name = name if name is not None else self._project_name
        dict = generate_project(self._path, name, server_language, clients, json=True, code_base_path=self._sylk.sylkJson.get('configs',{}).get('codeBasePath'))
        project = generate_project(self._path, name, server_language, clients, code_base_path=self._sylk.sylkJson.get('configs',{}).get('codeBasePath'))
        self._sylk.execute(CommandMap._ADD_RESOURCE, {"project": dict}, [])
        self._project = project
        return project

    def AddClient(self):
        pass

    def AddService(
        self,
        name,
        dependencies,
        description,
        methods,
        package,
        extensions=None,
        tag=None,
        order_pkg=[]
    ):
        self._unsaved_change = True
        path_with_domain = package.package + '.' + name
        service = generate_service(
            self._path,
            path_with_domain,
            self._sylk.sylkJson.get("project")["server"]["language"],
            dependencies=dependencies,
            description=description,
            extensions=extensions,
            methods=methods,
            sylk_json=self._sylk.sylkJson,
            tag=tag
        )
        if next((s for s in package.services if s.name == service.name), None) is None:
            package.services.append(service)
            self._sylk.execute(
                CommandMap._ADD_RESOURCE,
                {
                    "packages": {
                        f"{package.package.replace('.','/')}": MessageToDict(
                            package
                        )
                    }
                },
                order_pkg
            )
            return service
        else:
            logging.error(
                f"Cannot create service '{service.name}' already exists under '{package.name}' package"
            )
        return service

    def AddRPC(self, package, service, name, order_pkg=[], *args):
        self._unsaved_change = True
        # service_name = service.name
        # service_ver = service.full_name.split(".")[2]
        package_path = (
            f"{package.package.replace('.','/')}"
        )
        _IN = args[0][0]
        _OUT = args[0][1]
        RPC = generate_rpc(self._path, name, _IN[0], _OUT[0], _IN[1], _OUT[1], args[1])
        service.methods.append(RPC)
        
        for i, svc in enumerate(package.services):
            if svc.name == service.name:
                package.services[i].methods.append(RPC)
                break
        
        self._sylk.execute(
            CommandMap._ADD_RESOURCE,
            {
                "packages": {
                    package_path: MessageToDict(package)
                }
            },
            order_pkg
        )

    def AddPackage(
        self,
        name,
        dependencies=[],
        messages=[],
        description=None,
        extensions=None,
        version_component=None,
        order_pkg=[]
    ):
        self._unsaved_change = True
        if name == self._domain:
            path_with_domain = self._domain
        else:
            path_with_domain = self._domain + '.' + name
        dict = generate_package(
            self._path,
            path_with_domain,
            dependencies=dependencies,
            messages=messages,
            description=description,
            extensions=extensions,
            json=True,
            sylk_json=self._sylk.sylkJson,
            version=version_component
        )
        package = generate_package(
            self._path,
            path_with_domain,
            dependencies=dependencies,
            messages=messages,
            description=description,
            extensions=extensions,
            sylk_json=self._sylk.sylkJson,
            version=version_component
        )
        self._sylk.execute(
            CommandMap._ADD_RESOURCE,
            {
                "packages": {
                    f"{path_with_domain.replace('.','/')}": dict
                }
            },
            order_pkg
        )
        return package

    def AddMessage(
        self,
        package,
        name,
        fields,
        description=None,
        options=None,
        extensions=None,
        domain=None,
        tag=None,
        order_pkg=[]
    ):
        self._unsaved_change = True
        path_with_domain = self._domain + '.' + name
        message = generate_message(
            self._path,
            self._domain if domain is None else domain,
            package,
            name,
            fields,
            option=options,
            description=description,
            extensions=extensions,
            sylk_json=self._sylk.sylkJson,
            tag=tag,
        )
        if next((m for m in package.messages if m.name == message.name), None) is None:
            package.messages.append(message)
            self._sylk.execute(
                CommandMap._ADD_RESOURCE,
                {
                    "packages": {
                        f"{package.package.replace('.','/')}": MessageToDict(
                            package
                        )
                    }
                },
                order_pkg
            )
            return message
        else:
            logging.error(
                f"Cannot create message '{message.name}' already exists under '{package.name}' package"
            )
        return message

    def AddEnum(
        self,
        package,
        name,
        enum_values,
        description=None,
        domain=None,
        tag=None,
        order_pkg=[]
    ):
        self._unsaved_change = True
        enum = generate_enum(
            self._path,
            self._domain if domain is None else domain,
            package,
            name,
            enum_values,
            description=description,
            tag=tag
        )
        
        package.enums.append(enum)
        self._sylk.execute(
            CommandMap._ADD_RESOURCE,
            {
                "packages": {
                    f"{package.package.replace('.','/')}": MessageToDict(
                        package
                    )
                }
            },
            order_pkg
        )
        return enum

    def ReplaceService(
        self,
        service
    ):
        self._unsaved_change = True
        self._sylk.execute(
            CommandMap._EDIT_RESOURCE, MessageToDict(service)
        )
        return service

    def EditService(
        self, name, dependencies, description, methods, extensions=None, version="v1"
    ):
        self._unsaved_change = True
        service = generate_service(
            self._path,
            self._domain,
            name,
            self._sylk.sylkJson.get("project")["server"]["language"],
            dependencies=dependencies,
            description=description,
            methods=methods,
            extensions=extensions,
            sylk_json=self._sylk.sylkJson,
            version=version,
        )
        self._sylk.execute(CommandMap._EDIT_RESOURCE, MessageToDict(service))
        return service

    def ReplacePackage(
        self,
        package
    ):
        self._unsaved_change = True
        self._sylk.execute(
            CommandMap._EDIT_RESOURCE, MessageToDict(package)
        )
        return package

    def EditPackage(
        self,
        name,
        dependencies=[],
        messages=[],
        enums=[],
        description=None,
        extensions=None,
        version="v1",
    ):
        self._unsaved_change = True
        package = generate_package(
            self._path,
            name,
            dependencies=dependencies,
            messages=messages,
            description=description,
            enums=enums,
            extensions=extensions,
            sylk_json=self._sylk.sylkJson,
            version=version,
        )
        self._sylk.execute(CommandMap._EDIT_RESOURCE, MessageToDict(package))
        return package

    def ReplaceMessage(
        self,
        package_path,
        message_name,
        message
    ):
        self._unsaved_change = True
        self._sylk.execute(
            CommandMap._EDIT_RESOURCE, MessageToDict(message), old_name=message_name, package=package_path
        )
        return message

    def EditMessage(
        self,
        package,
        name,
        fields,
        description=None,
        options=None,
        old_name=None,
        extensions=None,
        tag=None
    ):
        self._unsaved_change = True
        message = generate_message(
            self._path,
            self._domain,
            package,
            name,
            fields,
            option=options,
            description=description,
            extensions=extensions,
            sylk_json=self._sylk.sylkJson,
            tag=tag
        )
        self._sylk.execute(
            CommandMap._EDIT_RESOURCE, MessageToDict(message), old_name=old_name, package=package.package
        )
        return message

    def EditEnum(
        self,
        package,
        name,
        enum_values,
        description=None,
        tag=None,
    ):
        self._unsaved_change = True
        enum = generate_enum(self._path, self._domain, package, name, enum_values,tag=tag,description=description)
        self._sylk.execute(CommandMap._EDIT_RESOURCE, MessageToDict(enum))

    def ReplaceEnum(
        self,
        package_path,
        enum_name,
        enum
    ): 
        self._unsaved_change = True
        self._sylk.execute(
            CommandMap._EDIT_RESOURCE, MessageToDict(enum), old_name=enum_name, package=package_path
        )
        return enum

    def EditRPC(
        self,
        service,
        name,
        input_type,
        output_type,
        client_stream,
        server_stream,
        description,
        extensions=None,
    ):
        self._unsaved_change = True
        RPC = generate_rpc(
            self._path,
            name,
            client_stream,
            server_stream,
            input_type,
            output_type,
            description,
        )
        self._sylk.execute(CommandMap._EDIT_RESOURCE, MessageToDict(RPC))

    def RemoveService(self, full_name):
        self._unsaved_change = True
        self._sylk.execute(CommandMap._REMOVE_RESOURCE, "service", { "full_name": full_name })


    def RemoveEnum(self, full_name):
        self._unsaved_change = True
        self._sylk.execute(CommandMap._REMOVE_RESOURCE, full_name)

    def RemoveMessage(self, full_name):
        self._unsaved_change = True
        self._sylk.execute(CommandMap._REMOVE_RESOURCE, full_name)

    def RemoveRpc(self, full_name):
        self._unsaved_change = True
        self._sylk.execute(CommandMap._REMOVE_RESOURCE, full_name)

    def RemoveField(self, full_name):
        self._unsaved_change = True
        self._sylk.execute(CommandMap._REMOVE_RESOURCE, full_name)

    def RemoveOneofField(self, full_name):
        self._unsaved_change = True
        self._sylk.execute(CommandMap._REMOVE_RESOURCE, full_name)

    def RemoveEnumValue(self, full_name):
        self._unsaved_change = True
        self._sylk.execute(CommandMap._REMOVE_RESOURCE, full_name)

    def Save(self):
        logging.debug("Saving sylk.build architect process")

        self._sylk.save()
        self._unsaved_change = False

    def undo(self):
        self._sylk.undo()

    def redo(self):
        self._sylk.redo()
