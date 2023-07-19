from google.protobuf import empty_pb2 as _empty_pb2
from sylk.SylkMethod.v1 import SylkMethod_pb2 as _SylkMethod_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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
    __slots__ = ["project_id", "service", "method"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    service: str
    method: _SylkMethod_pb2.SylkMethod
    def __init__(self, project_id: _Optional[str] = ..., service: _Optional[str] = ..., method: _Optional[_Union[_SylkMethod_pb2.SylkMethod, _Mapping]] = ...) -> None: ...

class CreateMethodResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkMethod_pb2.SylkMethodDisplay
    def __init__(self, result: _Optional[_Union[_SylkMethod_pb2.SylkMethodDisplay, _Mapping]] = ...) -> None: ...

class DeleteMethodRequest(_message.Message):
    __slots__ = ["project_id", "method"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    method: str
    def __init__(self, project_id: _Optional[str] = ..., method: _Optional[str] = ...) -> None: ...

class UpdateMethodRequest(_message.Message):
    __slots__ = ["project_id", "method", "update"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    method: str
    update: _SylkMethod_pb2.SylkMethod
    def __init__(self, project_id: _Optional[str] = ..., method: _Optional[str] = ..., update: _Optional[_Union[_SylkMethod_pb2.SylkMethod, _Mapping]] = ...) -> None: ...

class UpdateMethodResponse(_message.Message):
    __slots__ = ["method", "updated"]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    method: str
    updated: _SylkMethod_pb2.SylkMethodDisplay
    def __init__(self, method: _Optional[str] = ..., updated: _Optional[_Union[_SylkMethod_pb2.SylkMethodDisplay, _Mapping]] = ...) -> None: ...
