from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkUserStatuses(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEFAULT_SYLKUSERSTATUSES: _ClassVar[SylkUserStatuses]
    ACTIVE: _ClassVar[SylkUserStatuses]
    INACTIVE: _ClassVar[SylkUserStatuses]
    PENDING: _ClassVar[SylkUserStatuses]

class SylkUserRoles(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEFAULT_SYLKUSERROLES: _ClassVar[SylkUserRoles]
    ADMIN: _ClassVar[SylkUserRoles]
    CONTRIBUTER: _ClassVar[SylkUserRoles]
    READER: _ClassVar[SylkUserRoles]
DEFAULT_SYLKUSERSTATUSES: SylkUserStatuses
ACTIVE: SylkUserStatuses
INACTIVE: SylkUserStatuses
PENDING: SylkUserStatuses
DEFAULT_SYLKUSERROLES: SylkUserRoles
ADMIN: SylkUserRoles
CONTRIBUTER: SylkUserRoles
READER: SylkUserRoles

class PersonalAccessToken(_message.Message):
    __slots__ = ["token", "org_id", "description", "expires_at", "created_at", "revoked", "user_id"]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    EXPIRES_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    REVOKED_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    token: str
    org_id: str
    description: str
    expires_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    revoked: bool
    user_id: str
    def __init__(self, token: _Optional[str] = ..., org_id: _Optional[str] = ..., description: _Optional[str] = ..., expires_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., revoked: bool = ..., user_id: _Optional[str] = ...) -> None: ...

class SylkUser(_message.Message):
    __slots__ = ["email", "orgs_ids", "locale", "given_name", "nickname", "status", "picture", "connection", "user_id", "email_verified", "family_name"]
    class OrgsIdsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: SylkUserRoles
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[SylkUserRoles, str]] = ...) -> None: ...
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ORGS_IDS_FIELD_NUMBER: _ClassVar[int]
    LOCALE_FIELD_NUMBER: _ClassVar[int]
    GIVEN_NAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    PICTURE_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    EMAIL_VERIFIED_FIELD_NUMBER: _ClassVar[int]
    FAMILY_NAME_FIELD_NUMBER: _ClassVar[int]
    email: str
    orgs_ids: _containers.ScalarMap[str, SylkUserRoles]
    locale: str
    given_name: str
    nickname: str
    status: SylkUserStatuses
    picture: str
    connection: str
    user_id: str
    email_verified: bool
    family_name: str
    def __init__(self, email: _Optional[str] = ..., orgs_ids: _Optional[_Mapping[str, SylkUserRoles]] = ..., locale: _Optional[str] = ..., given_name: _Optional[str] = ..., nickname: _Optional[str] = ..., status: _Optional[_Union[SylkUserStatuses, str]] = ..., picture: _Optional[str] = ..., connection: _Optional[str] = ..., user_id: _Optional[str] = ..., email_verified: bool = ..., family_name: _Optional[str] = ...) -> None: ...

class SylkUserDisplay(_message.Message):
    __slots__ = ["user", "last_active", "created_at", "updated_at"]
    USER_FIELD_NUMBER: _ClassVar[int]
    LAST_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    user: SylkUser
    last_active: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, user: _Optional[_Union[SylkUser, _Mapping]] = ..., last_active: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
