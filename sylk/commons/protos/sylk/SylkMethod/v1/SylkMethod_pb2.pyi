from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkMethodDisplay(_message.Message):
    __slots__ = ["created_at", "method", "updated_at"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    method: SylkMethod
    updated_at: _timestamp_pb2.Timestamp
    def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., method: _Optional[_Union[SylkMethod, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SylkMethod(_message.Message):
    __slots__ = ["client_streaming", "full_name", "type", "name", "server_streaming", "description", "kind", "extensions", "input_type", "output_type", "uri"]
    class ExtensionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Struct
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    CLIENT_STREAMING_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SERVER_STREAMING_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    INPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    client_streaming: bool
    full_name: str
    type: str
    name: str
    server_streaming: bool
    description: str
    kind: str
    extensions: _containers.MessageMap[str, _struct_pb2.Struct]
    input_type: str
    output_type: str
    uri: str
    def __init__(self, client_streaming: bool = ..., full_name: _Optional[str] = ..., type: _Optional[str] = ..., name: _Optional[str] = ..., server_streaming: bool = ..., description: _Optional[str] = ..., kind: _Optional[str] = ..., extensions: _Optional[_Mapping[str, _struct_pb2.Struct]] = ..., input_type: _Optional[str] = ..., output_type: _Optional[str] = ..., uri: _Optional[str] = ...) -> None: ...
