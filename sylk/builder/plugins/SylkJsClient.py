# Copyright (c) 2023 Sylk.build.

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
from sylk import __version__
from sylk.commons import helpers, file_system, resources, pretty
from sylk.builder.plugins.static import gitignore_ts, js_package_json, interceptors_js
import inspect


@builder.hookimpl
def pre_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    pretty.print_info("🔌 Starting sylk build process %s plugin" % (__name__))


@builder.hookimpl
def post_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    if (
        file_system.check_if_dir_exists(
            file_system.join_path(sylk_json.path, "node_modules")
        )
        == False
    ):
        # proc = subprocess.run('npm i')
        subprocess.check_call("npm i", shell=True)

        # if proc.returncode != 0:
        # pretty.print_error("ERROR occured during installation of node modules. some more info on specific error can be found above")
        # exit(proc.returncode)
    if (
        file_system.check_if_dir_exists(
            file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "javascript", "utils")
        )
        == False
    ):
        file_system.mkdir(
            file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "javascript", "utils")
        )

    file_system.cpDir(
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "server", "services", "utils"),
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "javascript", "utils"),
    )
    for f in file_system.walkFiles(file_system.join_path(sylk_json.path, sylk_json._root_protos)):
        if file_system.check_if_file_exists(
            file_system.join_path(
                sylk_json.path,
                sylk_json.code_base_path,
                "clients",
                "javascript",
                "protos",
                f.split(".")[0],
                "v1",
                f,
            )
        ):
            file_system.copyFile(
                file_system.join_path(sylk_json.path, sylk_json._root_protos, f),
                file_system.join_path(
                    sylk_json.path,
                    sylk_json.code_base_path,
                    "clients",
                    "javascript",
                    "protos",
                    f.split(".")[0],
                    "v1",
                    f,
                ),
            )
        else:
            file_system.wFile(
                file_system.join_path(
                    sylk_json.path,
                    sylk_json.code_base_path,
                    "clients",
                    "javascript",
                    "protos",
                    f.split(".")[0],
                    "v1",
                    f,
                ),
                "",
                True,
                False,
                True,
            )
            file_system.copyFile(
                file_system.join_path(sylk_json.path, sylk_json._root_protos, f),
                file_system.join_path(
                    sylk_json.path,
                    sylk_json.code_base_path,
                    "clients",
                    "javascript",
                    "protos",
                    f.split(".")[0],
                    "v1",
                    f,
                ),
            )

    # file_system.cpDir(file_system.join_path(sylk_json.path,'protos'),file_system.join_path(sylk_json.path,'clients','javascript','protos'))

    # pretty.print_success("Finished sylk build process %s plugin" % (__name__))
    return (__name__, "OK")


@builder.hookimpl
def init_project_structure(
    sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext
):
    directories = [
        # Clients
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "javascript"),
        file_system.join_path(sylk_json.path, sylk_json.code_base_path, "clients", "javascript", "protos"),
        # Utils
        file_system.join_path(sylk_json.path, sylk_json.code_base_path,"services", "utils"),
        # Protos
        file_system.join_path(sylk_json.path, sylk_json.code_base_path,"services", "protos"),
    ]

    for dir in directories:
        file_system.mkdir(dir)
    # package.json
    file_system.wFile(
        file_system.join_path(sylk_json.path, "package.json"),
        js_package_json(sylk_json.project.get("packageName")),
    )

    # Bin files
    # file_system.wFile(file_system.join_path(
    # sylk_json.path, 'bin', 'init-ts.sh'), bash_init_script_ts)
    # file_system.wFile(file_system.join_path(
    # sylk_json.path, 'bin', 'proto.js'), protos_compile_script_ts)
    file_system.wFile(
        file_system.join_path(
            sylk_json.path, sylk_json.code_base_path, "clients", "javascript", "utils", "interceptors.js"
        ),
        interceptors_js(__version__.__version__),
        force=True,
    )
    file_system.wFile(
        file_system.join_path(sylk_json.path, ".sylk", "contxt.json"), '{"files":[]}'
    )

    # .gitignore
    file_system.wFile(file_system.join_path(sylk_json.path, ".gitignore"), gitignore_ts)

    return [directories]


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
        ("grpc.keepalive_time_ms", 120000),
        ("grpc.http2.min_time_between_pings_ms", 120000),
        ("grpc.keepalive_timeout_ms", 20000),
        ("grpc.http2.max_pings_without_data", 0),
        ("grpc.keepalive_permit_without_calls", 1),
        ("interceptors", "interceptorsProviders"),
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

                        # Append to exports
                        elif "append_exports" in hook.split(":")[2]:
                            if mini_hooks[hook] is not None:
                                for exp in mini_hooks[hook]:
                                    exports.append(exp)

                        # Append to exports
                        elif "override_stubs" in hook.split(":")[2]:
                            if mini_hooks[hook] is not None:
                                for stub in mini_hooks[hook]:
                                    override_stubs[stub] = mini_hooks[hook][stub]

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
                        elif "add_before_init" in hook.split(":")[2]:
                            if mini_hooks[hook] is not None:
                                before_init = mini_hooks[hook]

                        elif "append_interceptors" in hook.split(":")[2]:
                            if mini_hooks[hook] is not None:
                                for intrcpt in mini_hooks[hook]:
                                    interceptors.append(intrcpt)
                    else:
                        pretty.print_warning(f"[{__name__}] `{hook}` missing command")

    if (
        file_system.check_if_dir_exists(
            file_system.join_path(sylk_json.path, "clients", "javascript")
        )
        == False
    ):
        file_system.mkdir(
            file_system.join_path(sylk_json.path, "clients", "javascript")
        )

    client = helpers.SylkClientJs(
        sylk_json.project.get("packageName"),
        sylk_json.services,
        sylk_json.packages,
        sylk_context,
        pre_data={
            "imports": imports,
            "exports": exports,
            "stubs": override_stubs,
            "client_options": client_options,
            "before_init": before_init,
            "interceptors": interceptors,
        },
    )
    file_system.wFile(
        file_system.join_path(sylk_json.path, "clients", "javascript", "index.js"),
        client.__str__(),
        overwrite=True,
    )
