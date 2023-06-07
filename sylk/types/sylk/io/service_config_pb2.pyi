from sylk.types.google.rpc import code_pb2 as _code_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServiceConfig(_message.Message):
    __slots__ = ["load_balancing_policy", "method_config"]
    LOAD_BALANCING_POLICY_FIELD_NUMBER: _ClassVar[int]
    METHOD_CONFIG_FIELD_NUMBER: _ClassVar[int]
    load_balancing_policy: str
    method_config: _containers.RepeatedCompositeFieldContainer[MethodConfig]
    def __init__(self, load_balancing_policy: _Optional[str] = ..., method_config: _Optional[_Iterable[_Union[MethodConfig, _Mapping]]] = ...) -> None: ...

class MethodConfig(_message.Message):
    __slots__ = ["name", "retry_policy", "wait_for_ready", "timeout", "max_request_message_bytes", "max_response_message_bytes", "retry_throttling"]
    class MethodPath(_message.Message):
        __slots__ = ["service", "method"]
        SERVICE_FIELD_NUMBER: _ClassVar[int]
        METHOD_FIELD_NUMBER: _ClassVar[int]
        service: str
        method: str
        def __init__(self, service: _Optional[str] = ..., method: _Optional[str] = ...) -> None: ...
    class RetryPolicy(_message.Message):
        __slots__ = ["max_attempts", "initial_backoff", "max_backoff", "backoff_multiplier", "retryable_status_codes"]
        MAX_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
        INITIAL_BACKOFF_FIELD_NUMBER: _ClassVar[int]
        MAX_BACKOFF_FIELD_NUMBER: _ClassVar[int]
        BACKOFF_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
        RETRYABLE_STATUS_CODES_FIELD_NUMBER: _ClassVar[int]
        max_attempts: int
        initial_backoff: str
        max_backoff: str
        backoff_multiplier: float
        retryable_status_codes: _containers.RepeatedScalarFieldContainer[_code_pb2.Code]
        def __init__(self, max_attempts: _Optional[int] = ..., initial_backoff: _Optional[str] = ..., max_backoff: _Optional[str] = ..., backoff_multiplier: _Optional[float] = ..., retryable_status_codes: _Optional[_Iterable[_Union[_code_pb2.Code, str]]] = ...) -> None: ...
    class RetryThrottling(_message.Message):
        __slots__ = ["max_tokens", "token_ratio"]
        MAX_TOKENS_FIELD_NUMBER: _ClassVar[int]
        TOKEN_RATIO_FIELD_NUMBER: _ClassVar[int]
        max_tokens: float
        token_ratio: float
        def __init__(self, max_tokens: _Optional[float] = ..., token_ratio: _Optional[float] = ...) -> None: ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_READY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    MAX_REQUEST_MESSAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    MAX_RESPONSE_MESSAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    RETRY_THROTTLING_FIELD_NUMBER: _ClassVar[int]
    name: MethodConfig.MethodPath
    retry_policy: MethodConfig.RetryPolicy
    wait_for_ready: bool
    timeout: str
    max_request_message_bytes: int
    max_response_message_bytes: int
    retry_throttling: MethodConfig.RetryThrottling
    def __init__(self, name: _Optional[_Union[MethodConfig.MethodPath, _Mapping]] = ..., retry_policy: _Optional[_Union[MethodConfig.RetryPolicy, _Mapping]] = ..., wait_for_ready: bool = ..., timeout: _Optional[str] = ..., max_request_message_bytes: _Optional[int] = ..., max_response_message_bytes: _Optional[int] = ..., retry_throttling: _Optional[_Union[MethodConfig.RetryThrottling, _Mapping]] = ...) -> None: ...
