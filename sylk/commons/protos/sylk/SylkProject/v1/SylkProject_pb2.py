# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/SylkProject/v1/SylkProject.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from sylk.commons.protos.sylk.SylkUser.v1 import SylkUser_pb2 as sylk_dot_SylkUser_dot_v1_dot_SylkUser__pb2
from sylk.commons.protos.sylk.SylkClient.v1 import SylkClient_pb2 as sylk_dot_SylkClient_dot_v1_dot_SylkClient__pb2
from sylk.commons.protos.sylk.SylkServer.v1 import SylkServer_pb2 as sylk_dot_SylkServer_dot_v1_dot_SylkServer__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%sylk/SylkProject/v1/SylkProject.proto\x12\x13sylk.SylkProject.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1fsylk/SylkUser/v1/SylkUser.proto\x1a#sylk/SylkClient/v1/SylkClient.proto\x1a#sylk/SylkServer/v1/SylkServer.proto\x1a\x19google/protobuf/any.proto\"\x88\x02\n\x0bSylkProject\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x14\n\x0cjava_package\x18\x06 \x01(\t\x12\x12\n\ngo_package\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12/\n\x07\x63lients\x18\x04 \x03(\x0b\x32\x1e.sylk.SylkClient.v1.SylkClient\x12.\n\x06server\x18\x07 \x01(\x0b\x32\x1e.sylk.SylkServer.v1.SylkServer\x12\x14\n\x0cpackage_name\x18\x03 \x01(\t\x12(\n\nextensions\x18\t \x03(\x0b\x32\x14.google.protobuf.Any\"\xa1\x03\n\x12SylkProjectDisplay\x12\r\n\x05owner\x18\x04 \x01(\t\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nnumMethods\x18\x06 \x01(\x05\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x45\n\x07members\x18\x05 \x03(\x0b\x32\x34.sylk.SylkProject.v1.SylkProjectDisplay.MembersEntry\x12\x13\n\x0bnumServices\x18\x07 \x01(\x05\x12\x13\n\x0bnumMessages\x18\t \x01(\x05\x12\x13\n\x0bnumPackages\x18\x08 \x01(\x05\x12\x31\n\x07project\x18\x01 \x01(\x0b\x32 .sylk.SylkProject.v1.SylkProject\x1aO\n\x0cMembersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12.\n\x05value\x18\x02 \x01(\x0e\x32\x1f.sylk.SylkUser.v1.SylkUserRoles:\x02\x38\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylk.SylkProject.v1.SylkProject_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYLKPROJECTDISPLAY_MEMBERSENTRY._options = None
  _SYLKPROJECTDISPLAY_MEMBERSENTRY._serialized_options = b'8\001'
  _globals['_SYLKPROJECT']._serialized_start=230
  _globals['_SYLKPROJECT']._serialized_end=494
  _globals['_SYLKPROJECTDISPLAY']._serialized_start=497
  _globals['_SYLKPROJECTDISPLAY']._serialized_end=914
  _globals['_SYLKPROJECTDISPLAY_MEMBERSENTRY']._serialized_start=835
  _globals['_SYLKPROJECTDISPLAY_MEMBERSENTRY']._serialized_end=914
# @@protoc_insertion_point(module_scope)
