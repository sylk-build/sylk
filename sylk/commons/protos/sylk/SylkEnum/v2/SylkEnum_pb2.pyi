from sylk.SylkEnumValue.v1 import SylkEnumValue_pb2 as _SylkEnumValue_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkEnum(_message.Message):
    __slots__ = ["type", "kind", "description", "values", "name", "uri", "full_name", "tag"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    type: str
    kind: str
    description: str
    values: _containers.RepeatedCompositeFieldContainer[_SylkEnumValue_pb2.SylkEnumValue]
    name: str
    uri: str
    full_name: str
    tag: str
    def __init__(self, type: _Optional[str] = ..., kind: _Optional[str] = ..., description: _Optional[str] = ..., values: _Optional[_Iterable[_Union[_SylkEnumValue_pb2.SylkEnumValue, _Mapping]]] = ..., name: _Optional[str] = ..., uri: _Optional[str] = ..., full_name: _Optional[str] = ..., tag: _Optional[str] = ...) -> None: ...

class SylkEnumDisplay(_message.Message):
    __slots__ = ["updated_at", "enum", "created_at", "id"]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ENUM_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    updated_at: _timestamp_pb2.Timestamp
    enum: SylkEnum
    created_at: _timestamp_pb2.Timestamp
    id: str
    def __init__(self, updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., enum: _Optional[_Union[SylkEnum, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...
