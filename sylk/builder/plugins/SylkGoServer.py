# Copyright (c) 2022 sylk.build.

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
from sylk.commons import helpers, file_system, resources, pretty, protos
from sylk.builder.plugins.static import (
    gitignore_go,
    bash_init_script_go,
    bash_run_server_script_go,
    utils_go,
)


@builder.hookimpl
def pre_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    pretty.print_info("🔌 Starting sylk build process %s plugin" % (__name__))


@builder.hookimpl
def post_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    # TODO add postbuild validation of generated code
    # pretty.print_success("Finished sylk build process %s plugin" % (__name__))
    return (__name__, "OK")


@builder.hookimpl
def init_project_structure(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext, pre_data
):
    directories = [
        # Utils
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "services", "utils"),
        # Protos
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "services", sylk_json._root_protos),
    ]

    if pre_data.get('protos_only',False) == False:

        for dir in directories:
            file_system.mkdir(dir)
        # Utils
        file_system.wFile(
            file_system.join_path(sylk_json.path, sylk_json.code_base_path, "services", "utils", "utils.go"), utils_go
        )

        if sylk_json.get_server_language() == "go":
            file_system.wFile(
                file_system.join_path(sylk_json.path, "bin", "run-server.sh"),
                bash_run_server_script_go(sylk_json.code_base_path),
                overwrite=True
            )


        # .gitignore
        file_system.wFile(file_system.join_path(sylk_json.path, ".gitignore"), gitignore_go)

    return [directories]


@builder.hookimpl
def write_services(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    for svc in sylk_json.services:
        service_name = svc.get('name')
        ver = helpers.parse_version_component(svc.get("fullName"))
        if ver:
            service_version = svc.get("fullName").split(".")[-2]
            svc_path = file_system.join_path(
                    sylk_json.path,
                    sylk_json.code_base_path,
                    "services",
                    service_name,
                    service_version,
                    f"{service_name}.go",
                )
        else:
            svc_path = file_system.join_path(
                    sylk_json.path,
                    sylk_json.code_base_path,
                    "services",
                    service_name,
                    f"{service_name}.go",
                )
        if (
            file_system.check_if_file_exists(
                svc_path
            )
            == False
        ):
            service_code = helpers.SylkServiceGo(
                sylk_json.project.get("packageName"),
                service_name,
                svc.get("dependencies"),
                svc,
                context=sylk_context,
                sylk_json=sylk_json,
            ).to_str()
            file_system.wFile(
                svc_path,
                service_code,
                overwrite=True,
                force=True,
            )
        # else:
        #     pretty.print_info("Make sure you are editing the {0} file\n - See how to edit service written in Go".format(file_system.join_path(
        #         sylk_json.path, 'services',svc, f'{svc}.go')))


# mkdir $DST_DIR"/{0}"\nprotoc -I=$SRC_DIR --go_out=$DST_DIR --go_opt=paths=source_relative --go-grpc_out=$DST_DIR"/{0}"  --go-grpc_opt=paths=source_relative protos/{0}.proto


@builder.hookimpl
def pre_compile_protos(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    pretty.print_info("Running pre compile protos - go server")
    return {
        "sylk.builder.plugins.SylkProto:compile_protos():commands": [
            f"--proto_path={sylk_json._root_protos}/",
            f"--go_out=./{file_system.join_path(sylk_json.code_base_path,'services',sylk_json._root_protos)}",
            f"--go_opt=paths=source_relative",
            f"--go-grpc_out=./{file_system.join_path(sylk_json.code_base_path,'services',sylk_json._root_protos)}",
            f"--go-grpc_opt=paths=source_relative",
            f"-I./{sylk_json._root_protos}/",
        ],
        "sylk.builder.plugins.SylkProto:compile_protos():include_dirs": [],
    }


# @builder.hookimpl
# def compile_protos(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
#     services_protoc = []
#     packages_protoc = []
#     if sylk_json.services is not None:
#         for s in sylk_json.services:
#             services_protoc.append(s)
#     if sylk_json.packages is not None:
#         for p in sylk_json.packages:
#             packages_protoc.append(sylk_json.packages[p].get("name"))
#     file_system.wFile(
#         file_system.join_path(sylk_json.path, "bin", "init-go.sh"),
#         bash_init_script_go(
#             sylk_json.project.get("goPackage"), services_protoc, packages_protoc
#         ),
#         True,
#     )
#     # Running ./bin/init-go.sh script for compiling protos
#     # logging.info("Running ./bin/init-go.sh script for 'protoc' compiler")
#     subprocess.run(["bash", file_system.join_path(sylk_json.path, "bin", "init-go.sh")])


_OPEN_BRCK = "{"
_CLOSING_BRCK = "}"


@builder.hookimpl
def write_server(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext, pre_data
):
    if (
        file_system.check_if_file_exists(
            file_system.join_path(sylk_json.path, sylk_json.code_base_path, "server", "server.go")
        )
        == False
    ):
        go_package_name = sylk_json.project.get("goPackage")
        code_base_path = sylk_json.code_base_path +'/' if sylk_json.code_base_path is not None and sylk_json.code_base_path != '' else ''
        imports = ['"log"', '"fmt"', '"flag"', '"net"', '"google.golang.org/grpc"']
        services_bindings = []
        for svc in sylk_json.services:
            svc_name = svc.get('name')
            svc_path = "/".join(svc.get('fullName').split(".")[:-1])
            svc_ver = helpers.parse_version_component(svc.get('fullName'))
            if svc_ver is not None:
                svc_ver =f"v{svc_ver.get('version')}{svc_ver.get('channel') if svc_ver.get('channel') is not None else ''}{svc_ver.get('release') if svc_ver.get('release') is not None else ''}"
            else:
                svc_ver = ""
            # svc_ver = svc.split("/")[-2]
            base_protos = f'{sylk_json._root_protos}/' if sylk_json._root_protos is not None else ''
            imports.append(
                f'{svc_name}{svc_ver}Servicer "{file_system.join_path(go_package_name, sylk_json.code_base_path, "services", base_protos, svc_path)}"'
            )
            imports.append(
                f'{svc_name}{svc_ver} "{go_package_name}/{code_base_path}services/{svc_name}/{svc_ver}"'
            )
            temp_svc_name = svc_name[0].capitalize() + svc_name[1:]
            services_bindings.append(
                f"{svc_name}{svc_ver}Servicer.Register{temp_svc_name}Server(grpcServer, new({svc_name}{svc_ver}.{temp_svc_name}));"
            )
        services_bindings = "\n\t".join(services_bindings)
        imports = "\n\t".join(imports)
        port = sylk_json._config.get("port")
        server_code = f'// sylk.build Generated Server Code\n\
    package main\n\n\
    import (\n\t{imports}\n)\n\
    var (\n\
        port = flag.Int("port", {port}, "The server port")\n\
    )\n\n\
    func main() {_OPEN_BRCK}\n\
    \tflag.Parse()\n\
    \tlis, err := net.Listen("tcp", fmt.Sprintf("localhost:%d", *port))\n\
    \tif err != nil {_OPEN_BRCK}\n\
    \t\tlog.Fatalf("Failed to listen: %v", err)\n\
    \t{_CLOSING_BRCK}\n\
    \tvar opts []grpc.ServerOption\n\
    \tgrpcServer := grpc.NewServer(opts...)\n\
    \t{services_bindings}\n\
    \tlog.Printf("[sylk.build] Starting server (Go) at -> %d",*port)\n\
    \tgrpcServer.Serve(lis)\n\
    {_CLOSING_BRCK}'

        if (
            file_system.check_if_file_exists(
                file_system.join_path(sylk_json.path, sylk_json.code_base_path, "server", "server.go")
            )
            == False
        ):
            file_system.wFile(
                file_system.join_path(sylk_json.path, sylk_json.code_base_path, "server", "server.go"),
                server_code,
                overwrite=True,
            )
        else:
            pretty.print_warning(
                f"Make sure you make desired changes on {sylk_json.code_base_path}/server/server.go file !"
            )
