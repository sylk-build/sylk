from google.protobuf import empty_pb2 as _empty_pb2
from sylk.SylkField.v1 import SylkField_pb2 as _SylkField_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetFieldRequest(_message.Message):
    __slots__ = ["project_id", "package", "field"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    field: str
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., field: _Optional[str] = ...) -> None: ...

class GetFieldResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkField_pb2.SylkFieldDisplay
    def __init__(self, result: _Optional[_Union[_SylkField_pb2.SylkFieldDisplay, _Mapping]] = ...) -> None: ...

class CreateFieldRequest(_message.Message):
    __slots__ = ["project_id", "package", "field"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    field: _SylkField_pb2.SylkField
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., field: _Optional[_Union[_SylkField_pb2.SylkField, _Mapping]] = ...) -> None: ...

class CreateFieldResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkField_pb2.SylkFieldDisplay
    def __init__(self, result: _Optional[_Union[_SylkField_pb2.SylkFieldDisplay, _Mapping]] = ...) -> None: ...

class UpdateFieldRequest(_message.Message):
    __slots__ = ["project_id", "package", "field", "update", "is_oneof"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    IS_ONEOF_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    field: str
    update: _SylkField_pb2.SylkField
    is_oneof: bool
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., field: _Optional[str] = ..., update: _Optional[_Union[_SylkField_pb2.SylkField, _Mapping]] = ..., is_oneof: bool = ...) -> None: ...

class UpdateFieldResponse(_message.Message):
    __slots__ = ["field", "updated"]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    field: str
    updated: _SylkField_pb2.SylkFieldDisplay
    def __init__(self, field: _Optional[str] = ..., updated: _Optional[_Union[_SylkField_pb2.SylkFieldDisplay, _Mapping]] = ...) -> None: ...

class DeleteFieldRequest(_message.Message):
    __slots__ = ["project_id", "package", "field", "is_oneof"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    FIELD_FIELD_NUMBER: _ClassVar[int]
    IS_ONEOF_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    package: str
    field: str
    is_oneof: bool
    def __init__(self, project_id: _Optional[str] = ..., package: _Optional[str] = ..., field: _Optional[str] = ..., is_oneof: bool = ...) -> None: ...
