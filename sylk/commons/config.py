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

import importlib
import logging
import sys
from typing import overload
from sylk import config
from sylk.commons import file_system as _fs,helpers as _helpers,pretty as _pretty,config as _config
from sylk.commons.pretty import print_error, print_info, print_note, print_warning
from sylk.commons.protos.sylk.SylkConfigs.v1 import SylkConfigs_pb2 as SylkConfigs
from google.protobuf.json_format import MessageToDict,ParseDict

log = logging.getLogger('sylk.cli.main')

class SylkProjectConfig:

    def __init__(self,**kwargs) -> None:
        """Initalize a custom sylk.build project configurations
        Args
        ----
            
            client_channel_opt (Tuple[Tuple[str,any]])
            custom_templates (List[Tuple(str,str)])
            custom_plugins (List[Tuple(str,str)])
            template - Template options

        """
        self.client_channel_opt = kwargs.get('client_channel_opt')
        self.custom_templates = kwargs.get('custom_templates')
        self.custom_plugins = kwargs.get('custom_plugins')
        self.template = kwargs.get('template')
        self.deployment = kwargs.get('deployment')
        self.monitor = kwargs.get('monitor')
        self.proxy = kwargs.get('proxy')
        self.docs = kwargs.get('docs')
        self.format = kwargs.get('format','json')

    def config(self):
        temp_dict = {}
        if self.client_channel_opt:
            temp_dict['client_channel_opt'] = self.client_channel_opt
        if self.custom_templates:
            temp_dict['custom_templates'] = self.custom_templates
        if self.custom_plugins:
            temp_dict['custom_plugins'] = self.custom_plugins
        if self.template:
            temp_dict['template'] = self.template
        if self.deployment:
            temp_dict['deployment'] = self.deployment
        if self.monitor:
            temp_dict['monitor'] = self.monitor
        if self.proxy:
            temp_dict['proxy'] = self.proxy
        if self.docs:
            temp_dict['docs'] = self.docs
        if self.format:
            temp_dict['format'] = self.format

        return temp_dict


def parse_sylk_config(root_path:str,proto=False):
    if proto:
        sylk_config = SylkConfigs.SylkProjectConfigs()
        sylk_json_configs = parse_sylk_project_json_configs_proto(root_path)
        sylk_config.MergeFrom(sylk_json_configs)
    else:
        sylk_json_configs = parse_sylk_project_json_configs_proto(root_path)
        sylk_config = sylk_json_configs
    return sylk_config


def parse_project_config(root_path:str,proto=False):
    if proto:
        sylk_config = SylkConfigs.SylkCliConfigs()
        global_config = parse_global_config_proto()
        sylk_config.MergeFrom(global_config)
        
        config_file = parse_config_file_proto(root_path)

        if config_file is not None:
            sylk_config.MergeFrom(config_file)
        sylk_json_configs = parse_sylk_json_configs_proto(root_path)

        if sylk_json_configs is not None:
            sylk_config.MergeFrom(sylk_json_configs)

    else:
        global_config = parse_global_config_dict()

        sylk_json_configs = parse_sylk_json_configs(root_path)

        config_file = parse_config_file_dict(root_path)
        sylk_config = None 
        if sys.version_info[0] >= 3 and sys.version_info[1] >= 9:
            if sylk_json_configs is not None:
                sylk_config = global_config | sylk_json_configs

            if sylk_config is None:
                sylk_config = global_config
            if config_file:
                sylk_config = sylk_config | config_file 
        else:

            sylk_config = {**global_config, **sylk_json_configs } 
            # print_note(sylk_config,True,'sylk_config.py')

            if config_file is not None:
                sylk_config = {**sylk_config, **config_file }
    # print_note(merged_configs,True,'Merged Config')
    return sylk_config

def parse_sylk_json_configs(root_path):
    sylk_json_path = _fs.join_path(root_path,'sylk.json')
    SYLK_JSON = None
    if _fs.check_if_file_exists(sylk_json_path):
        SYLK_JSON = _fs.rFile(sylk_json_path, json=True)
        SYLK_JSON = _helpers.SylkJson(sylk_json=SYLK_JSON)
    return SYLK_JSON._config if SYLK_JSON is not None else None


def parse_sylk_project_json_configs_proto(root_path):
    SYLK_JSON = None
    if _fs.check_if_file_exists(root_path):
        if 'sylk.json' not in root_path:
            root_path = root_path +'/sylk.json'
        print_note(f'Loading sylk.build project from: {root_path}')

        SYLK_JSON = _fs.rFile(root_path, json=True)
        SYLK_JSON = _helpers.SylkJson(sylk_json=SYLK_JSON)
        if SYLK_JSON._config:
            return ParseDict(SYLK_JSON._config,SylkConfigs.SylkProjectConfigs())
        else:
            return None

def parse_sylk_json_configs_proto(root_path):
    SYLK_JSON = None
    if 'sylk.json' not in root_path:
        root_path = root_path +'/sylk.json'
    if _fs.check_if_file_exists(root_path):
        print_note(f'Loading sylk.build project from: {root_path}')

        SYLK_JSON = _fs.rFile(root_path, json=True)
        SYLK_JSON = _helpers.SylkJson(sylk_json=SYLK_JSON)
        if SYLK_JSON._config:
            if SYLK_JSON._config.get('template') is not None:
                del SYLK_JSON._config['template']
            return ParseDict(SYLK_JSON._config,SylkConfigs.SylkCliConfigs())
        else:
            return None

def parse_config_file_proto(root_path) -> SylkConfigs.SylkCliConfigs:
    custom_config_path = _fs.join_path(root_path,'config.py')
    sylk_prj_conf = None
    if _fs.check_if_file_exists(custom_config_path):
        if _fs.get_current_location() not in sys.path:
            sys.path.append(_fs.get_current_location())
        
        prj_conf_module = importlib.import_module('config')
        if hasattr(prj_conf_module,'configs'):
            sylk_prj_conf = get_file_config(prj_conf_module)
        else:
            print_warning('You must configure the parameters under \'configs = SylkConfigs.SylkCliConfigs()\' variable')
       
    else:
        log.debug("No custom project config.py file")
    return sylk_prj_conf

def parse_config_file_dict(root_path):
    custom_config_path = _fs.join_path(root_path,'config.py')
    sylk_prj_conf = None
    if _fs.check_if_file_exists(custom_config_path):
        
        if _fs.get_current_location() not in sys.path:
            sys.path.append(_fs.get_current_location())
        
        prj_conf_module = importlib.import_module('config')
        if hasattr(prj_conf_module,'configs'):
            temp_configs = get_file_config(prj_conf_module)
            sylk_prj_conf = SylkProjectConfig(
                # Client channel options see:  https://github.com/grpc/grpc/blob/v1.46.x/include/grpc/impl/codegen/grpc_types.h
                client_channel_opt = prj_conf_module.client_channel_opt  if hasattr(prj_conf_module,'client_channel_opt') else None,
                # Custom templates
                custom_templates = prj_conf_module.custom_templates  if hasattr(prj_conf_module,'custom_templates') else None,
                # Custom plugins
                custom_plugins = prj_conf_module.custom_plugins  if hasattr(prj_conf_module,'custom_plugins') else None,
                # Templating options
                template = prj_conf_module.template if hasattr(prj_conf_module,'template') else None,
                deployment = temp_configs.deployment,
                monitor = MessageToDict(temp_configs.monitor),
                proxy =  MessageToDict(temp_configs.proxy),
                host = temp_configs.host,
                plugins = temp_configs.plugins,
                docs = temp_configs.docs,
                format = temp_configs.format

            )
        else:
            print_warning('You must configure the parameters under \'configs = SylkConfig.Config()\' variable')
       

    else:
        log.debug("No custom project config.py file")
    return None if sylk_prj_conf is None else sylk_prj_conf.config()

def parse_global_config_dict() :
    global_config_path = dict_from_module(_config.config.configs)
    return global_config_path

def parse_global_config_proto():
    # temp_module = dict_from_module(_config)
    if hasattr(config,'configs'):
        return config.configs
    else:
        print_error('Global configs are not valid !')
    # if temp_module.get('Sylkio_templates'):
    #     temp_Sylki_templates = temp_module['Sylkio_templates']
    #     del temp_module['Sylkio_templates']
    # global_config_path:Config = ParseDict(temp_module,Config)
    # global_config_path.Sylkio_templates = temp_Sylki_templates
    # print(global_config_path.host)
    # temp_config = Config(
    #     # host=global_config_path.host,
    #     # port=global_config_path.port,
    #     docs=global_config_path.docs,
    #     deployment=global_config_path.deployment,
    #     proxy=global_config_path.proxy,
    #     monitor=global_config_path.monitor,
    #     Sylkio_templates=global_config_path.Sylkio_templates,
    #     token=global_config_path.token,
    #     analytics=global_config_path.analytics,
    #     first_run=global_config_path.first_run,
    #     template=global_config_path.template
    # )
    # return temp_config


def dict_from_module(module):
    context = {}
    for setting in dir(module):
        # you can write your filter here
        if setting.islower() and setting[0] != '_':
            context[setting] = getattr(module, setting)
    return context

def get_file_config(prj_config_module) -> SylkConfigs.SylkCliConfigs:
    return prj_config_module.configs