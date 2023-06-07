from sylk.commons.protos.sylk.SylkProject.v1 import SylkProject_pb2 as _SylkProject_pb2
from sylk.commons.protos.sylk.SylkUser.v1 import SylkUser_pb2 as _SylkUser_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkOrganizationDisplay(_message.Message):
    __slots__ = ["organization", "projects", "users"]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    PROJECTS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    organization: SylkOrganization
    projects: _containers.RepeatedCompositeFieldContainer[_SylkProject_pb2.SylkProjectDisplay]
    users: _containers.RepeatedCompositeFieldContainer[_SylkUser_pb2.SylkUserDisplay]
    def __init__(self, organization: _Optional[_Union[SylkOrganization, _Mapping]] = ..., projects: _Optional[_Iterable[_Union[_SylkProject_pb2.SylkProjectDisplay, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_SylkUser_pb2.SylkUserDisplay, _Mapping]]] = ...) -> None: ...

class SylkOrganization(_message.Message):
    __slots__ = ["orgId", "name", "owner", "domain"]
    ORGID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    orgId: str
    name: str
    owner: str
    domain: str
    def __init__(self, orgId: _Optional[str] = ..., name: _Optional[str] = ..., owner: _Optional[str] = ..., domain: _Optional[str] = ...) -> None: ...
