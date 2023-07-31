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
clients_languages_q = QCheckbox(
    name="clients",
    message="Choose clients languages (Use arrows keys to enable disable a language)",
    choices=[
        ("Python", SylkClient_pb2.python),
        ("Typescript", SylkClient_pb2.typescript),
        ("Go", SylkClient_pb2.go),
        ("NodeJs", SylkClient_pb2.nodejs),
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

sylk_neq_q = [server_language_q, clients_languages_q, domain_q]


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
    token=None
):
    domain_name = "domain"

    if project_id is not None:

        sylkCloud = SylkCloud(
            token=token if token is not None else configs.token if configs is not None else None,
            org_id=project_id.split(".")[0],
        )

        # If no options passed
        if server_language is None and clients == None and domain is None:
            results = ask_user_question(questions=sylk_neq_q)

            if results is None:
                print_warning("Must answer project creation questions")
                exit(1)
        # If someof the options has passed
        elif server_language is not None or clients is not None or domain is not None:
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

            results = ask_user_question(questions=questions)

            if results is None:
                print_warning("Must answer project creation questions")
                exit(1)
            else:
                if results.get("server") is None:
                    results["server"] = server_language
                if results.get("clients") is None:
                    results["clients"] = clients

        else:
            results = {}
            results["server"] = server_language
            results["clients"] = clients

        project = sylkCloud.pull_project(project_id)
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
        print_info(clients)
        print_info(server_language)
        ARCHITECT.AddProject(
            project_name, project.project.server.language if server_language is None else server_language, project.project.clients if len(clients) == 0 else list(map(lambda c: {"language": c}, clients))
        )
        # ARCHITECT._sylk = project
        ARCHITECT.SetConfig({"host": host, "port": int(port)})
        ARCHITECT.SetSylkVersion()
        ARCHITECT.Save()

        print_success(
            f'Success pulling ☁️  project!\n\tCreated new project "{project_name}"\n\t-> cd {project_path}\n\t-> And then continue developing your awesome services !\n\t-> For more info on how to use the sylk.build CLI go to https://docs.sylk.build/'
        )

    else:
        # If no options passed
        if server_language is None and clients == None and domain is None:
            results = ask_user_question(questions=sylk_neq_q)

            if results is None:
                print_warning("Must answer project creation questions")
                exit(1)
        # If someof the options has passed
        elif server_language is not None or clients is not None or domain is not None:
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

        else:
            results = {}
            results["server"] = server_language
            results["clients"] = clients
            results["domain"] = domain

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
            result_path = join_path(path, project_name)

        clients = []
        for k in results:
            if k == "server":
                if type(results[k]) == str:
                    server_langugae = results[k]
                else:
                    server_langugae = SylkServer_pb2.SylkServerLanguages.Name(
                        results[k]
                    )
                print_info(f"Server language: {server_langugae}")
            if k == "clients":
                for c in results[k]:
                    if type(c) == str:
                        client_lang = c
                    else:
                        client_lang = SylkClient_pb2.SylkClientLanguages.Name(c)
                    out_dir = join_path(result_path, "clients", client_lang)
                    print_info(f"Adding client: {client_lang}\n\t-> {out_dir}")
                    clients.append({"out_dir": out_dir, "language": client_lang})
            if k == "domain":
                domain_name = results[k]
                print_info(f"Project domain: {domain_name}\n")

        out_dir = join_path(
            result_path,
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
        if template != "@sylk/Blank" and template is not None:
            print_info("Starting sylk build project from template:")
            print_info(f'Creating new sylk.build project "{project_name}" [{template}]')
            attach_template(ARCHITECT, template)
            print_success(
                f'Success !\n\tCreated new project "{project_name}" from [{template}] template\n\t-> cd {root_dir}\n\t-> And then continue developing your awesome services !\n\t-> For more info on how to use the sylk.build CLI go to https://docs.sylk.build/'
            )
            # ARCHITECT = SylkArchitect(
            # path=sylk_json_path, domain=domain_name, project_name=project_name)
            # ARCHITECT.AddProject(server_language=server_langugae, clients=clients)
            # ARCHITECT.AddProject(server_language=server_langugae, clients=clients)
            # ARCHITECT.SetDomain(domain_name)
            exit(1)

        ARCHITECT.AddProject(server_language=server_langugae, clients=clients)
        ARCHITECT.SetDomain(domain_name)
        ARCHITECT.SetConfig({"host": host, "port": int(port), "protoBasePath": base_proto_path})
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

        subprocess.run(
            [
                "python",
                file_dir
                + "/commons/templates/{0}/{1}.template.py".format(
                    template_domain_name, template_name
                ),
                "--project-name",
                ARCHITECT._project_name,
            ]
        )
