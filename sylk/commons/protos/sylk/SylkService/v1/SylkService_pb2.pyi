from google.protobuf import timestamp_pb2 as _timestamp_pb2
from sylk.SylkMethod.v1 import SylkMethod_pb2 as _SylkMethod_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkService(_message.Message):
    __slots__ = ["dependencies", "description", "uri", "name", "full_name", "type", "methods", "extensions"]
    class ExtensionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Struct
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    DEPENDENCIES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    dependencies: _containers.RepeatedScalarFieldContainer[str]
    description: str
    uri: str
    name: str
    full_name: str
    type: str
    methods: _containers.RepeatedCompositeFieldContainer[_SylkMethod_pb2.SylkMethod]
    extensions: _containers.MessageMap[str, _struct_pb2.Struct]
    def __init__(self, dependencies: _Optional[_Iterable[str]] = ..., description: _Optional[str] = ..., uri: _Optional[str] = ..., name: _Optional[str] = ..., full_name: _Optional[str] = ..., type: _Optional[str] = ..., methods: _Optional[_Iterable[_Union[_SylkMethod_pb2.SylkMethod, _Mapping]]] = ..., extensions: _Optional[_Mapping[str, _struct_pb2.Struct]] = ...) -> None: ...

class SylkServiceDisplay(_message.Message):
    __slots__ = ["updated_at", "service", "created_at"]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    updated_at: _timestamp_pb2.Timestamp
    service: SylkService
    created_at: _timestamp_pb2.Timestamp
    def __init__(self, updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., service: _Optional[_Union[SylkService, _Mapping]] = ..., created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...
