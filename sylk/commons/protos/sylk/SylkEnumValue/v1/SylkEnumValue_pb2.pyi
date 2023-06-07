from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkEnumValueDisplay(_message.Message):
    __slots__ = ["enum_value", "updated_at", "created_at"]
    ENUM_VALUE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    enum_value: SylkEnumValue
    updated_at: _timestamp_pb2.Timestamp
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, enum_value: _Optional[_Union[SylkEnumValue, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SylkEnumValue(_message.Message):
    __slots__ = ["kind", "description", "index", "uri", "name", "number", "full_name", "type"]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    kind: str
    description: str
    index: int
    uri: str
    name: str
    number: int
    full_name: str
    type: str
    def __init__(self, kind: _Optional[str] = ..., description: _Optional[str] = ..., index: _Optional[int] = ..., uri: _Optional[str] = ..., name: _Optional[str] = ..., number: _Optional[int] = ..., full_name: _Optional[str] = ..., type: _Optional[str] = ...) -> None: ...
