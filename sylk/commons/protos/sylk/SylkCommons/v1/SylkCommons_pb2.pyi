from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkExtensions(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEFAULT_SYLKEXTENSIONS: _ClassVar[SylkExtensions]
    FileOptions: _ClassVar[SylkExtensions]
    MessageOptions: _ClassVar[SylkExtensions]
    FieldOptions: _ClassVar[SylkExtensions]
    ServiceOptions: _ClassVar[SylkExtensions]
    MethodOptions: _ClassVar[SylkExtensions]
DEFAULT_SYLKEXTENSIONS: SylkExtensions
FileOptions: SylkExtensions
MessageOptions: SylkExtensions
FieldOptions: SylkExtensions
ServiceOptions: SylkExtensions
MethodOptions: SylkExtensions

class SylkMethodContext(_message.Message):
    __slots__ = ["code", "type", "name"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    code: str
    type: str
    name: str
    def __init__(self, code: _Optional[str] = ..., type: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class SylkFileContext(_message.Message):
    __slots__ = ["file", "code", "methods"]
    FILE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    METHODS_FIELD_NUMBER: _ClassVar[int]
    file: str
    code: bytes
    methods: _containers.RepeatedCompositeFieldContainer[SylkMethodContext]
    def __init__(self, file: _Optional[str] = ..., code: _Optional[bytes] = ..., methods: _Optional[_Iterable[_Union[SylkMethodContext, _Mapping]]] = ...) -> None: ...

class SylkContext(_message.Message):
    __slots__ = ["files"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedCompositeFieldContainer[SylkFileContext]
    def __init__(self, files: _Optional[_Iterable[_Union[SylkFileContext, _Mapping]]] = ...) -> None: ...
