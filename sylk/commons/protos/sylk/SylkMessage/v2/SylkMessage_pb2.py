# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/SylkMessage/v2/SylkMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from sylk.commons.protos.sylk.SylkCommons.v1 import SylkCommons_pb2 as sylk_dot_SylkCommons_dot_v1_dot_SylkCommons__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from sylk.commons.protos.sylk.SylkField.v1 import SylkField_pb2 as sylk_dot_SylkField_dot_v1_dot_SylkField__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%sylk/SylkMessage/v2/SylkMessage.proto\x12\x13sylk.SylkMessage.v2\x1a\x19google/protobuf/any.proto\x1a%sylk/SylkCommons/v1/SylkCommons.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a!sylk/SylkField/v1/SylkField.proto\"\x9d\x03\n\x0bSylkMessage\x12;\n\x0e\x65xtension_type\x18\t \x01(\x0e\x32#.sylk.SylkCommons.v1.SylkExtensions\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x44\n\nextensions\x18\x08 \x03(\x0b\x32\x30.sylk.SylkMessage.v2.SylkMessage.ExtensionsEntry\x12\x11\n\tfull_name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0c\n\x04kind\x18\x07 \x01(\t\x12,\n\x06\x66ields\x18\x05 \x03(\x0b\x32\x1c.sylk.SylkField.v1.SylkField\x12\x0b\n\x03tag\x18\n \x01(\t\x12%\n\x07inlines\x18\x0b \x03(\x0b\x32\x14.google.protobuf.Any\x1aJ\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct:\x02\x38\x01\"\xb3\x01\n\x12SylkMessageDisplay\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x07message\x18\x01 \x01(\x0b\x32 .sylk.SylkMessage.v2.SylkMessage\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\n\n\x02id\x18\x04 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylk.SylkMessage.v2.SylkMessage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYLKMESSAGE_EXTENSIONSENTRY._options = None
  _SYLKMESSAGE_EXTENSIONSENTRY._serialized_options = b'8\001'
  _globals['_SYLKMESSAGE']._serialized_start=227
  _globals['_SYLKMESSAGE']._serialized_end=640
  _globals['_SYLKMESSAGE_EXTENSIONSENTRY']._serialized_start=566
  _globals['_SYLKMESSAGE_EXTENSIONSENTRY']._serialized_end=640
  _globals['_SYLKMESSAGEDISPLAY']._serialized_start=643
  _globals['_SYLKMESSAGEDISPLAY']._serialized_end=822
# @@protoc_insertion_point(module_scope)
