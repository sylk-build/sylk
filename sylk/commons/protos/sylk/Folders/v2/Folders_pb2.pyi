from google.protobuf import empty_pb2 as _empty_pb2
from sylk.SylkPackage.v2 import SylkPackage_pb2 as _SylkPackage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Folder(_message.Message):
    __slots__ = ["name", "path", "packages", "folders", "description"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    FOLDERS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    path: str
    packages: _containers.RepeatedCompositeFieldContainer[_SylkPackage_pb2.SylkPackage]
    folders: _containers.RepeatedCompositeFieldContainer[Folder]
    description: str
    def __init__(self, name: _Optional[str] = ..., path: _Optional[str] = ..., packages: _Optional[_Iterable[_Union[_SylkPackage_pb2.SylkPackage, _Mapping]]] = ..., folders: _Optional[_Iterable[_Union[Folder, _Mapping]]] = ..., description: _Optional[str] = ...) -> None: ...

class GetFolderRequest(_message.Message):
    __slots__ = ["project_id", "path"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    path: str
    def __init__(self, project_id: _Optional[str] = ..., path: _Optional[str] = ...) -> None: ...

class CreateFolderRequest(_message.Message):
    __slots__ = ["folder", "project_id"]
    FOLDER_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    folder: Folder
    project_id: str
    def __init__(self, folder: _Optional[_Union[Folder, _Mapping]] = ..., project_id: _Optional[str] = ...) -> None: ...

class ListFoldersRequest(_message.Message):
    __slots__ = ["project_id"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    def __init__(self, project_id: _Optional[str] = ...) -> None: ...

class DeleteFolderRequest(_message.Message):
    __slots__ = ["project_id", "folder_path"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    FOLDER_PATH_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    folder_path: str
    def __init__(self, project_id: _Optional[str] = ..., folder_path: _Optional[str] = ...) -> None: ...

class UpdateFolderRequest(_message.Message):
    __slots__ = ["project_id", "path", "name"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    path: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., path: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UpdatePackageResponse(_message.Message):
    __slots__ = ["project_id", "package", "updated"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    updated: _SylkPackage_pb2.SylkPackageDisplay
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., updated: _Optional[_Union[_SylkPackage_pb2.SylkPackageDisplay, _Mapping]] = ...) -> None: ...
