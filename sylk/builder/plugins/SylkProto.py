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
import os
import subprocess
import sys
import sylk.builder as builder
from sylk.commons import helpers, file_system
from sylk.commons.pretty import print_error, print_info, print_note
import pkg_resources
from grpc_tools import _protoc_compiler
import sylk_docs
log = logging.getLogger("sylk.cli.main")


@builder.hookimpl
def pre_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    if file_system.check_if_dir_exists(file_system.join_path(sylk_json.path, "protos")):
        print_info("🔌 Starting sylk build process %s plugin" % (__name__))
    else:
        file_system.mkdir(file_system.join_path(sylk_json.path, "protos"))
    return (__name__, "OK")


@builder.hookimpl
def post_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    # log.debug("Finished sylk build process %s plugin" % (__name__))
    return (__name__, "OK")


def run_protoc(command_arguments):
    command_arguments = [argument.encode() for argument in command_arguments]
    return _protoc_compiler.run_main(command_arguments)


@builder.hookimpl
def compile_protos(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext, pre_data
):
    well_known_protos = pkg_resources.resource_filename("grpc_tools", "_proto")
    sylk_protos = pkg_resources.resource_filename("sylk", "_proto")
    commands = []
    include_dirs = [
        "-I{}".format(well_known_protos),
        '-I{}'.format(sylk_protos)
    ]
    if pre_data:
        _hook_name = inspect.stack()[0][3]
        for mini_hooks in pre_data:
            for hook in mini_hooks:
                if __name__ == hook.split(":")[0]:
                    if hook.split(":")[2] is not None and _hook_name == hook.split(":")[
                        1
                    ].replace("()", ""):
                        if "include_dirs" in hook.split(":")[2]:
                            if (
                                mini_hooks[hook] is not None
                                and len(mini_hooks[hook]) > 0
                            ):
                                for d in mini_hooks[hook]:
                                    include_dirs.append("-I{}".format(d))
                        if "commands" in hook.split(":")[2]:
                            if (
                                mini_hooks[hook] is not None
                                and len(mini_hooks[hook]) > 0
                            ):
                                # print_error(mini_hooks[hook])
                                commands = commands + mini_hooks[hook]

    proto_files = []
    files = sylk_json._proto_tree.get_all_file_paths()
    # for pkg in sylk_json.packages:
    #     p= sylk_json.packages[pkg]
    #     msgs = sylk_json.packages[pkg].get('messages') if sylk_json.packages[pkg].get('messages') is not None else []
    #     svcs = sylk_json.packages[pkg].get('services') if sylk_json.packages[pkg].get('services') is not None else []
    #     enms = sylk_json.packages[pkg].get('enums') if sylk_json.packages[pkg].get('enums') is not None else []
    #     tags = [m.get('tag') for m in msgs if m.get('tag') is not None and m.get('tag') != '']
    #     if len(tags) == 0:
    #         tags.append(p.get('name'))
    #     enum_tags = [e.get('tag') for e in enms if e.get('tag') is not None and e.get('tag') != '']
    #     if len(tags) == 0 and p.get('name') not in tags:
    #         tags.append(p.get('name'))
    #     else:
    #         tags.extend(enum_tags)
    #     svc_tags = [s.get('tag') for s in svcs if s.get('tag') is not None and s.get('tag') != '']
    #     if len(svc_tags) == 0 and p.get('name') not in tags:
    #         tags.append(p.get('name'))
    #     else:
    #         tags.extend(svc_tags)
    #     if len(tags) > 0:
    #         for t in tags:
    #             proto_files.append(pkg + '/' + t +'.proto')
    #     else:
    #         ver = helpers.parse_version_component(pkg)
    #         if ver:
    #             pkg_name = pkg.split('/')[-2].lower()
    #         else:
    #             pkg_name = pkg.split('/')[-1].lower()
    #         proto_files.append(pkg + '/' + pkg_name +'.proto')
    
    if sylk_json.is_language("python"):
        protoc_params = (
            [
                c
                for c in list(
                    map(
                        lambda f: f
                        if "--python" in f
                        or "--grpc_python_out" in f
                        or "--pyi" in f
                        or "-I" in f
                        or "--proto_path" in f
                        or "--plugin" in f
                        or "--custom" in f
                        else None,
                        commands,
                    )
                )
                if c is not None
            ]
            + include_dirs
            + [f for f in files if 'google/' not in f]
        )
        # print_note(protoc_params)
        run_protoc(protoc_params)
        # protoc_params = ["protoc"] + [
        #         c
        #         for c in list(
        #             map(
        #                 lambda f: f
        #                 if "--plugin" in f
        #                 or "--custom" in f
        #                 or "--proto_path" in f
        #                 or "-I" in f
        #                 else None,
        #                 commands,
        #             )
        #         )
        #         if c is not None
        #     ] + include_dirs + [f for f in files if 'google/' not in f]
        # # print_note(protoc_params)
        # process = subprocess.Popen(
        #     protoc_params, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        # )
        # _, stderr = process.communicate()
        # if stderr:
        #     print_info(stderr.decode("utf-8"))
    else:
        protoc_params = ["protoc"] + commands + include_dirs + [f for f in files if 'google/' not in f]
        # print_note(protoc_params)
        process = subprocess.Popen(
            protoc_params, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        _, stderr = process.communicate()
        if stderr:
            print_info(stderr.decode("utf-8"))

    if sylk_json.is_language("go"):
        protoc_params = (
            ["protoc"]
            + [
                c
                for c in list(
                    map(
                        lambda f: f
                        if "--go" in f or "-I" in f or "--proto-path" in f
                        else None,
                        commands,
                    )
                )
                if c is not None
            ]
            + include_dirs
            + [f for f in files if 'google/' not in f]
        )
        process = subprocess.Popen(
            protoc_params, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        _, stderr = process.communicate()
        if stderr:
            print_info(stderr.decode("utf-8"))


@builder.hookimpl
def write_protos(sylk_json: helpers.SylkJson):
    file_system.removeDir(file_system.join_path(sylk_json.path, sylk_json._root_protos if sylk_json._root_protos is not None else '', sylk_json.domain))
    if sylk_json.packages is None:
        print_error(
            "Not supporting building project without any packages",
            True,
            "Build process error",
        )
        exit(1)

    for p in sylk_json.packages:
        tmp_pkg = sylk_json.packages[p]
        pkg = sylk_json.get_package(tmp_pkg.get('package'),False)
        tags = {}
        if pkg.services is not None:
            svcs_tags = [
                s.tag for s in pkg.services if s.tag != ''
            ]
            for t in svcs_tags:
                if tags.get(t) is None:
                    tags[t] = []
                tags[t].extend([
                    m.full_name for m in pkg.services if m.tag == t
                ])
        if pkg.enums is not None:
            enums_tags = [
                e.tag for e in pkg.enums if e.tag != ''
            ]
            for t in enums_tags:
                if tags.get(t) is None:
                    tags[t] = []
                tags[t].extend([
                    m.full_name for m in pkg.enums if m.tag == t
                ])
        if pkg.messages is not None:
            messages_tags = [
                m.tag for m in pkg.messages if m.tag != ''
            ]
            for t in messages_tags:
                if tags.get(t) is None:
                    tags[t] = []
                tags[t].extend([
                    m.full_name for m in pkg.messages if m.tag == t
                ])

        if len(tags.keys()) > 0:
            for t in tags:
                proto = helpers.SylkProtoFile(t,pkg,sylk_json,True)
                proto._set_file_path()
                print(proto._file_path)
                file_system.wFile(
                    proto._file_path,
                    proto.to_str(),
                    True,
                    False,
                    True,
                )
            if pkg.services is not None:
                svcs = [
                    s.full_name for s in pkg.services if s.tag == ''
                ]
                
            if pkg.enums is not None:
                enums = [
                    e.full_name for e in pkg.enums if e.tag == ''
                ]
                
            if pkg.messages is not None:
                msgs = [
                    m.full_name for m in pkg.messages if m.tag == ''
                ]
            
            if len(enums) > 0 or len(msgs) > 0 or len(svcs) > 0:
                proto = helpers.SylkProtoFile(pkg.name,pkg,sylk_json)
                file_system.wFile(
                    proto._file_path,
                    proto.to_str(),
                    True,
                    False,
                    True,
                )
            
        else:
            proto = helpers.SylkProtoFile(pkg.name,pkg,sylk_json)
            file_system.wFile(
                proto._file_path,
                proto.to_str(),
                True,
                False,
                True,
            )

        #     # print(tags)
        #     proto = helpers.SylkProto(
        #         pkg.name,
        #         imports=pkg.dependencies,
        #         package=pkg.package,
        #         services=pkg.services,
        #         messages=pkg.messages,
        #         enums=pkg.enums,
        #         description=pkg.description,
        #         extensions=pkg.extensions,
        #         sylk_json=sylk_json,
        #         tags=tags
        #     )
        #     proto.write_files()
        # else:
        #     proto = helpers.SylkProto(
        #         pkg.name,
        #         imports=pkg.dependencies,
        #         package=pkg.package,
        #         services=pkg.services,
        #         messages=pkg.messages,
        #         enums=pkg.enums,
        #         description=pkg.description,
        #         extensions=pkg.extensions,
        #         sylk_json=sylk_json,
        #         tags={}
        #     )
        #     proto.write_files()
    # for svc in sylk_json.services:
    #     if svc.get("methods") is None:
    #         print_error(f"Cannot build service [{svc}] proto file with 0 methods!")
    #         exit(1)

    #     svc_name = svc.get("name")
    #     svc_pkg_messages = []
    #     svc_pkg_enums = []
    #     svc_deps = svc.get("dependencies", [])
    #     try:
    #         svc_pkg = sylk_json.get_package(
    #             svc_name, version=svc.get("fullName").split(".")[-1]
    #         )
    #         svc_pkg_messages = sylk_json.packages[svc].get("messages")

    #         svc_pkg_enums = sylk_json.packages[svc].get("enums")
    #         if svc_pkg.get("dependencies") is not None:
    #             for d in svc_pkg.get("dependencies"):
    #                 if d not in svc_deps:
    #                     svc_deps.append(d)

    #     except Exception:
    #         pass

    #     svc_def = helpers.SylkProto(
    #         svc_name,
    #         imports=svc_deps,
    #         service=svc,
    #         package=svc.get("fullName")
    #         if (len(svc_pkg_messages) > 0 or len(svc_pkg_enums) > 0)
    #         else None,
    #         messages=svc_pkg_messages,
    #         enums=svc_pkg_enums,
    #         description=svc.get("description"),
    #         extensions=svc.get("extensions"),
    #         sylk_json=sylk_json,
    #     )

    #     log.debug(f"Writing proto file for service: {svc.get('name')}")
    #     file_system.wFile(
    #         file_system.join_path(sylk_json.path, svc),
    #         svc_def.__str__(),
    #         True,
    #         False,
    #         True,
    #     )

    # for pkg in sylk_json.packages:
    #     pkg_name = sylk_json.packages[pkg].get("name")
    #     # Checking if proto file already defined by service with the same name of the package
    #     svc = sylk_json.get_service(
    #         pkg_name, version=sylk_json.packages[pkg].get("package").split(".")[-1]
    #     )
    #     if svc is None:
    #         # If no service with the same name then we need to write a standalone proto file for packages
    #         pkg_full_name = sylk_json.packages[pkg].get("package")
    #         if sylk_json.packages[pkg].get("messages") is None:
    #             print_error(
    #                 f"Cannot build package [{sylk_json.packages[pkg].get('package')}] proto file with 0 messages!"
    #             )
    #             exit(1)

    #         pkg_def = helpers.SylkProto(
    #             pkg_name,
    #             sylk_json.packages[pkg].get("dependencies"),
    #             package=pkg_full_name,
    #             messages=sylk_json.packages[pkg].get("messages"),
    #             enums=sylk_json.packages[pkg].get("enums"),
    #             extensions=sylk_json.packages[pkg].get("extensions"),
    #             sylk_json=sylk_json,
    #         )
    #         log.debug(f"Writing proto file for package: {pkg_name}")
    #         file_system.wFile(
    #             file_system.join_path(sylk_json.path, pkg),
    #             pkg_def.__str__(),
    #             True,
    #             False,
    #             True,
    #         )
