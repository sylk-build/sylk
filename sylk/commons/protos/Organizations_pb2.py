# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Organizations.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import SylkApi_pb2 as SylkApi__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13Organizations.proto\x1a\rSylkApi.proto2\xaa\x06\n\rOrganizations\x12\x64\n\x0fGetOrganization\x12\'.sylk.SylkApi.v1.GetOrganizationRequest\x1a(.sylk.SylkApi.v1.GetOrganizationResponse\x12m\n\x12UpdateOrganization\x12*.sylk.SylkApi.v1.UpdateOrganizationRequest\x1a+.sylk.SylkApi.v1.UpdateOrganizationResponse\x12j\n\x11ListOrganizations\x12).sylk.SylkApi.v1.ListOrganizationsRequest\x1a(.sylk.SylkApi.v1.GetOrganizationResponse0\x01\x12g\n\x10\x41\x63\x63\x65prUserInvite\x12(.sylk.SylkApi.v1.AcceptUserInviteRequest\x1a).sylk.SylkApi.v1.AcceptUserInviteResponse\x12L\n\x07\x41\x64\x64User\x12\x1f.sylk.SylkApi.v1.AddUserRequest\x1a .sylk.SylkApi.v1.AddUserResponse\x12\x61\n\x0eUpdateUserRole\x12&.sylk.SylkApi.v1.UpdateUserRoleRequest\x1a\'.sylk.SylkApi.v1.UpdateUserRoleResponse\x12g\n\x10UpdateUserStatus\x12(.sylk.SylkApi.v1.UpdateUserStatusRequest\x1a).sylk.SylkApi.v1.UpdateUserStatusResponse\x12U\n\nRemoveUser\x12\".sylk.SylkApi.v1.RemoveUserRequest\x1a#.sylk.SylkApi.v1.RemoveUserResponseB Z\x1e/services/protos/Organizationsb\x06proto3')



_ORGANIZATIONS = DESCRIPTOR.services_by_name['Organizations']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z\036/services/protos/Organizations'
  _ORGANIZATIONS._serialized_start=39
  _ORGANIZATIONS._serialized_end=849
# @@protoc_insertion_point(module_scope)
