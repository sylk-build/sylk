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

from importlib import import_module,util
from pathlib import Path
from sylk.cli import prompter
from sylk import __version__

from sylk.commons import helpers as _helpers, file_system as _fs, pretty as _pretty
from sylk.commons.protos import sylkcore
import ast
from sylk.commons.helpers import Graph, MessageToDict,MessageToJson, is_semver_less, read_to_parse_protos

from sylk.commons.protos.sylk.SylkApi.v1.SylkApi_pb2 import GetAccessTokenRequest, GetProjectRequest, ListPackagesRequest, ListProjectsRequest, ListServicesRequest
from sylk.commons.protos.sylk.SylkConfigs.v1.SylkConfigs_pb2 import SylkProjectConfigs
from sylk.commons.protos.sylk.SylkOrganization.v1.SylkOrganization_pb2 import SylkOrganization
from sylk.commons.protos.sylk.Sylk.v1.Sylk_pb2 import SylkJson
from datetime import datetime

from sylk.tools.sylkprotoc import sylkprotoc, API as protocAPI

def validation_sylk_token(answers, current):
    if current[:5] != 'sylk_':
      raise prompter.inquirer_errors.ValidationError('', reason='Token is not valid')
    return True

class SylkCloud:

    def __init__(self,token=None,org_id=None,SylkJson=_helpers.SylkJson) -> None:
        self._token = token
        self.sylkJson = SylkJson
        self._org_id = org_id
        self._sylk_cloud = sylkcore('api.sylk.build',80)
        # Check if configs have valid token
        self.set_token()
        # Check if organization has orgId field
        self.set_org_id()
    
    def _validate_token(self):
        _pretty.print_note(f'🔑 Validating token: {self._token[0:5]}[REDACTED]')
        res, call = self._sylk_cloud.GetAccessToken_WithCall(GetAccessTokenRequest(token=self._token))
        for key, value in call.trailing_metadata():
            _pretty.print_note('cloud client received trailing metadata: key=%s value=%s' %
              (key, value))
        if res.result.expires_at.ToDatetime() <= datetime.now():
            _pretty.print_error('Token is expired!')
            exit(1)
        elif res.result.org_id != self._org_id and self._org_id is not None:
            _pretty.print_error(f'Token is not valid for organization ID: "{self._org_id}"')
            exit(1)
        else:
            self._org_id = res.result.org_id
            _pretty.print_success('🔓 Passed token validation')
            return True
        

    def set_org_id(self):
        if self._org_id is None:
            orgId = prompter.ask_user_question(questions=[prompter.QText('orgId','Enter organization ID')])
            if orgId is not None:
                self._org_id = orgId['orgId']

    def set_token(self):
        if self._token is None or self._token[:5] != 'sylk_':
            _pretty.print_info('Couldn\'t find any global sylk.build token...')
            token = prompter.ask_user_question(questions=[prompter.QPass('token','Enter your cloud token',validate=validation_sylk_token)])
            if token is not None:
                self._token = token['token']
                self._validate_token()
                p = Path(__file__).parents[2]
                config_file = _fs.rFile(_fs.join_path(p,'config.py'))
                for i, j in enumerate(config_file):
                    if 'token=' in j:
                        config_file[i] = '    ' + config_file[i].strip()[:6] + f'"{self._token}",\n'
                    _fs.wFile(_fs.join_path(p,'config.py'),content=''.join(config_file),overwrite=True)
            else:
                _pretty.print_info('Generate cloud tokens to remotly interacte with your sylk.build projects\n\t- See more information on https://docs.sylk.build/')
        else:
            self._validate_token()

    def pull_project(self,project_id=None,overwrite=False):
        projectId = project_id if project_id is not None else self._org_id+'.'+self.sylkJson.project.get('packageName')
        try:
            _md = (('sylk-build-token',self._token),)

            org_id = projectId.split('.')[0]

            # org = self._sylk_cloud.GetOrganization(request=GetOrganizationRequest(
            #     org_id=org_id,
            # ),metadata=_md)

            project = self._sylk_cloud.GetProject(
                request=GetProjectRequest(
                    project=projectId
                ),
                metadata=_md
            )
            # org = self._sylk_cloud.GetOrganization(
            #     request=GetOrganizationRequest(
            #         org_id=projectId.split('.')[0]
            #     ),
            #     metadata=(('sylk-build-token',self._token),)
            # )

            packages = {}
            services = {}

            pkgs = self._sylk_cloud.ListPackages(
                ListPackagesRequest(
                    project_id=projectId
                ),
                _md
            )

            for p in pkgs:
                domain = p.result.package.package.split('.')[0]
                p_ver = p.result.package.package.split('.')[-1]
                packages[f'protos/{domain}/{p.result.package.name}/{p_ver}/{p.result.package.name}.proto'] = p.result.package

            svcs = self._sylk_cloud.ListServices(
                ListServicesRequest(
                    project_id=projectId
                ),
                _md
            )

            for s in svcs:
                domain = s.result.service.full_name.split('.')[0]
                s_ver = s.result.service.full_name.split('.')[2]
                services[f'protos/{domain}/{s.result.service.name}/{s_ver}/{s.result.service.name}.proto'] = s.result.service

            sylk_org = SylkOrganization(
                domain="sylk",
                orgId=org_id
            )
            project.result.project.uri = _fs.get_current_location()

            sylk = SylkJson(
                organization=sylk_org,
                project=project.result.project,
                packages=packages,
                services=services,
                configs=SylkProjectConfigs(
                    host='localhost',
                    port=48800
                ),
                sylk_version=__version__.__version__
            )

            resources = []
            sylkDict = MessageToDict(sylk)
            for pkg in sylkDict['packages']:
                resources.append(sylkDict['packages'][pkg])
                try:
                    sort_topological = Graph(sylkDict['packages'][pkg]['messages']).topologicalSort()
                    temp_messages = []
                    for m in sort_topological[::-1]:
                        temp_messages.append(next((tmpM for tmpM in sylkDict['packages'][pkg]['messages'] if tmpM.get('fullName') == m),None))
                    sylkDict['packages'][pkg]['messages'] = temp_messages
                except KeyError as e:
                    _pretty.print_warning("Error while sorting the dependencies graph of package messages\n\t- If this error appeared right after making rename of message then ignore it...\n\t- Else please issue a bug report !")
                
            
            if overwrite:
                _fs.wFile('sylk.json',sylkDict,True,True)
            return sylk
        except Exception as e:
            _pretty.print_error(e.details(),True,f'Error occured during pulling project {projectId}')
            exit(1)

        
    def get_project(self):

        projects = self._sylk_cloud.GetProject(
            request=GetProjectRequest(project=self._org_id),
            metadata=(('sylk-build-token',self._token),)
        )
        for p in projects:
            print(p.result)
        

    def listProjects(self):
        return self._sylk_cloud.ListProjects(ListProjectsRequest(org_id=self._org_id),(('sylk-build-token',self._token),))

    def buildProject(self):
        
        if is_semver_less(self.sylkJson.sylk_version,"1.0.0"):
            _pretty.print_error("current project built with {} sylk cli version, build remote project is will be supported only later versions".format(self.sylkJson.sylk_version)) 
            exit(1)
            
        _pretty.print_info("connecting to sylk-protoc...")
        _sylk_protoc = sylkprotoc()
        protos_files = []
        for p in self.sylkJson.packages:
            protos_files.append('./'+p)
        for s in self.sylkJson.services:
            protos_files.append('./'+s)
        protos = read_to_parse_protos(protos_files)
        files = []
        # Process the results
        for file_path, file_contents in protos.items():
            _pretty.print_info(f'generating Code File -> {file_path}')
            file_name = '/'.join(file_path.split('/')[2:])
            files.append(protocAPI.GenerateFilesRequest(code=file_contents,file=file_name))

        _sylk_protoc.CodeGenerate(iter(files))
        code = _sylk_protoc.Compile(protocAPI.CompileRequest(files=protos))
        for c in code:
            _pretty.print_info('writing compiled proto file: {}'.format(c.path))
            _fs.wFile('services/protos/'+c.path,c.content,True,True)
