# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SylkService.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor

from typing import overload, Iterator, List, Dict
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import SylkMethod_pb2 as SylkMethod__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11SylkService.proto\x12\x13sylk.SylkService.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x10SylkMethod.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xb7\x02\n\x0bSylkService\x12\x14\n\x0c\x64\x65pendencies\x18\x07 \x03(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x11\n\tfull_name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x06 \x01(\t\x12/\n\x07methods\x18\x05 \x03(\x0b\x32\x1e.sylk.SylkMethod.v1.SylkMethod\x12\x44\n\nextensions\x18\x08 \x03(\x0b\x32\x30.sylk.SylkService.v1.SylkService.ExtensionsEntry\x1aJ\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct:\x02\x38\x01\"\xa7\x01\n\x12SylkServiceDisplay\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\x07service\x18\x01 \x01(\x0b\x32 .sylk.SylkService.v1.SylkService\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestampb\x06proto3')



_SYLKSERVICE = DESCRIPTOR.message_types_by_name['SylkService']
_SYLKSERVICE_EXTENSIONSENTRY = _SYLKSERVICE.nested_types_by_name['ExtensionsEntry']
_SYLKSERVICEDISPLAY = DESCRIPTOR.message_types_by_name['SylkServiceDisplay']

@overload
class SylkService(_message.Message):
	"""sylk.build generated message [sylk.SylkService.v1.SylkService]
	A class respresent a SylkService type
	
		"""
	dependencies = List[str] # type: List[str]
	description = str # type: str
	uri = str # type: str
	name = str # type: str
	full_name = str # type: str
	type = str # type: str
	methods = List[SylkMethod__pb2.SylkMethod] # type: List[SylkMethod__pb2.SylkMethod]
	extensions = Dict[str,google_dot_protobuf_dot_struct__pb2.Struct] # type: Dict[str,google_dot_protobuf_dot_struct__pb2.Struct]

	def __init__(self, dependencies=List[str], description=str, uri=str, name=str, full_name=str, type=str, methods=List[SylkMethod__pb2.SylkMethod], extensions=Dict[str,google_dot_protobuf_dot_struct__pb2.Struct]):
		"""
		

		Attributes:
		----------
		dependencies : List[str]
			
		description : str
			
		uri : str
			
		name : str
			
		full_name : str
			
		type : str
			
		methods : List[SylkMethod__pb2.SylkMethod]
			
		extensions : Dict[str,google_dot_protobuf_dot_struct__pb2.Struct]
			
		"""
		pass
SylkService = _reflection.GeneratedProtocolMessageType('SylkService', (_message.Message,), {

  'ExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SYLKSERVICE_EXTENSIONSENTRY,
    '__module__' : 'SylkService_pb2'
    # @@protoc_insertion_point(class_scope:sylk.SylkService.v1.SylkService.ExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _SYLKSERVICE,
  '__module__' : 'SylkService_pb2'
  # @@protoc_insertion_point(class_scope:sylk.SylkService.v1.SylkService)
  })
_sym_db.RegisterMessage(SylkService)
_sym_db.RegisterMessage(SylkService.ExtensionsEntry)


@overload
class SylkServiceDisplay(_message.Message):
	"""sylk.build generated message [sylk.SylkService.v1.SylkServiceDisplay]
	A class respresent a SylkServiceDisplay type
	
		"""
	updated_at = google_dot_protobuf_dot_timestamp__pb2.Timestamp # type: google_dot_protobuf_dot_timestamp__pb2.Timestamp
	service = SylkService # type: SylkService
	created_at = google_dot_protobuf_dot_timestamp__pb2.Timestamp # type: google_dot_protobuf_dot_timestamp__pb2.Timestamp

	def __init__(self, updated_at=google_dot_protobuf_dot_timestamp__pb2.Timestamp, service=SylkService, created_at=google_dot_protobuf_dot_timestamp__pb2.Timestamp):
		"""
		

		Attributes:
		----------
		updated_at : google_dot_protobuf_dot_timestamp__pb2.Timestamp
			
		service : SylkService
			
		created_at : google_dot_protobuf_dot_timestamp__pb2.Timestamp
			
		"""
		pass
SylkServiceDisplay = _reflection.GeneratedProtocolMessageType('SylkServiceDisplay', (_message.Message,), {
  'DESCRIPTOR' : _SYLKSERVICEDISPLAY,
  '__module__' : 'SylkService_pb2'
  # @@protoc_insertion_point(class_scope:sylk.SylkService.v1.SylkServiceDisplay)
  })
_sym_db.RegisterMessage(SylkServiceDisplay)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYLKSERVICE_EXTENSIONSENTRY._options = None
  _SYLKSERVICE_EXTENSIONSENTRY._serialized_options = b'8\001'
  _SYLKSERVICE._serialized_start=124
  _SYLKSERVICE._serialized_end=435
  _SYLKSERVICE_EXTENSIONSENTRY._serialized_start=361
  _SYLKSERVICE_EXTENSIONSENTRY._serialized_end=435
  _SYLKSERVICEDISPLAY._serialized_start=438
  _SYLKSERVICEDISPLAY._serialized_end=605
# @@protoc_insertion_point(module_scope)
