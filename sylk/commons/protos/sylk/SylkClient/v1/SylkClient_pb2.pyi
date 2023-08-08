from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkClientLanguages(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEFAULT_SYLKCLIENTLANGUAGES: _ClassVar[SylkClientLanguages]
    python: _ClassVar[SylkClientLanguages]
    nodejs: _ClassVar[SylkClientLanguages]
    typescript: _ClassVar[SylkClientLanguages]
    go: _ClassVar[SylkClientLanguages]
    webpack: _ClassVar[SylkClientLanguages]
DEFAULT_SYLKCLIENTLANGUAGES: SylkClientLanguages
python: SylkClientLanguages
nodejs: SylkClientLanguages
typescript: SylkClientLanguages
go: SylkClientLanguages
webpack: SylkClientLanguages

class SylkClient(_message.Message):
    __slots__ = ["language", "out_dir"]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    OUT_DIR_FIELD_NUMBER: _ClassVar[int]
    language: SylkClientLanguages
    out_dir: str
    def __init__(self, language: _Optional[_Union[SylkClientLanguages, str]] = ..., out_dir: _Optional[str] = ...) -> None: ...
