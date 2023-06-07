# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sylk/SylkApi/v1/SylkApi.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from sylk.commons.protos.sylk.SylkOrganization.v1 import SylkOrganization_pb2 as sylk_dot_SylkOrganization_dot_v1_dot_SylkOrganization__pb2
from sylk.commons.protos.sylk.SylkUser.v1 import SylkUser_pb2 as sylk_dot_SylkUser_dot_v1_dot_SylkUser__pb2
from sylk.commons.protos.sylk.SylkProject.v1 import SylkProject_pb2 as sylk_dot_SylkProject_dot_v1_dot_SylkProject__pb2
from sylk.commons.protos.sylk.SylkPackage.v1 import SylkPackage_pb2 as sylk_dot_SylkPackage_dot_v1_dot_SylkPackage__pb2
from sylk.commons.protos.sylk.SylkService.v1 import SylkService_pb2 as sylk_dot_SylkService_dot_v1_dot_SylkService__pb2
from sylk.commons.protos.sylk.SylkMessage.v1 import SylkMessage_pb2 as sylk_dot_SylkMessage_dot_v1_dot_SylkMessage__pb2
from sylk.commons.protos.sylk.SylkMethod.v1 import SylkMethod_pb2 as sylk_dot_SylkMethod_dot_v1_dot_SylkMethod__pb2
from sylk.commons.protos.sylk.SylkField.v1 import SylkField_pb2 as sylk_dot_SylkField_dot_v1_dot_SylkField__pb2
from sylk.commons.protos.sylk.SylkEnum.v1 import SylkEnum_pb2 as sylk_dot_SylkEnum_dot_v1_dot_SylkEnum__pb2
from sylk.commons.protos.sylk.SylkEnumValue.v1 import SylkEnumValue_pb2 as sylk_dot_SylkEnumValue_dot_v1_dot_SylkEnumValue__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsylk/SylkApi/v1/SylkApi.proto\x12\x0fsylk.SylkApi.v1\x1a/sylk/SylkOrganization/v1/SylkOrganization.proto\x1a\x1fsylk/SylkUser/v1/SylkUser.proto\x1a%sylk/SylkProject/v1/SylkProject.proto\x1a%sylk/SylkPackage/v1/SylkPackage.proto\x1a%sylk/SylkService/v1/SylkService.proto\x1a%sylk/SylkMessage/v1/SylkMessage.proto\x1a#sylk/SylkMethod/v1/SylkMethod.proto\x1a!sylk/SylkField/v1/SylkField.proto\x1a\x1fsylk/SylkEnum/v1/SylkEnum.proto\x1a)sylk/SylkEnumValue/v1/SylkEnumValue.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"$\n\x12RemoveUserResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"K\n\x11RemoveUserRequest\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12\x12\n\nuser_email\x18\x01 \x01(\t\x12\x0e\n\x06org_id\x18\x02 \x01(\t\"g\n\x19UpdateOrganizationRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12:\n\x06update\x18\x02 \x01(\x0b\x32*.sylk.SylkOrganization.v1.SylkOrganization\"\\\n\x17GetOrganizationResponse\x12\x41\n\x06result\x18\x01 \x01(\x0b\x32\x31.sylk.SylkOrganization.v1.SylkOrganizationDisplay\"(\n\x16GetOrganizationRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\t\"*\n\x18UpdateUserStatusResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"w\n\x17UpdateUserStatusRequest\x12\x18\n\x10user_email_or_id\x18\x01 \x01(\t\x12\x0e\n\x06org_id\x18\x03 \x01(\t\x12\x32\n\x06status\x18\x02 \x01(\x0e\x32\".sylk.SylkUser.v1.SylkUserStatuses\"(\n\x16UpdateUserRoleResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"{\n\x15UpdateUserRoleRequest\x12-\n\x04role\x18\x03 \x01(\x0e\x32\x1f.sylk.SylkUser.v1.SylkUserRoles\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x0e\n\x06org_id\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x04 \x01(\t\"\'\n\x15\x44\x65leteProjectResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\'\n\x14\x44\x65leteProjectRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\"e\n\x15UpdateProjectResponse\x12\x38\n\x07updated\x18\x02 \x01(\x0b\x32\'.sylk.SylkProject.v1.SylkProjectDisplay\x12\x12\n\nproject_id\x18\x01 \x01(\t\"\\\n\x14UpdateProjectRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x30\n\x06update\x18\x02 \x01(\x0b\x32 .sylk.SylkProject.v1.SylkProject\"M\n\x12GetProjectResponse\x12\x37\n\x06result\x18\x01 \x01(\x0b\x32\'.sylk.SylkProject.v1.SylkProjectDisplay\"$\n\x11GetProjectRequest\x12\x0f\n\x07project\x18\x01 \x01(\t\"D\n\x0fGetUserResponse\x12\x31\n\x06result\x18\x01 \x01(\x0b\x32!.sylk.SylkUser.v1.SylkUserDisplay\"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"!\n\x0f\x41\x64\x64UserResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"t\n\x0e\x41\x64\x64UserRequest\x12-\n\x04role\x18\x02 \x01(\x0e\x32\x1f.sylk.SylkUser.v1.SylkUserRoles\x12\x0e\n\x06org_id\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\x12\n\nuser_email\x18\x01 \x01(\t\"*\n\x18\x41\x63\x63\x65ptUserInviteResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"8\n\x17\x41\x63\x63\x65ptUserInviteRequest\x12\r\n\x05\x65mail\x18\x01 \x01(\t\x12\x0e\n\x06org_id\x18\x02 \x01(\t\"R\n\x12UpdateUserResponse\x12+\n\x07updated\x18\x02 \x01(\x0b\x32\x1a.sylk.SylkUser.v1.SylkUser\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"P\n\x11UpdateUserRequest\x12*\n\x06update\x18\x02 \x01(\x0b\x32\x1a.sylk.SylkUser.v1.SylkUser\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"\x80\x01\n\x12\x43reateUserResponse\x12(\n\x04user\x18\x01 \x01(\x0b\x32\x1a.sylk.SylkUser.v1.SylkUser\x12@\n\x0corganization\x18\x02 \x01(\x0b\x32*.sylk.SylkOrganization.v1.SylkOrganization\"M\n\x11\x43reateUserRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12(\n\x04user\x18\x02 \x01(\x0b\x32\x1a.sylk.SylkUser.v1.SylkUser\"+\n\x18ListOrganizationsRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\"i\n\x1aUpdateOrganizationResponse\x12;\n\x07updated\x18\x02 \x01(\x0b\x32*.sylk.SylkOrganization.v1.SylkOrganization\x12\x0e\n\x06org_id\x18\x01 \x01(\t\"8\n\x11GetPackageRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07package\x18\x02 \x01(\t\"M\n\x12GetPackageResponse\x12\x37\n\x06result\x18\x01 \x01(\x0b\x32\'.sylk.SylkPackage.v1.SylkPackageDisplay\"]\n\x14\x43reatePackageRequest\x12\x31\n\x07package\x18\x02 \x01(\x0b\x32 .sylk.SylkPackage.v1.SylkPackage\x12\x12\n\nproject_id\x18\x01 \x01(\t\"d\n\x15\x43reatePackageResponse\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x37\n\x06result\x18\x02 \x01(\x0b\x32\'.sylk.SylkPackage.v1.SylkPackageDisplay\"m\n\x14UpdatePackageRequest\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0f\n\x07package\x18\x01 \x01(\t\x12\x30\n\x06update\x18\x03 \x01(\x0b\x32 .sylk.SylkPackage.v1.SylkPackage\"v\n\x15UpdatePackageResponse\x12\x38\n\x07updated\x18\x03 \x01(\x0b\x32\'.sylk.SylkPackage.v1.SylkPackageDisplay\x12\x0f\n\x07package\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\";\n\x14\x44\x65letePackageRequest\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x0f\n\x07package\x18\x01 \x01(\t\"<\n\x15\x44\x65letePackageResponse\x12\x0f\n\x07package\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"8\n\x11GetServiceRequest\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"M\n\x12GetServiceResponse\x12\x37\n\x06result\x18\x01 \x01(\x0b\x32\'.sylk.SylkService.v1.SylkServiceDisplay\"]\n\x14\x43reateServiceRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x31\n\x07service\x18\x02 \x01(\x0b\x32 .sylk.SylkService.v1.SylkService\"d\n\x15\x43reateServiceResponse\x12\x37\n\x06result\x18\x02 \x01(\x0b\x32\'.sylk.SylkService.v1.SylkServiceDisplay\x12\x12\n\nproject_id\x18\x01 \x01(\t\"m\n\x14UpdateServiceRequest\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x30\n\x06update\x18\x03 \x01(\x0b\x32 .sylk.SylkService.v1.SylkService\"v\n\x15UpdateServiceResponse\x12\x38\n\x07updated\x18\x03 \x01(\x0b\x32\'.sylk.SylkService.v1.SylkServiceDisplay\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\";\n\x14\x44\x65leteServiceRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\"<\n\x15\x44\x65leteServiceResponse\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\")\n\x13ListServicesRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\")\n\x13ListPackagesRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\"8\n\x11GetMessageRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"M\n\x12GetMessageResponse\x12\x37\n\x06result\x18\x01 \x01(\x0b\x32\'.sylk.SylkMessage.v1.SylkMessageDisplay\"n\n\x14\x43reateMessageRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07package\x18\x02 \x01(\t\x12\x31\n\x07message\x18\x03 \x01(\x0b\x32 .sylk.SylkMessage.v1.SylkMessage\"u\n\x15\x43reateMessageResponse\x12\x37\n\x06result\x18\x03 \x01(\x0b\x32\'.sylk.SylkMessage.v1.SylkMessageDisplay\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"m\n\x14UpdateMessageRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x30\n\x06update\x18\x03 \x01(\x0b\x32 .sylk.SylkMessage.v1.SylkMessage\"v\n\x15UpdateMessageResponse\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x38\n\x07updated\x18\x03 \x01(\x0b\x32\'.sylk.SylkMessage.v1.SylkMessageDisplay\x12\x12\n\nproject_id\x18\x01 \x01(\t\";\n\x14\x44\x65leteMessageRequest\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"<\n\x15\x44\x65leteMessageResponse\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\"6\n\x10GetMethodRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\"J\n\x11GetMethodResponse\x12\x35\n\x06result\x18\x01 \x01(\x0b\x32%.sylk.SylkMethod.v1.SylkMethodDisplay\"j\n\x13\x43reateMethodRequest\x12\x0f\n\x07service\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12.\n\x06method\x18\x03 \x01(\x0b\x32\x1e.sylk.SylkMethod.v1.SylkMethod\"r\n\x14\x43reateMethodResponse\x12\x35\n\x06result\x18\x03 \x01(\x0b\x32%.sylk.SylkMethod.v1.SylkMethodDisplay\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07service\x18\x02 \x01(\t\"i\n\x13UpdateMethodRequest\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12.\n\x06update\x18\x03 \x01(\x0b\x32\x1e.sylk.SylkMethod.v1.SylkMethod\"r\n\x14UpdateMethodResponse\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x36\n\x07updated\x18\x03 \x01(\x0b\x32%.sylk.SylkMethod.v1.SylkMethodDisplay\"9\n\x13\x44\x65leteMethodRequest\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\":\n\x14\x44\x65leteMethodResponse\x12\x0e\n\x06method\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"4\n\x0fGetFieldRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\r\n\x05\x66ield\x18\x02 \x01(\t\"G\n\x10GetFieldResponse\x12\x33\n\x06result\x18\x01 \x01(\x0b\x32#.sylk.SylkField.v1.SylkFieldDisplay\"e\n\x12UpdateFieldRequest\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12,\n\x06update\x18\x03 \x01(\x0b\x32\x1c.sylk.SylkField.v1.SylkField\"n\n\x13UpdateFieldResponse\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12\x34\n\x07updated\x18\x03 \x01(\x0b\x32#.sylk.SylkField.v1.SylkFieldDisplay\"7\n\x12\x44\x65leteFieldRequest\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"8\n\x13\x44\x65leteFieldResponse\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"f\n\x12\x43reateFieldRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12+\n\x05\x66ield\x18\x03 \x01(\x0b\x32\x1c.sylk.SylkField.v1.SylkField\"J\n\x13\x43reateFieldResponse\x12\x33\n\x06result\x18\x01 \x01(\x0b\x32#.sylk.SylkField.v1.SylkFieldDisplay\"2\n\x0eGetEnumRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0c\n\x04\x65num\x18\x02 \x01(\t\"D\n\x0fGetEnumResponse\x12\x31\n\x06result\x18\x01 \x01(\x0b\x32!.sylk.SylkEnum.v1.SylkEnumDisplay\"b\n\x11\x43reateEnumRequest\x12\x0f\n\x07package\x18\x02 \x01(\t\x12(\n\x04\x65num\x18\x03 \x01(\x0b\x32\x1a.sylk.SylkEnum.v1.SylkEnum\x12\x12\n\nproject_id\x18\x01 \x01(\t\"[\n\x12\x43reateEnumResponse\x12\x31\n\x06result\x18\x02 \x01(\x0b\x32!.sylk.SylkEnum.v1.SylkEnumDisplay\x12\x12\n\nproject_id\x18\x01 \x01(\t\"a\n\x11UpdateEnumRequest\x12*\n\x06update\x18\x03 \x01(\x0b\x32\x1a.sylk.SylkEnum.v1.SylkEnum\x12\x0c\n\x04\x65num\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"j\n\x12UpdateEnumResponse\x12\x0c\n\x04\x65num\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x32\n\x07updated\x18\x03 \x01(\x0b\x32!.sylk.SylkEnum.v1.SylkEnumDisplay\"5\n\x11\x44\x65leteEnumRequest\x12\x0c\n\x04\x65num\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"6\n\x12\x44\x65leteEnumResponse\x12\x0c\n\x04\x65num\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"=\n\x13GetEnumValueRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\nenum_value\x18\x02 \x01(\t\"S\n\x14GetEnumValueResponse\x12;\n\x06result\x18\x01 \x01(\x0b\x32+.sylk.SylkEnumValue.v1.SylkEnumValueDisplay\"t\n\x16\x43reateEnumValueRequest\x12\x0c\n\x04\x65num\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x38\n\nenum_value\x18\x03 \x01(\x0b\x32$.sylk.SylkEnumValue.v1.SylkEnumValue\"V\n\x17\x43reateEnumValueResponse\x12;\n\x06result\x18\x01 \x01(\x0b\x32+.sylk.SylkEnumValue.v1.SylkEnumValueDisplay\"v\n\x16UpdateEnumValueRequest\x12\x34\n\x06update\x18\x03 \x01(\x0b\x32$.sylk.SylkEnumValue.v1.SylkEnumValue\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\nenum_value\x18\x02 \x01(\t\"\x7f\n\x17UpdateEnumValueResponse\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12<\n\x07updated\x18\x03 \x01(\x0b\x32+.sylk.SylkEnumValue.v1.SylkEnumValueDisplay\x12\x12\n\nenum_value\x18\x02 \x01(\t\"@\n\x16\x44\x65leteEnumValueRequest\x12\x12\n\nenum_value\x18\x02 \x01(\t\x12\x12\n\nproject_id\x18\x01 \x01(\t\"A\n\x17\x44\x65leteEnumValueResponse\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x12\n\nenum_value\x18\x02 \x01(\t\"a\n\x1eListOrganizationsResponseCache\x12?\n\rorganizations\x18\x01 \x03(\x0b\x32(.sylk.SylkApi.v1.GetOrganizationResponse\"%\n\x13ListProjectsRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\t\"Y\n\x14\x43reateProjectRequest\x12\x31\n\x07project\x18\x02 \x01(\x0b\x32 .sylk.SylkProject.v1.SylkProject\x12\x0e\n\x06org_id\x18\x01 \x01(\t\"`\n\x15\x43reateProjectResponse\x12\x0e\n\x06org_id\x18\x02 \x01(\t\x12\x37\n\x06result\x18\x01 \x01(\x0b\x32\'.sylk.SylkProject.v1.SylkProjectDisplay\"R\n\x19ListProjectsResponseCache\x12\x35\n\x08projects\x18\x01 \x03(\x0b\x32#.sylk.SylkApi.v1.GetProjectResponse\"9\n\rCachedSession\x12(\n\x07session\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct\"o\n\x18\x43reateAccessTokenRequest\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x0e\n\x06org_id\x18\x01 \x01(\t\x12.\n\nexpires_at\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"+\n\x19\x43reateAccessTokenResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\")\n\x17ListAccessTokensRequest\x12\x0e\n\x06org_id\x18\x01 \x01(\t\"O\n\x16GetAccessTokenResponse\x12\x35\n\x06result\x18\x01 \x01(\x0b\x32%.sylk.SylkUser.v1.PersonalAccessToken\"&\n\x15GetAccessTokenRequest\x12\r\n\x05token\x18\x01 \x01(\t\"9\n\x18RevokeAccessTokenRequest\x12\r\n\x05token\x18\x01 \x01(\t\x12\x0e\n\x06org_id\x18\x02 \x01(\t\"+\n\x19RevokeAccessTokenResponse\x12\x0e\n\x06status\x18\x01 \x01(\tBAZ?github.com/sylk-build/sylk-core/services/protos/sylk/SylkApi/v1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sylk.SylkApi.v1.SylkApi_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z?github.com/sylk-build/sylk-core/services/protos/sylk/SylkApi/v1'
  _globals['_REMOVEUSERRESPONSE']._serialized_start=499
  _globals['_REMOVEUSERRESPONSE']._serialized_end=535
  _globals['_REMOVEUSERREQUEST']._serialized_start=537
  _globals['_REMOVEUSERREQUEST']._serialized_end=612
  _globals['_UPDATEORGANIZATIONREQUEST']._serialized_start=614
  _globals['_UPDATEORGANIZATIONREQUEST']._serialized_end=717
  _globals['_GETORGANIZATIONRESPONSE']._serialized_start=719
  _globals['_GETORGANIZATIONRESPONSE']._serialized_end=811
  _globals['_GETORGANIZATIONREQUEST']._serialized_start=813
  _globals['_GETORGANIZATIONREQUEST']._serialized_end=853
  _globals['_UPDATEUSERSTATUSRESPONSE']._serialized_start=855
  _globals['_UPDATEUSERSTATUSRESPONSE']._serialized_end=897
  _globals['_UPDATEUSERSTATUSREQUEST']._serialized_start=899
  _globals['_UPDATEUSERSTATUSREQUEST']._serialized_end=1018
  _globals['_UPDATEUSERROLERESPONSE']._serialized_start=1020
  _globals['_UPDATEUSERROLERESPONSE']._serialized_end=1060
  _globals['_UPDATEUSERROLEREQUEST']._serialized_start=1062
  _globals['_UPDATEUSERROLEREQUEST']._serialized_end=1185
  _globals['_DELETEPROJECTRESPONSE']._serialized_start=1187
  _globals['_DELETEPROJECTRESPONSE']._serialized_end=1226
  _globals['_DELETEPROJECTREQUEST']._serialized_start=1228
  _globals['_DELETEPROJECTREQUEST']._serialized_end=1267
  _globals['_UPDATEPROJECTRESPONSE']._serialized_start=1269
  _globals['_UPDATEPROJECTRESPONSE']._serialized_end=1370
  _globals['_UPDATEPROJECTREQUEST']._serialized_start=1372
  _globals['_UPDATEPROJECTREQUEST']._serialized_end=1464
  _globals['_GETPROJECTRESPONSE']._serialized_start=1466
  _globals['_GETPROJECTRESPONSE']._serialized_end=1543
  _globals['_GETPROJECTREQUEST']._serialized_start=1545
  _globals['_GETPROJECTREQUEST']._serialized_end=1581
  _globals['_GETUSERRESPONSE']._serialized_start=1583
  _globals['_GETUSERRESPONSE']._serialized_end=1651
  _globals['_GETUSERREQUEST']._serialized_start=1653
  _globals['_GETUSERREQUEST']._serialized_end=1686
  _globals['_ADDUSERRESPONSE']._serialized_start=1688
  _globals['_ADDUSERRESPONSE']._serialized_end=1721
  _globals['_ADDUSERREQUEST']._serialized_start=1723
  _globals['_ADDUSERREQUEST']._serialized_end=1839
  _globals['_ACCEPTUSERINVITERESPONSE']._serialized_start=1841
  _globals['_ACCEPTUSERINVITERESPONSE']._serialized_end=1883
  _globals['_ACCEPTUSERINVITEREQUEST']._serialized_start=1885
  _globals['_ACCEPTUSERINVITEREQUEST']._serialized_end=1941
  _globals['_UPDATEUSERRESPONSE']._serialized_start=1943
  _globals['_UPDATEUSERRESPONSE']._serialized_end=2025
  _globals['_UPDATEUSERREQUEST']._serialized_start=2027
  _globals['_UPDATEUSERREQUEST']._serialized_end=2107
  _globals['_CREATEUSERRESPONSE']._serialized_start=2110
  _globals['_CREATEUSERRESPONSE']._serialized_end=2238
  _globals['_CREATEUSERREQUEST']._serialized_start=2240
  _globals['_CREATEUSERREQUEST']._serialized_end=2317
  _globals['_LISTORGANIZATIONSREQUEST']._serialized_start=2319
  _globals['_LISTORGANIZATIONSREQUEST']._serialized_end=2362
  _globals['_UPDATEORGANIZATIONRESPONSE']._serialized_start=2364
  _globals['_UPDATEORGANIZATIONRESPONSE']._serialized_end=2469
  _globals['_GETPACKAGEREQUEST']._serialized_start=2471
  _globals['_GETPACKAGEREQUEST']._serialized_end=2527
  _globals['_GETPACKAGERESPONSE']._serialized_start=2529
  _globals['_GETPACKAGERESPONSE']._serialized_end=2606
  _globals['_CREATEPACKAGEREQUEST']._serialized_start=2608
  _globals['_CREATEPACKAGEREQUEST']._serialized_end=2701
  _globals['_CREATEPACKAGERESPONSE']._serialized_start=2703
  _globals['_CREATEPACKAGERESPONSE']._serialized_end=2803
  _globals['_UPDATEPACKAGEREQUEST']._serialized_start=2805
  _globals['_UPDATEPACKAGEREQUEST']._serialized_end=2914
  _globals['_UPDATEPACKAGERESPONSE']._serialized_start=2916
  _globals['_UPDATEPACKAGERESPONSE']._serialized_end=3034
  _globals['_DELETEPACKAGEREQUEST']._serialized_start=3036
  _globals['_DELETEPACKAGEREQUEST']._serialized_end=3095
  _globals['_DELETEPACKAGERESPONSE']._serialized_start=3097
  _globals['_DELETEPACKAGERESPONSE']._serialized_end=3157
  _globals['_GETSERVICEREQUEST']._serialized_start=3159
  _globals['_GETSERVICEREQUEST']._serialized_end=3215
  _globals['_GETSERVICERESPONSE']._serialized_start=3217
  _globals['_GETSERVICERESPONSE']._serialized_end=3294
  _globals['_CREATESERVICEREQUEST']._serialized_start=3296
  _globals['_CREATESERVICEREQUEST']._serialized_end=3389
  _globals['_CREATESERVICERESPONSE']._serialized_start=3391
  _globals['_CREATESERVICERESPONSE']._serialized_end=3491
  _globals['_UPDATESERVICEREQUEST']._serialized_start=3493
  _globals['_UPDATESERVICEREQUEST']._serialized_end=3602
  _globals['_UPDATESERVICERESPONSE']._serialized_start=3604
  _globals['_UPDATESERVICERESPONSE']._serialized_end=3722
  _globals['_DELETESERVICEREQUEST']._serialized_start=3724
  _globals['_DELETESERVICEREQUEST']._serialized_end=3783
  _globals['_DELETESERVICERESPONSE']._serialized_start=3785
  _globals['_DELETESERVICERESPONSE']._serialized_end=3845
  _globals['_LISTSERVICESREQUEST']._serialized_start=3847
  _globals['_LISTSERVICESREQUEST']._serialized_end=3888
  _globals['_LISTPACKAGESREQUEST']._serialized_start=3890
  _globals['_LISTPACKAGESREQUEST']._serialized_end=3931
  _globals['_GETMESSAGEREQUEST']._serialized_start=3933
  _globals['_GETMESSAGEREQUEST']._serialized_end=3989
  _globals['_GETMESSAGERESPONSE']._serialized_start=3991
  _globals['_GETMESSAGERESPONSE']._serialized_end=4068
  _globals['_CREATEMESSAGEREQUEST']._serialized_start=4070
  _globals['_CREATEMESSAGEREQUEST']._serialized_end=4180
  _globals['_CREATEMESSAGERESPONSE']._serialized_start=4182
  _globals['_CREATEMESSAGERESPONSE']._serialized_end=4299
  _globals['_UPDATEMESSAGEREQUEST']._serialized_start=4301
  _globals['_UPDATEMESSAGEREQUEST']._serialized_end=4410
  _globals['_UPDATEMESSAGERESPONSE']._serialized_start=4412
  _globals['_UPDATEMESSAGERESPONSE']._serialized_end=4530
  _globals['_DELETEMESSAGEREQUEST']._serialized_start=4532
  _globals['_DELETEMESSAGEREQUEST']._serialized_end=4591
  _globals['_DELETEMESSAGERESPONSE']._serialized_start=4593
  _globals['_DELETEMESSAGERESPONSE']._serialized_end=4653
  _globals['_GETMETHODREQUEST']._serialized_start=4655
  _globals['_GETMETHODREQUEST']._serialized_end=4709
  _globals['_GETMETHODRESPONSE']._serialized_start=4711
  _globals['_GETMETHODRESPONSE']._serialized_end=4785
  _globals['_CREATEMETHODREQUEST']._serialized_start=4787
  _globals['_CREATEMETHODREQUEST']._serialized_end=4893
  _globals['_CREATEMETHODRESPONSE']._serialized_start=4895
  _globals['_CREATEMETHODRESPONSE']._serialized_end=5009
  _globals['_UPDATEMETHODREQUEST']._serialized_start=5011
  _globals['_UPDATEMETHODREQUEST']._serialized_end=5116
  _globals['_UPDATEMETHODRESPONSE']._serialized_start=5118
  _globals['_UPDATEMETHODRESPONSE']._serialized_end=5232
  _globals['_DELETEMETHODREQUEST']._serialized_start=5234
  _globals['_DELETEMETHODREQUEST']._serialized_end=5291
  _globals['_DELETEMETHODRESPONSE']._serialized_start=5293
  _globals['_DELETEMETHODRESPONSE']._serialized_end=5351
  _globals['_GETFIELDREQUEST']._serialized_start=5353
  _globals['_GETFIELDREQUEST']._serialized_end=5405
  _globals['_GETFIELDRESPONSE']._serialized_start=5407
  _globals['_GETFIELDRESPONSE']._serialized_end=5478
  _globals['_UPDATEFIELDREQUEST']._serialized_start=5480
  _globals['_UPDATEFIELDREQUEST']._serialized_end=5581
  _globals['_UPDATEFIELDRESPONSE']._serialized_start=5583
  _globals['_UPDATEFIELDRESPONSE']._serialized_end=5693
  _globals['_DELETEFIELDREQUEST']._serialized_start=5695
  _globals['_DELETEFIELDREQUEST']._serialized_end=5750
  _globals['_DELETEFIELDRESPONSE']._serialized_start=5752
  _globals['_DELETEFIELDRESPONSE']._serialized_end=5808
  _globals['_CREATEFIELDREQUEST']._serialized_start=5810
  _globals['_CREATEFIELDREQUEST']._serialized_end=5912
  _globals['_CREATEFIELDRESPONSE']._serialized_start=5914
  _globals['_CREATEFIELDRESPONSE']._serialized_end=5988
  _globals['_GETENUMREQUEST']._serialized_start=5990
  _globals['_GETENUMREQUEST']._serialized_end=6040
  _globals['_GETENUMRESPONSE']._serialized_start=6042
  _globals['_GETENUMRESPONSE']._serialized_end=6110
  _globals['_CREATEENUMREQUEST']._serialized_start=6112
  _globals['_CREATEENUMREQUEST']._serialized_end=6210
  _globals['_CREATEENUMRESPONSE']._serialized_start=6212
  _globals['_CREATEENUMRESPONSE']._serialized_end=6303
  _globals['_UPDATEENUMREQUEST']._serialized_start=6305
  _globals['_UPDATEENUMREQUEST']._serialized_end=6402
  _globals['_UPDATEENUMRESPONSE']._serialized_start=6404
  _globals['_UPDATEENUMRESPONSE']._serialized_end=6510
  _globals['_DELETEENUMREQUEST']._serialized_start=6512
  _globals['_DELETEENUMREQUEST']._serialized_end=6565
  _globals['_DELETEENUMRESPONSE']._serialized_start=6567
  _globals['_DELETEENUMRESPONSE']._serialized_end=6621
  _globals['_GETENUMVALUEREQUEST']._serialized_start=6623
  _globals['_GETENUMVALUEREQUEST']._serialized_end=6684
  _globals['_GETENUMVALUERESPONSE']._serialized_start=6686
  _globals['_GETENUMVALUERESPONSE']._serialized_end=6769
  _globals['_CREATEENUMVALUEREQUEST']._serialized_start=6771
  _globals['_CREATEENUMVALUEREQUEST']._serialized_end=6887
  _globals['_CREATEENUMVALUERESPONSE']._serialized_start=6889
  _globals['_CREATEENUMVALUERESPONSE']._serialized_end=6975
  _globals['_UPDATEENUMVALUEREQUEST']._serialized_start=6977
  _globals['_UPDATEENUMVALUEREQUEST']._serialized_end=7095
  _globals['_UPDATEENUMVALUERESPONSE']._serialized_start=7097
  _globals['_UPDATEENUMVALUERESPONSE']._serialized_end=7224
  _globals['_DELETEENUMVALUEREQUEST']._serialized_start=7226
  _globals['_DELETEENUMVALUEREQUEST']._serialized_end=7290
  _globals['_DELETEENUMVALUERESPONSE']._serialized_start=7292
  _globals['_DELETEENUMVALUERESPONSE']._serialized_end=7357
  _globals['_LISTORGANIZATIONSRESPONSECACHE']._serialized_start=7359
  _globals['_LISTORGANIZATIONSRESPONSECACHE']._serialized_end=7456
  _globals['_LISTPROJECTSREQUEST']._serialized_start=7458
  _globals['_LISTPROJECTSREQUEST']._serialized_end=7495
  _globals['_CREATEPROJECTREQUEST']._serialized_start=7497
  _globals['_CREATEPROJECTREQUEST']._serialized_end=7586
  _globals['_CREATEPROJECTRESPONSE']._serialized_start=7588
  _globals['_CREATEPROJECTRESPONSE']._serialized_end=7684
  _globals['_LISTPROJECTSRESPONSECACHE']._serialized_start=7686
  _globals['_LISTPROJECTSRESPONSECACHE']._serialized_end=7768
  _globals['_CACHEDSESSION']._serialized_start=7770
  _globals['_CACHEDSESSION']._serialized_end=7827
  _globals['_CREATEACCESSTOKENREQUEST']._serialized_start=7829
  _globals['_CREATEACCESSTOKENREQUEST']._serialized_end=7940
  _globals['_CREATEACCESSTOKENRESPONSE']._serialized_start=7942
  _globals['_CREATEACCESSTOKENRESPONSE']._serialized_end=7985
  _globals['_LISTACCESSTOKENSREQUEST']._serialized_start=7987
  _globals['_LISTACCESSTOKENSREQUEST']._serialized_end=8028
  _globals['_GETACCESSTOKENRESPONSE']._serialized_start=8030
  _globals['_GETACCESSTOKENRESPONSE']._serialized_end=8109
  _globals['_GETACCESSTOKENREQUEST']._serialized_start=8111
  _globals['_GETACCESSTOKENREQUEST']._serialized_end=8149
  _globals['_REVOKEACCESSTOKENREQUEST']._serialized_start=8151
  _globals['_REVOKEACCESSTOKENREQUEST']._serialized_end=8208
  _globals['_REVOKEACCESSTOKENRESPONSE']._serialized_start=8210
  _globals['_REVOKEACCESSTOKENRESPONSE']._serialized_end=8253
# @@protoc_insertion_point(module_scope)
