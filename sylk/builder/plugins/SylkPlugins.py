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
import sylk.builder as builder
from sylk.commons import helpers, file_system, pretty
from sylk.commons.errors import SylkValidationError


@builder.hookimpl
def post_build(sylk_json: helpers.SylkJson, sylk_context: helpers.SylkContext):
    pretty.print_info("Post sylk.build build process %s plugin" % (__name__))
    # protos = []
    # for p in sylk_json.packages:
    #     pkg = sylk_json.packages[p]
    #     pkg_name = pkg['name']
    #     protos.append(f'./protos/{pkg_name}.proto')
    # pretty.print_info(sylk_json._config.get('plugins'))
    # protoc_params = ['protoc'] + protos
    # pretty.print_note(protoc_params)
    # process = subprocess.Popen(protoc_params,
    #                     stdout=subprocess.PIPE,
    #                     stderr=subprocess.PIPE)
    # _, stderr = process.communicate()
    # if stderr:
    #     pretty.print_info(stderr.decode('utf-8'))
    return (__name__, "OK")
