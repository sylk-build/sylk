from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ActionTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_ACTIONTYPES: _ClassVar[ActionTypes]
    createEnumValue: _ClassVar[ActionTypes]
    updateEnumValue: _ClassVar[ActionTypes]
    deleteEnumValue: _ClassVar[ActionTypes]
    createField: _ClassVar[ActionTypes]
    updateField: _ClassVar[ActionTypes]
    deleteField: _ClassVar[ActionTypes]
    createMessage: _ClassVar[ActionTypes]
    updateMessage: _ClassVar[ActionTypes]
    deleteMessage: _ClassVar[ActionTypes]
    createPackage: _ClassVar[ActionTypes]
    updatePackage: _ClassVar[ActionTypes]
    deletePackage: _ClassVar[ActionTypes]
    createService: _ClassVar[ActionTypes]
    updateService: _ClassVar[ActionTypes]
    deleteService: _ClassVar[ActionTypes]
    createProject: _ClassVar[ActionTypes]
    updateProject: _ClassVar[ActionTypes]
    deleteProject: _ClassVar[ActionTypes]
    createEnum: _ClassVar[ActionTypes]
    updateEnum: _ClassVar[ActionTypes]
    deleteEnum: _ClassVar[ActionTypes]
    addUser: _ClassVar[ActionTypes]
    updateUserRole: _ClassVar[ActionTypes]
    createOrganization: _ClassVar[ActionTypes]
    updateOrganization: _ClassVar[ActionTypes]
    removeUser: _ClassVar[ActionTypes]
    createMethod: _ClassVar[ActionTypes]
    updateMethod: _ClassVar[ActionTypes]
    deleteMethod: _ClassVar[ActionTypes]

class ResourceTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_RESOURCETYPES: _ClassVar[ResourceTypes]
    User: _ClassVar[ResourceTypes]
    Organization: _ClassVar[ResourceTypes]
    Package: _ClassVar[ResourceTypes]
    Service: _ClassVar[ResourceTypes]
    Message: _ClassVar[ResourceTypes]
    Enum: _ClassVar[ResourceTypes]
    Method: _ClassVar[ResourceTypes]
    Field: _ClassVar[ResourceTypes]
    EnumValue: _ClassVar[ResourceTypes]
    Project: _ClassVar[ResourceTypes]
UNKNOWN_ACTIONTYPES: ActionTypes
createEnumValue: ActionTypes
updateEnumValue: ActionTypes
deleteEnumValue: ActionTypes
createField: ActionTypes
updateField: ActionTypes
deleteField: ActionTypes
createMessage: ActionTypes
updateMessage: ActionTypes
deleteMessage: ActionTypes
createPackage: ActionTypes
updatePackage: ActionTypes
deletePackage: ActionTypes
createService: ActionTypes
updateService: ActionTypes
deleteService: ActionTypes
createProject: ActionTypes
updateProject: ActionTypes
deleteProject: ActionTypes
createEnum: ActionTypes
updateEnum: ActionTypes
deleteEnum: ActionTypes
addUser: ActionTypes
updateUserRole: ActionTypes
createOrganization: ActionTypes
updateOrganization: ActionTypes
removeUser: ActionTypes
createMethod: ActionTypes
updateMethod: ActionTypes
deleteMethod: ActionTypes
UNKNOWN_RESOURCETYPES: ResourceTypes
User: ResourceTypes
Organization: ResourceTypes
Package: ResourceTypes
Service: ResourceTypes
Message: ResourceTypes
Enum: ResourceTypes
Method: ResourceTypes
Field: ResourceTypes
EnumValue: ResourceTypes
Project: ResourceTypes

class EncodedPagination(_message.Message):
    __slots__ = ["params", "skip", "total_size"]
    PARAMS_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    params: _struct_pb2.Struct
    skip: int
    total_size: int
    def __init__(self, params: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., skip: _Optional[int] = ..., total_size: _Optional[int] = ...) -> None: ...

class ActivityLog(_message.Message):
    __slots__ = ["user_id", "created_at", "metadata", "org_id", "id", "user_email", "type"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    created_at: _timestamp_pb2.Timestamp
    metadata: _struct_pb2.Struct
    org_id: str
    id: str
    user_email: str
    type: ActionTypes
    def __init__(self, user_id: _Optional[str] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., org_id: _Optional[str] = ..., id: _Optional[str] = ..., user_email: _Optional[str] = ..., type: _Optional[_Union[ActionTypes, str]] = ...) -> None: ...

class PaginationResponse(_message.Message):
    __slots__ = ["next_page_token"]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    next_page_token: str
    def __init__(self, next_page_token: _Optional[str] = ...) -> None: ...

class GetActivityLogsResponse(_message.Message):
    __slots__ = ["logs", "pagination"]
    LOGS_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    logs: _containers.RepeatedCompositeFieldContainer[ActivityLog]
    pagination: PaginationResponse
    def __init__(self, logs: _Optional[_Iterable[_Union[ActivityLog, _Mapping]]] = ..., pagination: _Optional[_Union[PaginationResponse, _Mapping]] = ...) -> None: ...

class PaginationRequest(_message.Message):
    __slots__ = ["page_size", "page_token"]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    def __init__(self, page_size: _Optional[int] = ..., page_token: _Optional[str] = ...) -> None: ...

class ListActivityLogsRequest(_message.Message):
    __slots__ = ["user_id", "org_id", "until", "activity_type", "pagination", "resource_type", "resource"]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    UNTIL_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    PAGINATION_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    org_id: str
    until: _timestamp_pb2.Timestamp
    activity_type: ActionTypes
    pagination: PaginationRequest
    resource_type: ResourceTypes
    resource: str
    def __init__(self, user_id: _Optional[str] = ..., org_id: _Optional[str] = ..., until: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., activity_type: _Optional[_Union[ActionTypes, str]] = ..., pagination: _Optional[_Union[PaginationRequest, _Mapping]] = ..., resource_type: _Optional[_Union[ResourceTypes, str]] = ..., resource: _Optional[str] = ...) -> None: ...
