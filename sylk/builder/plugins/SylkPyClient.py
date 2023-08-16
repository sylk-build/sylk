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

import logging
import subprocess
import sylk.builder as builder
from sylk.commons import helpers, file_system, resources, pretty
from sylk.builder.plugins.static import gitignore_py
import inspect


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
                        sylk_json.path, sylk_json.code_base_path, "clients", "python", "/".join(temp_path)
                    )
                )
                == False
            ):
                file_system.mkdir(
                    file_system.join_path(
                        sylk_json.path, sylk_json.code_base_path, "clients", "python", "/".join(temp_path)
                    )
                )
            if (
                file_system.check_if_file_exists(
                    file_system.join_path(
                        sylk_json.path,
                        sylk_json.code_base_path,
                        "clients",
                        "python",
                        "/".join(temp_path),
                        "__init__.py",
                    )
                )
                == False
            ):
                file_system.wFile(
                    file_system.join_path(
                        sylk_json.path,
                        sylk_json.code_base_path,
                        "clients",
                        "python",
                        "/".join(temp_path),
                        "__init__.py",
                    ),
                    "",
                )
        # name = pkg.split('/')[-1].split('.')[0]
        # pkg_path = '/'.join(pkg.split('/')[:-1])
        # if file_system.check_if_file_exists(file_system.join_path(sylk_json.path, 'services', pkg_path,f'{name}_pb2.py')) == False:
        #     try:
        #         file_system.copyFile(file_system.join_path(sylk_json.path, 'clients','python', pkg_path,f'{name}_pb2.py'),file_system.join_path(sylk_json.path, 'services', '/'.join(temp_path),f'{name}_pb2.py'))
        #     except Exception as e:
        #         pass
        # print(file_system.join_path(sylk_json.path, 'services', '/'.join(temp_path),'__init__.py'))
        # file_system.mv(file_system.join_path(sylk_json.path, pkg_path, file),
        #             file_system.join_path(sylk_json.path, 'services',  target_file, file))

    # for svc in sylk_json.services:
    #     # svc_path = '/'.join(svc.split('/')[:-1])
    #     target_file = "/".join(svc.split("/")[:-1])
    #     temp_path = []
    #     for d in target_file.split("/"):
    #         temp_path.append(d)
    #         if (
    #             file_system.check_if_dir_exists(
    #                 file_system.join_path(
    #                     sylk_json.path, "clients", "python", "/".join(temp_path)
    #                 )
    #             )
    #             == False
    #         ):
    #             file_system.mkdir(
    #                 file_system.join_path(
    #                     sylk_json.path, "clients", "python", "/".join(temp_path)
    #                 )
    #             )
    #         if (
    #             file_system.check_if_file_exists(
    #                 file_system.join_path(
    #                     sylk_json.path,
    #                     "clients",
    #                     "python",
    #                     "/".join(temp_path),
    #                     "__init__.py",
    #                 )
    #             )
    #             == False
    #         ):
    #             file_system.wFile(
    #                 file_system.join_path(
    #                     sylk_json.path,
    #                     "clients",
    #                     "python",
    #                     "/".join(temp_path),
    #                     "__init__.py",
    #                 ),
    #                 "",
    #             )
        # name = svc.split('/')[-1].split('.')[0]
        # svc_path = '/'.join(svc.split('/')[:-1])
        # if file_system.check_if_file_exists(file_system.join_path(sylk_json.path, 'services', svc_path,f'{name}_pb2.py')) == False:
        #     try:
        #         file_system.copyFile(file_system.join_path(sylk_json.path, 'clients','python', svc_path,f'{name}_pb2.py'),file_system.join_path(sylk_json.path, 'services', '/'.join(temp_path),f'{name}_pb2.py'))
        #     except Exception as e:
        #         pass
        # print(file_system.join_path(sylk_json.path, 'services', '/'.join(temp_path),'__init__.py'))
        # file_system.mv(file_system.join_path(sylk_json.path, svc_path, file),
        #             file_system.join_path(sylk_json.path, 'services',  target_file, file))

    return (__name__, "OK")


@builder.hookimpl
def init_project_structure(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext, pre_data
):
    directories = [
        # Clients
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "python"),
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "python", sylk_json._root_protos),
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
        if sylk_json.project.get("server").get("language") != "python":
            file_system.wFile(
                file_system.join_path(sylk_json.path, "bin", "init-py.sh"), bash_init_script
            )

        # .gitignore
        file_system.wFile(file_system.join_path(sylk_json.path, ".gitignore"), gitignore_py)
        for file in files:
            file_system.wFile(file, "")

    return [directories, files]


@builder.hookimpl
def pre_compile_protos(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    pretty.print_info("Running pre compile protos - python client")
    file_system.removeDir(file_system.join_path(sylk_json.path, sylk_json.code_base_path, 'clients', 'python', sylk_json._root_protos, sylk_json.domain))
    protos_out = file_system.join_path(sylk_json.code_base_path,'clients','python', sylk_json._root_protos)
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
def write_clients(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext, pre_data
):
    imports = []
    exports = []
    override_stubs = {}
    before_init = ""
    interceptors = []
    client_options = [
        ("grpc.keepalive_permit_without_calls", 1),
        ("grpc.keepalive_time_ms", 120000),
        ("grpc.keepalive_timeout_ms", 20000),
        ("grpc.http2.min_time_between_pings_ms", 120000),
        ("grpc.http2.max_pings_without_data", 1),
    ]
    """Parse pre data"""
    if pre_data:
        _hook_name = inspect.stack()[0][3]
        for mini_hooks in pre_data:
            for hook in mini_hooks:
                if __name__ == hook.split(":")[0]:
                    if hook.split(":")[2] is not None and _hook_name == hook.split(":")[
                        1
                    ].replace("()", ""):
                        # Append to exports
                        if "append_imports" in hook.split(":")[2]:
                            if mini_hooks[hook] is not None:
                                for imp in mini_hooks[hook]:
                                    imports.append(imp)

                        elif "append_client_options" in hook.split(":")[2]:
                            if mini_hooks[hook] is not None:
                                for k, v in mini_hooks[hook]:
                                    old_value = next(
                                        (i for i in client_options if i[0] == k),
                                        (None, None),
                                    )[1]
                                    if k not in list(
                                        map(lambda x: x[0], client_options)
                                    ):
                                        client_options.append((k, v))
                                    elif v != old_value:
                                        client_options.remove((k, old_value))
                                        client_options.append((k, v))

    for f in file_system.walkFiles(
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "services", sylk_json._root_protos)
    ):
        if ".py" in f:
            file = file_system.rFile(
                file_system.join_path(sylk_json.path, sylk_json.code_base_path, "services", sylk_json._root_protos, f)
            )
            if "_grpc" not in f:
                index = 13
            else:
                index = 0
            for l in file[index:]:
                if (
                    "import " in l
                    and "grpc" not in l
                    and "typing" not in l
                    and "google.protobuf" not in l
                ):
                    file[index] = l.replace("import ", "from . import ")

                index += 1
            file_system.wFile(
                file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "python", f),
                "".join(file),
                True,
            )

    client = helpers.SylkClientPy(
        sylk_json.project.get("packageName"),
        sylk_json.services,
        sylk_json.packages,
        sylk_context,
        pre_data={"imports": imports, "client_options": client_options},
        sylk_json=sylk_json
    )
    file_system.wFile(
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "python", "__init__.py"),
        client.__str__(),
        overwrite=True,
    )


@builder.hookimpl
def override_generated_classes(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext
):
    if sylk_json.project.get("server").get("language") != "python":
        for f in file_system.walkFiles(
            file_system.join_path(sylk_json.path, sylk_json.code_base_path, "services", sylk_json._root_protos)
        ):
            name = f.split("_pb2")
            if "_grpc" not in name:
                file_content = file_system.rFile(
                    file_system.join_path(sylk_json.path, sylk_json.code_base_path, "services", sylk_json._root_protos, f)
                )
                file_content.insert(
                    5, "\nfrom typing import overload, Iterator, List, Dict\n"
                )
                if len(name) > 1:
                    name = name[0]

                    # svc_proto = next((svc for svc in sylk_json.services if svc == name),None)
                    pkg_proto = next(
                        (
                            pkg
                            for pkg in sylk_json.packages
                            if pkg.split("/")[-1].split(".")[0] == name
                        ),
                        None,
                    )
                    if pkg_proto is not None:
                        pkg_proto_name = pkg_proto.split("/")[-1].split(".")[0]

                        for m in sylk_json.packages[pkg_proto].get("messages"):
                            index = 0
                            for l in file_content:
                                message_name = m["name"]
                                message_description = (
                                    m.get("description")
                                    if m.get("description") is not None
                                    else ""
                                )
                                if (
                                    f"{message_name} = _reflection"
                                    in l[: len(message_name) + 15]
                                ):
                                    temp_fields = []
                                    init_fields = []
                                    docstring_fields = []
                                    # pretty.print_info(init_fields)
                                    for field in m["fields"]:
                                        fName = field["name"]
                                        fDescription = (
                                            field.get("description")
                                            if field.get("description") is not None
                                            else ""
                                        )
                                        key_type = (
                                            field.get("keyType").split("_")[-1].lower()
                                            if field.get("keyType") is not None
                                            and field.get("keyType") != -1
                                            else None
                                        )
                                        value_type = (
                                            field.get("valueType")
                                            .split("_")[-1]
                                            .lower()
                                            if field.get("valueType") is not None
                                            and field.get("valueType") != -1
                                            else None
                                        )
                                        fType = parse_proto_type_to_py(
                                            field["fieldType"].split("_")[-1].lower(),
                                            field["label"].split("_")[-1].lower(),
                                            field.get("messageType"),
                                            field.get("enumType"),
                                            current_pkg=pkg_proto_name,
                                            key_type=key_type,
                                            value_type=value_type,
                                        )
                                        if (
                                            field["fieldType"].split("_")[-1].lower()
                                            == "enum"
                                        ):
                                            temp_fields.append(
                                                f"{fName} = {fType} # type: int"
                                            )
                                        elif (
                                            field["fieldType"].split("_")[-1].lower()
                                            == "oneof"
                                        ):
                                            for f_oneof in field.get("oneofFields"):
                                                fOneofName = f_oneof["name"]
                                                fOneofType = parse_proto_type_to_py(
                                                    f_oneof["fieldType"]
                                                    .split("_")[-1]
                                                    .lower(),
                                                    "optional",
                                                    f_oneof.get("messageType"),
                                                    f_oneof.get("enumType"),
                                                    current_pkg=pkg_proto_name,
                                                )
                                                if (
                                                    f_oneof["fieldType"]
                                                    .split("_")[-1]
                                                    .lower()
                                                    == "enum"
                                                ):
                                                    temp_fields.append(
                                                        f"{fOneofName} = {fOneofType} # type: int"
                                                    )
                                                else:
                                                    temp_fields.append(
                                                        f"{fOneofName} = {fOneofType} # type: {fOneofType}"
                                                    )
                                        else:
                                            temp_fields.append(
                                                f"{fName} = {fType} # type: {fType}"
                                            )

                                        if field.get("fieldType") != "TYPE_ONEOF":
                                            init_fields.append(f"{fName}={fType}")
                                        else:
                                            for f_oneof in field.get("oneofFields"):
                                                fOneofName = f_oneof["name"]
                                                fOneofType = parse_proto_type_to_py(
                                                    f_oneof["fieldType"]
                                                    .split("_")[-1]
                                                    .lower(),
                                                    "optional",
                                                    f_oneof.get("messageType"),
                                                    f_oneof.get("enumType"),
                                                    current_pkg=pkg_proto_name,
                                                )
                                                init_fields.append(
                                                    f"{fOneofName}={fOneofType}"
                                                )
                                        docstring_fields.append(
                                            f"{fName} : {fType}\n\t\t\t{fDescription}"
                                        )

                                    temp_fields = "\n\t".join(temp_fields)
                                    init_fields = ", ".join(init_fields)
                                    docstring = "{0}\n\n\t\tAttributes:\n\t\t----------\n\t\t{1}".format(
                                        message_description,
                                        "\n\t\t".join(docstring_fields),
                                    )

                                    file_content.insert(
                                        index,
                                        f'\n@overload\nclass {message_name}(_message.Message):\n\t"""sylk.build generated message [{sylk_json.domain}.{pkg_proto_name}.v1.{message_name}]\n\tA class respresent a {message_name} type\n\t{message_description}\n\t\t"""\n\t{temp_fields}\n\n\tdef __init__(self, {init_fields}):\n\t\t"""\n\t\t{docstring}\n\t\t"""\n\t\tpass\n',
                                    )
                                    break
                                index += 1
                        file_system.wFile(
                            file_system.join_path(
                                sylk_json.path, sylk_json.code_base_path, "services", sylk_json._root_protos, f
                            ),
                            "".join(file_content),
                            True,
                        )


bash_init_script = '#!/bin/bash\n\n\
declare -a services=("protos")\n\
echo "[sylk.build] init-py.sh starting protoc compiler"\n\
DESTDIR="./protos"\n\
for SERVICE in "${services[@]}"; do\n\
    python3 -m grpc_tools.protoc --proto_path=$SERVICE/ --python_out=$DESTDIR --grpc_python_out=$DESTDIR $SERVICE/*.proto\n\
done\n\
statuscode=$?\n\
echo "Exit code for python protoc -> "$statuscode\n\
exit 0'


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
