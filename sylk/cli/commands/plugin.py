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

from time import time
import os
import shutil
import subprocess
from sylk.architect import SylkArchitect
from sylk.commons import file_system
from sylk.commons.helpers import SylkJson
from sylk.commons.pretty import print_info, print_warning, print_note


def is_module_executable(module_name):
    return shutil.which(module_name) is not None


def run(args):
    st = time()

    path = os.getcwd()
    plugs = []
    includes = ['-I']
    plug_path = ''
    for i in args.I:
        includes.append(i)
    print(includes)
    for p in args.plugin:
        # print(os.access(p, os.X_OK))
        spec = is_module_executable(p)
        if spec:
            plug_name = p.split('protoc-gen-')[1]
            plugs = plugs + [
                f'--{plug_name}_out={args.out_dir}',
                f'--{plug_name}_opt={args.opt}',
            ]
        elif '.py' not in p:
            if args.dir is not None:
                plug_path = args.dir + '/' + p + '.py'
            else:
                plug_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + f'/protoc/plugins/{p}.py'
            plugs = plugs + [
                f'--plugin=protoc-gen-{p}={plug_path}',
                f'--{p}_out={args.out_dir}'
            ]
        else:
            if args.dir is not None:
                plug_path =  os.path.abspath(args.dir + '/' + p + '.py')
            else:
                plug_path = os.path.abspath(os.getcwd() +'/'+ p)
            plug_name = p.split('.')[0]
            plugs = plugs + [
                    f'--plugin=protoc-gen-{plug_name}={plug_path}',
                    f'--{plug_name}_out={args.out_dir}',

            ]
        if file_system.is_file_executable(plug_path) or spec:
            print_info(f"🔌 Running plugin: {p}")

            # if len(args.protos) == 0:
                # sylk = SylkArchitect('./sylk.json')
            proto_files = args.protos if args.protos is not None else []
            protoc_params = ['protoc'] + proto_files + plugs + includes
            print(protoc_params)
            process = subprocess.Popen(protoc_params,
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)
            _, stderr = process.communicate()
            if stderr:
                print_info(stderr.decode('utf-8'))
        else:
            print_warning(f'plugin {p} is not executable file')
            print_info(f'Make sure you have permissions to edit the file mode and make it excutable.')
    et = time()
    rt = et - st
    print_note(f'Plugin time: {rt:.3f}s')
    exit(0)