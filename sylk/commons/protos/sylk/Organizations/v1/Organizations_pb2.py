# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/Organizations/v1/Organizations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sylk.commons.protos.sylk.SylkApi.v1 import SylkApi_pb2 as sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)sylk/Organizations/v1/Organizations.proto\x12\x15sylk.Organizations.v1\x1a\x1dsylk/SylkApi/v1/SylkApi.proto2\xaa\x06\n\rOrganizations\x12g\n\x10\x41\x63\x63\x65prUserInvite\x12(.sylk.SylkApi.v1.AcceptUserInviteRequest\x1a).sylk.SylkApi.v1.AcceptUserInviteResponse\x12\x64\n\x0fGetOrganization\x12\'.sylk.SylkApi.v1.GetOrganizationRequest\x1a(.sylk.SylkApi.v1.GetOrganizationResponse\x12m\n\x12UpdateOrganization\x12*.sylk.SylkApi.v1.UpdateOrganizationRequest\x1a+.sylk.SylkApi.v1.UpdateOrganizationResponse\x12j\n\x11ListOrganizations\x12).sylk.SylkApi.v1.ListOrganizationsRequest\x1a(.sylk.SylkApi.v1.GetOrganizationResponse0\x01\x12L\n\x07\x41\x64\x64User\x12\x1f.sylk.SylkApi.v1.AddUserRequest\x1a .sylk.SylkApi.v1.AddUserResponse\x12g\n\x10UpdateUserStatus\x12(.sylk.SylkApi.v1.UpdateUserStatusRequest\x1a).sylk.SylkApi.v1.UpdateUserStatusResponse\x12U\n\nRemoveUser\x12\".sylk.SylkApi.v1.RemoveUserRequest\x1a#.sylk.SylkApi.v1.RemoveUserResponse\x12\x61\n\x0eUpdateUserRole\x12&.sylk.SylkApi.v1.UpdateUserRoleRequest\x1a\'.sylk.SylkApi.v1.UpdateUserRoleResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylk.Organizations.v1.Organizations_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_ORGANIZATIONS']._serialized_start=100
  _globals['_ORGANIZATIONS']._serialized_end=910
# @@protoc_insertion_point(module_scope)
