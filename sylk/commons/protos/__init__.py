from typing import Tuple, Iterator, Any
import grpc
import sys
from functools import partial
from . import Packages_pb2_grpc as PackagesService
from . import Projects_pb2_grpc as ProjectsService
from . import Users_pb2_grpc as UsersService
from . import Organizations_pb2_grpc as OrganizationsService
from . import Messages_pb2_grpc as MessagesService
from . import Methods_pb2_grpc as MethodsService
from . import Enums_pb2_grpc as EnumsService
from . import Fields_pb2_grpc as FieldsService
from . import Services_pb2_grpc as ServicesService
from . import EnumValues_pb2_grpc as EnumValuesService
from . import Sylk_pb2 as Sylk
from . import SylkEnum_pb2 as SylkEnum
from . import SylkOrganization_pb2 as SylkOrganization
from . import SylkMessage_pb2 as SylkMessage
from . import SylkField_pb2 as SylkField
from . import SylkServer_pb2 as SylkServer
from . import SylkPackage_pb2 as SylkPackage
from . import SylkProject_pb2 as SylkProject
from . import SylkClient_pb2 as SylkClient
from . import SylkCommons_pb2 as SylkCommons
from . import SylkConfigs_pb2 as SylkConfigs
from . import SylkApi_pb2 as SylkApi
from . import SylkEnumValue_pb2 as SylkEnumValue
from . import SylkUser_pb2 as SylkUser
from . import SylkMethod_pb2 as SylkMethod
from . import SylkService_pb2 as SylkService

# For available channel options in python visit https://github.com/grpc/grpc/blob/v1.46.x/include/grpc/impl/codegen/grpc_types.h
_CHANNEL_OPTIONS = (("grpc.keepalive_permit_without_calls", 1),
	("grpc.keepalive_time_ms", 120000),
	("grpc.keepalive_timeout_ms", 20000),
	("grpc.http2.min_time_between_pings_ms", 120000),
	("grpc.http2.max_pings_without_data", 1),)

class sylkcore:

	def __init__(self, host="localhost", port=50051, timeout=10):
		channel = grpc.insecure_channel('{0}:{1}'.format(host, port),_CHANNEL_OPTIONS)
		try:
			grpc.channel_ready_future(channel).result(timeout=timeout)
		except grpc.FutureTimeoutError:
			sys.exit('Error connecting to server')
		self.PackagesStub = PackagesService.PackagesStub(channel)
		self.ProjectsStub = ProjectsService.ProjectsStub(channel)
		self.UsersStub = UsersService.UsersStub(channel)
		self.OrganizationsStub = OrganizationsService.OrganizationsStub(channel)
		self.MessagesStub = MessagesService.MessagesStub(channel)
		self.MethodsStub = MethodsService.MethodsStub(channel)
		self.EnumsStub = EnumsService.EnumsStub(channel)
		self.FieldsStub = FieldsService.FieldsStub(channel)
		self.ServicesStub = ServicesService.ServicesStub(channel)
		self.EnumValuesStub = EnumValuesService.EnumValuesStub(channel)

	def GetPackage_WithCall(self, request: SylkApi.GetPackageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetPackageResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.PackagesStub.GetPackage.with_call(request,metadata=metadata)

	def GetPackage(self, request: SylkApi.GetPackageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetPackageResponse:
		"""webezyio - """

		return self.PackagesStub.GetPackage(request,metadata=metadata)

	def CreatePackage_WithCall(self, request: SylkApi.CreatePackageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.CreatePackageResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.PackagesStub.CreatePackage.with_call(request,metadata=metadata)

	def CreatePackage(self, request: SylkApi.CreatePackageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.CreatePackageResponse:
		"""webezyio - """

		return self.PackagesStub.CreatePackage(request,metadata=metadata)

	def UpdatePackage_WithCall(self, request: SylkApi.UpdatePackageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdatePackageResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.PackagesStub.UpdatePackage.with_call(request,metadata=metadata)

	def UpdatePackage(self, request: SylkApi.UpdatePackageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdatePackageResponse:
		"""webezyio - """

		return self.PackagesStub.UpdatePackage(request,metadata=metadata)

	def DeletePackage_WithCall(self, request: SylkApi.DeletePackageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.DeletePackageResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.PackagesStub.DeletePackage.with_call(request,metadata=metadata)

	def DeletePackage(self, request: SylkApi.DeletePackageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.DeletePackageResponse:
		"""webezyio - """

		return self.PackagesStub.DeletePackage(request,metadata=metadata)

	def ListPackages_WithCall(self, request: SylkApi.ListPackagesRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[Iterator[SylkApi.GetPackageResponse], Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.PackagesStub.ListPackages.with_call(request,metadata=metadata)

	def ListPackages(self, request: SylkApi.ListPackagesRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Iterator[SylkApi.GetPackageResponse]:
		"""webezyio - """

		return self.PackagesStub.ListPackages(request,metadata=metadata)

	def GetProject_WithCall(self, request: SylkApi.GetProjectRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetProjectResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ProjectsStub.GetProject.with_call(request,metadata=metadata)

	def GetProject(self, request: SylkApi.GetProjectRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetProjectResponse:
		"""webezyio - """

		return self.ProjectsStub.GetProject(request,metadata=metadata)

	def UpdateProject_WithCall(self, request: SylkApi.UpdateProjectRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateProjectResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ProjectsStub.UpdateProject.with_call(request,metadata=metadata)

	def UpdateProject(self, request: SylkApi.UpdateProjectRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateProjectResponse:
		"""webezyio - """

		return self.ProjectsStub.UpdateProject(request,metadata=metadata)

	def DeleteProject_WithCall(self, request: SylkApi.DeleteProjectRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.DeleteProjectResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ProjectsStub.DeleteProject.with_call(request,metadata=metadata)

	def DeleteProject(self, request: SylkApi.DeleteProjectRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.DeleteProjectResponse:
		"""webezyio - """

		return self.ProjectsStub.DeleteProject(request,metadata=metadata)

	def AddUserProject_WithCall(self, request: SylkApi.AddUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.AddUserResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ProjectsStub.AddUserProject.with_call(request,metadata=metadata)

	def AddUserProject(self, request: SylkApi.AddUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.AddUserResponse:
		"""webezyio - """

		return self.ProjectsStub.AddUserProject(request,metadata=metadata)

	def UpdateUserRoleProject_WithCall(self, request: SylkApi.UpdateUserRoleRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateUserRoleResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ProjectsStub.UpdateUserRoleProject.with_call(request,metadata=metadata)

	def UpdateUserRoleProject(self, request: SylkApi.UpdateUserRoleRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateUserRoleResponse:
		"""webezyio - """

		return self.ProjectsStub.UpdateUserRoleProject(request,metadata=metadata)

	def UpdateUserStatusProject_WithCall(self, request: SylkApi.UpdateUserStatusRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateUserStatusResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ProjectsStub.UpdateUserStatusProject.with_call(request,metadata=metadata)

	def UpdateUserStatusProject(self, request: SylkApi.UpdateUserStatusRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateUserStatusResponse:
		"""webezyio - """

		return self.ProjectsStub.UpdateUserStatusProject(request,metadata=metadata)

	def RemoveUserProject_WithCall(self, request: SylkApi.RemoveUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.RemoveUserResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ProjectsStub.RemoveUserProject.with_call(request,metadata=metadata)

	def RemoveUserProject(self, request: SylkApi.RemoveUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.RemoveUserResponse:
		"""webezyio - """

		return self.ProjectsStub.RemoveUserProject(request,metadata=metadata)

	def ListProjects_WithCall(self, request: SylkApi.ListProjectsRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[Iterator[SylkApi.GetProjectResponse], Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ProjectsStub.ListProjects.with_call(request,metadata=metadata)

	def ListProjects(self, request: SylkApi.ListProjectsRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Iterator[SylkApi.GetProjectResponse]:
		"""webezyio - """

		return self.ProjectsStub.ListProjects(request,metadata=metadata)

	def CreateProject_WithCall(self, request: SylkApi.CreateProjectRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.CreateProjectResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ProjectsStub.CreateProject.with_call(request,metadata=metadata)

	def CreateProject(self, request: SylkApi.CreateProjectRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.CreateProjectResponse:
		"""webezyio - """

		return self.ProjectsStub.CreateProject(request,metadata=metadata)

	def GetUser_WithCall(self, request: SylkApi.GetUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetUserResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.UsersStub.GetUser.with_call(request,metadata=metadata)

	def GetUser(self, request: SylkApi.GetUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetUserResponse:
		"""webezyio - """

		return self.UsersStub.GetUser(request,metadata=metadata)

	def UpdateUser_WithCall(self, request: SylkApi.UpdateUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateUserResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.UsersStub.UpdateUser.with_call(request,metadata=metadata)

	def UpdateUser(self, request: SylkApi.UpdateUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateUserResponse:
		"""webezyio - """

		return self.UsersStub.UpdateUser(request,metadata=metadata)

	def CreateUser_WithCall(self, request: SylkApi.CreateUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.CreateUserResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.UsersStub.CreateUser.with_call(request,metadata=metadata)

	def CreateUser(self, request: SylkApi.CreateUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.CreateUserResponse:
		"""webezyio - """

		return self.UsersStub.CreateUser(request,metadata=metadata)

	def CreateAccessToken_WithCall(self, request: SylkApi.CreateAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.CreateAccessTokenResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.UsersStub.CreateAccessToken.with_call(request,metadata=metadata)

	def CreateAccessToken(self, request: SylkApi.CreateAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.CreateAccessTokenResponse:
		"""webezyio - """

		return self.UsersStub.CreateAccessToken(request,metadata=metadata)

	def GetAccessToken_WithCall(self, request: SylkApi.GetAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetAccessTokenResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.UsersStub.GetAccessToken.with_call(request,metadata=metadata)

	def GetAccessToken(self, request: SylkApi.GetAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetAccessTokenResponse:
		"""webezyio - """

		return self.UsersStub.GetAccessToken(request,metadata=metadata)

	def ListAccessTokens_WithCall(self, request: SylkApi.ListAccessTokensRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[Iterator[SylkApi.GetAccessTokenResponse], Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.UsersStub.ListAccessTokens.with_call(request,metadata=metadata)

	def ListAccessTokens(self, request: SylkApi.ListAccessTokensRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Iterator[SylkApi.GetAccessTokenResponse]:
		"""webezyio - """

		return self.UsersStub.ListAccessTokens(request,metadata=metadata)

	def RevokeAccessToken_WithCall(self, request: SylkApi.RevokeAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.RevokeAccessTokenResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.UsersStub.RevokeAccessToken.with_call(request,metadata=metadata)

	def RevokeAccessToken(self, request: SylkApi.RevokeAccessTokenRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.RevokeAccessTokenResponse:
		"""webezyio - """

		return self.UsersStub.RevokeAccessToken(request,metadata=metadata)

	def GetOrganization_WithCall(self, request: SylkApi.GetOrganizationRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetOrganizationResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.GetOrganization.with_call(request,metadata=metadata)

	def GetOrganization(self, request: SylkApi.GetOrganizationRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetOrganizationResponse:
		"""webezyio - """

		return self.OrganizationsStub.GetOrganization(request,metadata=metadata)

	def UpdateOrganization_WithCall(self, request: SylkApi.UpdateOrganizationRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateOrganizationResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.UpdateOrganization.with_call(request,metadata=metadata)

	def UpdateOrganization(self, request: SylkApi.UpdateOrganizationRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateOrganizationResponse:
		"""webezyio - """

		return self.OrganizationsStub.UpdateOrganization(request,metadata=metadata)

	def ListOrganizations_WithCall(self, request: SylkApi.ListOrganizationsRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[Iterator[SylkApi.GetOrganizationResponse], Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.ListOrganizations.with_call(request,metadata=metadata)

	def ListOrganizations(self, request: SylkApi.ListOrganizationsRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Iterator[SylkApi.GetOrganizationResponse]:
		"""webezyio - """

		return self.OrganizationsStub.ListOrganizations(request,metadata=metadata)

	def AcceprUserInvite_WithCall(self, request: SylkApi.AcceptUserInviteRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.AcceptUserInviteResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.AcceprUserInvite.with_call(request,metadata=metadata)

	def AcceprUserInvite(self, request: SylkApi.AcceptUserInviteRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.AcceptUserInviteResponse:
		"""webezyio - """

		return self.OrganizationsStub.AcceprUserInvite(request,metadata=metadata)

	def AddUser_WithCall(self, request: SylkApi.AddUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.AddUserResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.AddUser.with_call(request,metadata=metadata)

	def AddUser(self, request: SylkApi.AddUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.AddUserResponse:
		"""webezyio - """

		return self.OrganizationsStub.AddUser(request,metadata=metadata)

	def UpdateUserRole_WithCall(self, request: SylkApi.UpdateUserRoleRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateUserRoleResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.UpdateUserRole.with_call(request,metadata=metadata)

	def UpdateUserRole(self, request: SylkApi.UpdateUserRoleRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateUserRoleResponse:
		"""webezyio - """

		return self.OrganizationsStub.UpdateUserRole(request,metadata=metadata)

	def UpdateUserStatus_WithCall(self, request: SylkApi.UpdateUserStatusRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateUserStatusResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.UpdateUserStatus.with_call(request,metadata=metadata)

	def UpdateUserStatus(self, request: SylkApi.UpdateUserStatusRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateUserStatusResponse:
		"""webezyio - """

		return self.OrganizationsStub.UpdateUserStatus(request,metadata=metadata)

	def RemoveUser_WithCall(self, request: SylkApi.RemoveUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.RemoveUserResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.OrganizationsStub.RemoveUser.with_call(request,metadata=metadata)

	def RemoveUser(self, request: SylkApi.RemoveUserRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.RemoveUserResponse:
		"""webezyio - """

		return self.OrganizationsStub.RemoveUser(request,metadata=metadata)

	def GetMessage_WithCall(self, request: SylkApi.GetMessageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetMessageResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.MessagesStub.GetMessage.with_call(request,metadata=metadata)

	def GetMessage(self, request: SylkApi.GetMessageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetMessageResponse:
		"""webezyio - """

		return self.MessagesStub.GetMessage(request,metadata=metadata)

	def CreateMessage_WithCall(self, request: SylkApi.CreateMessageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.CreateMessageResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.MessagesStub.CreateMessage.with_call(request,metadata=metadata)

	def CreateMessage(self, request: SylkApi.CreateMessageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.CreateMessageResponse:
		"""webezyio - """

		return self.MessagesStub.CreateMessage(request,metadata=metadata)

	def UpdateMessage_WithCall(self, request: SylkApi.UpdateMessageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateMessageResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.MessagesStub.UpdateMessage.with_call(request,metadata=metadata)

	def UpdateMessage(self, request: SylkApi.UpdateMessageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateMessageResponse:
		"""webezyio - """

		return self.MessagesStub.UpdateMessage(request,metadata=metadata)

	def DeleteMessage_WithCall(self, request: SylkApi.DeleteMessageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.DeleteMessageResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.MessagesStub.DeleteMessage.with_call(request,metadata=metadata)

	def DeleteMessage(self, request: SylkApi.DeleteMessageRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.DeleteMessageResponse:
		"""webezyio - """

		return self.MessagesStub.DeleteMessage(request,metadata=metadata)

	def GetMethod_WithCall(self, request: SylkApi.GetMethodRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetMethodResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.MethodsStub.GetMethod.with_call(request,metadata=metadata)

	def GetMethod(self, request: SylkApi.GetMethodRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetMethodResponse:
		"""webezyio - """

		return self.MethodsStub.GetMethod(request,metadata=metadata)

	def CreateMethod_WithCall(self, request: SylkApi.CreateMethodRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.CreateMethodResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.MethodsStub.CreateMethod.with_call(request,metadata=metadata)

	def CreateMethod(self, request: SylkApi.CreateMethodRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.CreateMethodResponse:
		"""webezyio - """

		return self.MethodsStub.CreateMethod(request,metadata=metadata)

	def UpdateMethod_WithCall(self, request: SylkApi.UpdateMethodRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateMethodResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.MethodsStub.UpdateMethod.with_call(request,metadata=metadata)

	def UpdateMethod(self, request: SylkApi.UpdateMethodRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateMethodResponse:
		"""webezyio - """

		return self.MethodsStub.UpdateMethod(request,metadata=metadata)

	def DeleteMethod_WithCall(self, request: SylkApi.DeleteMethodRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.DeleteMethodResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.MethodsStub.DeleteMethod.with_call(request,metadata=metadata)

	def DeleteMethod(self, request: SylkApi.DeleteMethodRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.DeleteMethodResponse:
		"""webezyio - """

		return self.MethodsStub.DeleteMethod(request,metadata=metadata)

	def GetEnum_WithCall(self, request: SylkApi.GetEnumRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetEnumResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.EnumsStub.GetEnum.with_call(request,metadata=metadata)

	def GetEnum(self, request: SylkApi.GetEnumRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetEnumResponse:
		"""webezyio - """

		return self.EnumsStub.GetEnum(request,metadata=metadata)

	def CreateEnum_WithCall(self, request: SylkApi.CreateEnumRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.CreateEnumResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.EnumsStub.CreateEnum.with_call(request,metadata=metadata)

	def CreateEnum(self, request: SylkApi.CreateEnumRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.CreateEnumResponse:
		"""webezyio - """

		return self.EnumsStub.CreateEnum(request,metadata=metadata)

	def UpdateEnum_WithCall(self, request: SylkApi.UpdateEnumRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateEnumResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.EnumsStub.UpdateEnum.with_call(request,metadata=metadata)

	def UpdateEnum(self, request: SylkApi.UpdateEnumRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateEnumResponse:
		"""webezyio - """

		return self.EnumsStub.UpdateEnum(request,metadata=metadata)

	def DeleteEnum_WithCall(self, request: SylkApi.DeleteEnumRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.DeleteEnumResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.EnumsStub.DeleteEnum.with_call(request,metadata=metadata)

	def DeleteEnum(self, request: SylkApi.DeleteEnumRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.DeleteEnumResponse:
		"""webezyio - """

		return self.EnumsStub.DeleteEnum(request,metadata=metadata)

	def GetField_WithCall(self, request: SylkApi.GetFieldRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetFieldResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.FieldsStub.GetField.with_call(request,metadata=metadata)

	def GetField(self, request: SylkApi.GetFieldRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetFieldResponse:
		"""webezyio - """

		return self.FieldsStub.GetField(request,metadata=metadata)

	def CreateField_WithCall(self, request: SylkApi.CreateFieldRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.CreateFieldResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.FieldsStub.CreateField.with_call(request,metadata=metadata)

	def CreateField(self, request: SylkApi.CreateFieldRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.CreateFieldResponse:
		"""webezyio - """

		return self.FieldsStub.CreateField(request,metadata=metadata)

	def UpdateField_WithCall(self, request: SylkApi.UpdateFieldRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateFieldResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.FieldsStub.UpdateField.with_call(request,metadata=metadata)

	def UpdateField(self, request: SylkApi.UpdateFieldRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateFieldResponse:
		"""webezyio - """

		return self.FieldsStub.UpdateField(request,metadata=metadata)

	def DeleteField_WithCall(self, request: SylkApi.DeleteFieldRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.DeleteFieldResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.FieldsStub.DeleteField.with_call(request,metadata=metadata)

	def DeleteField(self, request: SylkApi.DeleteFieldRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.DeleteFieldResponse:
		"""webezyio - """

		return self.FieldsStub.DeleteField(request,metadata=metadata)

	def GetService_WithCall(self, request: SylkApi.GetServiceRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetServiceResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ServicesStub.GetService.with_call(request,metadata=metadata)

	def GetService(self, request: SylkApi.GetServiceRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetServiceResponse:
		"""webezyio - """

		return self.ServicesStub.GetService(request,metadata=metadata)

	def CreateService_WithCall(self, request: SylkApi.CreateServiceRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.CreateServiceResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ServicesStub.CreateService.with_call(request,metadata=metadata)

	def CreateService(self, request: SylkApi.CreateServiceRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.CreateServiceResponse:
		"""webezyio - """

		return self.ServicesStub.CreateService(request,metadata=metadata)

	def UpdateService_WithCall(self, request: SylkApi.UpdateServiceRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateServiceResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ServicesStub.UpdateService.with_call(request,metadata=metadata)

	def UpdateService(self, request: SylkApi.UpdateServiceRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateServiceResponse:
		"""webezyio - """

		return self.ServicesStub.UpdateService(request,metadata=metadata)

	def DeleteService_WithCall(self, request: SylkApi.DeleteServiceRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.DeleteServiceResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ServicesStub.DeleteService.with_call(request,metadata=metadata)

	def DeleteService(self, request: SylkApi.DeleteServiceRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.DeleteServiceResponse:
		"""webezyio - """

		return self.ServicesStub.DeleteService(request,metadata=metadata)

	def ListServices_WithCall(self, request: SylkApi.ListServicesRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[Iterator[SylkApi.GetServiceResponse], Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.ServicesStub.ListServices.with_call(request,metadata=metadata)

	def ListServices(self, request: SylkApi.ListServicesRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Iterator[SylkApi.GetServiceResponse]:
		"""webezyio - """

		return self.ServicesStub.ListServices(request,metadata=metadata)

	def GetEnumValue_WithCall(self, request: SylkApi.GetEnumValueRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.GetEnumValueResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.EnumValuesStub.GetEnumValue.with_call(request,metadata=metadata)

	def GetEnumValue(self, request: SylkApi.GetEnumValueRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.GetEnumValueResponse:
		"""webezyio - """

		return self.EnumValuesStub.GetEnumValue(request,metadata=metadata)

	def CreateEnumValue_WithCall(self, request: SylkApi.CreateEnumValueRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.CreateEnumValueResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.EnumValuesStub.CreateEnumValue.with_call(request,metadata=metadata)

	def CreateEnumValue(self, request: SylkApi.CreateEnumValueRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.CreateEnumValueResponse:
		"""webezyio - """

		return self.EnumValuesStub.CreateEnumValue(request,metadata=metadata)

	def UpdateEnumValue_WithCall(self, request: SylkApi.UpdateEnumValueRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.UpdateEnumValueResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.EnumValuesStub.UpdateEnumValue.with_call(request,metadata=metadata)

	def UpdateEnumValue(self, request: SylkApi.UpdateEnumValueRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.UpdateEnumValueResponse:
		"""webezyio - """

		return self.EnumValuesStub.UpdateEnumValue(request,metadata=metadata)

	def DeleteEnumValue_WithCall(self, request: SylkApi.DeleteEnumValueRequest, metadata: Tuple[Tuple[str,str]] = ()) -> Tuple[SylkApi.DeleteEnumValueResponse, Any]:
		"""webezyio -  Returns: RPC output and a call object"""

		return self.EnumValuesStub.DeleteEnumValue.with_call(request,metadata=metadata)

	def DeleteEnumValue(self, request: SylkApi.DeleteEnumValueRequest, metadata: Tuple[Tuple[str,str]] = ()) -> SylkApi.DeleteEnumValueResponse:
		"""webezyio - """

		return self.EnumValuesStub.DeleteEnumValue(request,metadata=metadata)