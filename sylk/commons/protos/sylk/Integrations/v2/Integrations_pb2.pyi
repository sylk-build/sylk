from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Integration(_message.Message):
    __slots__ = ["org_id", "installed_by", "active", "data"]
    ORG_ID_FIELD_NUMBER: _ClassVar[int]
    INSTALLED_BY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    org_id: str
    installed_by: str
    active: bool
    data: _any_pb2.Any
    def __init__(self, org_id: _Optional[str] = ..., installed_by: _Optional[str] = ..., active: bool = ..., data: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class GetIntegrationRequest(_message.Message):
    __slots__ = ["id"]
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class GetIntegrationResponse(_message.Message):
    __slots__ = ["integration"]
    INTEGRATION_FIELD_NUMBER: _ClassVar[int]
    integration: Integration
    def __init__(self, integration: _Optional[_Union[Integration, _Mapping]] = ...) -> None: ...
