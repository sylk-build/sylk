# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: WebezyConfig.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper

from typing import overload, Iterator, List, Dict
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import WebezyPrometheus_pb2 as WebezyPrometheus__pb2
from . import WebezyProxy_pb2 as WebezyProxy__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from . import WebezyTemplate_pb2 as WebezyTemplate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12WebezyConfig.proto\x12\x16webezy.WebezyConfig.v1\x1a\x16WebezyPrometheus.proto\x1a\x11WebezyProxy.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x14WebezyTemplate.proto\"Q\n\rWebezyMonitor\x12@\n\nprometheus\x18\x01 \x01(\x0b\x32,.webezy.WebezyPrometheus.v1.PrometheusConfig\"\x98\x04\n\x0cWebezyConfig\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\x05\x12:\n\ndeployment\x18\x03 \x01(\x0e\x32&.webezy.WebezyConfig.v1.DeploymentType\x12\x31\n\x05proxy\x18\x04 \x01(\x0b\x32\".webezy.WebezyProxy.v1.ProxyConfig\x12\x30\n\x04\x64ocs\x18\x05 \x01(\x0b\x32\".webezy.WebezyConfig.v1.WebezyDocs\x12:\n\x08template\x18\x06 \x01(\x0b\x32(.webezy.WebezyTemplate.v1.TemplateConfig\x12\x36\n\x07monitor\x18\x07 \x01(\x0b\x32%.webezy.WebezyConfig.v1.WebezyMonitor\x12\x11\n\tanalytics\x18\x08 \x01(\x08\x12\r\n\x05token\x18\t \x01(\t\x12\x11\n\tfirst_run\x18\n \x01(\x08\x12\x1a\n\x12webezyio_templates\x18\x0b \x03(\t\x12\x44\n\x08\x66\x65\x61tures\x18\x0c \x03(\x0b\x32\x32.webezy.WebezyConfig.v1.WebezyConfig.FeaturesEntry\x12\x0f\n\x07plugins\x18\r \x03(\t\x1a/\n\rFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08:\x02\x38\x01\"\x1a\n\nWebezyDocs\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t*C\n\x0e\x44\x65ploymentType\x12\x1a\n\x16UNKNOWN_DEPLOYMENTTYPE\x10\x00\x12\t\n\x05LOCAL\x10\x01\x12\n\n\x06\x44OCKER\x10\x02\x62\x06proto3')

_DEPLOYMENTTYPE = DESCRIPTOR.enum_types_by_name['DeploymentType']
DeploymentType = enum_type_wrapper.EnumTypeWrapper(_DEPLOYMENTTYPE)
UNKNOWN_DEPLOYMENTTYPE = 0
LOCAL = 1
DOCKER = 2


_WEBEZYMONITOR = DESCRIPTOR.message_types_by_name['WebezyMonitor']
_WEBEZYCONFIG = DESCRIPTOR.message_types_by_name['WebezyConfig']
_WEBEZYCONFIG_FEATURESENTRY = _WEBEZYCONFIG.nested_types_by_name['FeaturesEntry']
_WEBEZYDOCS = DESCRIPTOR.message_types_by_name['WebezyDocs']

@overload
class WebezyMonitor(_message.Message):
	"""webezyio generated message [webezy.WebezyConfig.v1.WebezyMonitor]
	A class respresent a WebezyMonitor type
	WebezyMonitor configurations
		"""
	prometheus = WebezyPrometheus__pb2.PrometheusConfig # type: WebezyPrometheus__pb2.PrometheusConfig

	def __init__(self, prometheus=WebezyPrometheus__pb2.PrometheusConfig):
		"""
		Attributes:
		----------
		prometheus : WebezyPrometheus__pb2.PrometheusConfig
			The prometheus client configurations
		"""
		pass
WebezyMonitor = _reflection.GeneratedProtocolMessageType('WebezyMonitor', (_message.Message,), {
  'DESCRIPTOR' : _WEBEZYMONITOR,
  '__module__' : 'WebezyConfig_pb2'
  # @@protoc_insertion_point(class_scope:webezy.WebezyConfig.v1.WebezyMonitor)
  })
_sym_db.RegisterMessage(WebezyMonitor)

@overload
class WebezyDocs(_message.Message):
	"""webezyio generated message [webezy.WebezyConfig.v1.WebezyDocs]
	A class respresent a WebezyDocs type
	Main configurations for Auto generated docs
		"""
	file = str # type: str

	def __init__(self, file=str):
		"""
		Attributes:
		----------
		file : str
			The main README.md file path should be placed with different path if you want to write custom README.md file 
		"""
		pass
WebezyDocs = _reflection.GeneratedProtocolMessageType('WebezyDocs', (_message.Message,), {
  'DESCRIPTOR' : _WEBEZYDOCS,
  '__module__' : 'WebezyConfig_pb2'
  # @@protoc_insertion_point(class_scope:webezy.WebezyConfig.v1.WebezyDocs)
  })
_sym_db.RegisterMessage(WebezyDocs)


@overload
class WebezyConfig(_message.Message):
	"""webezyio generated message [webezy.WebezyConfig.v1.WebezyConfig]
	A class respresent a WebezyConfig type
	The main configuration structure
		"""
	host = str # type: str
	port = int # type: int
	deployment = enum_type_wrapper.EnumTypeWrapper # type: enum_type_wrapper.EnumTypeWrapper
	proxy = WebezyProxy__pb2.ProxyConfig # type: WebezyProxy__pb2.ProxyConfig
	docs = WebezyDocs # type: WebezyDocs
	template = WebezyTemplate__pb2.TemplateConfig # type: WebezyTemplate__pb2.TemplateConfig
	monitor = WebezyMonitor # type: WebezyMonitor
	analytics = bool # type: bool
	token = str # type: str
	first_run = bool # type: bool
	webezyio_templates = List[str] # type: List[str]
	features = Dict[str,bool] # type: Dict[str,bool]
	plugins = List[str] # type: List[str]

	def __init__(self, host=str, port=int, deployment=enum_type_wrapper.EnumTypeWrapper, proxy=WebezyProxy__pb2.ProxyConfig, docs=WebezyDocs, template=WebezyTemplate__pb2.TemplateConfig, monitor=WebezyMonitor, analytics=bool, token=str, first_run=bool, webezyio_templates=List[str], features=Dict[str,bool], plugins=List[str]):
		"""
		Attributes:
		----------
		host : str
			The webezy.io server host
		port : int
			The server port
		deployment : enum_type_wrapper.EnumTypeWrapper
			The project deployment type
		proxy : WebezyProxy__pb2.ProxyConfig
			
		docs : WebezyDocs
			
		template : WebezyTemplate__pb2.TemplateConfig
			
		monitor : WebezyMonitor
			
		analytics : bool
			
		token : str
			
		first_run : bool
			
		webezyio_templates : List[str]
			
		features : Dict[str,bool]
			
		plugins : List[str]
			
		"""
		pass
WebezyConfig = _reflection.GeneratedProtocolMessageType('WebezyConfig', (_message.Message,), {

  'FeaturesEntry' : _reflection.GeneratedProtocolMessageType('FeaturesEntry', (_message.Message,), {
    'DESCRIPTOR' : _WEBEZYCONFIG_FEATURESENTRY,
    '__module__' : 'WebezyConfig_pb2'
    # @@protoc_insertion_point(class_scope:webezy.WebezyConfig.v1.WebezyConfig.FeaturesEntry)
    })
  ,
  'DESCRIPTOR' : _WEBEZYCONFIG,
  '__module__' : 'WebezyConfig_pb2'
  # @@protoc_insertion_point(class_scope:webezy.WebezyConfig.v1.WebezyConfig)
  })
_sym_db.RegisterMessage(WebezyConfig)
_sym_db.RegisterMessage(WebezyConfig.FeaturesEntry)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WEBEZYCONFIG_FEATURESENTRY._options = None
  _WEBEZYCONFIG_FEATURESENTRY._serialized_options = b'8\001'
  _DEPLOYMENTTYPE._serialized_start=791
  _DEPLOYMENTTYPE._serialized_end=858
  _WEBEZYMONITOR._serialized_start=141
  _WEBEZYMONITOR._serialized_end=222
  _WEBEZYCONFIG._serialized_start=225
  _WEBEZYCONFIG._serialized_end=761
  _WEBEZYCONFIG_FEATURESENTRY._serialized_start=714
  _WEBEZYCONFIG_FEATURESENTRY._serialized_end=761
  _WEBEZYDOCS._serialized_start=763
  _WEBEZYDOCS._serialized_end=789
# @@protoc_insertion_point(module_scope)
