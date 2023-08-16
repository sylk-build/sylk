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

import inspect
import logging
import subprocess
import sylk.builder as builder
from sylk.commons import helpers, file_system, pretty, resources, protos
from sylk.builder.plugins.static import gitignore_py


@builder.hookimpl
def pre_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    pretty.print_info("🔌 Starting sylk build process %s plugin" % (__name__))


@builder.hookimpl
def post_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    # TODO add postbuild validation of generated code
    # pretty.print_success("Finished sylk build process %s plugin" % (__name__))
    for pkg in sylk_json.packages:
        # pkg_path = '/'.join(pkg.split('/')[:-1])
        base = f'{sylk_json._root_protos}/' if sylk_json._root_protos != '' else ''
        target_file = base+"/".join(pkg.split("/"))
        temp_path = []

        for d in target_file.split("/"):
            temp_path.append(d)
            if (
                file_system.check_if_dir_exists(
                    file_system.join_path(
                        sylk_json.path, sylk_json.code_base_path, "services", "/".join(temp_path)
                    )
                )
                == False
            ):
                file_system.mkdir(
                    file_system.join_path(
                        sylk_json.path, sylk_json.code_base_path, "services", "/".join(temp_path)
                    )
                )
            if (
                file_system.check_if_file_exists(
                    file_system.join_path(
                        sylk_json.path, sylk_json.code_base_path, "services", "/".join(temp_path), "__init__.py"
                    )
                )
                == False
            ):
                file_system.wFile(
                    file_system.join_path(
                        sylk_json.path, sylk_json.code_base_path, "services", "/".join(temp_path), "__init__.py"
                    ),
                    "",
                )
        name = pkg.split("/")[-1].split(".")[0]
        pkg_path = "/".join(pkg.split("/")[:-1])
        # if (
        #     file_system.check_if_file_exists(
        #         file_system.join_path(
        #             sylk_json.path, "services", pkg_path, f"{name}_pb2.py"
        #         )
        #     )
        #     == False
        # ):
        #     try:
        #         file_system.copyFile(
        #             file_system.join_path(
        #                 sylk_json.path, "clients", "python", pkg_path, f"{name}_pb2.py"
        #             ),
        #             file_system.join_path(
        #                 sylk_json.path,
        #                 "services",
        #                 "/".join(temp_path),
        #                 f"{name}_pb2.py",
        #             ),
        #         )
        #     except Exception as e:
        #         pass
    

    return (__name__, "OK")


@builder.hookimpl
def init_project_structure(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext, pre_data
):
    directories = [
        # Clients
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "python"),
        # Protos
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "services", sylk_json._root_protos),
    ]
    
    # Init files
    files = [
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "services", "__init__.py"),
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "python", "__init__.py"),
        file_system.join_path(sylk_json.path, sylk_json._root_protos, "__init__.py"),
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "__init__.py"),
    ]

    if pre_data.get('protos_only',False) == False:

        for dir in directories:
            file_system.mkdir(dir)

       
        # Bin files
        file_system.wFile(
            file_system.join_path(sylk_json.path, "bin", "init.sh"), bash_init_script
        )
        if sylk_json.get_server_language() == "python":
            file_system.wFile(
                file_system.join_path(sylk_json.path, "bin", "run-server.sh"),
                bash_run_server_script(sylk_json.code_base_path,sylk_json._root_protos),
                overwrite=True
            )
        # file_system.wFile(file_system.join_path(sylk_json.path,'.sylk','contxt.json'),'{"files":[]}')
        # .gitignore
        file_system.wFile(file_system.join_path(sylk_json.path, ".gitignore"), gitignore_py)
        for file in files:
            file_system.wFile(file, "")

    return [directories, files]


@builder.hookimpl
def write_services(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    for svc in sylk_json.services:
        service_name = svc.get("name")
        ver = helpers.parse_version_component(svc.get("fullName"))
        if ver:
            service_version = svc.get("fullName").split(".")[-2]
            svc_path = file_system.join_path(
                    sylk_json.path,
                    sylk_json.code_base_path,
                    "services",
                    service_name,
                    service_version,
                    f"{service_name}.py",
                )
        else:
            svc_path = file_system.join_path(
                    sylk_json.path,
                    sylk_json.code_base_path,
                    "services",
                    service_name,
                    f"{service_name}.py",
                )

        if (
            file_system.check_if_file_exists(
                svc_path
            )
            == False
        ):
            service_code = helpers.SylkServicePy(
                sylk_json.project.get("packageName"),
                service_name,
                svc.get("dependencies"),
                svc,
                context=sylk_context,
                sylk_json=sylk_json,
            ).to_str()
            file_system.wFile(
                file_system.join_path(
                    sylk_json.path, sylk_json.code_base_path, "services", service_name, "__init__.py"
                ),
                "",
                overwrite=False,
                force=True,
            )
            file_system.wFile(
                file_system.join_path(
                    '/'.join(svc_path.split('/')[:-1]),
                    "__init__.py",
                ),
                "",
                overwrite=False,
                force=True,
            )
            file_system.wFile(
                svc_path,
                service_code,
                overwrite=True,
                force=True,
            )
        # else:
        #     pretty.print_info("Make sure you are editing the {0} file\n - See how to edit service written in python".format(file_system.join_path(
        #         sylk_json.path, 'services', f'{svc}.py')))


@builder.hookimpl
def pre_compile_protos(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    pretty.print_info("Running pre compile protos - python server")
    proto_path = file_system.join_path(sylk_json.path,'services',sylk_json._root_protos, sylk_json.domain)
    file_system.removeDir(proto_path)
    protos_out = file_system.join_path(sylk_json.code_base_path, 'services', sylk_json._root_protos)
    return {
        "sylk.builder.plugins.SylkProto:compile_protos():commands": [
            f"--proto_path={sylk_json._root_protos}/",
            f"--python_out=./{protos_out}",
            f"--pyi_out=./{protos_out}",
            f"--grpc_python_out=./{protos_out}",
            f"-I./{sylk_json._root_protos}/",
        ],
        "sylk.builder.plugins.SylkProto:compile_protos():include_dirs": [],
    }


@builder.hookimpl
def write_server(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext, pre_data
):
    # pretty.print_error(pre_data,True,'pre_data')

    if (
        file_system.check_if_file_exists(
            file_system.join_path(sylk_json.path, sylk_json.code_base_path, "server", "server.py")
        )
        == False
    ):
        imports = [
            "_ONE_DAY_IN_SECONDS = 60 * 60 * 24",
            "from concurrent import futures",
            "import time",
            "import grpc",
        ]
        services_bindings = []
        svcs = []
        for svc in sylk_json.services:
            version = None
            pkg_path = sylk_json._proto_tree.get_parent(svc.get('fullName')).full_path
            ver = sylk_json._proto_tree._parse_version_component(pkg_path)
            code_base_path = '' if sylk_json.code_base_path is None or sylk_json.code_base_path == '' else f'{sylk_json.code_base_path}.'
            base_protos = f'{code_base_path}services.{sylk_json._root_protos}' if sylk_json._root_protos is not None and sylk_json._root_protos != '' else f'{code_base_path}services'
            svc_desc_path = f'{base_protos}.{pkg_path}'

            svc_name = svc.get('name')
            if ver is not None:
                version = pkg_path.split('.')[-1]
                svc_impl_path = f'{code_base_path}services.{svc_name}.{version}.{svc_name}'
                svc_desc_module_name = svc.get('tag') if svc.get('tag') is not None else pkg_path.split('.')[-2]
            else:
                svc_impl_path = f'{code_base_path}services.{svc_name}.{svc_name}'
                svc_desc_module_name = svc.get('tag') if svc.get('tag') is not None else pkg_path.split('.')[-2]

            # svc_name = sylk_json.services[svc].get("name")
            svc_ver = version if version is not None else ''
            svcs.append(
                (
                    svc_impl_path,
                    svc_name,
                    svc_ver,
                )
            )
            imports.append(
                f"from {svc_desc_path} import {svc_desc_module_name}_pb2_grpc as {svc_desc_module_name}_{svc_ver}_pb2_grpc"
            )
            services_bindings.append(
                f"{svc_desc_module_name}_{svc_ver}_pb2_grpc.add_{svc_name}Servicer_to_server({svc_name}_{svc_ver}(),server)"
            )
        # svcs = ', '.join(svcs)
        for s in svcs:
            imports.append(f"from {s[0]} import {s[1]} as {s[1]}_{s[2]}")
        services_bindings = "\n\t".join(services_bindings)
        port = sylk_json._config.get("port")
        imports = "\n".join(imports)
        server_code = f'"""sylk.build Generated Server Code"""\n\
{imports}\n\n\
def serve(host="0.0.0.0:{port}"):\n\
\tserver = grpc.server(futures.ThreadPoolExecutor(max_workers=10))\n\
\t{services_bindings}\n\
\tserver.add_insecure_port(host)\n\
\tserver.start()\n\
\tprint("[*] Started sylk.build server at -> %s" % (host))\n\
\ttry:\n\
\t\twhile True:\n\
\t\t\ttime.sleep(_ONE_DAY_IN_SECONDS)\n\
\texcept KeyboardInterrupt:\n\
\t\tserver.stop(0)\n\n\
if __name__ == "__main__":\n\
\tserve()'
        file_system.wFile(
            file_system.join_path(sylk_json.path, sylk_json.code_base_path, "server", "server.py"),
            server_code,
            overwrite=True,
        )
    else:
        pretty.print_info("Make sure you are adding new services into server/server.py")


# @builder.hookimpl
# def rebuild_context(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
#     if sylk_json.services is not None:
#         for svc in sylk_json.services:
#             try:
#                 svcFile = file_system.rFile(file_system.join_path(
#                     sylk_json.path, 'services', f'{svc}.py'))
#                 is_init = False
#                 for l in svcFile:
#                     if '__init__' in l:
#                         is_init = True
#                         break
#                 # Non RPC functions should have # @skip line above func name
#                 function_code_inlines = helpers.parse_code_file(svcFile, '@skip')
#                 # Parse all rpc's in file by default # @rpc seperator
#                 rpc_code_inlines = helpers.parse_code_file(svcFile)
#                 for f in sylk_context.files:

#                     if svc in f.get('file'):
#                         # Iterating all regular functions
#                         for func in function_code_inlines:
#                             func_code = []
#                             for l in func:
#                                 if '@rpc @@sylk.build' in l:
#                                     break

#                                 func_code.append(l)

#                             sylk_context.set_method_code(svc, func_code[0].split(
#                                 'def ')[1].split('(')[0], ''.join(func_code))
#                         methods_i = 0
#                         for r in sylk_json.services[svc]['methods']:
#                             if next((m for m in f.get('methods') if m['name'] == r['name']),None) is None:
#                                 new_rpc_context = {'name': r.get('name'), 'type': 'rpc', 'code': '\t\tpass'}
#                                 sylk_context.new_rpc(svc, new_rpc_context)
#                         # Iterating all RPC's functions
#                         for m in f.get('methods'):
#                             if m['type'] == 'rpc':
#                                 # Checking if edit to method has happened - meaning canot find in sylk.json all context methods
#                                 if next((r for r in sylk_json.services[svc]['methods'] if r['name'] == m['name']), None) == None:
#                                     # Getting method details from sylk.json
#                                     new_method = sylk_json.services[svc]['methods'][methods_i]
#                                     # Building new context with old func code
#                                     new_rpc_context = {'name': new_method.get(
#                                         'name'), 'type': 'rpc', 'code': ''.join(rpc_code_inlines[methods_i][1:])}
#                                     # Editing inplace the RPC context
#                                     sylk_context.edit_rpc(
#                                         svc, m.get('name'), new_rpc_context)
#                                 else:
#                                     # Setting new context
#                                     sylk_context.set_rpc_code(svc, m.get('name'), ''.join(
#                                         rpc_code_inlines[methods_i][1:]))

#                                 methods_i += 1

#             except Exception as e:
#                 pretty.print_error(e)
#                 logging.debug(e)
#     if sylk_context is not None:
#         file_system.wFile(file_system.join_path(
#             sylk_json.path, '.sylk', 'context.json'), sylk_context.dump(), True, True)


@builder.hookimpl
def override_generated_classes(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext
):
    pass
    # for f in file_system.walkFiles(file_system.join_path(sylk_json.path, 'services', 'protos')):
    #     name = f.split('_pb2')
    #     if '_grpc' not in name:
    #         file_content = file_system.rFile(
    #             file_system.join_path(sylk_json.path, 'services', 'protos', f))
    #         file_content.insert(
    #             5, '\nfrom typing import overload, Iterator, List, Dict\n')
    #         if len(name) > 1:
    #             name = name[0]

    #             # svc_proto = next((svc for svc in sylk_json.services if svc == name),None)
    #             pkg_proto = next((pkg for pkg in sylk_json.packages if pkg.split(
    #                 '/')[-1].split('.')[0] == name), None)
    #             if pkg_proto is not None:
    #                 pkg_proto_name = pkg_proto.split('/')[-1].split('.')[0]

    #                 for m in sylk_json.packages[pkg_proto].get('messages'):
    #                     index = 0
    #                     for l in file_content:
    #                         message_description = m.get('description') if m.get('description') is not None else ''
    #                         message_name = m['name']
    #                         if f'{message_name} = _reflection' in l[:len(message_name)+15]:
    #                             temp_fields = []
    #                             init_fields = []
    #                             docstring_fields = []
    #                             for field in m['fields']:
    #                                 key_type = field.get('keyType').split('_')[-1].lower() if field.get('keyType') is not None and field.get('keyType') != -1 else None
    #                                 value_type = field.get('valueType').split('_')[-1].lower() if field.get('valueType') is not None and field.get('valueType') != -1 else None
    #                                 fName = field['name']
    #                                 fDescription = field.get('description') if field.get('description') is not None else ''

    #                                 fType = parse_proto_type_to_py(field['fieldType'].split(
    #                                     '_')[-1].lower(), field['label'].split('_')[-1].lower(), field.get('messageType'), field.get('enumType'),current_pkg=pkg_proto_name,key_type=key_type,value_type=value_type)
    #                                 if field['fieldType'].split(
    #                                     '_')[-1].lower() == 'enum':
    #                                     temp_fields.append(
    #                                         f'{fName} = {fType} # type: int')
    #                                 elif field['fieldType'].split(
    #                                     '_')[-1].lower() == 'oneof':
    #                                     for f_oneof in field.get('oneofFields'):
    #                                         fOneofName = f_oneof['name']
    #                                         fOneofType = parse_proto_type_to_py(f_oneof['fieldType'].split(
    #                                             '_')[-1].lower(), 'optional', f_oneof.get('messageType'), f_oneof.get('enumType'),current_pkg=pkg_proto_name)
    #                                         if f_oneof['fieldType'].split(
    #                                             '_')[-1].lower() == 'enum':
    #                                             temp_fields.append(
    #                                                 f'{fOneofName} = {fOneofType} # type: int')
    #                                         else:
    #                                             temp_fields.append(
    #                                                 f'{fOneofName} = {fOneofType} # type: {fOneofType}')
    #                                 else:
    #                                     temp_fields.append(
    #                                         f'{fName} = {fType} # type: {fType}')

    #                                 if field.get('fieldType') != 'TYPE_ONEOF':
    #                                     init_fields.append(f'{fName}={fType}')
    #                                 else:
    #                                     for f_oneof in field.get('oneofFields'):
    #                                         fOneofName = f_oneof['name']
    #                                         fOneofType = parse_proto_type_to_py(f_oneof['fieldType'].split(
    #                                             '_')[-1].lower(), 'optional', f_oneof.get('messageType'), f_oneof.get('enumType'),current_pkg=pkg_proto_name)
    #                                         init_fields.append(f'{fOneofName}={fOneofType}')
    #                                 docstring_fields.append(f'{fName} : {fType}\n\t\t\t{fDescription}')

    #                             # for field in m['fields']:
    #                             #     fName = field['name']
    #                             #     fType = parse_proto_type_to_py(field['fieldType'].split(
    #                             #         '_')[-1].lower(), field['label'].split('_')[-1].lower(), field.get('messageType'), field.get('enumType'))
    #                             #     temp_fields.append(
    #                             #         f'{fName} = {fType} # type: {fType}')
    #                             #     init_fields.append(f'{fName}={fType}')
    #                             temp_fields = '\n\t'.join(temp_fields)
    #                             init_fields = ', '.join(init_fields)
    #                             docstring = '{0}\n\n\t\tAttributes:\n\t\t----------\n\t\t{1}'.format(message_description,'\n\t\t'.join(docstring_fields))
    #                             file_content.insert(
    #                                 index, f'\n@overload\nclass {message_name}(_message.Message):\n\t"""sylk.build generated message [{sylk_json.domain}.{pkg_proto_name}.v1.{message_name}]\n\tA class respresent a {message_name} type\n\t{message_description}\n\t"""\n\t{temp_fields}\n\n\tdef __init__(self, {init_fields}):\n\t\t"""\n\t\t{docstring}\n\t\t"""\n\t\tpass\n')
    #                             break
    #                         index += 1
    #                 file_system.wFile(file_system.join_path(
    #                     sylk_json.path, 'services', 'protos', f), ''.join(file_content), True)


def parse_proto_type_to_py(
    type,
    label,
    messageType=None,
    enumType=None,
    current_pkg=None,
    key_type=None,
    value_type=None,
):
    temp_type = "None"
    if "int" in type:
        temp_type = "int"
    elif type == "float" or type == "double":
        temp_type = "float"
    elif type == "string":
        temp_type = "str"
    elif type == "byte":
        temp_type = "bytes"
    elif type == "message":
        # pretty.print_info(current_pkg)
        if messageType.split(".")[1] != current_pkg:
            if messageType.split(".")[1] == "protobuf":
                package_temp_name = messageType.split(".")[-1].lower()
                msg_temp_name = messageType.split(".")[-1]
                if messageType.split(".")[-1].lower() == "value":
                    package_temp_name = "struct"
                temp_type = "google_dot_protobuf_dot_{0}__pb2.{1}".format(
                    package_temp_name, msg_temp_name
                )
            else:
                temp_type = "{0}__pb2.{1}".format(
                    messageType.split(".")[1], messageType.split(".")[-1]
                )
        else:
            temp_type = "{1}".format(
                messageType.split(".")[1], messageType.split(".")[-1]
            )
    elif type == "enum":
        if enumType.split(".")[1] != current_pkg:
            temp_type = "{0}__pb2.{1}".format(
                enumType.split(".")[1], enumType.split(".")[-1]
            )
        else:
            temp_type = "{1}".format(enumType.split(".")[1], enumType.split(".")[-1])
        temp_type = "int"
    elif type == "bool":
        temp_type = "bool"
    elif type == "map":
        temp_type = f"Dict[{parse_proto_type_to_py(key_type,label,messageType,enumType,current_pkg)},{parse_proto_type_to_py(value_type,label,messageType,enumType,current_pkg)}]"

    if label == "repeated":
        temp_type = f"List[{temp_type}]"

    return temp_type


bash_init_script = '#!/bin/bash\n\n\
declare -a services=("protos")\n\
echo "[sylk.build] init.sh starting protoc compiler"\n\
DESTDIR="./protos"\n\
for SERVICE in "${services[@]}"; do\n\
    python3 -m grpc_tools.protoc --proto_path=$SERVICE/ --python_out=$DESTDIR --grpc_python_out=$DESTDIR $SERVICE/*.proto\n\
done\n\
statuscode=$?\n\
echo "Exit code for protoc -> "$statuscode\n\
[[ "$statuscode" != "0" ]] && { echo "Some error occured during init script"; exit 1; }\n\
exit 0'

def bash_run_server_script(code_base_path: str,root):
    pythonpath = f'./{file_system.join_path(code_base_path,"services")}:./:./{file_system.join_path(code_base_path,"services",root)}'
    return f'#!/bin/bash\n\n\
if [[ $1 == "debug" ]]\n\
then\n\
\techo "Debug Mode: $1"\n\
\tGRPC_VERBOSITY=DEBUG GRPC_TRACE=all PYTHONPATH={pythonpath} python3 {file_system.join_path(code_base_path,"server","server.py")}\n\
elif [[ $1 == "info" ]]\n\
then\n\
\techo "Info Mode: $1"\n\
\tGRPC_VERBOSITY=INFO GRPC_TRACE=all PYTHONPATH={pythonpath} python3 {file_system.join_path(code_base_path, "server", "server.py")}\n\
else\n\
\tPYTHONPATH={pythonpath} python3 {file_system.join_path(code_base_path, "server", "server.py")}\n\
fi'
