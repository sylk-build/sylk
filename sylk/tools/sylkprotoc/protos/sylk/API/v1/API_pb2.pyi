from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Compilers(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    DEFAULT_COMPILERS: _ClassVar[Compilers]
    PY: _ClassVar[Compilers]
    GO: _ClassVar[Compilers]
    TS: _ClassVar[Compilers]
DEFAULT_COMPILERS: Compilers
PY: Compilers
GO: Compilers
TS: Compilers

class File(_message.Message):
    __slots__ = ["path", "content"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    path: str
    content: bytes
    def __init__(self, path: _Optional[str] = ..., content: _Optional[bytes] = ...) -> None: ...

class GenerateFilesRequest(_message.Message):
    __slots__ = ["code", "file"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    FILE_FIELD_NUMBER: _ClassVar[int]
    code: str
    file: str
    def __init__(self, code: _Optional[str] = ..., file: _Optional[str] = ...) -> None: ...

class CompileRequest(_message.Message):
    __slots__ = ["files", "compiler"]
    FILES_FIELD_NUMBER: _ClassVar[int]
    COMPILER_FIELD_NUMBER: _ClassVar[int]
    files: _containers.RepeatedScalarFieldContainer[str]
    compiler: _containers.RepeatedScalarFieldContainer[Compilers]
    def __init__(self, files: _Optional[_Iterable[str]] = ..., compiler: _Optional[_Iterable[_Union[Compilers, str]]] = ...) -> None: ...
