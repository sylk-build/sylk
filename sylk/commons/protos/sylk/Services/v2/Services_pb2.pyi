from google.protobuf import empty_pb2 as _empty_pb2
from sylk.SylkService.v2 import SylkService_pb2 as _SylkService_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetServiceRequest(_message.Message):
    __slots__ = ["project_id", "service"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    service: str
    def __init__(self, project_id: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...

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
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkService_pb2.SylkServiceDisplay
    def __init__(self, result: _Optional[_Union[_SylkService_pb2.SylkServiceDisplay, _Mapping]] = ...) -> None: ...

class DeleteServiceRequest(_message.Message):
    __slots__ = ["project_id", "service"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    service: str
    def __init__(self, project_id: _Optional[str] = ..., service: _Optional[str] = ...) -> None: ...

class UpdateServiceRequest(_message.Message):
    __slots__ = ["project_id", "service", "update"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    service: str
    update: _SylkService_pb2.SylkService
    def __init__(self, project_id: _Optional[str] = ..., service: _Optional[str] = ..., update: _Optional[_Union[_SylkService_pb2.SylkService, _Mapping]] = ...) -> None: ...

class UpdateServiceResponse(_message.Message):
    __slots__ = ["project_id", "service", "updated"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    service: str
    updated: _SylkService_pb2.SylkServiceDisplay
    def __init__(self, project_id: _Optional[str] = ..., service: _Optional[str] = ..., updated: _Optional[_Union[_SylkService_pb2.SylkServiceDisplay, _Mapping]] = ...) -> None: ...
