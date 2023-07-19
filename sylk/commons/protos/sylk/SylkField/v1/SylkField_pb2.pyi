from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkFieldTypes(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEFAULT_SYLKFIELDTYPES: _ClassVar[SylkFieldTypes]
    TYPE_DOUBLE: _ClassVar[SylkFieldTypes]
    TYPE_FLOAT: _ClassVar[SylkFieldTypes]
    TYPE_INT64: _ClassVar[SylkFieldTypes]
    TYPE_UINT64: _ClassVar[SylkFieldTypes]
    TYPE_INT32: _ClassVar[SylkFieldTypes]
    TYPE_FIXED64: _ClassVar[SylkFieldTypes]
    TYPE_FIXED32: _ClassVar[SylkFieldTypes]
    TYPE_BOOL: _ClassVar[SylkFieldTypes]
    TYPE_STRING: _ClassVar[SylkFieldTypes]
    TYPE_GROUP: _ClassVar[SylkFieldTypes]
    TYPE_MESSAGE: _ClassVar[SylkFieldTypes]
    TYPE_BYTES: _ClassVar[SylkFieldTypes]
    TYPE_UINT32: _ClassVar[SylkFieldTypes]
    TYPE_ENUM: _ClassVar[SylkFieldTypes]
    TYPE_SFIXED32: _ClassVar[SylkFieldTypes]
    TYPE_SFIXED64: _ClassVar[SylkFieldTypes]
    TYPE_SINT32: _ClassVar[SylkFieldTypes]
    TYPE_SINT64: _ClassVar[SylkFieldTypes]
    TYPE_MAP: _ClassVar[SylkFieldTypes]
    TYPE_ONEOF: _ClassVar[SylkFieldTypes]

class SylkFieldLabels(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEFAULT_SYLKFIELDLABELS: _ClassVar[SylkFieldLabels]
    LABEL_OPTIONAL: _ClassVar[SylkFieldLabels]
    LABEL_REQUIRED: _ClassVar[SylkFieldLabels]
    LABEL_REPEATED: _ClassVar[SylkFieldLabels]
DEFAULT_SYLKFIELDTYPES: SylkFieldTypes
TYPE_DOUBLE: SylkFieldTypes
TYPE_FLOAT: SylkFieldTypes
TYPE_INT64: SylkFieldTypes
TYPE_UINT64: SylkFieldTypes
TYPE_INT32: SylkFieldTypes
TYPE_FIXED64: SylkFieldTypes
TYPE_FIXED32: SylkFieldTypes
TYPE_BOOL: SylkFieldTypes
TYPE_STRING: SylkFieldTypes
TYPE_GROUP: SylkFieldTypes
TYPE_MESSAGE: SylkFieldTypes
TYPE_BYTES: SylkFieldTypes
TYPE_UINT32: SylkFieldTypes
TYPE_ENUM: SylkFieldTypes
TYPE_SFIXED32: SylkFieldTypes
TYPE_SFIXED64: SylkFieldTypes
TYPE_SINT32: SylkFieldTypes
TYPE_SINT64: SylkFieldTypes
TYPE_MAP: SylkFieldTypes
TYPE_ONEOF: SylkFieldTypes
DEFAULT_SYLKFIELDLABELS: SylkFieldLabels
LABEL_OPTIONAL: SylkFieldLabels
LABEL_REQUIRED: SylkFieldLabels
LABEL_REPEATED: SylkFieldLabels

class SylkOneOfField(_message.Message):
    __slots__ = ["enum_type", "full_name", "uri", "message_type", "field_type", "name", "description", "label", "index", "kind"]
    ENUM_TYPE_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    enum_type: str
    full_name: str
    uri: str
    message_type: str
    field_type: SylkFieldTypes
    name: str
    description: str
    label: SylkFieldLabels
    index: int
    kind: str
    def __init__(self, enum_type: _Optional[str] = ..., full_name: _Optional[str] = ..., uri: _Optional[str] = ..., message_type: _Optional[str] = ..., field_type: _Optional[_Union[SylkFieldTypes, str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., label: _Optional[_Union[SylkFieldLabels, str]] = ..., index: _Optional[int] = ..., kind: _Optional[str] = ...) -> None: ...

class SylkField(_message.Message):
    __slots__ = ["type", "uri", "oneof_fields", "name", "description", "enum_type", "field_type", "message_type", "kind", "full_name", "extensions", "index", "label", "key_type", "value_type"]
    class ExtensionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Struct
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    ONEOF_FIELDS_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENUM_TYPE_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    FULL_NAME_FIELD_NUMBER: _ClassVar[int]
    EXTENSIONS_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    type: str
    uri: str
    oneof_fields: _containers.RepeatedCompositeFieldContainer[SylkOneOfField]
    name: str
    description: str
    enum_type: str
    field_type: SylkFieldTypes
    message_type: str
    kind: str
    full_name: str
    extensions: _containers.MessageMap[str, _struct_pb2.Struct]
    index: int
    label: SylkFieldLabels
    key_type: SylkFieldTypes
    value_type: SylkFieldTypes
    def __init__(self, type: _Optional[str] = ..., uri: _Optional[str] = ..., oneof_fields: _Optional[_Iterable[_Union[SylkOneOfField, _Mapping]]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., enum_type: _Optional[str] = ..., field_type: _Optional[_Union[SylkFieldTypes, str]] = ..., message_type: _Optional[str] = ..., kind: _Optional[str] = ..., full_name: _Optional[str] = ..., extensions: _Optional[_Mapping[str, _struct_pb2.Struct]] = ..., index: _Optional[int] = ..., label: _Optional[_Union[SylkFieldLabels, str]] = ..., key_type: _Optional[_Union[SylkFieldTypes, str]] = ..., value_type: _Optional[_Union[SylkFieldTypes, str]] = ...) -> None: ...

class SylkFieldDisplay(_message.Message):
    __slots__ = ["created_at", "field", "updated_at", "id"]
    CREATED_AT_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    created_at: _timestamp_pb2.Timestamp
    field: SylkField
    updated_at: _timestamp_pb2.Timestamp
    id: str
    def __init__(self, created_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., field: _Optional[_Union[SylkField, _Mapping]] = ..., updated_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., id: _Optional[str] = ...) -> None: ...
