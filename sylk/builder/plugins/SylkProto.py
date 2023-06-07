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
import subprocess
import sys
import sylk.builder as builder
from sylk.commons import helpers, file_system
from sylk.commons.pretty import print_error, print_info, print_note
import pkg_resources
from grpc_tools import _protoc_compiler
log = logging.getLogger('sylk.cli.main')

@builder.hookimpl
def pre_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    if file_system.check_if_dir_exists(file_system.join_path(sylk_json.path, 'protos')):
        print_info("🔌 Starting sylk build process %s plugin" % (__name__))
    else:
        file_system.mkdir(file_system.join_path(sylk_json.path, 'protos'))
    return (__name__,'OK')


@builder.hookimpl
def post_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    # log.debug("Finished sylk build process %s plugin" % (__name__))
    return (__name__,'OK')

def run_protoc(command_arguments):
    command_arguments = [argument.encode() for argument in command_arguments]
    return _protoc_compiler.run_main(command_arguments)

@builder.hookimpl
def compile_protos(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext,pre_data):
    well_known_protos = pkg_resources.resource_filename('grpc_tools', '_proto')
    sylk_protos = pkg_resources.resource_filename('sylk', '_proto')
    commands = []
    include_dirs = ['-I{}'.format(well_known_protos),
        # '-I{}'.format(sylk_json.path+'/protos')
    ]
    if pre_data:
        _hook_name = inspect.stack()[0][3]
        for mini_hooks in pre_data:
            for hook in mini_hooks:
                if __name__ == hook.split(':')[0]:
                    if hook.split(':')[2] is not None and _hook_name == hook.split(':')[1].replace('()',''):
                        
                        if 'include_dirs' in hook.split(':')[2]:
                            if mini_hooks[hook] is not None and len(mini_hooks[hook]) > 0:
                                for d in mini_hooks[hook]:
                                    include_dirs.append('-I{}'.format(d))
                        if 'commands' in hook.split(':')[2]:
                            if mini_hooks[hook] is not None and len(mini_hooks[hook]) > 0:
                                # print_error(mini_hooks[hook])
                                commands = commands + mini_hooks[hook]

    proto_files = []
    for pkg in sylk_json.packages:
        proto_files.append('/'.join(pkg.split('/')[1:]))
    
    for svc in sylk_json.services:
        proto_files.append('/'.join(svc.split('/')[1:]))


    if sylk_json.is_language("python"):
        protoc_params = [c for c in list(map(lambda f: f if '--python' in f or '--grpc_python_out' in f or '--pyi' in f or '-I' in f or '--proto-path' in f else None,commands)) if c is not None]+ include_dirs + proto_files
        print_note(protoc_params)
        run_protoc(protoc_params)
    else:
        protoc_params = ['protoc']+ commands +include_dirs+ proto_files
        # print_note(protoc_params)
        process = subprocess.Popen(protoc_params,
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE)
        _, stderr = process.communicate()
        if stderr:
            print_info(stderr.decode('utf-8'))

    if sylk_json.is_language("go"):
        protoc_params = ['protoc']+ [c for c in list(map(lambda f: f if '--go' in f or '-I' in f or '--proto-path' in f else None,commands)) if c is not None] +include_dirs+ proto_files
        # print_note(protoc_params)
        process = subprocess.Popen(protoc_params,
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE)
        _, stderr = process.communicate()
        if stderr:
            print_info(stderr.decode('utf-8'))
        
@builder.hookimpl
def write_protos(sylk_json: helpers.SylkJson):
    if sylk_json.services is None:
        print_error("Not supporting building project without any services",True,'Build process error')
        exit(1)

    if sylk_json.packages is None:
        print_error("Not supporting building project without any packages",True,'Build process error')
        exit(1)

    for svc in sylk_json.services:
        if sylk_json.services[svc].get('methods') is None:
            print_error(f"Cannot build service [{svc}] proto file with 0 methods!")
            exit(1)

        svc_def = helpers.SylkProto(svc.split('/')[-1].split('.')[0], sylk_json.services[svc].get(
            'dependencies'), sylk_json.services[svc], description=sylk_json.services[svc].get('description'),extensions=sylk_json.services[svc].get('extensions'),sylk_json=sylk_json)
        
        log.debug(f"Writing proto file for service: {svc}")
        file_system.wFile(file_system.join_path(
            sylk_json.path, svc), svc_def.__str__(), True,False,True)

    for pkg in sylk_json.packages:
        pkg_name = sylk_json.packages[pkg].get('name')
        pkg_full_name = package = sylk_json.packages[pkg].get('package')
        if sylk_json.packages[pkg].get('messages') is None:
            print_error(f"Cannot build package [{sylk_json.packages[pkg].get('package')}] proto file with 0 messages!")
            exit(1)
        pkg_def = helpers.SylkProto(pkg_name,
                                  sylk_json.packages[pkg].get('dependencies'),
                                  package=pkg_full_name,
                                  messages=sylk_json.packages[pkg].get(
                                      'messages'),
                                  enums=sylk_json.packages[pkg].get('enums'),
                                  extensions=sylk_json.packages[pkg].get('extensions'),
                                  sylk_json=sylk_json)
        log.debug(f"Writing proto file for package: {pkg_name}")
        file_system.wFile(file_system.join_path(
            sylk_json.path, pkg), pkg_def.__str__(), True,False,True)
