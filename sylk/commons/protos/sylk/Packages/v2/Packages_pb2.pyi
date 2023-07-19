from sylk.SylkPackage.v2 import SylkPackage_pb2 as _SylkPackage_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetPackageRequest(_message.Message):
    __slots__ = ["project_id", "package"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ...) -> None: ...

class GetPackageResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkPackage_pb2.SylkPackageDisplay
    def __init__(self, result: _Optional[_Union[_SylkPackage_pb2.SylkPackageDisplay, _Mapping]] = ...) -> None: ...

class CreatePackageRequest(_message.Message):
    __slots__ = ["project_id", "package", "tags"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: _SylkPackage_pb2.SylkPackage
    tags: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[_Union[_SylkPackage_pb2.SylkPackage, _Mapping]] = ..., tags: _Optional[_Iterable[str]] = ...) -> None: ...

class CreatePackageResponse(_message.Message):
    __slots__ = ["project_id", "result"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    result: _SylkPackage_pb2.SylkPackageDisplay
    def __init__(self, project_id: _Optional[str] = ..., result: _Optional[_Union[_SylkPackage_pb2.SylkPackageDisplay, _Mapping]] = ...) -> None: ...

class DeletePackageRequest(_message.Message):
    __slots__ = ["project_id", "package"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ...) -> None: ...

class UpdatePackageRequest(_message.Message):
    __slots__ = ["project_id", "package", "update"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    update: _SylkPackage_pb2.SylkPackage
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., update: _Optional[_Union[_SylkPackage_pb2.SylkPackage, _Mapping]] = ...) -> None: ...

class UpdatePackageResponse(_message.Message):
    __slots__ = ["project_id", "package", "updated"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    updated: _SylkPackage_pb2.SylkPackageDisplay
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., updated: _Optional[_Union[_SylkPackage_pb2.SylkPackageDisplay, _Mapping]] = ...) -> None: ...
