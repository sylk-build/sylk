from sylk.SylkProject.v1 import SylkProject_pb2 as _SylkProject_pb2
from sylk.SylkOrganization.v1 import SylkOrganization_pb2 as _SylkOrganization_pb2
from sylk.SylkService.v1 import SylkService_pb2 as _SylkService_pb2
from sylk.SylkPackage.v1 import SylkPackage_pb2 as _SylkPackage_pb2
from sylk.SylkConfigs.v1 import SylkConfigs_pb2 as _SylkConfigs_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkJson(_message.Message):
    __slots__ = ["sylk_version", "project", "organization", "services", "packages", "configs"]
    class ServicesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _SylkService_pb2.SylkService
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_SylkService_pb2.SylkService, _Mapping]] = ...) -> None: ...
    class PackagesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _SylkPackage_pb2.SylkPackage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_SylkPackage_pb2.SylkPackage, _Mapping]] = ...) -> None: ...
    SYLK_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    SERVICES_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    sylk_version: str
    project: _SylkProject_pb2.SylkProject
    organization: _SylkOrganization_pb2.SylkOrganization
    services: _containers.MessageMap[str, _SylkService_pb2.SylkService]
    packages: _containers.MessageMap[str, _SylkPackage_pb2.SylkPackage]
    configs: _SylkConfigs_pb2.SylkProjectConfigs
    def __init__(self, sylk_version: _Optional[str] = ..., project: _Optional[_Union[_SylkProject_pb2.SylkProject, _Mapping]] = ..., organization: _Optional[_Union[_SylkOrganization_pb2.SylkOrganization, _Mapping]] = ..., services: _Optional[_Mapping[str, _SylkService_pb2.SylkService]] = ..., packages: _Optional[_Mapping[str, _SylkPackage_pb2.SylkPackage]] = ..., configs: _Optional[_Union[_SylkConfigs_pb2.SylkProjectConfigs, _Mapping]] = ...) -> None: ...
