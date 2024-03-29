# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/io/service_config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sylk.types.google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1csylk/io/service_config.proto\x12\x07Sylk.build\x1a\x15google/rpc/code.proto\"\\\n\rServiceConfig\x12\x1d\n\x15load_balancing_policy\x18\x01 \x01(\t\x12,\n\rmethod_config\x18\x02 \x03(\x0b\x32\x15.Sylk.build.MethodConfig\"\xb5\x04\n\x0cMethodConfig\x12.\n\x04name\x18\x01 \x03(\x0b\x32 .Sylk.build.MethodConfig.MethodPath\x12\x37\n\x0cretry_policy\x18\x02 \x01(\x0b\x32!.Sylk.build.MethodConfig.RetryPolicy\x12\x16\n\x0ewait_for_ready\x18\x03 \x01(\x08\x12\x0f\n\x07timeout\x18\x04 \x01(\t\x12!\n\x19max_request_message_bytes\x18\x05 \x01(\x05\x12\"\n\x1amax_response_message_bytes\x18\x06 \x01(\x05\x12?\n\x10retry_throttling\x18\x07 \x01(\x0b\x32%.Sylk.build.MethodConfig.RetryThrottling\x1a-\n\nMethodPath\x12\x0f\n\x07service\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x1a\x9f\x01\n\x0bRetryPolicy\x12\x14\n\x0cmax_attempts\x18\x01 \x01(\x05\x12\x17\n\x0finitial_backoff\x18\x02 \x01(\t\x12\x13\n\x0bmax_backoff\x18\x03 \x01(\t\x12\x1a\n\x12\x62\x61\x63koff_multiplier\x18\x04 \x01(\x01\x12\x30\n\x16retryable_status_codes\x18\x05 \x03(\x0e\x32\x10.google.rpc.Code\x1a:\n\x0fRetryThrottling\x12\x12\n\nmax_tokens\x18\x01 \x01(\x01\x12\x13\n\x0btoken_ratio\x18\x02 \x01(\x01\x42\x43ZAgithub.com/sylk-build/sylk-io/types/service_config;service_configb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Sylk.build.service_config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'ZAgithub.com/sylk-build/sylk-io/types/service_config;service_config'
  _globals['_SERVICECONFIG']._serialized_start=64
  _globals['_SERVICECONFIG']._serialized_end=156
  _globals['_METHODCONFIG']._serialized_start=159
  _globals['_METHODCONFIG']._serialized_end=724
  _globals['_METHODCONFIG_METHODPATH']._serialized_start=457
  _globals['_METHODCONFIG_METHODPATH']._serialized_end=502
  _globals['_METHODCONFIG_RETRYPOLICY']._serialized_start=505
  _globals['_METHODCONFIG_RETRYPOLICY']._serialized_end=664
  _globals['_METHODCONFIG_RETRYTHROTTLING']._serialized_start=666
  _globals['_METHODCONFIG_RETRYTHROTTLING']._serialized_end=724
# @@protoc_insertion_point(module_scope)
