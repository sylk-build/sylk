# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/API/v1/API.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15sylk/API/v1/API.proto\x12\x0bsylk.API.v1\"%\n\x04\x46ile\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\x0c\"2\n\x14GenerateFilesRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0c\n\x04\x66ile\x18\x02 \x01(\t\"I\n\x0e\x43ompileRequest\x12\r\n\x05\x66iles\x18\x01 \x03(\t\x12(\n\x08\x63ompiler\x18\x02 \x03(\x0e\x32\x16.sylk.API.v1.Compilers*:\n\tCompilers\x12\x15\n\x11\x44\x45\x46\x41ULT_COMPILERS\x10\x00\x12\x06\n\x02PY\x10\x01\x12\x06\n\x02GO\x10\x02\x12\x06\n\x02TS\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylk.API.v1.API_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_COMPILERS']._serialized_start=204
  _globals['_COMPILERS']._serialized_end=262
  _globals['_FILE']._serialized_start=38
  _globals['_FILE']._serialized_end=75
  _globals['_GENERATEFILESREQUEST']._serialized_start=77
  _globals['_GENERATEFILESREQUEST']._serialized_end=127
  _globals['_COMPILEREQUEST']._serialized_start=129
  _globals['_COMPILEREQUEST']._serialized_end=202
# @@protoc_insertion_point(module_scope)
