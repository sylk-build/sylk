from typing import Tuple, Iterator, Any
import grpc
import sys
from functools import partial
from sylk.commons.interceptors import sylk_client_pre_rpc
import logging
from .sylk.Packages.v1 import Packages_pb2_grpc as PackagesService
from .sylk.Methods.v1 import Methods_pb2_grpc as MethodsService
from .sylk.Users.v1 import Users_pb2_grpc as UsersService
from .sylk.Enums.v1 import Enums_pb2_grpc as EnumsService
from .sylk.Messages.v1 import Messages_pb2_grpc as MessagesService
from .sylk.Organizations.v1 import Organizations_pb2_grpc as OrganizationsService
from .sylk.Fields.v1 import Fields_pb2_grpc as FieldsService
from .sylk.Projects.v1 import Projects_pb2_grpc as ProjectsService
from .sylk.EnumValues.v1 import EnumValues_pb2_grpc as EnumValuesService
from .sylk.Services.v1 import Services_pb2_grpc as ServicesService
from .sylk.SylkUser.v1 import SylkUser_pb2 as SylkUser
from .sylk.SylkMethod.v1 import SylkMethod_pb2 as SylkMethod
from .sylk.SylkPackage.v1 import SylkPackage_pb2 as SylkPackage
from .sylk.SylkCommons.v1 import SylkCommons_pb2 as SylkCommons
from .sylk.SylkMessage.v1 import SylkMessage_pb2 as SylkMessage
from .sylk.SylkConfigs.v1 import SylkConfigs_pb2 as SylkConfigs
from .sylk.SylkClient.v1 import SylkClient_pb2 as SylkClient
from .sylk.SylkProject.v1 import SylkProject_pb2 as SylkProject
from .sylk.SylkEnumValue.v1 import SylkEnumValue_pb2 as SylkEnumValue
from .sylk.SylkField.v1 import SylkField_pb2 as SylkField
from .sylk.SylkServer.v1 import SylkServer_pb2 as SylkServer
from .sylk.SylkApi.v1 import SylkApi_pb2 as SylkApi
from .sylk.Sylk.v1 import Sylk_pb2 as Sylk
from .sylk.SylkService.v1 import SylkService_pb2 as SylkService
from .sylk.SylkEnum.v1 import SylkEnum_pb2 as SylkEnum
from .sylk.SylkOrganization.v1 import SylkOrganization_pb2 as SylkOrganization

# For available channel options in python visit https://github.com/grpc/grpc/blob/v1.46.x/include/grpc/impl/codegen/grpc_types.h
_CHANNEL_OPTIONS = (("grpc.keepalive_permit_without_calls", 1),
	("grpc.keepalive_time_ms", 120000),
	("grpc.keepalive_timeout_ms", 20000),
	("grpc.http2.min_time_between_pings_ms", 120000),
	("grpc.http2.max_pings_without_data", 1),)

# Global metadata
_METADATA = (('sylk-version','0.1.2'),)

# Global auth key that will be verified by sylk client
_GLOBAL_AUTH_KEY = None

# Generated thanks to [sylk.build](https://www.sylk.build)
class sylkcore:

	def __init__(self, host="localhost", port=44880, timeout=10, log_level='ERROR'):
		logging.root.setLevel(log_level)
		self._sylk_global_auth_key = _GLOBAL_AUTH_KEY
		channel = grpc.insecure_channel('{0}:{1}'.format(host, port),_CHANNEL_OPTIONS)
		try:
			grpc.channel_ready_future(channel).result(timeout=timeout)
		except grpc.FutureTimeoutError:
			logging.error('Timed out: Server seems to be offline. Verify your connection configs.')
			sys.exit(1)
		self.PackagesStub = PackagesService.PackagesStub(channel)
		self.MethodsStub = MethodsService.MethodsStub(channel)
		self.UsersStub = UsersService.UsersStub(channel)
		self.EnumsStub = EnumsService.EnumsStub(channel)
		self.MessagesStub = MessagesService.MessagesStub(channel)
		self.OrganizationsStub = OrganizationsService.OrganizationsStub(channel)
		self.FieldsStub = FieldsService.FieldsStub(channel)
		self.ProjectsStub = ProjectsService.ProjectsStub(channel)
		self.EnumValuesStub = EnumValuesService.EnumValuesStub(channel)
		self.ServicesStub = ServicesService.ServicesStub(channel)

	
	def GetPackage_WithCall(self, request: SylkApi.GetPackageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetPackageResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.PackagesStub.GetPackage.with_call(request,metadata=metadata)

	
	def GetPackage(self, request: SylkApi.GetPackageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetPackageResponse:
		"""sylk - """

		return self.PackagesStub.GetPackage(request,metadata=metadata)

	
	def CreatePackage_WithCall(self, request: SylkApi.CreatePackageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.CreatePackageResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.PackagesStub.CreatePackage.with_call(request,metadata=metadata)

	
	def CreatePackage(self, request: SylkApi.CreatePackageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.CreatePackageResponse:
		"""sylk - """

		return self.PackagesStub.CreatePackage(request,metadata=metadata)

	
	def DeletePackage_WithCall(self, request: SylkApi.DeletePackageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.DeletePackageResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.PackagesStub.DeletePackage.with_call(request,metadata=metadata)

	
	def DeletePackage(self, request: SylkApi.DeletePackageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.DeletePackageResponse:
		"""sylk - """

		return self.PackagesStub.DeletePackage(request,metadata=metadata)

	
	def UpdatePackage_WithCall(self, request: SylkApi.UpdatePackageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdatePackageResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.PackagesStub.UpdatePackage.with_call(request,metadata=metadata)

	
	def UpdatePackage(self, request: SylkApi.UpdatePackageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdatePackageResponse:
		"""sylk - """

		return self.PackagesStub.UpdatePackage(request,metadata=metadata)

	
	def ListPackages_WithCall(self, request: SylkApi.ListPackagesRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[Iterator[SylkApi.GetPackageResponse], Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.PackagesStub.ListPackages.with_call(request,metadata=metadata)

	
	def ListPackages(self, request: SylkApi.ListPackagesRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Iterator[SylkApi.GetPackageResponse]:
		"""sylk - """

		return self.PackagesStub.ListPackages(request,metadata=metadata)

	
	def CreateMethod_WithCall(self, request: SylkApi.CreateMethodRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.CreateMethodResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.MethodsStub.CreateMethod.with_call(request,metadata=metadata)

	
	def CreateMethod(self, request: SylkApi.CreateMethodRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.CreateMethodResponse:
		"""sylk - """

		return self.MethodsStub.CreateMethod(request,metadata=metadata)

	
	def GetMethod_WithCall(self, request: SylkApi.GetMethodRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetMethodResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.MethodsStub.GetMethod.with_call(request,metadata=metadata)

	
	def GetMethod(self, request: SylkApi.GetMethodRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetMethodResponse:
		"""sylk - """

		return self.MethodsStub.GetMethod(request,metadata=metadata)

	
	def DeleteMethod_WithCall(self, request: SylkApi.DeleteMethodRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.DeleteMethodResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.MethodsStub.DeleteMethod.with_call(request,metadata=metadata)

	
	def DeleteMethod(self, request: SylkApi.DeleteMethodRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.DeleteMethodResponse:
		"""sylk - """

		return self.MethodsStub.DeleteMethod(request,metadata=metadata)

	
	def UpdateMethod_WithCall(self, request: SylkApi.UpdateMethodRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateMethodResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.MethodsStub.UpdateMethod.with_call(request,metadata=metadata)

	
	def UpdateMethod(self, request: SylkApi.UpdateMethodRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateMethodResponse:
		"""sylk - """

		return self.MethodsStub.UpdateMethod(request,metadata=metadata)

	
	def CreateUser_WithCall(self, request: SylkApi.CreateUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.CreateUserResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.UsersStub.CreateUser.with_call(request,metadata=metadata)

	
	def CreateUser(self, request: SylkApi.CreateUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.CreateUserResponse:
		"""sylk - """

		return self.UsersStub.CreateUser(request,metadata=metadata)

	
	def GetAccessToken_WithCall(self, request: SylkApi.GetAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetAccessTokenResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.UsersStub.GetAccessToken.with_call(request,metadata=metadata)

	
	def GetAccessToken(self, request: SylkApi.GetAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetAccessTokenResponse:
		"""sylk - """

		return self.UsersStub.GetAccessToken(request,metadata=metadata)

	
	def CreateAccessToken_WithCall(self, request: SylkApi.CreateAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.CreateAccessTokenResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.UsersStub.CreateAccessToken.with_call(request,metadata=metadata)

	
	def CreateAccessToken(self, request: SylkApi.CreateAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.CreateAccessTokenResponse:
		"""sylk - """

		return self.UsersStub.CreateAccessToken(request,metadata=metadata)

	
	def GetUser_WithCall(self, request: SylkApi.GetUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetUserResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.UsersStub.GetUser.with_call(request,metadata=metadata)

	
	def GetUser(self, request: SylkApi.GetUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetUserResponse:
		"""sylk - """

		return self.UsersStub.GetUser(request,metadata=metadata)

	
	def ListAccessTokens_WithCall(self, request: SylkApi.ListAccessTokensRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[Iterator[SylkApi.GetAccessTokenResponse], Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.UsersStub.ListAccessTokens.with_call(request,metadata=metadata)

	
	def ListAccessTokens(self, request: SylkApi.ListAccessTokensRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Iterator[SylkApi.GetAccessTokenResponse]:
		"""sylk - """

		return self.UsersStub.ListAccessTokens(request,metadata=metadata)

	
	def RevokeAccessToken_WithCall(self, request: SylkApi.RevokeAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.RevokeAccessTokenResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.UsersStub.RevokeAccessToken.with_call(request,metadata=metadata)

	
	def RevokeAccessToken(self, request: SylkApi.RevokeAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.RevokeAccessTokenResponse:
		"""sylk - """

		return self.UsersStub.RevokeAccessToken(request,metadata=metadata)

	
	def UpdateUser_WithCall(self, request: SylkApi.UpdateUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateUserResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.UsersStub.UpdateUser.with_call(request,metadata=metadata)

	
	def UpdateUser(self, request: SylkApi.UpdateUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateUserResponse:
		"""sylk - """

		return self.UsersStub.UpdateUser(request,metadata=metadata)

	
	def GetEnum_WithCall(self, request: SylkApi.GetEnumRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetEnumResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.EnumsStub.GetEnum.with_call(request,metadata=metadata)

	
	def GetEnum(self, request: SylkApi.GetEnumRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetEnumResponse:
		"""sylk - """

		return self.EnumsStub.GetEnum(request,metadata=metadata)

	
	def UpdateEnum_WithCall(self, request: SylkApi.UpdateEnumRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateEnumResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.EnumsStub.UpdateEnum.with_call(request,metadata=metadata)

	
	def UpdateEnum(self, request: SylkApi.UpdateEnumRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateEnumResponse:
		"""sylk - """

		return self.EnumsStub.UpdateEnum(request,metadata=metadata)

	
	def DeleteEnum_WithCall(self, request: SylkApi.DeleteEnumRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.DeleteEnumResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.EnumsStub.DeleteEnum.with_call(request,metadata=metadata)

	
	def DeleteEnum(self, request: SylkApi.DeleteEnumRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.DeleteEnumResponse:
		"""sylk - """

		return self.EnumsStub.DeleteEnum(request,metadata=metadata)

	
	def CreateEnum_WithCall(self, request: SylkApi.CreateEnumRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.CreateEnumResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.EnumsStub.CreateEnum.with_call(request,metadata=metadata)

	
	def CreateEnum(self, request: SylkApi.CreateEnumRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.CreateEnumResponse:
		"""sylk - """

		return self.EnumsStub.CreateEnum(request,metadata=metadata)

	
	def GetMessage_WithCall(self, request: SylkApi.GetMessageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetMessageResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.MessagesStub.GetMessage.with_call(request,metadata=metadata)

	
	def GetMessage(self, request: SylkApi.GetMessageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetMessageResponse:
		"""sylk - """

		return self.MessagesStub.GetMessage(request,metadata=metadata)

	
	def UpdateMessage_WithCall(self, request: SylkApi.UpdateMessageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateMessageResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.MessagesStub.UpdateMessage.with_call(request,metadata=metadata)

	
	def UpdateMessage(self, request: SylkApi.UpdateMessageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateMessageResponse:
		"""sylk - """

		return self.MessagesStub.UpdateMessage(request,metadata=metadata)

	
	def CreateMessage_WithCall(self, request: SylkApi.CreateMessageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.CreateMessageResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.MessagesStub.CreateMessage.with_call(request,metadata=metadata)

	
	def CreateMessage(self, request: SylkApi.CreateMessageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.CreateMessageResponse:
		"""sylk - """

		return self.MessagesStub.CreateMessage(request,metadata=metadata)

	
	def DeleteMessage_WithCall(self, request: SylkApi.DeleteMessageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.DeleteMessageResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.MessagesStub.DeleteMessage.with_call(request,metadata=metadata)

	
	def DeleteMessage(self, request: SylkApi.DeleteMessageRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.DeleteMessageResponse:
		"""sylk - """

		return self.MessagesStub.DeleteMessage(request,metadata=metadata)

	
	def AcceprUserInvite_WithCall(self, request: SylkApi.AcceptUserInviteRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.AcceptUserInviteResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.AcceprUserInvite.with_call(request,metadata=metadata)

	
	def AcceprUserInvite(self, request: SylkApi.AcceptUserInviteRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.AcceptUserInviteResponse:
		"""sylk - """

		return self.OrganizationsStub.AcceprUserInvite(request,metadata=metadata)

	
	def GetOrganization_WithCall(self, request: SylkApi.GetOrganizationRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetOrganizationResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.GetOrganization.with_call(request,metadata=metadata)

	
	def GetOrganization(self, request: SylkApi.GetOrganizationRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetOrganizationResponse:
		"""sylk - """

		return self.OrganizationsStub.GetOrganization(request,metadata=metadata)

	
	def UpdateOrganization_WithCall(self, request: SylkApi.UpdateOrganizationRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateOrganizationResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.UpdateOrganization.with_call(request,metadata=metadata)

	
	def UpdateOrganization(self, request: SylkApi.UpdateOrganizationRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateOrganizationResponse:
		"""sylk - """

		return self.OrganizationsStub.UpdateOrganization(request,metadata=metadata)

	
	def ListOrganizations_WithCall(self, request: SylkApi.ListOrganizationsRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[Iterator[SylkApi.GetOrganizationResponse], Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.ListOrganizations.with_call(request,metadata=metadata)

	
	def ListOrganizations(self, request: SylkApi.ListOrganizationsRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Iterator[SylkApi.GetOrganizationResponse]:
		"""sylk - """

		return self.OrganizationsStub.ListOrganizations(request,metadata=metadata)

	
	def AddUser_WithCall(self, request: SylkApi.AddUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.AddUserResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.AddUser.with_call(request,metadata=metadata)

	
	def AddUser(self, request: SylkApi.AddUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.AddUserResponse:
		"""sylk - """

		return self.OrganizationsStub.AddUser(request,metadata=metadata)

	
	def UpdateUserStatus_WithCall(self, request: SylkApi.UpdateUserStatusRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateUserStatusResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.UpdateUserStatus.with_call(request,metadata=metadata)

	
	def UpdateUserStatus(self, request: SylkApi.UpdateUserStatusRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateUserStatusResponse:
		"""sylk - """

		return self.OrganizationsStub.UpdateUserStatus(request,metadata=metadata)

	
	def RemoveUser_WithCall(self, request: SylkApi.RemoveUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.RemoveUserResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.RemoveUser.with_call(request,metadata=metadata)

	
	def RemoveUser(self, request: SylkApi.RemoveUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.RemoveUserResponse:
		"""sylk - """

		return self.OrganizationsStub.RemoveUser(request,metadata=metadata)

	
	def UpdateUserRole_WithCall(self, request: SylkApi.UpdateUserRoleRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateUserRoleResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.UpdateUserRole.with_call(request,metadata=metadata)

	
	def UpdateUserRole(self, request: SylkApi.UpdateUserRoleRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateUserRoleResponse:
		"""sylk - """

		return self.OrganizationsStub.UpdateUserRole(request,metadata=metadata)

	
	def CreateField_WithCall(self, request: SylkApi.CreateFieldRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.CreateFieldResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.FieldsStub.CreateField.with_call(request,metadata=metadata)

	
	def CreateField(self, request: SylkApi.CreateFieldRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.CreateFieldResponse:
		"""sylk - """

		return self.FieldsStub.CreateField(request,metadata=metadata)

	
	def GetField_WithCall(self, request: SylkApi.GetFieldRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetFieldResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.FieldsStub.GetField.with_call(request,metadata=metadata)

	
	def GetField(self, request: SylkApi.GetFieldRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetFieldResponse:
		"""sylk - """

		return self.FieldsStub.GetField(request,metadata=metadata)

	
	def DeleteField_WithCall(self, request: SylkApi.DeleteFieldRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.DeleteFieldResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.FieldsStub.DeleteField.with_call(request,metadata=metadata)

	
	def DeleteField(self, request: SylkApi.DeleteFieldRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.DeleteFieldResponse:
		"""sylk - """

		return self.FieldsStub.DeleteField(request,metadata=metadata)

	
	def UpdateField_WithCall(self, request: SylkApi.UpdateFieldRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateFieldResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.FieldsStub.UpdateField.with_call(request,metadata=metadata)

	
	def UpdateField(self, request: SylkApi.UpdateFieldRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateFieldResponse:
		"""sylk - """

		return self.FieldsStub.UpdateField(request,metadata=metadata)

	
	def UpdateUserRoleProject_WithCall(self, request: SylkApi.UpdateUserRoleRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateUserRoleResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ProjectsStub.UpdateUserRoleProject.with_call(request,metadata=metadata)

	
	def UpdateUserRoleProject(self, request: SylkApi.UpdateUserRoleRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateUserRoleResponse:
		"""sylk - """

		return self.ProjectsStub.UpdateUserRoleProject(request,metadata=metadata)

	
	def RemoveUserProject_WithCall(self, request: SylkApi.RemoveUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.RemoveUserResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ProjectsStub.RemoveUserProject.with_call(request,metadata=metadata)

	
	def RemoveUserProject(self, request: SylkApi.RemoveUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.RemoveUserResponse:
		"""sylk - """

		return self.ProjectsStub.RemoveUserProject(request,metadata=metadata)

	
	def AddUserProject_WithCall(self, request: SylkApi.AddUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.AddUserResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ProjectsStub.AddUserProject.with_call(request,metadata=metadata)

	
	def AddUserProject(self, request: SylkApi.AddUserRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.AddUserResponse:
		"""sylk - """

		return self.ProjectsStub.AddUserProject(request,metadata=metadata)

	
	def GetProject_WithCall(self, request: SylkApi.GetProjectRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetProjectResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ProjectsStub.GetProject.with_call(request,metadata=metadata)

	
	def GetProject(self, request: SylkApi.GetProjectRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetProjectResponse:
		"""sylk - """

		return self.ProjectsStub.GetProject(request,metadata=metadata)

	
	def UpdateProject_WithCall(self, request: SylkApi.UpdateProjectRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateProjectResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ProjectsStub.UpdateProject.with_call(request,metadata=metadata)

	
	def UpdateProject(self, request: SylkApi.UpdateProjectRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateProjectResponse:
		"""sylk - """

		return self.ProjectsStub.UpdateProject(request,metadata=metadata)

	
	def CreateProject_WithCall(self, request: SylkApi.CreateProjectRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.CreateProjectResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ProjectsStub.CreateProject.with_call(request,metadata=metadata)

	
	def CreateProject(self, request: SylkApi.CreateProjectRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.CreateProjectResponse:
		"""sylk - """

		return self.ProjectsStub.CreateProject(request,metadata=metadata)

	
	def DeleteProject_WithCall(self, request: SylkApi.DeleteProjectRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.DeleteProjectResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ProjectsStub.DeleteProject.with_call(request,metadata=metadata)

	
	def DeleteProject(self, request: SylkApi.DeleteProjectRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.DeleteProjectResponse:
		"""sylk - """

		return self.ProjectsStub.DeleteProject(request,metadata=metadata)

	
	def ListProjects_WithCall(self, request: SylkApi.ListProjectsRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[Iterator[SylkApi.GetProjectResponse], Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ProjectsStub.ListProjects.with_call(request,metadata=metadata)

	
	def ListProjects(self, request: SylkApi.ListProjectsRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Iterator[SylkApi.GetProjectResponse]:
		"""sylk - """

		return self.ProjectsStub.ListProjects(request,metadata=metadata)

	
	def UpdateUserStatusProject_WithCall(self, request: SylkApi.UpdateUserStatusRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateUserStatusResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ProjectsStub.UpdateUserStatusProject.with_call(request,metadata=metadata)

	
	def UpdateUserStatusProject(self, request: SylkApi.UpdateUserStatusRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateUserStatusResponse:
		"""sylk - """

		return self.ProjectsStub.UpdateUserStatusProject(request,metadata=metadata)

	
	def GetEnumValue_WithCall(self, request: SylkApi.GetEnumValueRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetEnumValueResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.EnumValuesStub.GetEnumValue.with_call(request,metadata=metadata)

	
	def GetEnumValue(self, request: SylkApi.GetEnumValueRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetEnumValueResponse:
		"""sylk - """

		return self.EnumValuesStub.GetEnumValue(request,metadata=metadata)

	
	def CreateEnumValue_WithCall(self, request: SylkApi.CreateEnumValueRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.CreateEnumValueResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.EnumValuesStub.CreateEnumValue.with_call(request,metadata=metadata)

	
	def CreateEnumValue(self, request: SylkApi.CreateEnumValueRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.CreateEnumValueResponse:
		"""sylk - """

		return self.EnumValuesStub.CreateEnumValue(request,metadata=metadata)

	
	def DeleteEnumValue_WithCall(self, request: SylkApi.DeleteEnumValueRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.DeleteEnumValueResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.EnumValuesStub.DeleteEnumValue.with_call(request,metadata=metadata)

	
	def DeleteEnumValue(self, request: SylkApi.DeleteEnumValueRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.DeleteEnumValueResponse:
		"""sylk - """

		return self.EnumValuesStub.DeleteEnumValue(request,metadata=metadata)

	
	def UpdateEnumValue_WithCall(self, request: SylkApi.UpdateEnumValueRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateEnumValueResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.EnumValuesStub.UpdateEnumValue.with_call(request,metadata=metadata)

	
	def UpdateEnumValue(self, request: SylkApi.UpdateEnumValueRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateEnumValueResponse:
		"""sylk - """

		return self.EnumValuesStub.UpdateEnumValue(request,metadata=metadata)

	
	def CreateService_WithCall(self, request: SylkApi.CreateServiceRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.CreateServiceResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ServicesStub.CreateService.with_call(request,metadata=metadata)

	
	def CreateService(self, request: SylkApi.CreateServiceRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.CreateServiceResponse:
		"""sylk - """

		return self.ServicesStub.CreateService(request,metadata=metadata)

	
	def GetService_WithCall(self, request: SylkApi.GetServiceRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.GetServiceResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ServicesStub.GetService.with_call(request,metadata=metadata)

	
	def GetService(self, request: SylkApi.GetServiceRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.GetServiceResponse:
		"""sylk - """

		return self.ServicesStub.GetService(request,metadata=metadata)

	
	def UpdateService_WithCall(self, request: SylkApi.UpdateServiceRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.UpdateServiceResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ServicesStub.UpdateService.with_call(request,metadata=metadata)

	
	def UpdateService(self, request: SylkApi.UpdateServiceRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.UpdateServiceResponse:
		"""sylk - """

		return self.ServicesStub.UpdateService(request,metadata=metadata)

	
	def ListServices_WithCall(self, request: SylkApi.ListServicesRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[Iterator[SylkApi.GetServiceResponse], Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ServicesStub.ListServices.with_call(request,metadata=metadata)

	
	def ListServices(self, request: SylkApi.ListServicesRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Iterator[SylkApi.GetServiceResponse]:
		"""sylk - """

		return self.ServicesStub.ListServices(request,metadata=metadata)

	
	def DeleteService_WithCall(self, request: SylkApi.DeleteServiceRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> Tuple[SylkApi.DeleteServiceResponse, Any]:
		"""sylk -  Returns: RPC output and a call object"""

		return self.ServicesStub.DeleteService.with_call(request,metadata=metadata)

	
	def DeleteService(self, request: SylkApi.DeleteServiceRequest, metadata: Tuple[Tuple[str,str]] = _METADATA) -> SylkApi.DeleteServiceResponse:
		"""sylk - """

		return self.ServicesStub.DeleteService(request,metadata=metadata)