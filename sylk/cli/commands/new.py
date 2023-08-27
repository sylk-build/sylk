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
from tkinter import E
from typing import List, Literal
from sylk import architect
from sylk.cli import prompter
from sylk.cli.prompter import QCheckbox, QConfirm, QList, QText, ask_user_question
from sylk.cli.theme import SylkTheme
from sylk.commons import file_system, protos
from sylk.commons.helpers import SylkEnumValue, SylkField, _BUILTINS_TEMPLATES
from sylk.commons.pretty import (
    print_info,
    print_warning,
    print_error,
    print_note,
    print_success,
)
from sylk.commons.file_system import join_path, mkdir, wFile
from sylk.architect import SylkArchitect
from sylk.cli.commands.cloud import SylkCloud
import os
import inquirer
from inquirer import errors
from sylk.commons.protos.sylk.SylkClient.v1 import SylkClient_pb2
from sylk.commons.protos.sylk.SylkServer.v1 import SylkServer_pb2
from google.protobuf.json_format import MessageToDict

_TEMPLATES = _BUILTINS_TEMPLATES


def validate_client(answers, current):
    if len(current) == 0:
        raise errors.ValidationError(current, "Must chose at least 1 client !")
    return True


def validate_domain(answers, current):
    if "." in current:
        raise errors.ValidationError(
            current,
            "Domain name MUST not include suffix like '.com' / '.io' and so on.",
        )
    return True


server_language_q = QList(
    name="server",
    message="Choose server language",
    choices=[
        ("Python", SylkServer_pb2.python),
        ("Typescript", SylkServer_pb2.typescript),
        ("Go", SylkServer_pb2.go),
        ("NodeJs", SylkServer_pb2.nodejs),
    ],
    default=SylkServer_pb2.python,
)
def code_base_q(language: SylkServer_pb2.SylkServerLanguages):
    return QText(
        name='code_base_path',
        message='Enter code base path',
        default= 'src' if language in[SylkServer_pb2.typescript,SylkServer_pb2.nodejs,SylkServer_pb2.python] else 'pkg' if language == SylkServer_pb2.go else ''
    )
clients_languages_q = QCheckbox(
    name="clients",
    message="Choose clients languages (Use arrows keys to enable disable a language)",
    choices=[
        ("Python", SylkClient_pb2.python),
        ("Typescript", SylkClient_pb2.typescript),
        ("Go", SylkClient_pb2.go),
        ("NodeJs", SylkClient_pb2.nodejs),
        ("Webpack", SylkClient_pb2.webpack),
    ],
    default=[SylkClient_pb2.python],
    validate=validate_client,
)
domain_q = QText(
    name="domain",
    message="Enter domain name",
    default="domain",
    validate=validate_domain,
)
base_proto_path_q = QText(
    name="base_proto_path",
    message="Enter your proto path",
    default="protos"
) 

sylk_neq_q = [base_proto_path_q, server_language_q, clients_languages_q, domain_q]


def create_new_project(
    project_name: str,
    path: str = None,
    host: str = None,
    port: int = None,
    server_language: str = None,
    clients=[],
    domain: str = None,
    template: _TEMPLATES = "@sylk/Blank",
    project_id=None,
    configs=None,
    base_proto_path=None,
    format='json',
    token=None,
    code_base=None
):
    domain_name = domain if domain is not None else 'domain'
    if project_id is not None:

        sylkCloud = SylkCloud(
            token=token if token is not None else configs.token if configs is not None else None,
            org_id=project_id.split(".")[0],
        )
        # If no options passed
        if server_language is None and clients == None and domain is None and code_base is None and base_proto_path is None:
            results = ask_user_question(questions=sylk_neq_q)
            tmp_code_base_path = ask_user_question(questions=[code_base_q(results.get("server"))])
            if tmp_code_base_path.get('code_base_path'):
                results["code_base_path"] = tmp_code_base_path['code_base_path']
            else:
                results["code_base_path"] = code_base
            if results is None:
                print_warning("Must answer project creation questions")
                exit(1)
        # If someof the options has passed
        elif server_language is not None or clients is not None or domain is not None or code_base is not None or base_proto_path is not None:
            questions = []

            if server_language is None:
                questions.append(server_language_q)
            else:
                print_note(f"Passed server language: {server_language}")

            if clients is None:
                questions.append(clients_languages_q)
            else:
                clients_display = ", ".join(clients)
                print_note(f"Passed client languages: {clients_display}")

            if base_proto_path is None:
                questions.append(base_proto_path_q)
            else:
                print_note(f"Passed base proto path: {base_proto_path}")

            results = ask_user_question(questions=questions)

            if results is None:
                print_warning("Must answer project creation questions")
                exit(1)
            else:
                if results.get("server") is None:
                    results["server"] = server_language
                if results.get("clients") is None:
                    results["clients"] = clients
                if results.get("base_proto_path") is None:
                    results["base_proto_path"] = base_proto_path
                if code_base is None:
                    tmp_code_base_path = ask_user_question([code_base_q(results.get("server"))])
                    results["code_base_path"] = tmp_code_base_path.get('code_base_path')
                else:
                    results["code_base_path"] = code_base
        else:
            results = {}
            results["server"] = server_language
            results["clients"] = clients
            results["base_proto_path"] = base_proto_path
            if code_base is None:
                tmp_code_base_path = ask_user_question([code_base_q(results.get("server"))])
                results["code_base_path"] = tmp_code_base.get('code_base_path')
            else:
                results["code_base_path"] = code_base

        project = sylkCloud.pull_project(project_id,domain=domain_name if domain_name != 'domain' else None)
        if path is None:
            try:
                root = os.getcwd()
                result_path = inquirer.prompt(
                    [
                        inquirer.Path(
                            "root_dir",
                            default=join_path(root, project_name),
                            message="Enter a root dir path",
                            exists=False,
                        )
                    ],
                    theme=SylkTheme(),
                )
                if result_path is not None:
                    result_path = result_path["root_dir"]
            except Exception:
                print_error(f"Error root dir exists\n[{join_path(root,project_name)}]")
                exit(1)
        else:
            if path == ".":
                path = os.getcwd()
                result_path = join_path(path)
            else:
                result_path = join_path(path, project_name)
        project.project.uri = result_path
        project_path = join_path(result_path, "sylk.json")
        if (
            project.project.server.language == SylkServer_pb2.SylkServerLanguages.go
            and project.project.go_package == ""
        ):
            go_package_input = prompter.QText(
                name="go_package",
                message="Enter a prefix to support Go package",
                default="github.com/{}".format(project.project.package_name),
            )
            go_package = prompter.ask_user_question(questions=[go_package_input])
            if go_package is not None:
                go_package = go_package["go_package"]
            else:
                go_package = "github.com/{}".format(project.project.package_name)
            project.project.go_package = go_package

        mkdir(result_path)
        # print_info(MessageToDict(project),True,'JSON:')
        wFile(project_path, MessageToDict(project), overwrite=True, json=True)
        print_info(f'saved sylk schema into: {project_path}')
        ARCHITECT = SylkArchitect(
            path=project_path, domain=domain_name, project_name=project_name, format=format
        )
        # print_info(clients)
        # print_info(server_language)
        ARCHITECT.SetConfig({"host": host, "port": int(port), "protoBasePath": results["base_proto_path"], "codeBasePath": results["code_base_path"]})
        ARCHITECT.AddProject(
            project_name, project.project.server.language if server_language is None else server_language, project.project.clients if len(results["clients"]) == 0 else list(map(lambda c: {"language": SylkClient_pb2.SylkClientLanguages.Name(c) if type(c) != str else c}, results["clients"]))
        )
        # ARCHITECT._sylk = project
        ARCHITECT.SetSylkVersion()
        ARCHITECT.Save()

        print_success(
            f'Success pulling ☁️  project!\n\tCreated new project "{project_name}"\n\t-> cd {project_path}\n\t-> And then continue developing your awesome services !\n\t-> For more info on how to use the sylk.build CLI go to https://docs.sylk.build/'
        )

    else:

        # If no options passed
        if server_language is None and clients == None and domain is None and code_base is None and base_proto_path is None:
            
            results = ask_user_question(questions=sylk_neq_q)
            tmp_code_base_path = ask_user_question(questions=[code_base_q(results['server'])])
            if tmp_code_base_path.get('code_base_path'):
                results["code_base_path"] = tmp_code_base_path['code_base_path']
            else:
                results["code_base_path"] = code_base

            if results is None:
                print_warning("Must answer project creation questions")
                exit(1)
            
        # If someof the options has passed
        elif server_language is not None or clients is not None or domain is not None or code_base is not None or base_proto_path is not None:
            questions = []

            if server_language is None:
                questions.append(server_language_q)
            else:
                print_note(f"Passed server language: {server_language}")

            if clients is None:
                questions.append(clients_languages_q)
            else:
                clients_display = ", ".join(clients)
                print_note(f"Passed client languages: {clients_display}")

            if domain is None:
                questions.append(domain_q)
            else:
                print_note(f"Passed domain: {domain}")

            if base_proto_path is None:
                questions.append(base_proto_path_q)
            else:
                print_note(f"Passed base proto path: {base_proto_path}")

            results = ask_user_question(questions=questions)

            if results is None:
                print_warning("Must answer project creation questions")
                exit(1)
            else:
                if results.get("server") is None:
                    results["server"] = server_language
                if results.get("clients") is None:
                    results["clients"] = clients
                if results.get("domain") is None:
                    results["domain"] = domain
                if results.get("base_proto_path") is None:
                    results["base_proto_path"] = base_proto_path   
                if code_base is None:
                    tmp_code_base = ask_user_question(questions=[code_base_q(server_language)])
                    results["code_base_path"] = tmp_code_base.get('code_base_path')
                else:
                    results["code_base_path"] = code_base

        else:
            results = {}
            results["server"] = server_language
            results["clients"] = clients
            results["domain"] = domain
            results["base_proto_path"] = base_proto_path
            if code_base is None:
                tmp_code_base = ask_user_question(questions=[code_base_q(server_language)])
                results["code_base_path"] = tmp_code_base.get('code_base_path')
            else:
                results["code_base_path"] = code_base

            
        if path is None:
            try:
                root = os.getcwd()
                result_path = inquirer.prompt(
                    [
                        inquirer.Path(
                            "root_dir",
                            default=join_path(root, project_name),
                            message="Enter a root dir path",
                            exists=False,
                        )
                    ],
                    theme=SylkTheme(),
                )
                if result_path is not None:
                    result_path = result_path["root_dir"]
            except Exception:
                print_error(f"Error root dir exists\n[{join_path(root,project_name)}]")
                exit(1)
        else:
            if path == ".":
                path = os.getcwd()
                result_path = join_path(path)
            else:
                result_path = join_path(path, project_name)

        clients = []
        for k in results:
            if k == "server":
                if type(results[k]) == str:
                    server_language = results[k]
                else:
                    server_language = SylkServer_pb2.SylkServerLanguages.Name(
                        results[k]
                    )
                print_info(f"Server language: {server_language}")
            if k == "clients":
                for c in results[k]:
                    if type(c) == str:
                        client_lang = c
                    else:
                        client_lang = SylkClient_pb2.SylkClientLanguages.Name(c)
                    out_dir = join_path(result_path, results.get("code_base_path") if results.get("code_base_path") is not None else '', "clients", client_lang)
                    print_info(f"Adding client: {client_lang}\n\t-> {out_dir}")
                    clients.append({"out_dir": out_dir, "language": client_lang})
            if k == "domain":
                domain_name = results[k]
                print_info(f"Project domain: {domain_name}\n")

        out_dir = join_path(
            result_path,
            results.get("code_base_path") if results.get("code_base_path") is not None else '',
            "clients",
            results["server"]
            if type(results["server"]) == str
            else SylkClient_pb2.SylkClientLanguages.Name(results["server"]),
        )
        if (
            next(
                (
                    c
                    for c in clients
                    if c.get("language")
                    == (
                        results["server"]
                        if type(results["server"]) == str
                        else SylkServer_pb2.SylkServerLanguages.Name(results["server"])
                    )
                ),
                None,
            )
            is None
        ):
            print_warning(
                "Auto-Adding client {} - Any project by default is assigned with client in the server specified language !".format(
                    SylkServer_pb2.SylkServerLanguages.Name(results["server"])
                    if type(results["server"]) != str
                    else results["server"]
                )
            )
            clients.append(
                {
                    "out_dir": out_dir,
                    "language": SylkClient_pb2.SylkClientLanguages.Name(
                        results["server"]
                    )
                    if type(results["server"]) != str
                    else results["server"],
                }
            )
        root_dir = result_path
        sylk_json_path = join_path(root_dir, "sylk.json")
        mkdir(result_path)

        ARCHITECT = SylkArchitect(
            path=sylk_json_path, domain=domain_name, project_name=project_name
        )
        ARCHITECT.SetConfig({"host": host, "port": int(port), "protoBasePath": results["base_proto_path"], "codeBasePath": results["code_base_path"]})
        ARCHITECT.SetDomain(domain_name)
        if template != "@sylk/Blank" and template is not None:
            print_info("Starting sylk build project from template:")
            print_info(f'Creating new sylk.build project "{project_name}" [{template}]')
            attach_template(ARCHITECT, template)
            print_success(
                f'Success !\n\tCreated new project "{project_name}" from [{template}] template\n\t-> cd {root_dir}\n\t-> And then continue developing your awesome services !\n\t-> For more info on how to use the sylk.build CLI go to https://docs.sylk.build/'
            )
            # ARCHITECT = SylkArchitect(
            # path=sylk_json_path, domain=domain_name, project_name=project_name)
            # ARCHITECT.AddProject(server_language=server_language, clients=clients)
            # ARCHITECT.AddProject(server_language=server_language, clients=clients)
            # ARCHITECT.SetDomain(domain_name)
            exit(1)

        
        ARCHITECT.AddProject(server_language=server_language, clients=clients)
        ARCHITECT.SetSylkVersion()
        ARCHITECT.Save()

        print_success(
            f'🚀 Success !\n\tCreated new project "{project_name}"\n\t-> cd {root_dir}\n\t-> And then continue developing your awesome services !\n\t-> For more info on how to use the sylk.build CLI go to https://docs.sylk.build/'
        )


def attach_template(ARCHITECT: SylkArchitect, template: _TEMPLATES):
    if template != "@sylk/Blank" and template is not None:
        file_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
        template_domain_name = template.split("/")[0].split("@")[-1]
        template_name = template.split("/")[-1]
        print(
            file_dir
            + "/commons/templates/{0}/{1}.template.py".format(
                template_domain_name, template_name
            )
        )
        # print(file_system.get_current_location())
        os.chdir(ARCHITECT._path.split("sylk.json")[0])
        # print(file_system.get_current_location())
        proto_path = ARCHITECT._sylk.sylkJson.get('configs',{}).get('protoBasePath')
        code_path = ARCHITECT._sylk.sylkJson.get('configs',{}).get('codeBasePath')
        optionals = []
        if proto_path is not None:
            optionals.append('--proto-path')
            optionals.append(proto_path)
        if code_path is not None:
            optionals.append('--code-base')
            optionals.append(code_path)
        process= [
                "python",
                file_dir
                + "/commons/templates/{0}/{1}.template.py".format(
                    template_domain_name, template_name
                ),
                "--project-name",
                ARCHITECT._project_name,
            ] + optionals
        subprocess.run(
            process
        )
