# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/io/pagination.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18sylk/io/pagination.proto\x12\x07Sylk.build\":\n\x11PaginationRequest\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\"-\n\x12PaginationResponse\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\tB;Z9github.com/sylk-build/sylk-io/types/pagination;paginationb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Sylk.build.pagination_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z9github.com/sylk-build/sylk-io/types/pagination;pagination'
  _globals['_PAGINATIONREQUEST']._serialized_start=37
  _globals['_PAGINATIONREQUEST']._serialized_end=95
  _globals['_PAGINATIONRESPONSE']._serialized_start=97
  _globals['_PAGINATIONRESPONSE']._serialized_end=142
# @@protoc_insertion_point(module_scope)
