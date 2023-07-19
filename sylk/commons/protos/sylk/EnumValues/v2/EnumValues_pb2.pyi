from sylk.SylkEnumValue.v1 import SylkEnumValue_pb2 as _SylkEnumValue_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetEnumValueRequest(_message.Message):
    __slots__ = ["project_id", "package", "enum_value"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    enum_value: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., enum_value: _Optional[str] = ...) -> None: ...

class GetEnumValueResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkEnumValue_pb2.SylkEnumValueDisplay
    def __init__(self, result: _Optional[_Union[_SylkEnumValue_pb2.SylkEnumValueDisplay, _Mapping]] = ...) -> None: ...

class CreateEnumValueRequest(_message.Message):
    __slots__ = ["project_id", "package", "enum_value"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    enum_value: _SylkEnumValue_pb2.SylkEnumValue
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., enum_value: _Optional[_Union[_SylkEnumValue_pb2.SylkEnumValue, _Mapping]] = ...) -> None: ...

class CreateEnumValueResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkEnumValue_pb2.SylkEnumValueDisplay
    def __init__(self, result: _Optional[_Union[_SylkEnumValue_pb2.SylkEnumValueDisplay, _Mapping]] = ...) -> None: ...

class UpdateEnumValueRequest(_message.Message):
    __slots__ = ["project_id", "enum_value", "package", "update"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    enum_value: str
    package: str
    update: _SylkEnumValue_pb2.SylkEnumValue
    def __init__(self, project_id: _Optional[str] = ..., enum_value: _Optional[str] = ..., package: _Optional[str] = ..., update: _Optional[_Union[_SylkEnumValue_pb2.SylkEnumValue, _Mapping]] = ...) -> None: ...

class UpdateEnumValueResponse(_message.Message):
    __slots__ = ["project_id", "enum_value", "updated"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    enum_value: str
    updated: _SylkEnumValue_pb2.SylkEnumValueDisplay
    def __init__(self, project_id: _Optional[str] = ..., enum_value: _Optional[str] = ..., updated: _Optional[_Union[_SylkEnumValue_pb2.SylkEnumValueDisplay, _Mapping]] = ...) -> None: ...

class DeleteEnumValueRequest(_message.Message):
    __slots__ = ["project_id", "enum_value", "package"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    enum_value: str
    package: str
    def __init__(self, project_id: _Optional[str] = ..., enum_value: _Optional[str] = ..., package: _Optional[str] = ...) -> None: ...
