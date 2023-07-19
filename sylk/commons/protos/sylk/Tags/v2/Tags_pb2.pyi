from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Tag(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class GetTagRequest(_message.Message):
    __slots__ = ["project_id", "package", "name"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class CreateTagRequest(_message.Message):
    __slots__ = ["project_id", "package", "tag"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    tag: Tag
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., tag: _Optional[_Union[Tag, _Mapping]] = ...) -> None: ...

class DeleteTagRequest(_message.Message):
    __slots__ = ["project_id", "package", "name"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    name: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class UpdateTagRequest(_message.Message):
    __slots__ = ["update", "tag", "project_id", "package"]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    update: Tag
    tag: str
    project_id: str
    package: str
    def __init__(self, update: _Optional[_Union[Tag, _Mapping]] = ..., tag: _Optional[str] = ..., project_id: _Optional[str] = ..., package: _Optional[str] = ...) -> None: ...

class TagResourceRequest(_message.Message):
    __slots__ = ["project_id", "package", "tag", "resource"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    tag: str
    resource: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., tag: _Optional[str] = ..., resource: _Optional[str] = ...) -> None: ...

class ListTagsRequest(_message.Message):
    __slots__ = ["project_id", "package"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ...) -> None: ...

class UntagResourceRequest(_message.Message):
    __slots__ = ["project_id", "package", "tag", "resource"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    tag: str
    resource: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., tag: _Optional[str] = ..., resource: _Optional[str] = ...) -> None: ...
