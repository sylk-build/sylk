# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OtherPackage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor

from typing import overload, Iterator, List, Dict
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12OtherPackage.proto\x12\x16webezy.OtherPackage.v1\"#\n\x0cOtherMessage\x12\x13\n\x0bStringField\x18\x01 \x01(\tb\x06proto3')



_OTHERMESSAGE = DESCRIPTOR.message_types_by_name['OtherMessage']

@overload
class OtherMessage:
	"""webezyio generated message [webezy.OtherPackage.v1.OtherMessage]
	A class respresent a OtherMessage type
	"""
	StringField = str # type: str

	def __init__(self, StringField=str):
		pass
OtherMessage = _reflection.GeneratedProtocolMessageType('OtherMessage', (_message.Message,), {
  'DESCRIPTOR' : _OTHERMESSAGE,
  '__module__' : 'OtherPackage_pb2'
  # @@protoc_insertion_point(class_scope:webezy.OtherPackage.v1.OtherMessage)
  })
_sym_db.RegisterMessage(OtherMessage)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OTHERMESSAGE._serialized_start=46
  _OTHERMESSAGE._serialized_end=81
# @@protoc_insertion_point(module_scope)
