from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sylk.SylkMessage.v1 import SylkMessage_pb2 as _SylkMessage_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from sylk.SylkEnum.v1 import SylkEnum_pb2 as _SylkEnum_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkPackage(_message.Message):
    __slots__ = ["messages", "extensions", "type", "description", "enums", "package", "dependencies", "name", "uri"]
    class ExtensionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Struct
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENUMS_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    messages: _containers.RepeatedCompositeFieldContainer[_SylkMessage_pb2.SylkMessage]
    extensions: _containers.MessageMap[str, _struct_pb2.Struct]
    type: str
    description: str
    enums: _containers.RepeatedCompositeFieldContainer[_SylkEnum_pb2.SylkEnum]
    package: str
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    name: str
    uri: str
    def __init__(self, messages: _Optional[_Iterable[_Union[_SylkMessage_pb2.SylkMessage, _Mapping]]] = ..., extensions: _Optional[_Mapping[str, _struct_pb2.Struct]] = ..., type: _Optional[str] = ..., description: _Optional[str] = ..., enums: _Optional[_Iterable[_Union[_SylkEnum_pb2.SylkEnum, _Mapping]]] = ..., package: _Optional[str] = ..., dependencies: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., uri: _Optional[str] = ...) -> None: ...

class SylkPackageDisplay(_message.Message):
    __slots__ = ["package", "created_at", "updated_at"]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    package: SylkPackage
    created_at: _timestamp_pb2.Timestamp
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, package: _Optional[_Union[SylkPackage, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
