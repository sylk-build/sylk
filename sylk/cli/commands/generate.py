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
from pprint import pprint
from sylk.cli.prompter import QCheckbox, QConfirm, QList, QText, ask_user_question
from sylk.architect import SylkArchitect
from sylk.cli.theme import SylkTheme
from sylk.commons.helpers import SylkJson, SylkField, SylkEnumValue, _WellKnowns,_WellMap, parse_version_component
from sylk.commons.pretty import (
    print_info,
    print_warning,
    print_error,
    print_note,
    print_success,
    bcolors,
)
from sylk.commons.protos.sylk.SylkField.v1.SylkField_pb2 import (
    SylkFieldLabels,
    SylkFieldTypes,
)
from sylk.commons.errors import SylkProtoError
from sylk.commons.protos.sylk.SylkCommons.v1.SylkCommons_pb2 import (
    FieldOptions,
    MessageOptions,
    MethodOptions,
    ServiceOptions,
    SylkExtensions,
)

import inquirer
from inquirer import errors
import re

from sylk.commons.sylk import SylkTree

fields_opt = [
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_DOUBLE),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_FLOAT),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_INT64),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_UINT64),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_INT32),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_UINT32),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_BOOL),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_STRING),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_MESSAGE),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_BYTES),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_ENUM),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_ONEOF),
    SylkFieldTypes.Name(SylkFieldTypes.TYPE_MAP),
]
field_label = [
    SylkFieldLabels.Name(SylkFieldLabels.LABEL_OPTIONAL),
    SylkFieldLabels.Name(SylkFieldLabels.LABEL_REPEATED),
]

well_known_type = _WellKnowns


def package(
    results,
    sylk_json: SylkJson,
    architect: SylkArchitect,
    expand=False,
    verbose=False,
    deps=[]
):
    pkg = results["package"].replace('/','.')
    pkg_name = ""
    ver = parse_version_component(pkg)
    if ver:
        pkg_name = pkg.split('.')[-2]
    else:
        print_warning('creating package without a version component is risky for backward and forward compatibility\nmake sure you know what your doing: https://docs.sylk.build/proto/packages#unversioned-packages')
        pkg_name = pkg.split('.')[-1]
    if pkg_name.lower() == "package":
        print_error(
            "Do not name your package as 'package' it can cause issues down the road\n\t-> please choose another name for your package"
        )
        exit(1)
    list_depend = well_known_type
    prj_name = sylk_json.project.get("name")
    description = None
    if sylk_json.packages is not None:
        try:
            if sylk_json.domain == pkg:
                pkg_name = sylk_json.domain
            else:
                pkg_name = sylk_json.domain+'.'+pkg
            if sylk_json.get_package(pkg_name):
                print_error(
                    f'Package [{pkg}] is already defined under "{prj_name}" project'
                )
                exit(1)
        except Exception:
            pass
            # logging.debug("Package not found continuing...")
        for p in sylk_json.packages:
            if sylk_json.packages[p]["package"] not in deps:
                list_depend.append(sylk_json.packages[p]["package"])
    temp_d_list = []
    if expand:
        description = ask_user_question(
            questions=[QText(name="description", message="Enter package description")]
        )

        if description is not None:
            description = description.get("description")
        else:
            description = ''
            print_warning('canceling description for package')

        dependencies = ask_user_question(
            questions=[
                QCheckbox(
                    name="dependencies",
                    message="Choose package dependencies (Use arrows keys to enable disable a language)",
                    choices=list_depend,
                )
            ]
        )
        if dependencies:
            temp_d_list = dependencies["dependencies"]
            list_depend.extend(deps)
        else:
            print_warning('canceling dependencies attachment to package')
            

    if verbose:
        print_note(pkg, True, "Adding package")
    sylk_json._proto_tree.add_node(sylk_json.domain+'.'+pkg_name,'package')
    new_pkg = sylk_json._proto_tree._find_node(pkg,sylk_json._proto_tree.root)
    if len(deps) > 0:
        for d in deps:
            temp_d_list.append(d)
            new_pkg.references.append(d)
    pkgs = sylk_json._proto_tree.topological_sort()[::-1]
    if pkg_name not in pkgs:
        pkgs.append(pkg_name)
    architect.AddPackage(pkg, temp_d_list, description=description, version_component=ver, order_pkg=pkgs)
    architect.Save()
    print_success(f'Success !\n\t- Created new package "{pkg_name}"')


def service(
    results,
    sylk_json: SylkJson,
    architect: SylkArchitect,
    expand=False,
    verbose=False,
    deps=[],
    tag=None,
):
    svc = results["service"]
    svc = results["service"].replace('/','.')
    svc_name = ""
    parent=results.get('package') if results.get('package') is not None else sylk_json.domain+'.'+'.'.join(svc.split('.')[:-1])
    ver = parse_version_component(svc)
    svc_name = svc.split('.')[-1]
    description=None
    if svc_name.lower() == "service":
        print_error(
            "Do not set service name as 'service' it can cause issues down the road\n\t-> Please choose another name for your service"
        )
        exit(1)
    list_depend = []
    if expand:
        if sylk_json.packages is not None:
            for p in sylk_json.packages:
                if sylk_json.packages[p]["name"].lower() == svc_name:
                    print_error(
                        f"Cannot create service {svc}, package by the same name is already exists !"
                    )
                    exit(1)
                if sylk_json.packages[p]["package"] not in deps:
                    list_depend.append(
                        (sylk_json.packages[p]["package"], sylk_json.packages[p]["package"])
                    )
            description = ask_user_question(
                questions=[QText(name="description", message="Enter service description")]
            )
            if description is not None:
                description = description.get("description")
            else:
                description = ''
                print_warning('canceling description for package')
            depend = ask_user_question(
                questions=[
                    QCheckbox(
                        name="dependencies",
                        message="Choose service dependencies (Use arrows keys to enable disable a language)",
                        choices=list_depend,
                    )
                ]
            )
            if depend is not None:
                list_depend = depend["dependencies"]
            else:
                print_warning('canceling dependencies attachment to package')
            list_depend.extend(deps)

    if sylk_json.services is not None:
        service = sylk_json.get_service(svc_name, sylk_json.domain +'.'+ parent)
        if service is not None:
            print_error(
                f"Service '{svc}' already exists under '{sylk_json.project.get('name')}'\n\t- Create the service under new package version"
            )
            exit(1)

    if verbose:
        print_note(svc, True, "Added Service")
    package = sylk_json.get_package(parent, False)
    if len(deps) > 0:
        for d in deps:
            if d not in package.dependencies:
                package.dependencies.append(d)
            else:
                print_warning('skipping attaching \'{}\' as it is already attached to package dependencies'.format(d))
    pkgs = sylk_json._proto_tree.topological_sort()[::-1]
    if package.package not in pkgs:
        pkgs.append(package.package)
    architect.AddService(svc_name, list_depend, description=description, methods=[], package=package,tag=tag,order_pkg=pkgs)
    architect.Save()

    print_success(f'Success !\n\t- Created new service : "{svc}"')


def message(
    results,
    sylk_json: SylkJson,
    architect: SylkArchitect,
    expand=False,
    verbose=False,
    parent: str = None,
    deps = [],
    tag = None
):
    msg = results["message"].replace('/','.')
    msg_name = msg.split('.')[-1]
    description=None
    
    if '.'.join(msg.split('.')[:-1]) == sylk_json.domain:
        pkg_name = sylk_json.domain
    else:
        pkg_name = sylk_json.domain+'.'+'.'.join(msg.split('.')[:-1])
    pkg=results.get('package') if results.get('package') is not None else pkg_name
    if msg_name.lower() == "message":
        print_error(
            "Do not name your message as 'message' it can cause issues down the road\n\t-> please choose another name for your message"
        )
        exit(1)
    msg_full_name = "{0}.{1}".format(pkg, msg_name)
    description = ""
    add_field = True
    temp_fields = []
    msg_fields = []
    pkg = sylk_json.get_package(
        pkg, False
    )
    avail_msgs = []
    avail_field_ext = []
    avail_msg_ext = []
    sylk_json._proto_tree.add_node(msg_full_name,'message')

    for msg in pkg.messages:
        if msg.extension_type == 0:
            if msg.description is not None and msg.full_name != msg_full_name:
                desc = f" - " + bcolors.OKBLUE + msg.description + bcolors.ENDC
            else:
                desc = ""
            avail_msgs.append((f"{msg.name}{desc}", msg.full_name))
        else:
            if SylkExtensions.Name(msg.extension_type) == "FieldOptions":
                for f in msg.fields:
                    avail_field_ext.append((f"FieldOptions | {f.name}", f.full_name))
            elif SylkExtensions.Name(msg.extension_type) == "MessageOptions":
                for f in msg.fields:
                    avail_msg_ext.append((f"MessageOptions | {f.name}", f.full_name))

    avail_enums = []
    for enum in pkg.enums:
        avail_enums.append((enum.name, enum.full_name))
    
    dependencies = pkg.dependencies
    for d in deps:
        if d not in dependencies:
            dependencies.append(d)
    for d in dependencies:
        if "google.protobuf" in d:
            for _,msgs in _WellMap:
                for m in msgs:
                    avail_msgs.append(
                            (
                                "{} [{}]".format(m,d+'.'+m),
                                "{0}.{1}".format(d, m),
                            )
                        )
        else:
            d_package = sylk_json.get_package(
                d,False
            )
            if d_package is not None:
                for msg in d_package.messages:
                    if msg.description is not None:
                        desc = " - " + bcolors.OKBLUE + msg.description + bcolors.ENDC
                    else:
                        desc = ""
                    avail_msgs.append(
                        (f"{msg.name} [{msg.full_name}]" + desc, msg.full_name)
                    )
                for enm in d_package.enums:
                    if enm.description is not None:
                        desc = " - " + bcolors.OKBLUE + enm.description + bcolors.ENDC
                    else:
                        desc = ""
                    avail_enums.append(
                        (f"{enm.name} [{enm.full_name}]" + desc, enm.full_name)
                    )

            for m in d_package.messages:
                if m.extension_type is not None:
                    if SylkExtensions.Name(msg.extension_type) == "FieldOptions":
                        for f in msg.fields:
                            avail_field_ext.append(
                                (f"FieldOptions | {f.name}", f.full_name)
                            )
                    elif SylkExtensions.Name(msg.extension_type) == "MessageOptions":
                        for f in msg.fields:
                            avail_msg_ext.append(
                                (f"MessageOptions | {f.name}", f.full_name)
                            )
    extend = None
    if expand:
        extend = ask_user_question(
            questions=[
                QConfirm(name="extend", message="Do you want to extend a message?")
            ]
        )

        if extend.get("extend"):
            avail_options = [
                SylkExtensions.Name(SylkExtensions.FieldOptions),
                SylkExtensions.Name(SylkExtensions.MessageOptions),
                SylkExtensions.Name(SylkExtensions.FileOptions),
                SylkExtensions.Name(SylkExtensions.ServiceOptions),
                SylkExtensions.Name(SylkExtensions.MethodOptions),
            ]
            extend = ask_user_question(
                questions=[
                    QList(
                        name="extend",
                        message="Choose message extension",
                        choices=avail_options,
                    )
                ]
            )
            extend = SylkExtensions.Value(extend["extend"])
        else:
            extend = None
            # add_extension = inquirer.prompt([inquirer.List('add_message_extension','Do you want to add message level extension?')],theme=SylkTheme())

        description = inquirer.prompt(
            [inquirer.Text("description", "Enter message description", "")],
            theme=SylkTheme(),
        )
        if description is not None:
            description = description["description"]

    while add_field == True:
        opt = []
        for f in fields_opt:
            opt.append((f.split("_")[1].lower(), f))
        labels = []
        for l in field_label:
            labels.append((l.split("_")[1].lower(), l))

        field = inquirer.prompt(
            [
                inquirer.Text("field", "Enter field name", validate=validation),
                inquirer.List("fieldType", "Choose field type", choices=opt),
            ],
            theme=SylkTheme(),
        )
        label = None
        if field is not None:
            if (
                field.get("fieldType") != "TYPE_MAP"
                and field.get("fieldType") != "TYPE_ONEOF"
            ):
                label = inquirer.prompt(
                    [inquirer.List("fieldLabel", "Choose field label", choices=labels)],
                    theme=SylkTheme(),
                )

        message_type = None
        enum_type = None

        if field["fieldType"] == SylkFieldTypes.Name(SylkFieldTypes.TYPE_MESSAGE):
            if len(avail_msgs) == 0:
                print_warning("No messages availabe for field")
                exit(1)
            else:
                message = inquirer.prompt(
                    [
                        inquirer.List(
                            "message", "Choose available messages", choices=avail_msgs
                        )
                    ],
                    theme=SylkTheme(),
                )
                message_type = message["message"]
                sylk_json._proto_tree.add_field_reference(msg_full_name,field["field"],message_type)

        elif field["fieldType"] == SylkFieldTypes.Name(SylkFieldTypes.TYPE_ENUM):
            if len(avail_enums) == 0:
                print_warning("No enums available for field")
                exit(1)
            else:
                message = inquirer.prompt(
                    [
                        inquirer.List(
                            "enum", "Choose available enums", choices=avail_enums
                        )
                    ],
                    theme=SylkTheme(),
                )
                enum_type = message["enum"]
                sylk_json._proto_tree.add_field_reference(msg_full_name,field["field"],enum_type)

        if field is None:
            add_field = False
        else:
            new_field = field["field"]
            field_exists_validation(new_field, temp_fields, msg_full_name)
            sylk_json._proto_tree.add_node(msg_full_name+'.'+new_field,'field')
            f_ext = None
            if expand:
                if len(avail_field_ext) > 0 and extend == None:
                    extend_field = inquirer.prompt(
                        [
                            inquirer.Confirm(
                                "extend", message="Do you want to add field extension?"
                            )
                        ],
                        theme=SylkTheme(),
                    )
                    if extend_field.get("extend"):
                        f_ext = inquirer.prompt(
                            [
                                inquirer.List(
                                    "extensions",
                                    "Choose extension",
                                    choices=avail_field_ext,
                                )
                            ],
                            theme=SylkTheme(),
                        )
                        temp_pkg = sylk_json.get_package(
                            f_ext["extensions"].split(".")[1], False
                        )
                        temp_msg = next(
                            (
                                m
                                for m in temp_pkg.messages
                                if m.name == f_ext["extensions"].split(".")[3]
                            ),
                            None,
                        )
                        temp_field = next(
                            (
                                f
                                for f in temp_msg.fields
                                if f.name == f_ext["extensions"].split(".")[-1]
                            ),
                            None,
                        )
                        if SylkFieldTypes.Name(temp_field.field_type) == "TYPE_BOOL":
                            f_ext_v = inquirer.prompt(
                                [
                                    inquirer.Confirm(
                                        "ext_value",
                                        "Enter extension bool value",
                                        default=False,
                                    )
                                ],
                                theme=SylkTheme(),
                            )
                        elif (
                            SylkFieldTypes.Name(temp_field.field_type) == "TYPE_DOUBLE"
                            or SylkFieldTypes.Name(temp_field.field_type)
                            == "TYPE_FLOAT"
                        ):
                            f_ext_v = inquirer.prompt(
                                [
                                    inquirer.Text(
                                        "ext_value",
                                        "Enter extension float value",
                                        validate=float_value_validate,
                                    )
                                ],
                                theme=SylkTheme(),
                            )
                            try:
                                f_ext_v = float(f_ext_v["ext_value"])
                            except Exception as e:
                                logging.exception(e)
                                exit(1)
                        elif (
                            SylkFieldTypes.Name(temp_field.field_type) == "TYPE_INT32"
                            or SylkFieldTypes.Name(temp_field.field_type)
                            == "TYPE_INT64"
                        ):
                            f_ext_v = inquirer.prompt(
                                [
                                    inquirer.Text(
                                        "ext_value",
                                        "Enter extension integer value",
                                        validate=int_value_validate,
                                    )
                                ],
                                theme=SylkTheme(),
                            )
                            try:
                                f_ext_v = int(f_ext_v["ext_value"])
                            except Exception as e:
                                logging.exception(e)
                                exit(1)
                        elif (
                            SylkFieldTypes.Name(temp_field.field_type) == "TYPE_STRING"
                        ):
                            f_ext_v = inquirer.prompt(
                                [
                                    inquirer.Text(
                                        "ext_value", "Enter extension string value"
                                    )
                                ],
                                theme=SylkTheme(),
                            )
                        temp_ext_name = f_ext["extensions"].split(".")
                        if ".".join(temp_ext_name[:-2]) == pkg.name:
                            f_ext = {".".join(temp_ext_name[-2:]): f_ext_v}
                        else:
                            f_ext = {f_ext["extensions"]: f_ext_v}

                f_description = inquirer.prompt(
                    [inquirer.Text("description", "Enter field description", "")],
                    theme=SylkTheme(),
                )
                if f_description is not None:
                    f_description = f_description["description"]
            else:
                f_description = ""

            temp_fields.append(new_field)
            map_types = None
            oneof_fields = []
            if field["fieldType"] == "TYPE_MAP":
                map_types = inquirer.prompt(
                    [
                        inquirer.List(
                            "keyType",
                            "[MAP] Choose key type",
                            choices=[
                                o
                                for o in opt
                                if o[1] != "TYPE_BOOL"
                                and o[1] != "TYPE_FLOAT"
                                and o[1] != "TYPE_DOUBLE"
                                and o[1] != "TYPE_ENUM"
                                and o[1] != "TYPE_MESSAGE"
                                and o[1] != "TYPE_MAP"
                                and o[1] != "TYPE_ONEOF"
                                and o[1] != "TYPE_BYTES"
                            ],
                        ),
                        inquirer.List(
                            "valueType",
                            "[MAP] Choose value type",
                            choices=[
                                o
                                for o in opt
                                if o[1] != "TYPE_MAP" and o[1] != "TYPE_ONEOF"
                            ],
                        ),
                    ],
                    theme=SylkTheme(),
                )

                if (
                    map_types.get("valueType") == "TYPE_MESSAGE"
                    or map_types.get("valueType") == "TYPE_ENUM"
                ):
                    if map_types.get("valueType") == "TYPE_MESSAGE":
                        if len(avail_msgs) == 0:
                            print_warning("[MAP] No messages availabe for field")
                            exit(1)
                        else:
                            message = inquirer.prompt(
                                [
                                    inquirer.List(
                                        "message",
                                        "[MAP] Choose available messages",
                                        choices=avail_msgs,
                                    )
                                ],
                                theme=SylkTheme(),
                            )
                            message_type = message["message"]
                            sylk_json._proto_tree.add_field_reference(msg_full_name,new_field,message_type)

                    elif map_types.get("valueType") == "TYPE_ENUM":
                        if len(avail_enums) == 0:
                            print_warning("[MAP] No enums available for field")
                            exit(1)
                        else:
                            message = inquirer.prompt(
                                [
                                    inquirer.List(
                                        "enum",
                                        "[MAP] Choose available enums",
                                        choices=avail_enums,
                                    )
                                ],
                                theme=SylkTheme(),
                            )
                            enum_type = message["enum"]
                            sylk_json._proto_tree.add_field_reference(msg_full_name,new_field,enum_type)

            elif field["fieldType"] == "TYPE_ONEOF":
                temp_fields_oneof = []
                add_field_oneof = True
                oneof_fields = add_fields_oneof(
                    add_field_oneof,
                    avail_msgs=avail_msgs,
                    avail_enums=avail_enums,
                    pre_fields=temp_fields_oneof,
                    msg_full_name=msg_full_name,
                    parent_field=new_field,
                    tree=sylk_json._proto_tree
                )


            msg_fields.append(
                SylkField(
                    new_field,
                    field["fieldType"],
                    label["fieldLabel"] if label is not None else "LABEL_OPTIONAL",
                    message_type=message_type,
                    enum_type=enum_type,
                    description=f_description,
                    extensions=f_ext,
                    key_type=map_types.get("keyType")
                    if map_types is not None
                    else None,
                    value_type=map_types.get("valueType")
                    if map_types is not None
                    else None,
                    oneof_fields=oneof_fields,
                ).to_dict()
            )

            nextfield = inquirer.prompt(
                [
                    inquirer.Confirm(
                        "continue", message="Add more fields?", default=True
                    )
                ],
                theme=SylkTheme(),
            )
            if nextfield is None:
                add_field = False
            else:
                if nextfield["continue"] == False:
                    add_field = False

        if verbose:
            print_note(field, True, "Added field")
    if next((m for m in pkg.messages if m.name == msg_name), None) is None:
        if verbose:
            print_note(msg_name, True, "Added Message")
        
        # msg_node = sylk_json._proto_tree.get_references(pkg.package + '.' msg_name)
        pkgs = sylk_json._proto_tree.topological_sort()[::-1]
        if pkg.package not in pkgs:
            pkgs.append(pkg.package)
        architect.AddMessage(
            pkg,
            msg_name,
            msg_fields,
            description,
            extend,
            tag=tag,
            order_pkg=pkgs
        )
        architect.Save()
        print_success(f"Created Message !\n\t- {msg_name}\n")
    else:
        print_error(f'Message "{msg_name}" already exists under "{pkg.package}"')


def add_fields_oneof(
    add_field: bool, avail_msgs, avail_enums, pre_fields, msg_full_name, parent_field, tree: SylkTree
):
    final_fields = pre_fields
    while add_field:
        opt = []
        for f in fields_opt:
            opt.append((f.split("_")[1].lower(), f))
        labels = []
        for l in field_label:
            labels.append((l.split("_")[1].lower(), l))

        field = inquirer.prompt(
            [
                inquirer.Text("field", "[ONEOF] Enter field name", validate=validation),
                inquirer.List(
                    "fieldType",
                    "[ONEOF] Choose field type",
                    choices=[o for o in opt if o != "TYPE_MAP" and o != "TYPE_ONEOF"],
                ),
            ],
            theme=SylkTheme(),
        )

        label = None
        message_type = None
        enum_type = None
        tree.add_node(msg_full_name+'.'+parent_field+'.'+field['field'],'field')
        if field["fieldType"] == SylkFieldTypes.Name(SylkFieldTypes.TYPE_MESSAGE):
            if len(avail_msgs) == 0:
                print_warning("[ONEOF] No messages availabe for field")
                exit(1)
            else:
                message = inquirer.prompt(
                    [
                        inquirer.List(
                            "message",
                            "[ONEOF] Choose available messages",
                            choices=avail_msgs,
                        )
                    ],
                    theme=SylkTheme(),
                )
                message_type = message["message"]
                tree.add_field_reference(msg_full_name,field['field'],message_type)

        elif field["fieldType"] == SylkFieldTypes.Name(SylkFieldTypes.TYPE_ENUM):
            if len(avail_enums) == 0:
                print_warning("[ONEOF] No enums available for field")
                exit(1)
            else:
                message = inquirer.prompt(
                    [
                        inquirer.List(
                            "enum",
                            "[ONEOF] Choose available enums",
                            choices=avail_enums,
                        )
                    ],
                    theme=SylkTheme(),
                )
                enum_type = message["enum"]
                tree.add_field_reference(msg_full_name,field['field'],enum_type)
        if field is None:
            add_field = False
        else:
            new_field = field["field"]
            field_exists_validation(
                new_field, final_fields, msg_full_name + "." + new_field
            )

        final_fields.append(
            SylkField(
                new_field,
                field["fieldType"],
                label["fieldLabel"] if label is not None else "LABEL_OPTIONAL",
                message_type=message_type,
                enum_type=enum_type,
                description=None,
                extensions=None,
                key_type=None,
                value_type=None,
                oneof_fields=[],
            ).to_dict()
        )

        nextfield = inquirer.prompt(
            [
                inquirer.Confirm(
                    "continue", message="[ONEOF] Add more fields?", default=True
                )
            ],
            theme=SylkTheme(),
        )
        if nextfield is None:
            add_field = False
        else:
            if nextfield["continue"] == False:
                add_field = False
    return final_fields


def rpc(
    results,
    sylk_json: SylkJson,
    architect: SylkArchitect,
    expand=None,
    parent: str = None,
    deps = [],
):
    rpc = results["rpc"].replace('/','.')
    svc = results.get('service') if results.get('service') is not None else sylk_json.domain+'.'+'.'.join(rpc.split('.')[:-1])
    pkg_path = '.'.join(svc.split('.')[:-1])
    full_name = "{0}.{1}".format(svc, rpc)
    if sylk_json.get_rpc(rpc) is not None:
        print_error(f'RPC [{rpc}] is already defined under "{svc}" service')
        exit(1)
    
    package = sylk_json.get_package(pkg_path,False)
    service = sylk_json.get_service(svc,False)
    dependencies = package.dependencies
    if dependencies is None:
        try:
            sylk_json.get_package(pkg_path)
            dependencies = [svc]
        except Exception:
            svc_name = svc.split(".")[1]
            print_error(
                f"Dependencies not listed under \"{svc}\"\n\tTry to attach a package to service\n\tRun: 'sylk package <some.package.v1> {svc}'"
            )
            print_warning(
                "Try and list all available packages with `$ sylk ls --type package`"
            )
            exit(1)
    
    avail = []
    for d in deps:
        if d not in dependencies:
            dependencies.append(d)
    for d in dependencies:
        if "google.protobuf" in d:
            for _, msgs in _WellMap:
                for m in msgs:
                    wellknown_msg = d+'.'+m
                    avail.append(('{} [{}]'.format(wellknown_msg.split('.')[-1],wellknown_msg),wellknown_msg))
        else:
            pkg = sylk_json.get_package(d)
            msgs = pkg.get("messages")
            if msgs is not None:
                for m in msgs:
                    avail.append(('{} [{}]'.format(m["fullName"].split('.')[-1],m["fullName"]),m["fullName"]))
    
    for m in package.messages:
        avail.append(('{} [{}]'.format(m.full_name.split('.')[-1],m.full_name),m.full_name))

    if len(avail) == 0:
        print_error("Messages not listed under packages")
        exit(1)

    description = None
    if expand:
        description = inquirer.prompt(
            [inquirer.Text("description", "Enter RPC description", "")],
            theme=SylkTheme(),
        )
        if description is not None:
            description = description["description"]

    inputs_outputs = inquirer.prompt(
        [
            inquirer.List("input_type", message="Choose the input type", choices=avail),
            inquirer.List(
                "output_type", message="Choose the output type", choices=avail
            ),
        ],
        theme=SylkTheme(),
    )
    if inputs_outputs is None:
        print_error("IN/OUT Types are required for RPC")
        exit(1)
    pkgs = sylk_json._proto_tree.topological_sort()[::-1]
    if package.package not in pkgs:
        pkgs.append(package.package)
    architect.AddRPC(
        package,
        service,
        svc+'.'+rpc.split('.')[-1],
        pkgs,
        [
            (results["type"][0], inputs_outputs["input_type"]),
            (results["type"][1], inputs_outputs["output_type"]),
        ],
        description,
    )
    architect.Save()
    print_success(f'Success !\n\tCreated new RPC "{rpc}"')
    lang = sylk_json.project.get("server").get("language")
    lang_suffix = (
        "ts" if lang == "typescript" else "py" if lang == "python" else "Unknown"
    )
    path_to_svc = sylk_json.path + "/services/" + svc.split(".")[1] + "." + lang_suffix
    print_warning(
        f'\t- Make sure you are adding the new RPC "{rpc}" method to your service implemantation file at {path_to_svc}'
    )
    print_warning(
        f"\t- For more information on how to edit your service implemantation files see https://docs.sylk.build/cli/edit?lang="
        + lang
    )


def enum(
    results,
    sylk_json: SylkJson,
    architect: SylkArchitect,
    parent: str,
    generate_package_func=None,
    tag = None
):
    enum = results["enum"].replace('/','.')
    enum_name = enum.split('.')[-1]
    description=None
    if sylk_json.domain == '.'.join(enum.split('.')[:-1]):
        pkg_name = sylk_json.domain
    else:
        pkg_name = sylk_json.domain + '.' + '.'.join(enum.split('.')[:-1])
    pkg=results.get('package') if results.get('package') is not None else pkg_name
    # pkg = results['package'] if parent is None else parent
    try:
        package = sylk_json.get_package(
            pkg, False
        )
    except Exception as e:
        if generate_package_func is not None:
            print_note(
                "Package {} is not valid, will create new default package.".format(pkg)
            )
            results["package"] = pkg.split(".")[1]
            generate_package_func(
                results, sylk_json, architect
            )
            sylk_json = SylkJson(architect._sylk.sylkJson.copy())
            package = sylk_json.get_package(
                pkg, False
            )
        else:
            print_error(
                "A function to create package instance is not specified. please create the package before creating message."
            )
            exit(1)

    # package = sylk_json.get_package(pkg.split('.')[1], False)
    if package.enums:
        if next((e for e in package.enums if e.name == enum_name), None) is not None:
            print_error(f'Enum "{enum_name}" already exists under "{pkg}" package')
            exit(1)
    add_value = True
    e_values = []
    while add_value:
        ev = inquirer.prompt(
            [
                inquirer.Text("name", "Enter value name", validate=validation),
                inquirer.Text(
                    "value", "Enter enum value", validate=enum_value_validate
                ),
            ],
            theme=SylkTheme(),
        )
        if ev is not None:
            if int(ev["value"]) == 0:
                print_warning(
                    "Enum values with 0 will be ignored by gRPC and should be used only as default value"
                )
            confirm = inquirer.prompt(
                [
                    inquirer.Confirm(
                        "continue", message="Add more values?", default=True
                    )
                ],
                theme=SylkTheme(),
            )
            v_name = ev["name"]

            if confirm.get("continue") == False or confirm.get("continue") == None:
                add_value = False
            if next((v for v in e_values if v["name"] == ev["name"]), None) is not None:
                print_error(
                    f"Enum values names must be unique, {v_name} appears already in {enum_name}"
                )
                exit(1)
            if (
                next(
                    (v for v in e_values if v.get("number") == int(ev.get("value"))),
                    None,
                )
                is not None
            ):
                print_error("Enum values must be unique inside the enum scope")
                exit(1)

            for e in package.enums:
                if next((v for v in e.values if v.name == ev["name"]), None):
                    print_error(
                        f"Enum values names must be unique in all enums in package, {v_name} appears already in {e.full_name}"
                    )
                    exit(1)
            for e in package.enums:
                if ev['name'] == e.name:
                    print_error(
                        f"Enum values names cannot be the same as messages names or enums that are already described in the proto package"
                    )
                    exit(1)

            e_values.append(SylkEnumValue(ev["name"], int(ev["value"])).to_dict())
        else:
            print_error("Enum values are required")
            exit(1)
    if next((v for v in e_values if v["number"] == 0), None) is None:
        e_values.insert(0, SylkEnumValue(f"UNKNOWN_{enum_name.upper()}", 0).to_dict())
        print_warning(f'Adding default enum value "UNKNOWN_{enum_name.upper()}" : 0')
    pkgs = sylk_json._proto_tree.topological_sort()[::-1]
    if package.package not in pkgs:
        pkgs.append(package.package)
    architect.AddEnum(package, enum_name, e_values, tag, order_pkg=pkgs)
    architect.Save()


def field_exists_validation(new_field, fields, msg):
    if new_field in fields:
        raise SylkProtoError("Message", f"Field {new_field} already exits under {msg}")
    return True


def enum_value_validate(answers, current):
    try:
        int(current)
    except Exception:
        raise errors.ValidationError(
            current, reason="Enum Value MUST be an integer value"
        )
    return True


def float_value_validate(answers, current):
    try:
        float(current)
    except Exception:
        raise errors.ValidationError(current, reason="Value must be valid float type")
    return True


def int_value_validate(answers, current):
    try:
        int(current)
    except Exception:
        raise errors.ValidationError(current, reason="Value must be valid integer type")
    return True


def validation(answers, current):
    if len(current) == 0:
        raise errors.ValidationError(current, reason="Resource name must not be blank")
    if len(re.findall("\s", current)) > 0:
        raise errors.ValidationError(
            current, reason="Resource name must not include blank spaces"
        )
    if len(re.findall("-", current)) > 0:
        raise errors.ValidationError(
            current,
            reason="Resource name must not include hyphens, underscores are allowed",
        )
    return True
