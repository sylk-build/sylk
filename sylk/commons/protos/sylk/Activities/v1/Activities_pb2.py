# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/Activities/v1/Activities.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sylk.commons.protos.sylk.ActivityLog.v1 import ActivityLog_pb2 as sylk_dot_ActivityLog_dot_v1_dot_ActivityLog__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#sylk/Activities/v1/Activities.proto\x12\x12sylk.Activities.v1\x1a%sylk/ActivityLog/v1/ActivityLog.proto2\xe1\x01\n\nActivities\x12\x64\n\x10ListActivityLogs\x12,.sylk.ActivityLog.v1.ListActivityLogsRequest\x1a .sylk.ActivityLog.v1.ActivityLog0\x01\x12m\n\x0fGetActivityLogs\x12,.sylk.ActivityLog.v1.ListActivityLogsRequest\x1a,.sylk.ActivityLog.v1.GetActivityLogsResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylk.Activities.v1.Activities_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ACTIVITIES']._serialized_start=99
  _globals['_ACTIVITIES']._serialized_end=324
# @@protoc_insertion_point(module_scope)