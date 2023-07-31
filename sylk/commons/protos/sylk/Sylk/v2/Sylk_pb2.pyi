from sylk.commons.protos.sylk.SylkProject.v1 import SylkProject_pb2 as _SylkProject_pb2
from sylk.commons.protos.sylk.SylkOrganization.v1 import SylkOrganization_pb2 as _SylkOrganization_pb2
from sylk.commons.protos.sylk.SylkService.v1 import SylkService_pb2 as _SylkService_pb2
from sylk.commons.protos.sylk.SylkPackage.v2 import SylkPackage_pb2 as _SylkPackage_pb2
from sylk.commons.protos.sylk.SylkConfigs.v1 import SylkConfigs_pb2 as _SylkConfigs_pb2
from sylk.commons.protos.sylk.SylkPackage.v1 import SylkPackage_pb2 as _SylkPackage_pb2_1
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SylkJson(_message.Message):
    __slots__ = ["organization", "packages", "configs", "sylk_version", "project"]
    class PackagesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _SylkPackage_pb2.SylkPackage
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_SylkPackage_pb2.SylkPackage, _Mapping]] = ...) -> None: ...
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    PACKAGES_FIELD_NUMBER: _ClassVar[int]
    CONFIGS_FIELD_NUMBER: _ClassVar[int]
    SYLK_VERSION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_FIELD_NUMBER: _ClassVar[int]
    organization: _SylkOrganization_pb2.SylkOrganization
    packages: _containers.MessageMap[str, _SylkPackage_pb2.SylkPackage]
    configs: _SylkConfigs_pb2.SylkProjectConfigs
    sylk_version: str
    project: _SylkProject_pb2.SylkProject
    def __init__(self, organization: _Optional[_Union[_SylkOrganization_pb2.SylkOrganization, _Mapping]] = ..., packages: _Optional[_Mapping[str, _SylkPackage_pb2.SylkPackage]] = ..., configs: _Optional[_Union[_SylkConfigs_pb2.SylkProjectConfigs, _Mapping]] = ..., sylk_version: _Optional[str] = ..., project: _Optional[_Union[_SylkProject_pb2.SylkProject, _Mapping]] = ...) -> None: ...
