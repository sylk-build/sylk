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

import sylk.builder as builder
from sylk.commons import helpers, file_system, pretty

@builder.hookimpl
def pre_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    pretty.print_info("🔌 Starting sylk build process %s plugin" % (__name__))


@builder.hookimpl
def init_project_structure(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext, pre_data
):

    directories = [
        # Clients
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "webpack"),
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "webpack", sylk_json._root_protos),
    ]
    if pre_data.get('protos_only',False) == False:

        for dir in directories:
            file_system.mkdir(dir)

    return [directories]


@builder.hookimpl
def pre_compile_protos(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    pretty.print_info("Running pre compile protos - webpack client")
    protos_out = file_system.join_path(sylk_json.code_base_path,'clients','webpack',sylk_json._root_protos)
    return {
        "sylk.builder.plugins.SylkProto:compile_protos():commands": [
            f"--proto_path={sylk_json._root_protos}/",
            f"--grpc-web_out=import_style=typescript,mode=grpcwebtext:./{protos_out}",
            f"--js_out=import_style=commonjs,binary:./{protos_out}",
            f"-I./{sylk_json._root_protos}/",
        ],
        "sylk.builder.plugins.SylkProto:compile_protos():include_dirs": [],
    }

@builder.hookimpl
def write_clients(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    if file_system.check_if_dir_exists(
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "webpack")
    ):
        file_system.mkdir(
            file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "webpack", sylk_json._root_protos)
        )
    else:
        file_system.mkdir(file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "webpack"))
        file_system.mkdir(
            file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "webpack", sylk_json._root_protos)
        )