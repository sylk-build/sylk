from sylk.commons.protos.sylk.SylkOrganization.v1 import SylkOrganization_pb2 as _SylkOrganization_pb2
from sylk.commons.protos.sylk.SylkUser.v1 import SylkUser_pb2 as _SylkUser_pb2
from sylk.commons.protos.sylk.SylkProject.v1 import SylkProject_pb2 as _SylkProject_pb2
from sylk.commons.protos.sylk.SylkPackage.v1 import SylkPackage_pb2 as _SylkPackage_pb2
from sylk.commons.protos.sylk.SylkService.v1 import SylkService_pb2 as _SylkService_pb2
from sylk.commons.protos.sylk.SylkMessage.v1 import SylkMessage_pb2 as _SylkMessage_pb2
from sylk.commons.protos.sylk.SylkMethod.v1 import SylkMethod_pb2 as _SylkMethod_pb2
from sylk.commons.protos.sylk.SylkField.v1 import SylkField_pb2 as _SylkField_pb2
from sylk.commons.protos.sylk.SylkEnum.v1 import SylkEnum_pb2 as _SylkEnum_pb2
from sylk.commons.protos.sylk.SylkEnumValue.v1 import SylkEnumValue_pb2 as _SylkEnumValue_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RemoveUserResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class RemoveUserRequest(_message.Message):
    __slots__ = ["project_id", "user_email", "org_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    user_email: str
    org_id: str
    def __init__(self, project_id: _Optional[str] = ..., user_email: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class UpdateOrganizationRequest(_message.Message):
    __slots__ = ["org_id", "update"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    update: _SylkOrganization_pb2.SylkOrganization
    def __init__(self, org_id: _Optional[str] = ..., update: _Optional[_Union[_SylkOrganization_pb2.SylkOrganization, _Mapping]] = ...) -> None: ...

class GetOrganizationResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkOrganization_pb2.SylkOrganizationDisplay
    def __init__(self, result: _Optional[_Union[_SylkOrganization_pb2.SylkOrganizationDisplay, _Mapping]] = ...) -> None: ...

class GetOrganizationRequest(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class UpdateUserStatusResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class UpdateUserStatusRequest(_message.Message):
    __slots__ = ["user_email_or_id", "org_id", "status"]
    USER_EMAIL_OR_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    user_email_or_id: str
    org_id: str
    status: _SylkUser_pb2.SylkUserStatuses
    def __init__(self, user_email_or_id: _Optional[str] = ..., org_id: _Optional[str] = ..., status: _Optional[_Union[_SylkUser_pb2.SylkUserStatuses, str]] = ...) -> None: ...

class UpdateUserRoleResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class UpdateUserRoleRequest(_message.Message):
    __slots__ = ["role", "user_id", "org_id", "project_id"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    role: _SylkUser_pb2.SylkUserRoles
    user_id: str
    org_id: str
    project_id: str
    def __init__(self, role: _Optional[_Union[_SylkUser_pb2.SylkUserRoles, str]] = ..., user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeleteProjectResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class DeleteProjectRequest(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: str
    def __init__(self, project: _Optional[str] = ...) -> None: ...

class UpdateProjectResponse(_message.Message):
    __slots__ = ["updated", "project_id"]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    updated: _SylkProject_pb2.SylkProjectDisplay
    project_id: str
    def __init__(self, updated: _Optional[_Union[_SylkProject_pb2.SylkProjectDisplay, _Mapping]] = ..., project_id: _Optional[str] = ...) -> None: ...

class UpdateProjectRequest(_message.Message):
    __slots__ = ["project_id", "update"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    update: _SylkProject_pb2.SylkProject
    def __init__(self, project_id: _Optional[str] = ..., update: _Optional[_Union[_SylkProject_pb2.SylkProject, _Mapping]] = ...) -> None: ...

class GetProjectResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkProject_pb2.SylkProjectDisplay
    def __init__(self, result: _Optional[_Union[_SylkProject_pb2.SylkProjectDisplay, _Mapping]] = ...) -> None: ...

class GetProjectRequest(_message.Message):
    __slots__ = ["project"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    project: str
    def __init__(self, project: _Optional[str] = ...) -> None: ...

class GetUserResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkUser_pb2.SylkUserDisplay
    def __init__(self, result: _Optional[_Union[_SylkUser_pb2.SylkUserDisplay, _Mapping]] = ...) -> None: ...

class GetUserRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class AddUserResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class AddUserRequest(_message.Message):
    __slots__ = ["role", "org_id", "project", "user_email"]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    role: _SylkUser_pb2.SylkUserRoles
    org_id: str
    project: str
    user_email: str
    def __init__(self, role: _Optional[_Union[_SylkUser_pb2.SylkUserRoles, str]] = ..., org_id: _Optional[str] = ..., project: _Optional[str] = ..., user_email: _Optional[str] = ...) -> None: ...

class AcceptUserInviteResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class AcceptUserInviteRequest(_message.Message):
    __slots__ = ["email", "org_id"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    email: str
    org_id: str
    def __init__(self, email: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class UpdateUserResponse(_message.Message):
    __slots__ = ["updated", "user_id"]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    updated: _SylkUser_pb2.SylkUser
    user_id: str
    def __init__(self, updated: _Optional[_Union[_SylkUser_pb2.SylkUser, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class UpdateUserRequest(_message.Message):
    __slots__ = ["update", "user_id"]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    update: _SylkUser_pb2.SylkUser
    user_id: str
    def __init__(self, update: _Optional[_Union[_SylkUser_pb2.SylkUser, _Mapping]] = ..., user_id: _Optional[str] = ...) -> None: ...

class CreateUserResponse(_message.Message):
    __slots__ = ["user", "organization"]
    USER_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    user: _SylkUser_pb2.SylkUser
    organization: _SylkOrganization_pb2.SylkOrganization
    def __init__(self, user: _Optional[_Union[_SylkUser_pb2.SylkUser, _Mapping]] = ..., organization: _Optional[_Union[_SylkOrganization_pb2.SylkOrganization, _Mapping]] = ...) -> None: ...

class CreateUserRequest(_message.Message):
    __slots__ = ["org_id", "user"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    user: _SylkUser_pb2.SylkUser
    def __init__(self, org_id: _Optional[str] = ..., user: _Optional[_Union[_SylkUser_pb2.SylkUser, _Mapping]] = ...) -> None: ...

class ListOrganizationsRequest(_message.Message):
    __slots__ = ["user_id"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class UpdateOrganizationResponse(_message.Message):
    __slots__ = ["updated", "org_id"]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    updated: _SylkOrganization_pb2.SylkOrganization
    org_id: str
    def __init__(self, updated: _Optional[_Union[_SylkOrganization_pb2.SylkOrganization, _Mapping]] = ..., org_id: _Optional[str] = ...) -> None: ...

class GetPackageRequest(_message.Message):
    __slots__ = ["project_id", "package"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ...) -> None: ...

class GetPackageResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkPackage_pb2.SylkPackageDisplay
    def __init__(self, result: _Optional[_Union[_SylkPackage_pb2.SylkPackageDisplay, _Mapping]] = ...) -> None: ...

class CreatePackageRequest(_message.Message):
    __slots__ = ["package", "project_id"]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    package: _SylkPackage_pb2.SylkPackage
    project_id: str
    def __init__(self, package: _Optional[_Union[_SylkPackage_pb2.SylkPackage, _Mapping]] = ..., project_id: _Optional[str] = ...) -> None: ...

class CreatePackageResponse(_message.Message):
    __slots__ = ["project_id", "result"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    result: _SylkPackage_pb2.SylkPackageDisplay
    def __init__(self, project_id: _Optional[str] = ..., result: _Optional[_Union[_SylkPackage_pb2.SylkPackageDisplay, _Mapping]] = ...) -> None: ...

class UpdatePackageRequest(_message.Message):
    __slots__ = ["project_id", "package", "update"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    update: _SylkPackage_pb2.SylkPackage
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., update: _Optional[_Union[_SylkPackage_pb2.SylkPackage, _Mapping]] = ...) -> None: ...

class UpdatePackageResponse(_message.Message):
    __slots__ = ["updated", "package", "project_id"]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    updated: _SylkPackage_pb2.SylkPackageDisplay
    package: str
    project_id: str
    def __init__(self, updated: _Optional[_Union[_SylkPackage_pb2.SylkPackageDisplay, _Mapping]] = ..., package: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeletePackageRequest(_message.Message):
    __slots__ = ["project_id", "package"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ...) -> None: ...

class DeletePackageResponse(_message.Message):
    __slots__ = ["package", "project_id"]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    package: str
    project_id: str
    def __init__(self, package: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class GetServiceRequest(_message.Message):
    __slots__ = ["service", "project_id"]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    service: str
    project_id: str
    def __init__(self, service: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class GetServiceResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkService_pb2.SylkServiceDisplay
    def __init__(self, result: _Optional[_Union[_SylkService_pb2.SylkServiceDisplay, _Mapping]] = ...) -> None: ...

class CreateServiceRequest(_message.Message):
    __slots__ = ["project_id", "service"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    service: _SylkService_pb2.SylkService
    def __init__(self, project_id: _Optional[str] = ..., service: _Optional[_Union[_SylkService_pb2.SylkService, _Mapping]] = ...) -> None: ...

class CreateServiceResponse(_message.Message):
    __slots__ = ["result", "project_id"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    result: _SylkService_pb2.SylkServiceDisplay
    project_id: str
    def __init__(self, result: _Optional[_Union[_SylkService_pb2.SylkServiceDisplay, _Mapping]] = ..., project_id: _Optional[str] = ...) -> None: ...

class UpdateServiceRequest(_message.Message):
    __slots__ = ["service", "project_id", "update"]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    service: str
    project_id: str
    update: _SylkService_pb2.SylkService
    def __init__(self, service: _Optional[str] = ..., project_id: _Optional[str] = ..., update: _Optional[_Union[_SylkService_pb2.SylkService, _Mapping]] = ...) -> None: ...

class UpdateServiceResponse(_message.Message):
    __slots__ = ["updated", "service", "project_id"]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    updated: _SylkService_pb2.SylkServiceDisplay
    service: str
    project_id: str
    def __init__(self, updated: _Optional[_Union[_SylkService_pb2.SylkServiceDisplay, _Mapping]] = ..., service: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeleteServiceRequest(_message.Message):
    __slots__ = ["project_id", "service"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    service: str
    def __init__(self, project_id: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...

class DeleteServiceResponse(_message.Message):
    __slots__ = ["project_id", "service"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    service: str
    def __init__(self, project_id: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...

class ListServicesRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class ListPackagesRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class GetMessageRequest(_message.Message):
    __slots__ = ["project_id", "message"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    message: str
    def __init__(self, project_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetMessageResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkMessage_pb2.SylkMessageDisplay
    def __init__(self, result: _Optional[_Union[_SylkMessage_pb2.SylkMessageDisplay, _Mapping]] = ...) -> None: ...

class CreateMessageRequest(_message.Message):
    __slots__ = ["project_id", "package", "message"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    message: _SylkMessage_pb2.SylkMessage
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., message: _Optional[_Union[_SylkMessage_pb2.SylkMessage, _Mapping]] = ...) -> None: ...

class CreateMessageResponse(_message.Message):
    __slots__ = ["result", "message", "project_id"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    result: _SylkMessage_pb2.SylkMessageDisplay
    message: str
    project_id: str
    def __init__(self, result: _Optional[_Union[_SylkMessage_pb2.SylkMessageDisplay, _Mapping]] = ..., message: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class UpdateMessageRequest(_message.Message):
    __slots__ = ["project_id", "message", "update"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    message: str
    update: _SylkMessage_pb2.SylkMessage
    def __init__(self, project_id: _Optional[str] = ..., message: _Optional[str] = ..., update: _Optional[_Union[_SylkMessage_pb2.SylkMessage, _Mapping]] = ...) -> None: ...

class UpdateMessageResponse(_message.Message):
    __slots__ = ["message", "updated", "project_id"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    message: str
    updated: _SylkMessage_pb2.SylkMessageDisplay
    project_id: str
    def __init__(self, message: _Optional[str] = ..., updated: _Optional[_Union[_SylkMessage_pb2.SylkMessageDisplay, _Mapping]] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeleteMessageRequest(_message.Message):
    __slots__ = ["message", "project_id"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    message: str
    project_id: str
    def __init__(self, message: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeleteMessageResponse(_message.Message):
    __slots__ = ["project_id", "message"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    message: str
    def __init__(self, project_id: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class GetMethodRequest(_message.Message):
    __slots__ = ["project_id", "method"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    method: str
    def __init__(self, project_id: _Optional[str] = ..., method: _Optional[str] = ...) -> None: ...

class GetMethodResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkMethod_pb2.SylkMethodDisplay
    def __init__(self, result: _Optional[_Union[_SylkMethod_pb2.SylkMethodDisplay, _Mapping]] = ...) -> None: ...

class CreateMethodRequest(_message.Message):
    __slots__ = ["service", "project_id", "method"]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    service: str
    project_id: str
    method: _SylkMethod_pb2.SylkMethod
    def __init__(self, service: _Optional[str] = ..., project_id: _Optional[str] = ..., method: _Optional[_Union[_SylkMethod_pb2.SylkMethod, _Mapping]] = ...) -> None: ...

class CreateMethodResponse(_message.Message):
    __slots__ = ["result", "project_id", "service"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    result: _SylkMethod_pb2.SylkMethodDisplay
    project_id: str
    service: str
    def __init__(self, result: _Optional[_Union[_SylkMethod_pb2.SylkMethodDisplay, _Mapping]] = ..., project_id: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...

class UpdateMethodRequest(_message.Message):
    __slots__ = ["method", "project_id", "update"]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    method: str
    project_id: str
    update: _SylkMethod_pb2.SylkMethod
    def __init__(self, method: _Optional[str] = ..., project_id: _Optional[str] = ..., update: _Optional[_Union[_SylkMethod_pb2.SylkMethod, _Mapping]] = ...) -> None: ...

class UpdateMethodResponse(_message.Message):
    __slots__ = ["method", "project_id", "updated"]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    method: str
    project_id: str
    updated: _SylkMethod_pb2.SylkMethodDisplay
    def __init__(self, method: _Optional[str] = ..., project_id: _Optional[str] = ..., updated: _Optional[_Union[_SylkMethod_pb2.SylkMethodDisplay, _Mapping]] = ...) -> None: ...

class DeleteMethodRequest(_message.Message):
    __slots__ = ["method", "project_id"]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    method: str
    project_id: str
    def __init__(self, method: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeleteMethodResponse(_message.Message):
    __slots__ = ["method", "project_id"]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    method: str
    project_id: str
    def __init__(self, method: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class GetFieldRequest(_message.Message):
    __slots__ = ["project_id", "field"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    field: str
    def __init__(self, project_id: _Optional[str] = ..., field: _Optional[str] = ...) -> None: ...

class GetFieldResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkField_pb2.SylkFieldDisplay
    def __init__(self, result: _Optional[_Union[_SylkField_pb2.SylkFieldDisplay, _Mapping]] = ...) -> None: ...

class UpdateFieldRequest(_message.Message):
    __slots__ = ["field", "project_id", "update"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    field: str
    project_id: str
    update: _SylkField_pb2.SylkField
    def __init__(self, field: _Optional[str] = ..., project_id: _Optional[str] = ..., update: _Optional[_Union[_SylkField_pb2.SylkField, _Mapping]] = ...) -> None: ...

class UpdateFieldResponse(_message.Message):
    __slots__ = ["project_id", "field", "updated"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    field: str
    updated: _SylkField_pb2.SylkFieldDisplay
    def __init__(self, project_id: _Optional[str] = ..., field: _Optional[str] = ..., updated: _Optional[_Union[_SylkField_pb2.SylkFieldDisplay, _Mapping]] = ...) -> None: ...

class DeleteFieldRequest(_message.Message):
    __slots__ = ["field", "project_id"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    field: str
    project_id: str
    def __init__(self, field: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeleteFieldResponse(_message.Message):
    __slots__ = ["field", "project_id"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    field: str
    project_id: str
    def __init__(self, field: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class CreateFieldRequest(_message.Message):
    __slots__ = ["project_id", "message", "field"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    message: str
    field: _SylkField_pb2.SylkField
    def __init__(self, project_id: _Optional[str] = ..., message: _Optional[str] = ..., field: _Optional[_Union[_SylkField_pb2.SylkField, _Mapping]] = ...) -> None: ...

class CreateFieldResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkField_pb2.SylkFieldDisplay
    def __init__(self, result: _Optional[_Union[_SylkField_pb2.SylkFieldDisplay, _Mapping]] = ...) -> None: ...

class GetEnumRequest(_message.Message):
    __slots__ = ["project_id", "enum"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    enum: str
    def __init__(self, project_id: _Optional[str] = ..., enum: _Optional[str] = ...) -> None: ...

class GetEnumResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkEnum_pb2.SylkEnumDisplay
    def __init__(self, result: _Optional[_Union[_SylkEnum_pb2.SylkEnumDisplay, _Mapping]] = ...) -> None: ...

class CreateEnumRequest(_message.Message):
    __slots__ = ["package", "enum", "project_id"]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    package: str
    enum: _SylkEnum_pb2.SylkEnum
    project_id: str
    def __init__(self, package: _Optional[str] = ..., enum: _Optional[_Union[_SylkEnum_pb2.SylkEnum, _Mapping]] = ..., project_id: _Optional[str] = ...) -> None: ...

class CreateEnumResponse(_message.Message):
    __slots__ = ["result", "project_id"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    result: _SylkEnum_pb2.SylkEnumDisplay
    project_id: str
    def __init__(self, result: _Optional[_Union[_SylkEnum_pb2.SylkEnumDisplay, _Mapping]] = ..., project_id: _Optional[str] = ...) -> None: ...

class UpdateEnumRequest(_message.Message):
    __slots__ = ["update", "enum", "project_id"]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    update: _SylkEnum_pb2.SylkEnum
    enum: str
    project_id: str
    def __init__(self, update: _Optional[_Union[_SylkEnum_pb2.SylkEnum, _Mapping]] = ..., enum: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class UpdateEnumResponse(_message.Message):
    __slots__ = ["enum", "project_id", "updated"]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    enum: str
    project_id: str
    updated: _SylkEnum_pb2.SylkEnumDisplay
    def __init__(self, enum: _Optional[str] = ..., project_id: _Optional[str] = ..., updated: _Optional[_Union[_SylkEnum_pb2.SylkEnumDisplay, _Mapping]] = ...) -> None: ...

class DeleteEnumRequest(_message.Message):
    __slots__ = ["enum", "project_id"]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    enum: str
    project_id: str
    def __init__(self, enum: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeleteEnumResponse(_message.Message):
    __slots__ = ["enum", "project_id"]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    enum: str
    project_id: str
    def __init__(self, enum: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class GetEnumValueRequest(_message.Message):
    __slots__ = ["project_id", "enum_value"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    enum_value: str
    def __init__(self, project_id: _Optional[str] = ..., enum_value: _Optional[str] = ...) -> None: ...

class GetEnumValueResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkEnumValue_pb2.SylkEnumValueDisplay
    def __init__(self, result: _Optional[_Union[_SylkEnumValue_pb2.SylkEnumValueDisplay, _Mapping]] = ...) -> None: ...

class CreateEnumValueRequest(_message.Message):
    __slots__ = ["enum", "project_id", "enum_value"]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    enum: str
    project_id: str
    enum_value: _SylkEnumValue_pb2.SylkEnumValue
    def __init__(self, enum: _Optional[str] = ..., project_id: _Optional[str] = ..., enum_value: _Optional[_Union[_SylkEnumValue_pb2.SylkEnumValue, _Mapping]] = ...) -> None: ...

class CreateEnumValueResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkEnumValue_pb2.SylkEnumValueDisplay
    def __init__(self, result: _Optional[_Union[_SylkEnumValue_pb2.SylkEnumValueDisplay, _Mapping]] = ...) -> None: ...

class UpdateEnumValueRequest(_message.Message):
    __slots__ = ["update", "project_id", "enum_value"]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    update: _SylkEnumValue_pb2.SylkEnumValue
    project_id: str
    enum_value: str
    def __init__(self, update: _Optional[_Union[_SylkEnumValue_pb2.SylkEnumValue, _Mapping]] = ..., project_id: _Optional[str] = ..., enum_value: _Optional[str] = ...) -> None: ...

class UpdateEnumValueResponse(_message.Message):
    __slots__ = ["project_id", "updated", "enum_value"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    updated: _SylkEnumValue_pb2.SylkEnumValueDisplay
    enum_value: str
    def __init__(self, project_id: _Optional[str] = ..., updated: _Optional[_Union[_SylkEnumValue_pb2.SylkEnumValueDisplay, _Mapping]] = ..., enum_value: _Optional[str] = ...) -> None: ...

class DeleteEnumValueRequest(_message.Message):
    __slots__ = ["enum_value", "project_id"]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    enum_value: str
    project_id: str
    def __init__(self, enum_value: _Optional[str] = ..., project_id: _Optional[str] = ...) -> None: ...

class DeleteEnumValueResponse(_message.Message):
    __slots__ = ["project_id", "enum_value"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    enum_value: str
    def __init__(self, project_id: _Optional[str] = ..., enum_value: _Optional[str] = ...) -> None: ...

class ListOrganizationsResponseCache(_message.Message):
    __slots__ = ["organizations"]
    ORGANIZATIONS_FIELD_NUMBER: _ClassVar[int]
    organizations: _containers.RepeatedCompositeFieldContainer[GetOrganizationResponse]
    def __init__(self, organizations: _Optional[_Iterable[_Union[GetOrganizationResponse, _Mapping]]] = ...) -> None: ...

class ListProjectsRequest(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class CreateProjectRequest(_message.Message):
    __slots__ = ["project", "org_id"]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    project: _SylkProject_pb2.SylkProject
    org_id: str
    def __init__(self, project: _Optional[_Union[_SylkProject_pb2.SylkProject, _Mapping]] = ..., org_id: _Optional[str] = ...) -> None: ...

class CreateProjectResponse(_message.Message):
    __slots__ = ["org_id", "result"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    result: _SylkProject_pb2.SylkProjectDisplay
    def __init__(self, org_id: _Optional[str] = ..., result: _Optional[_Union[_SylkProject_pb2.SylkProjectDisplay, _Mapping]] = ...) -> None: ...

class ListProjectsResponseCache(_message.Message):
    __slots__ = ["projects"]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    projects: _containers.RepeatedCompositeFieldContainer[GetProjectResponse]
    def __init__(self, projects: _Optional[_Iterable[_Union[GetProjectResponse, _Mapping]]] = ...) -> None: ...

class CachedSession(_message.Message):
    __slots__ = ["session"]
    SESSION_FIELD_NUMBER: _ClassVar[int]
    session: _struct_pb2.Struct
    def __init__(self, session: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CreateAccessTokenRequest(_message.Message):
    __slots__ = ["description", "org_id", "expires_at"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    description: str
    org_id: str
    expires_at: _timestamp_pb2.Timestamp
    def __init__(self, description: _Optional[str] = ..., org_id: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAccessTokenResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class ListAccessTokensRequest(_message.Message):
    __slots__ = ["org_id"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    def __init__(self, org_id: _Optional[str] = ...) -> None: ...

class GetAccessTokenResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkUser_pb2.PersonalAccessToken
    def __init__(self, result: _Optional[_Union[_SylkUser_pb2.PersonalAccessToken, _Mapping]] = ...) -> None: ...

class GetAccessTokenRequest(_message.Message):
    __slots__ = ["token"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...

class RevokeAccessTokenRequest(_message.Message):
    __slots__ = ["token", "org_id"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    token: str
    org_id: str
    def __init__(self, token: _Optional[str] = ..., org_id: _Optional[str] = ...) -> None: ...

class RevokeAccessTokenResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
