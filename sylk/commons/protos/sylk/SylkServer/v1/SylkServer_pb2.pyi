from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkServerLanguages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEFAULT_SYLKSERVERLANGUAGES: _ClassVar[SylkServerLanguages]
    python: _ClassVar[SylkServerLanguages]
    nodejs: _ClassVar[SylkServerLanguages]
    typescript: _ClassVar[SylkServerLanguages]
    go: _ClassVar[SylkServerLanguages]
DEFAULT_SYLKSERVERLANGUAGES: SylkServerLanguages
python: SylkServerLanguages
nodejs: SylkServerLanguages
typescript: SylkServerLanguages
go: SylkServerLanguages

class SylkServer(_message.Message):
    __slots__ = ["language"]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    language: SylkServerLanguages
    def __init__(self, language: _Optional[_Union[SylkServerLanguages, str]] = ...) -> None: ...
