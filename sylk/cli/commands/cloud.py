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
from sylk.builder.src.main import SylkBuilder
from sylk.cli import prompter
from sylk.cli.theme import SylkTheme
from sylk.commons import client_wrapper , helpers as _helpers, file_system as _fs, pretty as _pretty
from sylk.commons.protos import sylkcore
import ast
from sylk.commons.helpers import MessageToDict

from sylk.commons.protos.SylkApi_pb2 import GetAccessTokenRequest, GetOrganizationRequest, GetProjectRequest, ListPackagesRequest, ListProjectsRequest, ListServicesRequest
from sylk.commons.protos.SylkConfigs_pb2 import SylkCliConfigs, SylkProjectConfigs
from sylk.commons.protos.SylkOrganization_pb2 import SylkOrganization
from sylk.commons.protos.Sylk_pb2 import SylkJson
# import astor
from datetime import datetime

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
        _pretty.print_note(f'Validating token: {self._token[0:5]}[REDACTED]')
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
            _pretty.print_success('Passed token validation')
            return True
        

    def set_org_id(self):
        if self._org_id is None:
            orgId = prompter.ask_user_question(questions=[prompter.QText('orgId','Enter organization ID')])
            if orgId is not None:
                self._org_id = orgId['orgId']

    def set_token(self):
        if self._token is None or self._token[:5] != 'sylk_':
            _pretty.print_info('Couldn\'t find any global sylk.build token...')
            token = prompter.ask_user_question(questions=[prompter.QText('token','Enter your cloud token',validate=validation_sylk_token)])
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
            project = self._sylk_cloud.GetProject(
                request=GetProjectRequest(
                    project=projectId
                ),
                metadata=(('sylk-build-token',self._token),)
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
                (('sylk-build-token',self._token),)
            )

            for p in pkgs:
                packages[f'protos/v1/{p.result.package.name}.proto'] = p.result.package

            svcs = self._sylk_cloud.ListServices(
                ListServicesRequest(
                    project_id=projectId
                ),
                (('sylk-build-token',self._token),)
            )

            for s in svcs:
                services[s.result.service.name] = s.result.service

            sylk = SylkJson(
                organization=SylkOrganization(orgId=projectId.split('.')[0]),
                project=project.result.project,
                packages=packages,
                services=services,
                configs=SylkProjectConfigs(
                    host='localhost',
                    port=48800
                )
            )
            if overwrite:
                _fs.wFile('sylk.json',MessageToDict(sylk),True,True)
            # _pretty.print_info(sylk,True,'Project')
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
