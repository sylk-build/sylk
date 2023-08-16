from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkFrameworks(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN_FRAMEWORK: _ClassVar[SylkFrameworks]
    GRPC: _ClassVar[SylkFrameworks]
    SYLK_JS: _ClassVar[SylkFrameworks]
UNKNOWN_FRAMEWORK: SylkFrameworks
GRPC: SylkFrameworks
SYLK_JS: SylkFrameworks

class SylkTemplateConfigs(_message.Message):
    __slots__ = ["include", "exclude", "name", "description", "out_path", "include_code", "author"]
    INCLUDE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OUT_PATH_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CODE_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    include: _containers.RepeatedScalarFieldContainer[str]
    exclude: _containers.RepeatedScalarFieldContainer[str]
    name: str
    description: str
    out_path: str
    include_code: bool
    author: str
    def __init__(self, include: _Optional[_Iterable[str]] = ..., exclude: _Optional[_Iterable[str]] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., out_path: _Optional[str] = ..., include_code: bool = ..., author: _Optional[str] = ...) -> None: ...

class SylkProjectConfigs(_message.Message):
    __slots__ = ["description", "host", "template", "port", "current_version", "plugins", "proto_base_path", "proto_compiled_path", "code_base_path", "framework"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    CURRENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    PROTO_BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    PROTO_COMPILED_PATH_FIELD_NUMBER: _ClassVar[int]
    CODE_BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    description: str
    host: str
    template: SylkTemplateConfigs
    port: int
    current_version: str
    plugins: _containers.RepeatedScalarFieldContainer[str]
    proto_base_path: str
    proto_compiled_path: str
    code_base_path: str
    framework: SylkFrameworks
    def __init__(self, description: _Optional[str] = ..., host: _Optional[str] = ..., template: _Optional[_Union[SylkTemplateConfigs, _Mapping]] = ..., port: _Optional[int] = ..., current_version: _Optional[str] = ..., plugins: _Optional[_Iterable[str]] = ..., proto_base_path: _Optional[str] = ..., proto_compiled_path: _Optional[str] = ..., code_base_path: _Optional[str] = ..., framework: _Optional[_Union[SylkFrameworks, str]] = ...) -> None: ...

class SylkCliConfigs(_message.Message):
    __slots__ = ["sylk_templates", "port", "token", "analytics", "first_run", "host", "plugins", "proto_base_path", "proto_compiled_path", "template", "code_base_path", "framework"]
    SYLK_TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    ANALYTICS_FIELD_NUMBER: _ClassVar[int]
    FIRST_RUN_FIELD_NUMBER: _ClassVar[int]
    HOST_FIELD_NUMBER: _ClassVar[int]
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    PROTO_BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    PROTO_COMPILED_PATH_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CODE_BASE_PATH_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    sylk_templates: _containers.RepeatedScalarFieldContainer[str]
    port: int
    token: str
    analytics: bool
    first_run: bool
    host: str
    plugins: _containers.RepeatedScalarFieldContainer[str]
    proto_base_path: str
    proto_compiled_path: str
    template: SylkTemplateConfigs
    code_base_path: str
    framework: SylkFrameworks
    def __init__(self, sylk_templates: _Optional[_Iterable[str]] = ..., port: _Optional[int] = ..., token: _Optional[str] = ..., analytics: bool = ..., first_run: bool = ..., host: _Optional[str] = ..., plugins: _Optional[_Iterable[str]] = ..., proto_base_path: _Optional[str] = ..., proto_compiled_path: _Optional[str] = ..., template: _Optional[_Union[SylkTemplateConfigs, _Mapping]] = ..., code_base_path: _Optional[str] = ..., framework: _Optional[_Union[SylkFrameworks, str]] = ...) -> None: ...
