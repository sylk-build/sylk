# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SylkMessage.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf.internal import enum_type_wrapper

from typing import overload, Iterator, List, Dict
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from . import SylkField_pb2 as SylkField__pb2
from . import SylkCommons_pb2 as SylkCommons__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11SylkMessage.proto\x12\x13sylk.SylkMessage.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x0fSylkField.proto\x1a\x11SylkCommons.proto\"\xe4\x02\n\x0bSylkMessage\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12(\n\x06\x66ields\x18\x03 \x03(\x0b\x32\x18.sylk.SylkField.v1.Field\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x0c\n\x04kind\x18\x05 \x01(\t\x12\x11\n\tfull_name\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x07 \x01(\t\x12\x44\n\nextensions\x18\x08 \x03(\x0b\x32\x30.sylk.SylkMessage.v1.SylkMessage.ExtensionsEntry\x12;\n\x0e\x65xtension_type\x18\t \x01(\x0e\x32#.sylk.SylkCommons.v1.SylkExtensions\x1aI\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\x42\x32Z0github.com/sylk/core/services/protos/SylkMessageb\x06proto3')



_SYLKMESSAGE = DESCRIPTOR.message_types_by_name['SylkMessage']
_SYLKMESSAGE_EXTENSIONSENTRY = _SYLKMESSAGE.nested_types_by_name['ExtensionsEntry']

@overload
class SylkMessage(_message.Message):
	"""webezyio generated message [sylk.SylkMessage.v1.SylkMessage]
	A class respresent a SylkMessage type
	
	"""
	uri = str # type: str
	name = str # type: str
	fields = List[SylkField__pb2.Field] # type: List[SylkField__pb2.Field]
	type = str # type: str
	kind = str # type: str
	full_name = str # type: str
	description = str # type: str
	extensions = Dict[str,google_dot_protobuf_dot_struct__pb2.Value] # type: Dict[str,google_dot_protobuf_dot_struct__pb2.Value]
	extension_type = enum_type_wrapper.EnumTypeWrapper # type: enum_type_wrapper.EnumTypeWrapper

	def __init__(self, uri=str, name=str, fields=List[SylkField__pb2.Field], type=str, kind=str, full_name=str, description=str, extensions=Dict[str,google_dot_protobuf_dot_struct__pb2.Value], extension_type=enum_type_wrapper.EnumTypeWrapper):
		"""
		Attributes:
		----------
		uri : str
			
		name : str
			
		fields : List[SylkField__pb2.Field]
			
		type : str
			
		kind : str
			
		full_name : str
			
		description : str
			
		extensions : Dict[str,google_dot_protobuf_dot_struct__pb2.Value]
			
		extension_type : enum_type_wrapper.EnumTypeWrapper
			
		"""
		pass
SylkMessage = _reflection.GeneratedProtocolMessageType('SylkMessage', (_message.Message,), {

  'ExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SYLKMESSAGE_EXTENSIONSENTRY,
    '__module__' : 'SylkMessage_pb2'
    # @@protoc_insertion_point(class_scope:sylk.SylkMessage.v1.SylkMessage.ExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _SYLKMESSAGE,
  '__module__' : 'SylkMessage_pb2'
  # @@protoc_insertion_point(class_scope:sylk.SylkMessage.v1.SylkMessage)
  })
_sym_db.RegisterMessage(SylkMessage)
_sym_db.RegisterMessage(SylkMessage.ExtensionsEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z0github.com/sylk/core/services/protos/SylkMessage'
  _SYLKMESSAGE_EXTENSIONSENTRY._options = None
  _SYLKMESSAGE_EXTENSIONSENTRY._serialized_options = b'8\001'
  _SYLKMESSAGE._serialized_start=109
  _SYLKMESSAGE._serialized_end=465
  _SYLKMESSAGE_EXTENSIONSENTRY._serialized_start=392
  _SYLKMESSAGE_EXTENSIONSENTRY._serialized_end=465
# @@protoc_insertion_point(module_scope)
