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
from sylk.builder.src.main import SylkBuilder
from sylk.cli import prompter
from sylk.commons import proto_comparison
from sylk.commons.config import parse_project_config
from sylk.commons.pretty import print_error, print_note, print_success, print_warning
def build_all(path:str, pass_all: bool= False):
    st = time()
    prj_configs = parse_project_config(path,proto=True)
    sylkBuilder = SylkBuilder(path=path,configs=prj_configs)
    sylkBuilder.BuildAll()
    et = time()
    rt = et - st
    print_success('Sylk build finished succesfully')
    print_note(f'Build time: {rt:.3f}s')

class Framework:
    GRPC = "GRPC"
    SYLK_JS = "SYLK_JS"

def build_code(path:str, framework:Framework=Framework.GRPC, pass_all: bool= False):
    print_note(framework)
    if not hasattr(Framework, framework):
        raise ValueError(f"Invalid framework. Choose from: {[attr for attr in dir(Framework) if not callable(getattr(Framework, attr)) and not attr.startswith('__')]}")
    prj_configs = parse_project_config(path,proto=True)
    sylkBuilder = SylkBuilder(path=path,configs=prj_configs)
    sylkBuilder.BuildOnlyCode()

def build_protos(path:str, pass_all: bool= False):
    prj_configs = parse_project_config(path,proto=True)
    sylkBuilder = SylkBuilder(path=path,configs=prj_configs)
    sylkBuilder.BuildOnlyProtos()