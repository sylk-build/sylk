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

import logging
import subprocess
import sylk.builder as builder
from sylk.commons import helpers, file_system, resources, pretty, protos
from sylk.builder.plugins.static import gitignore_js, logger_js, js_package_json


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
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext
):
    directories = [
        # Utils
        file_system.join_path(sylk_json.path, "services", "utils"),
        # Protos
        file_system.join_path(sylk_json.path, "services", "protos"),
    ]

    for dir in directories:
        file_system.mkdir(dir)
    # Utils
    file_system.wFile(
        file_system.join_path(sylk_json.path, "services", "utils", "logger.js"),
        logger_js,
    )
    file_system.wFile(
        file_system.join_path(sylk_json.path, "package.json"),
        js_package_json(sylk_json.project.get("packageName")),
    )
    # Bin files
    services_protoc = []
    packages_protoc = []
    if sylk_json.services is not None:
        for s in sylk_json.services:
            services_protoc.append(s)
            if (
                file_system.check_if_dir_exists(
                    file_system.join_path(sylk_json.path, "services", "protos", s)
                )
                == False
            ):
                file_system.mkdir(
                    file_system.join_path(sylk_json.path, "services", "protos", s)
                )
            # if file_system.check_if_dir_exists(file_system.join_path(sylk_json.path, 'services', s)) == False:
            # file_system.mkdir(file_system.join_path(sylk_json.path, 'services',s))
    # if sylk_json.packages is not None:
    # for p in sylk_json.packages:
    # packages_protoc.append(sylk_json.packages[p].get('name'))
    # if file_system.check_if_dir_exists(file_system.join_path(sylk_json.path, 'services', 'protos', sylk_json.packages[p].get('name'))) == False:
    # file_system.mkdir(file_system.join_path(sylk_json.path, 'services', 'protos', sylk_json.packages[p].get('name')))

    # .gitignore
    file_system.wFile(file_system.join_path(sylk_json.path, ".gitignore"), gitignore_js)

    return [directories]


@builder.hookimpl
def write_services(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    for svc in sylk_json.services:
        if (
            file_system.check_if_file_exists(
                file_system.join_path(sylk_json.path, "services", svc, f"{svc}.js")
            )
            == False
        ):
            service_code = helpers.SylkServiceJs(
                sylk_json.project.get("packageName"),
                svc,
                sylk_json.services[svc].get("dependencies"),
                sylk_json.services[svc],
                context=sylk_context,
                sylk_json=sylk_json,
            ).to_str()
            file_system.wFile(
                file_system.join_path(sylk_json.path, "services", f"{svc}.js"),
                service_code,
                overwrite=True,
            )
        # else:
        #     pretty.print_info("Make sure you are editing the {0} file\n - See how to edit service written in Javascript".format(file_system.join_path(
        #         sylk_json.path, 'services', f'{svc}.js')))
        #     return (f'{svc}.js',)


_OPEN_BRCK = "{"
_CLOSING_BRCK = "}"


@builder.hookimpl
def write_server(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext, pre_data
):
    # pretty.print_error(pre_data,True,'pre_data')
    temp_imports = []
    imports = [
        "const services = require('./services')",
        "let grpc = require('@grpc/grpc-js');",
        "let protoLoader = require('@grpc/proto-loader');",
    ]
    services_bindings = []
    for svc in sylk_json.services:
        temp_imports.append(f"PROTO_PATH_{svc.upper()}")
        imports.append(
            f"const PROTO_PATH_{svc.upper()} = __dirname + '/protos/{svc}.proto';"
        )
        temp_svc_name = svc[0].capitalize() + svc[1:]
        services_bindings.append(
            f"server.addService(protoDescriptor{temp_svc_name}.{svc}.service, services.{svc});"
        )
    services_bindings = "\n\t".join(services_bindings)
    imports = "\n\t".join(imports)
    port = sylk_json._config.get("port")
    temp_imports = ", ".join(temp_imports)
    server_code = f"// sylk.build Generated Server Code\n\
{imports}\n\
var packageDefinition = protoLoader.loadSync(\n\
    [{temp_imports}],\n\
    {_OPEN_BRCK}\n\
        includeDirs: [`${_OPEN_BRCK}__dirname{_CLOSING_BRCK}`],\n\
        keepCase: true,\n\
        longs: String,\n\
        enums: String,\n\
        defaults: true,\n\
        oneofs: true,\n\
    {_CLOSING_BRCK}\n\
);\n\
var protoDescriptorTask = grpc.loadPackageDefinition(packageDefinition);\n\
function getServer() {_OPEN_BRCK}\n\
    let server = new grpc.Server();\n\
    {services_bindings}\n\
    return server;\n\
{_CLOSING_BRCK}\n\n\
const SylkServer = getServer();\n\
routeServer.bindAsync('0.0.0.0:{port}', grpc.ServerCredentials.createInsecure(), () => {_OPEN_BRCK}\n\
    console.log(`[i] 🔌 Starting sylk build server [::]:{port}`)\n\
    SylkServer.start();\n\
{_CLOSING_BRCK});"

    if (
        file_system.check_if_file_exists(
            file_system.join_path(sylk_json.path, "server.js")
        )
        == False
    ):
        file_system.wFile(
            file_system.join_path(sylk_json.path, "server.js"),
            server_code,
            overwrite=True,
        )
    else:
        pretty.print_warning("Make sure you make desired changes on server.js file !")
