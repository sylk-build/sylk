# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: SylkConfigs.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor

from typing import overload, Iterator, List, Dict
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11SylkConfigs.proto\x12\x13sylk.SylkConfigs.v1\"\x92\x01\n\x13SylkTemplateConfigs\x12\x0f\n\x07include\x18\x03 \x03(\t\x12\x0f\n\x07\x65xclude\x18\x02 \x03(\t\x12\x0c\n\x04name\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x10\n\x08out_path\x18\x06 \x01(\t\x12\x14\n\x0cinclude_code\x18\x01 \x01(\x08\x12\x0e\n\x06\x61uthor\x18\x07 \x01(\t\"\xab\x01\n\x12SylkProjectConfigs\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0c\n\x04host\x18\x01 \x01(\t\x12:\n\x08template\x18\x05 \x01(\x0b\x32(.sylk.SylkConfigs.v1.SylkTemplateConfigs\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\x17\n\x0f\x63urrent_version\x18\x04 \x01(\t\x12\x0f\n\x07plugins\x18\x06 \x03(\t\"y\n\x0eSylkCliConfigs\x12\x16\n\x0esylk_templates\x18\x06 \x03(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12\r\n\x05token\x18\x03 \x01(\t\x12\x11\n\tanalytics\x18\x04 \x01(\x08\x12\x11\n\tfirst_run\x18\x05 \x01(\x08\x12\x0c\n\x04host\x18\x01 \x01(\tb\x06proto3')



_SYLKTEMPLATECONFIGS = DESCRIPTOR.message_types_by_name['SylkTemplateConfigs']
_SYLKPROJECTCONFIGS = DESCRIPTOR.message_types_by_name['SylkProjectConfigs']
_SYLKCLICONFIGS = DESCRIPTOR.message_types_by_name['SylkCliConfigs']

@overload
class SylkTemplateConfigs(_message.Message):
	"""sylk.build generated message [sylk.SylkConfigs.v1.SylkTemplateConfigs]
	A class respresent a SylkTemplateConfigs type
	
		"""
	include = List[str] # type: List[str]
	exclude = List[str] # type: List[str]
	name = str # type: str
	description = str # type: str
	out_path = str # type: str
	include_code = bool # type: bool
	author = str # type: str

	def __init__(self, include=List[str], exclude=List[str], name=str, description=str, out_path=str, include_code=bool, author=str):
		"""
		

		Attributes:
		----------
		include : List[str]
			
		exclude : List[str]
			
		name : str
			
		description : str
			
		out_path : str
			
		include_code : bool
			
		author : str
			
		"""
		pass
SylkTemplateConfigs = _reflection.GeneratedProtocolMessageType('SylkTemplateConfigs', (_message.Message,), {
  'DESCRIPTOR' : _SYLKTEMPLATECONFIGS,
  '__module__' : 'SylkConfigs_pb2'
  # @@protoc_insertion_point(class_scope:sylk.SylkConfigs.v1.SylkTemplateConfigs)
  })
_sym_db.RegisterMessage(SylkTemplateConfigs)


@overload
class SylkProjectConfigs(_message.Message):
	"""sylk.build generated message [sylk.SylkConfigs.v1.SylkProjectConfigs]
	A class respresent a SylkProjectConfigs type
	
		"""
	description = str # type: str
	host = str # type: str
	template = SylkTemplateConfigs # type: SylkTemplateConfigs
	port = int # type: int
	current_version = str # type: str
	plugins = List[str] # type: List[str]

	def __init__(self, description=str, host=str, template=SylkTemplateConfigs, port=int, current_version=str, plugins=List[str]):
		"""
		

		Attributes:
		----------
		description : str
			
		host : str
			
		template : SylkTemplateConfigs
			
		port : int
			
		current_version : str
			
		plugins : List[str]
			
		"""
		pass
SylkProjectConfigs = _reflection.GeneratedProtocolMessageType('SylkProjectConfigs', (_message.Message,), {
  'DESCRIPTOR' : _SYLKPROJECTCONFIGS,
  '__module__' : 'SylkConfigs_pb2'
  # @@protoc_insertion_point(class_scope:sylk.SylkConfigs.v1.SylkProjectConfigs)
  })
_sym_db.RegisterMessage(SylkProjectConfigs)


@overload
class SylkCliConfigs(_message.Message):
	"""sylk.build generated message [sylk.SylkConfigs.v1.SylkCliConfigs]
	A class respresent a SylkCliConfigs type
	
		"""
	sylk_templates = List[str] # type: List[str]
	port = int # type: int
	token = str # type: str
	analytics = bool # type: bool
	first_run = bool # type: bool
	host = str # type: str

	def __init__(self, sylk_templates=List[str], port=int, token=str, analytics=bool, first_run=bool, host=str):
		"""
		

		Attributes:
		----------
		sylk_templates : List[str]
			
		port : int
			
		token : str
			
		analytics : bool
			
		first_run : bool
			
		host : str
			
		"""
		pass
SylkCliConfigs = _reflection.GeneratedProtocolMessageType('SylkCliConfigs', (_message.Message,), {
  'DESCRIPTOR' : _SYLKCLICONFIGS,
  '__module__' : 'SylkConfigs_pb2'
  # @@protoc_insertion_point(class_scope:sylk.SylkConfigs.v1.SylkCliConfigs)
  })
_sym_db.RegisterMessage(SylkCliConfigs)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SYLKTEMPLATECONFIGS._serialized_start=43
  _SYLKTEMPLATECONFIGS._serialized_end=189
  _SYLKPROJECTCONFIGS._serialized_start=192
  _SYLKPROJECTCONFIGS._serialized_end=363
  _SYLKCLICONFIGS._serialized_start=365
  _SYLKCLICONFIGS._serialized_end=486
# @@protoc_insertion_point(module_scope)
