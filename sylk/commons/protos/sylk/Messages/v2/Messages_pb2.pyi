from google.protobuf import empty_pb2 as _empty_pb2
from sylk.SylkMessage.v1 import SylkMessage_pb2 as _SylkMessage_pb2
from sylk.SylkMessage.v2 import SylkMessage_pb2 as _SylkMessage_pb2_1
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMessageRequest(_message.Message):
    __slots__ = ["project_id", "message", "package"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    message: str
    package: str
    def __init__(self, project_id: _Optional[str] = ..., message: _Optional[str] = ..., package: _Optional[str] = ...) -> None: ...

class GetMessageResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkMessage_pb2_1.SylkMessageDisplay
    def __init__(self, result: _Optional[_Union[_SylkMessage_pb2_1.SylkMessageDisplay, _Mapping]] = ...) -> None: ...

class CreateMessageRequest(_message.Message):
    __slots__ = ["project_id", "message", "package"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    message: _SylkMessage_pb2_1.SylkMessage
    package: str
    def __init__(self, project_id: _Optional[str] = ..., message: _Optional[_Union[_SylkMessage_pb2_1.SylkMessage, _Mapping]] = ..., package: _Optional[str] = ...) -> None: ...

class CreateMessageResponse(_message.Message):
    __slots__ = ["result"]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _SylkMessage_pb2_1.SylkMessageDisplay
    def __init__(self, result: _Optional[_Union[_SylkMessage_pb2_1.SylkMessageDisplay, _Mapping]] = ...) -> None: ...

class UpdateMessageRequest(_message.Message):
    __slots__ = ["project_id", "message", "package", "update"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    message: str
    package: str
    update: _SylkMessage_pb2_1.SylkMessage
    def __init__(self, project_id: _Optional[str] = ..., message: _Optional[str] = ..., package: _Optional[str] = ..., update: _Optional[_Union[_SylkMessage_pb2_1.SylkMessage, _Mapping]] = ...) -> None: ...

class UpdateMessageResponse(_message.Message):
    __slots__ = ["message", "updated"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    UPDATED_FIELD_NUMBER: _ClassVar[int]
    message: str
    updated: _SylkMessage_pb2_1.SylkMessageDisplay
    def __init__(self, message: _Optional[str] = ..., updated: _Optional[_Union[_SylkMessage_pb2_1.SylkMessageDisplay, _Mapping]] = ...) -> None: ...

class DeleteMessageRequest(_message.Message):
    __slots__ = ["project_id", "message", "package"]
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PACKAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    message: str
    package: str
    def __init__(self, project_id: _Optional[str] = ..., message: _Optional[str] = ..., package: _Optional[str] = ...) -> None: ...
