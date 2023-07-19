from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sylk.SylkCommons.v1 import SylkCommons_pb2 as _SylkCommons_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from sylk.SylkField.v1 import SylkField_pb2 as _SylkField_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkMessage(_message.Message):
    __slots__ = ["extension_type", "name", "uri", "extensions", "full_name", "type", "description", "kind", "fields"]
    class ExtensionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Struct
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    EXTENSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    extension_type: _SylkCommons_pb2.SylkExtensions
    name: str
    uri: str
    extensions: _containers.MessageMap[str, _struct_pb2.Struct]
    full_name: str
    type: str
    description: str
    kind: str
    fields: _containers.RepeatedCompositeFieldContainer[_SylkField_pb2.SylkField]
    def __init__(self, extension_type: _Optional[_Union[_SylkCommons_pb2.SylkExtensions, str]] = ..., name: _Optional[str] = ..., uri: _Optional[str] = ..., extensions: _Optional[_Mapping[str, _struct_pb2.Struct]] = ..., full_name: _Optional[str] = ..., type: _Optional[str] = ..., description: _Optional[str] = ..., kind: _Optional[str] = ..., fields: _Optional[_Iterable[_Union[_SylkField_pb2.SylkField, _Mapping]]] = ...) -> None: ...

class SylkMessageDisplay(_message.Message):
    __slots__ = ["updated_at", "message", "created_at"]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    updated_at: _timestamp_pb2.Timestamp
    message: SylkMessage
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., message: _Optional[_Union[SylkMessage, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
