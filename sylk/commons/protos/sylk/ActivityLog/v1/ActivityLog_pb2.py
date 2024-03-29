# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/ActivityLog/v1/ActivityLog.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%sylk/ActivityLog/v1/ActivityLog.proto\x12\x13sylk.ActivityLog.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"^\n\x11\x45ncodedPagination\x12\'\n\x06params\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0c\n\x04skip\x18\x02 \x01(\x05\x12\x12\n\ntotal_size\x18\x03 \x01(\x05\"\xd9\x01\n\x0b\x41\x63tivityLog\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12.\n\ncreated_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x08metadata\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12\x0e\n\x06org_id\x18\x04 \x01(\t\x12\n\n\x02id\x18\x05 \x01(\t\x12\x12\n\nuser_email\x18\x06 \x01(\t\x12.\n\x04type\x18\x07 \x01(\x0e\x32 .sylk.ActivityLog.v1.ActionTypes\"-\n\x12PaginationResponse\x12\x17\n\x0fnext_page_token\x18\x01 \x01(\t\"\x86\x01\n\x17GetActivityLogsResponse\x12.\n\x04logs\x18\x01 \x03(\x0b\x32 .sylk.ActivityLog.v1.ActivityLog\x12;\n\npagination\x18\x02 \x01(\x0b\x32\'.sylk.ActivityLog.v1.PaginationResponse\":\n\x11PaginationRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t\"\xa7\x02\n\x17ListActivityLogsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06org_id\x18\x02 \x01(\t\x12)\n\x05until\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x37\n\ractivity_type\x18\x04 \x01(\x0e\x32 .sylk.ActivityLog.v1.ActionTypes\x12:\n\npagination\x18\x05 \x01(\x0b\x32&.sylk.ActivityLog.v1.PaginationRequest\x12\x39\n\rresource_type\x18\x06 \x01(\x0e\x32\".sylk.ActivityLog.v1.ResourceTypes\x12\x10\n\x08resource\x18\x07 \x01(\t*\xc3\x04\n\x0b\x41\x63tionTypes\x12\x17\n\x13UNKNOWN_ACTIONTYPES\x10\x00\x12\x13\n\x0f\x63reateEnumValue\x10\x01\x12\x13\n\x0fupdateEnumValue\x10\x02\x12\x13\n\x0f\x64\x65leteEnumValue\x10\x03\x12\x0f\n\x0b\x63reateField\x10\x04\x12\x0f\n\x0bupdateField\x10\x05\x12\x0f\n\x0b\x64\x65leteField\x10\x06\x12\x11\n\rcreateMessage\x10\x07\x12\x11\n\rupdateMessage\x10\x08\x12\x11\n\rdeleteMessage\x10\t\x12\x11\n\rcreatePackage\x10\n\x12\x11\n\rupdatePackage\x10\x0b\x12\x11\n\rdeletePackage\x10\x0c\x12\x11\n\rcreateService\x10\r\x12\x11\n\rupdateService\x10\x0e\x12\x11\n\rdeleteService\x10\x0f\x12\x11\n\rcreateProject\x10\x10\x12\x11\n\rupdateProject\x10\x11\x12\x11\n\rdeleteProject\x10\x12\x12\x0e\n\ncreateEnum\x10\x13\x12\x0e\n\nupdateEnum\x10\x14\x12\x0e\n\ndeleteEnum\x10\x15\x12\x0b\n\x07\x61\x64\x64User\x10\x16\x12\x12\n\x0eupdateUserRole\x10\x17\x12\x16\n\x12\x63reateOrganization\x10\x18\x12\x16\n\x12updateOrganization\x10\x19\x12\x0e\n\nremoveUser\x10\x1a\x12\x10\n\x0c\x63reateMethod\x10\x1b\x12\x10\n\x0cupdateMethod\x10\x1c\x12\x10\n\x0c\x64\x65leteMethod\x10\x1d*\xaa\x01\n\rResourceTypes\x12\x19\n\x15UNKNOWN_RESOURCETYPES\x10\x00\x12\x08\n\x04User\x10\x01\x12\x10\n\x0cOrganization\x10\x02\x12\x0b\n\x07Package\x10\x03\x12\x0b\n\x07Service\x10\x04\x12\x0b\n\x07Message\x10\x05\x12\x08\n\x04\x45num\x10\x06\x12\n\n\x06Method\x10\x07\x12\t\n\x05\x46ield\x10\x08\x12\r\n\tEnumValue\x10\t\x12\x0b\n\x07Project\x10\nb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylk.ActivityLog.v1.ActivityLog_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ACTIONTYPES']._serialized_start=984
  _globals['_ACTIONTYPES']._serialized_end=1563
  _globals['_RESOURCETYPES']._serialized_start=1566
  _globals['_RESOURCETYPES']._serialized_end=1736
  _globals['_ENCODEDPAGINATION']._serialized_start=125
  _globals['_ENCODEDPAGINATION']._serialized_end=219
  _globals['_ACTIVITYLOG']._serialized_start=222
  _globals['_ACTIVITYLOG']._serialized_end=439
  _globals['_PAGINATIONRESPONSE']._serialized_start=441
  _globals['_PAGINATIONRESPONSE']._serialized_end=486
  _globals['_GETACTIVITYLOGSRESPONSE']._serialized_start=489
  _globals['_GETACTIVITYLOGSRESPONSE']._serialized_end=623
  _globals['_PAGINATIONREQUEST']._serialized_start=625
  _globals['_PAGINATIONREQUEST']._serialized_end=683
  _globals['_LISTACTIVITYLOGSREQUEST']._serialized_start=686
  _globals['_LISTACTIVITYLOGSREQUEST']._serialized_end=981
# @@protoc_insertion_point(module_scope)
