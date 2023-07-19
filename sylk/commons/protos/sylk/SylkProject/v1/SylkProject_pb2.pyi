from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sylk.commons.protos.sylk.SylkUser.v1 import SylkUser_pb2 as _SylkUser_pb2
from sylk.commons.protos.sylk.SylkClient.v1 import SylkClient_pb2 as _SylkClient_pb2
from sylk.commons.protos.sylk.SylkServer.v1 import SylkServer_pb2 as _SylkServer_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkProject(_message.Message):
    __slots__ = ["description", "java_package", "go_package", "name", "uri", "clients", "server", "package_name", "extensions"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    JAVA_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    GO_PACKAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    CLIENTS_FIELD_NUMBER: _ClassVar[int]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    description: str
    java_package: str
    go_package: str
    name: str
    uri: str
    clients: _containers.RepeatedCompositeFieldContainer[_SylkClient_pb2.SylkClient]
    server: _SylkServer_pb2.SylkServer
    package_name: str
    extensions: _containers.RepeatedCompositeFieldContainer[_any_pb2.Any]
    def __init__(self, description: _Optional[str] = ..., java_package: _Optional[str] = ..., go_package: _Optional[str] = ..., name: _Optional[str] = ..., uri: _Optional[str] = ..., clients: _Optional[_Iterable[_Union[_SylkClient_pb2.SylkClient, _Mapping]]] = ..., server: _Optional[_Union[_SylkServer_pb2.SylkServer, _Mapping]] = ..., package_name: _Optional[str] = ..., extensions: _Optional[_Iterable[_Union[_any_pb2.Any, _Mapping]]] = ...) -> None: ...

class SylkProjectDisplay(_message.Message):
    __slots__ = ["owner", "updated_at", "numMethods", "created_at", "members", "numServices", "numMessages", "numPackages", "project"]
    class MembersEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _SylkUser_pb2.SylkUserRoles
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_SylkUser_pb2.SylkUserRoles, str]] = ...) -> None: ...
    OWNER_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    NUMMETHODS_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NUMSERVICES_FIELD_NUMBER: _ClassVar[int]
    NUMMESSAGES_FIELD_NUMBER: _ClassVar[int]
    NUMPACKAGES_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    owner: str
    updated_at: _timestamp_pb2.Timestamp
    numMethods: int
    created_at: _timestamp_pb2.Timestamp
    members: _containers.ScalarMap[str, _SylkUser_pb2.SylkUserRoles]
    numServices: int
    numMessages: int
    numPackages: int
    project: SylkProject
    def __init__(self, owner: _Optional[str] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., numMethods: _Optional[int] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., members: _Optional[_Mapping[str, _SylkUser_pb2.SylkUserRoles]] = ..., numServices: _Optional[int] = ..., numMessages: _Optional[int] = ..., numPackages: _Optional[int] = ..., project: _Optional[_Union[SylkProject, _Mapping]] = ...) -> None: ...
