# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SylkMethod.proto
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
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10SylkMethod.proto\x12\x12sylk.SylkMethod.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xd8\x02\n\nSylkMethod\x12\x18\n\x10\x63lient_streaming\x18\x07 \x01(\x08\x12\x11\n\tfull_name\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\t \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10server_streaming\x18\x08 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x0c\n\x04kind\x18\n \x01(\t\x12\x42\n\nextensions\x18\x0b \x03(\x0b\x32..sylk.SylkMethod.v1.SylkMethod.ExtensionsEntry\x12\x12\n\ninput_type\x18\x05 \x01(\t\x12\x13\n\x0boutput_type\x18\x06 \x01(\t\x12\x0b\n\x03uri\x18\x01 \x01(\t\x1aJ\n\x0f\x45xtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct:\x02\x38\x01\"\xa3\x01\n\x11SylkMethodDisplay\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12.\n\x06method\x18\x01 \x01(\x0b\x32\x1e.sylk.SylkMethod.v1.SylkMethod\x12.\n\nupdated_at\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestampb\x06proto3')



_SYLKMETHOD = DESCRIPTOR.message_types_by_name['SylkMethod']
_SYLKMETHOD_EXTENSIONSENTRY = _SYLKMETHOD.nested_types_by_name['ExtensionsEntry']
_SYLKMETHODDISPLAY = DESCRIPTOR.message_types_by_name['SylkMethodDisplay']

@overload
class SylkMethod(_message.Message):
	"""sylk.build generated message [sylk.SylkMethod.v1.SylkMethod]
	A class respresent a SylkMethod type
	
		"""
	client_streaming = bool # type: bool
	full_name = str # type: str
	type = str # type: str
	name = str # type: str
	server_streaming = bool # type: bool
	description = str # type: str
	kind = str # type: str
	extensions = Dict[str,google_dot_protobuf_dot_struct__pb2.Struct] # type: Dict[str,google_dot_protobuf_dot_struct__pb2.Struct]
	input_type = str # type: str
	output_type = str # type: str
	uri = str # type: str

	def __init__(self, client_streaming=bool, full_name=str, type=str, name=str, server_streaming=bool, description=str, kind=str, extensions=Dict[str,google_dot_protobuf_dot_struct__pb2.Struct], input_type=str, output_type=str, uri=str):
		"""
		

		Attributes:
		----------
		client_streaming : bool
			
		full_name : str
			
		type : str
			
		name : str
			
		server_streaming : bool
			
		description : str
			
		kind : str
			
		extensions : Dict[str,google_dot_protobuf_dot_struct__pb2.Struct]
			
		input_type : str
			
		output_type : str
			
		uri : str
			
		"""
		pass
SylkMethod = _reflection.GeneratedProtocolMessageType('SylkMethod', (_message.Message,), {

  'ExtensionsEntry' : _reflection.GeneratedProtocolMessageType('ExtensionsEntry', (_message.Message,), {
    'DESCRIPTOR' : _SYLKMETHOD_EXTENSIONSENTRY,
    '__module__' : 'SylkMethod_pb2'
    # @@protoc_insertion_point(class_scope:sylk.SylkMethod.v1.SylkMethod.ExtensionsEntry)
    })
  ,
  'DESCRIPTOR' : _SYLKMETHOD,
  '__module__' : 'SylkMethod_pb2'
  # @@protoc_insertion_point(class_scope:sylk.SylkMethod.v1.SylkMethod)
  })
_sym_db.RegisterMessage(SylkMethod)
_sym_db.RegisterMessage(SylkMethod.ExtensionsEntry)


@overload
class SylkMethodDisplay(_message.Message):
	"""sylk.build generated message [sylk.SylkMethod.v1.SylkMethodDisplay]
	A class respresent a SylkMethodDisplay type
	
		"""
	created_at = google_dot_protobuf_dot_timestamp__pb2.Timestamp # type: google_dot_protobuf_dot_timestamp__pb2.Timestamp
	method = SylkMethod # type: SylkMethod
	updated_at = google_dot_protobuf_dot_timestamp__pb2.Timestamp # type: google_dot_protobuf_dot_timestamp__pb2.Timestamp

	def __init__(self, created_at=google_dot_protobuf_dot_timestamp__pb2.Timestamp, method=SylkMethod, updated_at=google_dot_protobuf_dot_timestamp__pb2.Timestamp):
		"""
		

		Attributes:
		----------
		created_at : google_dot_protobuf_dot_timestamp__pb2.Timestamp
			
		method : SylkMethod
			
		updated_at : google_dot_protobuf_dot_timestamp__pb2.Timestamp
			
		"""
		pass
SylkMethodDisplay = _reflection.GeneratedProtocolMessageType('SylkMethodDisplay', (_message.Message,), {
  'DESCRIPTOR' : _SYLKMETHODDISPLAY,
  '__module__' : 'SylkMethod_pb2'
  # @@protoc_insertion_point(class_scope:sylk.SylkMethod.v1.SylkMethodDisplay)
  })
_sym_db.RegisterMessage(SylkMethodDisplay)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYLKMETHOD_EXTENSIONSENTRY._options = None
  _SYLKMETHOD_EXTENSIONSENTRY._serialized_options = b'8\001'
  _SYLKMETHOD._serialized_start=104
  _SYLKMETHOD._serialized_end=448
  _SYLKMETHOD_EXTENSIONSENTRY._serialized_start=374
  _SYLKMETHOD_EXTENSIONSENTRY._serialized_end=448
  _SYLKMETHODDISPLAY._serialized_start=451
  _SYLKMETHODDISPLAY._serialized_end=614
# @@protoc_insertion_point(module_scope)