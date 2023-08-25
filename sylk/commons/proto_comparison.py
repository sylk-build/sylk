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

"""
Module for comparing protobuf files.
"""

import os
import hashlib
from sylk.commons import helpers
from sylk.commons.file_system import join_path

CHUNK_SIZE = 64 * 1024  # 64KB

def hash_string(s, algorithm='sha256'):
    """Hash a string using the specified algorithm."""
    data = s.encode('utf-8')
    hasher = hashlib.new(algorithm)
    hasher.update(data)
    return hasher.hexdigest()

def hash_file(file_path, algorithm='sha256'):
    """Return the hash of the given file."""
    hasher = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as f:
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break
            hasher.update(chunk)
    
    return hasher.hexdigest()

def is_different(schema_proto, existing_proto, algorithm='sha256'):
    """
    Check if the content of a file is different from an in-memory string.
    
    Parameters:
    - schema_proto: The protofile content based on schema model (as a string)
    - existing_proto: Path to the file
    - algorithm: Hashing algorithm to use (default is 'sha256')
    
    Returns:
    - True if contents are different, False otherwise
    """
    if os.path.getsize(existing_proto) < CHUNK_SIZE:
        return hash_string(schema_proto, algorithm) != hash_file(existing_proto, algorithm)

    # Convert the schema_proto to bytes for chunked comparison
    schema_bytes = schema_proto.encode('utf-8')
    schema_idx = 0
    with open(existing_proto, 'rb') as f:
        while True:
            file_chunk = f.read(CHUNK_SIZE)
            schema_chunk = schema_bytes[schema_idx:schema_idx + CHUNK_SIZE]
            if not file_chunk and not schema_chunk:
                break

            if hashlib.new(algorithm, file_chunk).digest() != hashlib.new(algorithm, schema_chunk).digest():
                return True

            schema_idx += CHUNK_SIZE

    return False

def compare_proto_files(proto_dir, sylk_json: helpers.SylkJson):
    """
    Recursively compare protobuf files between existing protos directory tree and existing sylk schema.
    
    Parameters:
    - proto_dir: Directory containing the protobuf files
    - sylk_json: The sylk schema object
    
    Returns:
    - List of filenames that are different
    """

    sylk_schema_files = sylk_to_files(sylk_json)
    different_files = []
    new_files = []

    for dirpath, dirnames, filenames in os.walk(proto_dir if proto_dir != '' else os.getcwd()):
        
        for filename in [f for f in filenames if '.proto' in f]:
            # Compute the relative path
            rel_path = os.path.relpath(dirpath, proto_dir)
            # Full paths for proto file and its corresponding snapshot
            proto_file_path = os.path.join(rel_path, filename)
            file_path = os.path.join(sylk_json.path, sylk_json._root_protos, rel_path, filename)
            # Check if the snapshot exists
            if sylk_schema_files.get(proto_file_path) is None:
                new_files.append(proto_file_path)
                continue
            
            # Check if files are different
            if is_different(sylk_schema_files.get(proto_file_path), file_path):
                different_files.append(os.path.join(rel_path, filename))
    return different_files, new_files

def sylk_to_files(sylk_json: helpers.SylkJson):
    files = {}
    # Handle existing schema:
    if sylk_json.packages is not None and len(sylk_json.packages.keys()) > 0:
        for p in sylk_json.packages:
            tmp_pkg = sylk_json.packages[p]
            pkg = sylk_json.get_package(tmp_pkg.get('package'),False)
            tags = {}
            if pkg.services is not None:
                svcs_tags = [
                    s.tag for s in pkg.services if s.tag != ''
                ]
                for t in svcs_tags:
                    if tags.get(t) is None:
                        tags[t] = []
                    tags[t].extend([
                        m.full_name for m in pkg.services if m.tag == t
                    ])
            if pkg.enums is not None:
                enums_tags = [
                    e.tag for e in pkg.enums if e.tag != ''
                ]
                for t in enums_tags:
                    if tags.get(t) is None:
                        tags[t] = []
                    tags[t].extend([
                        m.full_name for m in pkg.enums if m.tag == t
                    ])
            if pkg.messages is not None:
                messages_tags = [
                    m.tag for m in pkg.messages if m.tag != ''
                ]
                for t in messages_tags:
                    if tags.get(t) is None:
                        tags[t] = []
                    tags[t].extend([
                        m.full_name for m in pkg.messages if m.tag == t
                    ])

            if len(tags.keys()) > 0:
                for t in tags:
                    proto = helpers.SylkProtoFile(t,pkg,sylk_json,True)
                    proto._set_file_path()
                    suffix = '/' if sylk_json._root_protos != '' else ''
                    prefix = join_path(sylk_json.path,sylk_json._root_protos)
                    files[proto._file_path.split(prefix+suffix)[1]] = proto.to_str()
                    
                if pkg.services is not None:
                    svcs = [
                        s.full_name for s in pkg.services if s.tag == ''
                    ]
                    
                if pkg.enums is not None:
                    enums = [
                        e.full_name for e in pkg.enums if e.tag == ''
                    ]
                    
                if pkg.messages is not None:
                    msgs = [
                        m.full_name for m in pkg.messages if m.tag == ''
                    ]
                
                if len(enums) > 0 or len(msgs) > 0 or len(svcs) > 0:
                    proto = helpers.SylkProtoFile(pkg.name,pkg,sylk_json)
                    suffix = '/' if sylk_json._root_protos != '' else ''
                    prefix = join_path(sylk_json.path,sylk_json._root_protos)
                    files[proto._file_path.split(prefix+suffix)[1]] = proto.to_str()
                
            else:
                proto = helpers.SylkProtoFile(pkg.name,pkg,sylk_json)
                suffix = '/' if sylk_json._root_protos != '' else ''
                prefix = join_path(sylk_json.path,sylk_json._root_protos)
                files[proto._file_path.split(prefix+suffix)[1]] = proto.to_str()

    return files