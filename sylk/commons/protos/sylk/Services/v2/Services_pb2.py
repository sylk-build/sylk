# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/Services/v2/Services.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from sylk.commons.protos.sylk.SylkService.v2 import SylkService_pb2 as sylk_dot_SylkService_dot_v2_dot_SylkService__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fsylk/Services/v2/Services.proto\x12\x10sylk.Services.v2\x1a\x1bgoogle/protobuf/empty.proto\x1a%sylk/SylkService/v2/SylkService.proto\"8\n\x11GetServiceRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\"M\n\x12GetServiceResponse\x12\x37\n\x06result\x18\x01 \x01(\x0b\x32\'.sylk.SylkService.v2.SylkServiceDisplay\"]\n\x14\x43reateServiceRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x31\n\x07service\x18\x02 \x01(\x0b\x32 .sylk.SylkService.v2.SylkService\"P\n\x15\x43reateServiceResponse\x12\x37\n\x06result\x18\x01 \x01(\x0b\x32\'.sylk.SylkService.v2.SylkServiceDisplay\";\n\x14\x44\x65leteServiceRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\"m\n\x14UpdateServiceRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x30\n\x06update\x18\x03 \x01(\x0b\x32 .sylk.SylkService.v2.SylkService\"v\n\x15UpdateServiceResponse\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x38\n\x07updated\x18\x03 \x01(\x0b\x32\'.sylk.SylkService.v2.SylkServiceDisplay2\xf8\x02\n\x08Services\x12W\n\nGetService\x12#.sylk.Services.v2.GetServiceRequest\x1a$.sylk.Services.v2.GetServiceResponse\x12O\n\rDeleteService\x12&.sylk.Services.v2.DeleteServiceRequest\x1a\x16.google.protobuf.Empty\x12`\n\rCreateService\x12&.sylk.Services.v2.CreateServiceRequest\x1a\'.sylk.Services.v2.CreateServiceResponse\x12`\n\rUpdateService\x12&.sylk.Services.v2.UpdateServiceRequest\x1a\'.sylk.Services.v2.UpdateServiceResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylk.Services.v2.Services_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_GETSERVICEREQUEST']._serialized_start=121
  _globals['_GETSERVICEREQUEST']._serialized_end=177
  _globals['_GETSERVICERESPONSE']._serialized_start=179
  _globals['_GETSERVICERESPONSE']._serialized_end=256
  _globals['_CREATESERVICEREQUEST']._serialized_start=258
  _globals['_CREATESERVICEREQUEST']._serialized_end=351
  _globals['_CREATESERVICERESPONSE']._serialized_start=353
  _globals['_CREATESERVICERESPONSE']._serialized_end=433
  _globals['_DELETESERVICEREQUEST']._serialized_start=435
  _globals['_DELETESERVICEREQUEST']._serialized_end=494
  _globals['_UPDATESERVICEREQUEST']._serialized_start=496
  _globals['_UPDATESERVICEREQUEST']._serialized_end=605
  _globals['_UPDATESERVICERESPONSE']._serialized_start=607
  _globals['_UPDATESERVICERESPONSE']._serialized_end=725
  _globals['_SERVICES']._serialized_start=728
  _globals['_SERVICES']._serialized_end=1104
# @@protoc_insertion_point(module_scope)
