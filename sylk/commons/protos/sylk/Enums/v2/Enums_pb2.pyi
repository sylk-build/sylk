from sylk.SylkEnum.v2 import SylkEnum_pb2 as _SylkEnum_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEnumRequest(_message.Message):
    __slots__ = ["project_id", "package", "enum"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    enum: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., enum: _Optional[str] = ...) -> None: ...

class GetEnumResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkEnum_pb2.SylkEnumDisplay
    def __init__(self, result: _Optional[_Union[_SylkEnum_pb2.SylkEnumDisplay, _Mapping]] = ...) -> None: ...

class CreateEnumRequest(_message.Message):
    __slots__ = ["project_id", "package", "enum"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    enum: _SylkEnum_pb2.SylkEnum
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., enum: _Optional[_Union[_SylkEnum_pb2.SylkEnum, _Mapping]] = ...) -> None: ...

class CreateEnumResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkEnum_pb2.SylkEnumDisplay
    def __init__(self, result: _Optional[_Union[_SylkEnum_pb2.SylkEnumDisplay, _Mapping]] = ...) -> None: ...

class DeleteEnumRequest(_message.Message):
    __slots__ = ["project_id", "package", "enum"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    enum: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., enum: _Optional[str] = ...) -> None: ...

class UpdateEnumRequest(_message.Message):
    __slots__ = ["project_id", "package", "enum", "update"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    enum: str
    update: _SylkEnum_pb2.SylkEnum
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., enum: _Optional[str] = ..., update: _Optional[_Union[_SylkEnum_pb2.SylkEnum, _Mapping]] = ...) -> None: ...

class UpdateEnumResponse(_message.Message):
    __slots__ = ["project_id", "enum", "update"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    enum: str
    update: _SylkEnum_pb2.SylkEnum
    def __init__(self, project_id: _Optional[str] = ..., enum: _Optional[str] = ..., update: _Optional[_Union[_SylkEnum_pb2.SylkEnum, _Mapping]] = ...) -> None: ...
