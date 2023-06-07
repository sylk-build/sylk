// Copyright 2023 Sylk.  All rights reserved.

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v3.21.12
// source: sylk/io/service_config.proto

package service_config

import (
	code "google.golang.org/genproto/googleapis/rpc/code"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type ServiceConfig struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	LoadBalancingPolicy string          `protobuf:"bytes,1,opt,name=load_balancing_policy,json=loadBalancingPolicy,proto3" json:"load_balancing_policy,omitempty"`
	MethodConfig        []*MethodConfig `protobuf:"bytes,2,rep,name=method_config,json=methodConfig,proto3" json:"method_config,omitempty"`
}

func (x *ServiceConfig) Reset() {
	*x = ServiceConfig{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_io_service_config_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ServiceConfig) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ServiceConfig) ProtoMessage() {}

func (x *ServiceConfig) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_io_service_config_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ServiceConfig.ProtoReflect.Descriptor instead.
func (*ServiceConfig) Descriptor() ([]byte, []int) {
	return file_sylk_io_service_config_proto_rawDescGZIP(), []int{0}
}

func (x *ServiceConfig) GetLoadBalancingPolicy() string {
	if x != nil {
		return x.LoadBalancingPolicy
	}
	return ""
}

func (x *ServiceConfig) GetMethodConfig() []*MethodConfig {
	if x != nil {
		return x.MethodConfig
	}
	return nil
}

type MethodConfig struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name                    *MethodConfig_MethodPath      `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	RetryPolicy             *MethodConfig_RetryPolicy     `protobuf:"bytes,2,opt,name=retry_policy,json=retryPolicy,proto3" json:"retry_policy,omitempty"`
	WaitForReady            bool                          `protobuf:"varint,3,opt,name=wait_for_ready,json=waitForReady,proto3" json:"wait_for_ready,omitempty"`
	Timeout                 string                        `protobuf:"bytes,4,opt,name=timeout,proto3" json:"timeout,omitempty"`
	MaxRequestMessageBytes  int32                         `protobuf:"varint,5,opt,name=max_request_message_bytes,json=maxRequestMessageBytes,proto3" json:"max_request_message_bytes,omitempty"`
	MaxResponseMessageBytes int32                         `protobuf:"varint,6,opt,name=max_response_message_bytes,json=maxResponseMessageBytes,proto3" json:"max_response_message_bytes,omitempty"`
	RetryThrottling         *MethodConfig_RetryThrottling `protobuf:"bytes,7,opt,name=retry_throttling,json=retryThrottling,proto3" json:"retry_throttling,omitempty"`
}

func (x *MethodConfig) Reset() {
	*x = MethodConfig{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_io_service_config_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *MethodConfig) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MethodConfig) ProtoMessage() {}

func (x *MethodConfig) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_io_service_config_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MethodConfig.ProtoReflect.Descriptor instead.
func (*MethodConfig) Descriptor() ([]byte, []int) {
	return file_sylk_io_service_config_proto_rawDescGZIP(), []int{1}
}

func (x *MethodConfig) GetName() *MethodConfig_MethodPath {
	if x != nil {
		return x.Name
	}
	return nil
}

func (x *MethodConfig) GetRetryPolicy() *MethodConfig_RetryPolicy {
	if x != nil {
		return x.RetryPolicy
	}
	return nil
}

func (x *MethodConfig) GetWaitForReady() bool {
	if x != nil {
		return x.WaitForReady
	}
	return false
}

func (x *MethodConfig) GetTimeout() string {
	if x != nil {
		return x.Timeout
	}
	return ""
}

func (x *MethodConfig) GetMaxRequestMessageBytes() int32 {
	if x != nil {
		return x.MaxRequestMessageBytes
	}
	return 0
}

func (x *MethodConfig) GetMaxResponseMessageBytes() int32 {
	if x != nil {
		return x.MaxResponseMessageBytes
	}
	return 0
}

func (x *MethodConfig) GetRetryThrottling() *MethodConfig_RetryThrottling {
	if x != nil {
		return x.RetryThrottling
	}
	return nil
}

type MethodConfig_MethodPath struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Service string `protobuf:"bytes,1,opt,name=service,proto3" json:"service,omitempty"`
	Method  string `protobuf:"bytes,2,opt,name=method,proto3" json:"method,omitempty"`
}

func (x *MethodConfig_MethodPath) Reset() {
	*x = MethodConfig_MethodPath{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_io_service_config_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *MethodConfig_MethodPath) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MethodConfig_MethodPath) ProtoMessage() {}

func (x *MethodConfig_MethodPath) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_io_service_config_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MethodConfig_MethodPath.ProtoReflect.Descriptor instead.
func (*MethodConfig_MethodPath) Descriptor() ([]byte, []int) {
	return file_sylk_io_service_config_proto_rawDescGZIP(), []int{1, 0}
}

func (x *MethodConfig_MethodPath) GetService() string {
	if x != nil {
		return x.Service
	}
	return ""
}

func (x *MethodConfig_MethodPath) GetMethod() string {
	if x != nil {
		return x.Method
	}
	return ""
}

type MethodConfig_RetryPolicy struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The maximum number of RPC attempts, including the original RPC.
	// This field is required and must be two or greater.
	MaxAttempts int32 `protobuf:"varint,1,opt,name=max_attempts,json=maxAttempts,proto3" json:"max_attempts,omitempty"`
	// Exponential backoff parameters. The initial retry attempt will occur at
	// random(0, initialBackoff). In general, the nth attempt since the last
	// server pushback response (if any), will occur at random(0,
	//
	//	min(initialBackoff*backoffMultiplier**(n-1), maxBackoff)).
	//
	// The following two fields take their form from:
	// https://developers.google.com/protocol-buffers/docs/proto3#json
	// They are representations of the proto3 Duration type. Note that the
	// numeric portion of the string must be a valid JSON number.
	// They both must be greater than zero.
	InitialBackoff    string  `protobuf:"bytes,2,opt,name=initial_backoff,json=initialBackoff,proto3" json:"initial_backoff,omitempty"`            // Required. Long decimal with "s" appended
	MaxBackoff        string  `protobuf:"bytes,3,opt,name=max_backoff,json=maxBackoff,proto3" json:"max_backoff,omitempty"`                        // Required. Long decimal with "s" appended
	BackoffMultiplier float64 `protobuf:"fixed64,4,opt,name=backoff_multiplier,json=backoffMultiplier,proto3" json:"backoff_multiplier,omitempty"` // Required. Must be greater than zero.
	// The set of status codes which may be retried.
	//
	// Status codes are specified in the integer form or the case-insensitive
	// string form (eg. [14], ["UNAVAILABLE"] or ["unavailable"])
	//
	// This field is required and must be non-empty.
	RetryableStatusCodes []code.Code `protobuf:"varint,5,rep,packed,name=retryable_status_codes,json=retryableStatusCodes,proto3,enum=google.rpc.Code" json:"retryable_status_codes,omitempty"`
}

func (x *MethodConfig_RetryPolicy) Reset() {
	*x = MethodConfig_RetryPolicy{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_io_service_config_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *MethodConfig_RetryPolicy) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MethodConfig_RetryPolicy) ProtoMessage() {}

func (x *MethodConfig_RetryPolicy) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_io_service_config_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MethodConfig_RetryPolicy.ProtoReflect.Descriptor instead.
func (*MethodConfig_RetryPolicy) Descriptor() ([]byte, []int) {
	return file_sylk_io_service_config_proto_rawDescGZIP(), []int{1, 1}
}

func (x *MethodConfig_RetryPolicy) GetMaxAttempts() int32 {
	if x != nil {
		return x.MaxAttempts
	}
	return 0
}

func (x *MethodConfig_RetryPolicy) GetInitialBackoff() string {
	if x != nil {
		return x.InitialBackoff
	}
	return ""
}

func (x *MethodConfig_RetryPolicy) GetMaxBackoff() string {
	if x != nil {
		return x.MaxBackoff
	}
	return ""
}

func (x *MethodConfig_RetryPolicy) GetBackoffMultiplier() float64 {
	if x != nil {
		return x.BackoffMultiplier
	}
	return 0
}

func (x *MethodConfig_RetryPolicy) GetRetryableStatusCodes() []code.Code {
	if x != nil {
		return x.RetryableStatusCodes
	}
	return nil
}

// If a RetryThrottlingPolicy is provided, gRPC will automatically throttle
// retry attempts and hedged RPCs when the client’s ratio of failures to
// successes exceeds a threshold.
//
// For each server name, the gRPC client will maintain a token_count which is
// initially set to maxTokens, and can take values between 0 and maxTokens.
//
// Every outgoing RPC (regardless of service or method invoked) will change
// token_count as follows:
//
//   - Every failed RPC will decrement the token_count by 1.
//   - Every successful RPC will increment the token_count by tokenRatio.
//
// If token_count is less than or equal to maxTokens / 2, then RPCs will not
// be retried and hedged RPCs will not be sent.
type MethodConfig_RetryThrottling struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	// The number of tokens starts at maxTokens. The token_count will always be
	// between 0 and maxTokens.
	//
	// This field is required and must be in the range (0, 1000].  Up to 3
	// decimal places are supported
	MaxTokens float64 `protobuf:"fixed64,1,opt,name=max_tokens,json=maxTokens,proto3" json:"max_tokens,omitempty"`
	// The amount of tokens to add on each successful RPC. Typically this will
	// be some number between 0 and 1, e.g., 0.1.
	//
	// This field is required and must be greater than zero. Up to 3 decimal
	// places are supported.
	TokenRatio float64 `protobuf:"fixed64,2,opt,name=token_ratio,json=tokenRatio,proto3" json:"token_ratio,omitempty"`
}

func (x *MethodConfig_RetryThrottling) Reset() {
	*x = MethodConfig_RetryThrottling{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_io_service_config_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *MethodConfig_RetryThrottling) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*MethodConfig_RetryThrottling) ProtoMessage() {}

func (x *MethodConfig_RetryThrottling) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_io_service_config_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use MethodConfig_RetryThrottling.ProtoReflect.Descriptor instead.
func (*MethodConfig_RetryThrottling) Descriptor() ([]byte, []int) {
	return file_sylk_io_service_config_proto_rawDescGZIP(), []int{1, 2}
}

func (x *MethodConfig_RetryThrottling) GetMaxTokens() float64 {
	if x != nil {
		return x.MaxTokens
	}
	return 0
}

func (x *MethodConfig_RetryThrottling) GetTokenRatio() float64 {
	if x != nil {
		return x.TokenRatio
	}
	return 0
}

var File_sylk_io_service_config_proto protoreflect.FileDescriptor

var file_sylk_io_service_config_proto_rawDesc = []byte{
	0x0a, 0x1c, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x69, 0x6f, 0x2f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63,
	0x65, 0x5f, 0x63, 0x6f, 0x6e, 0x66, 0x69, 0x67, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x07,
	0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x69, 0x6f, 0x1a, 0x15, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f,
	0x72, 0x70, 0x63, 0x2f, 0x63, 0x6f, 0x64, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x7f,
	0x0a, 0x0d, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x43, 0x6f, 0x6e, 0x66, 0x69, 0x67, 0x12,
	0x32, 0x0a, 0x15, 0x6c, 0x6f, 0x61, 0x64, 0x5f, 0x62, 0x61, 0x6c, 0x61, 0x6e, 0x63, 0x69, 0x6e,
	0x67, 0x5f, 0x70, 0x6f, 0x6c, 0x69, 0x63, 0x79, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x13,
	0x6c, 0x6f, 0x61, 0x64, 0x42, 0x61, 0x6c, 0x61, 0x6e, 0x63, 0x69, 0x6e, 0x67, 0x50, 0x6f, 0x6c,
	0x69, 0x63, 0x79, 0x12, 0x3a, 0x0a, 0x0d, 0x6d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x5f, 0x63, 0x6f,
	0x6e, 0x66, 0x69, 0x67, 0x18, 0x02, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x15, 0x2e, 0x73, 0x79, 0x6c,
	0x6b, 0x2e, 0x69, 0x6f, 0x2e, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x43, 0x6f, 0x6e, 0x66, 0x69,
	0x67, 0x52, 0x0c, 0x6d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x43, 0x6f, 0x6e, 0x66, 0x69, 0x67, 0x22,
	0x9b, 0x06, 0x0a, 0x0c, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x43, 0x6f, 0x6e, 0x66, 0x69, 0x67,
	0x12, 0x34, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x20,
	0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x69, 0x6f, 0x2e, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x43,
	0x6f, 0x6e, 0x66, 0x69, 0x67, 0x2e, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x50, 0x61, 0x74, 0x68,
	0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x44, 0x0a, 0x0c, 0x72, 0x65, 0x74, 0x72, 0x79, 0x5f,
	0x70, 0x6f, 0x6c, 0x69, 0x63, 0x79, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x21, 0x2e, 0x73,
	0x79, 0x6c, 0x6b, 0x2e, 0x69, 0x6f, 0x2e, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x43, 0x6f, 0x6e,
	0x66, 0x69, 0x67, 0x2e, 0x52, 0x65, 0x74, 0x72, 0x79, 0x50, 0x6f, 0x6c, 0x69, 0x63, 0x79, 0x52,
	0x0b, 0x72, 0x65, 0x74, 0x72, 0x79, 0x50, 0x6f, 0x6c, 0x69, 0x63, 0x79, 0x12, 0x24, 0x0a, 0x0e,
	0x77, 0x61, 0x69, 0x74, 0x5f, 0x66, 0x6f, 0x72, 0x5f, 0x72, 0x65, 0x61, 0x64, 0x79, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x08, 0x52, 0x0c, 0x77, 0x61, 0x69, 0x74, 0x46, 0x6f, 0x72, 0x52, 0x65, 0x61,
	0x64, 0x79, 0x12, 0x18, 0x0a, 0x07, 0x74, 0x69, 0x6d, 0x65, 0x6f, 0x75, 0x74, 0x18, 0x04, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x07, 0x74, 0x69, 0x6d, 0x65, 0x6f, 0x75, 0x74, 0x12, 0x39, 0x0a, 0x19,
	0x6d, 0x61, 0x78, 0x5f, 0x72, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x5f, 0x6d, 0x65, 0x73, 0x73,
	0x61, 0x67, 0x65, 0x5f, 0x62, 0x79, 0x74, 0x65, 0x73, 0x18, 0x05, 0x20, 0x01, 0x28, 0x05, 0x52,
	0x16, 0x6d, 0x61, 0x78, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x4d, 0x65, 0x73, 0x73, 0x61,
	0x67, 0x65, 0x42, 0x79, 0x74, 0x65, 0x73, 0x12, 0x3b, 0x0a, 0x1a, 0x6d, 0x61, 0x78, 0x5f, 0x72,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x5f, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x5f,
	0x62, 0x79, 0x74, 0x65, 0x73, 0x18, 0x06, 0x20, 0x01, 0x28, 0x05, 0x52, 0x17, 0x6d, 0x61, 0x78,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x42,
	0x79, 0x74, 0x65, 0x73, 0x12, 0x50, 0x0a, 0x10, 0x72, 0x65, 0x74, 0x72, 0x79, 0x5f, 0x74, 0x68,
	0x72, 0x6f, 0x74, 0x74, 0x6c, 0x69, 0x6e, 0x67, 0x18, 0x07, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x25,
	0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x69, 0x6f, 0x2e, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x43,
	0x6f, 0x6e, 0x66, 0x69, 0x67, 0x2e, 0x52, 0x65, 0x74, 0x72, 0x79, 0x54, 0x68, 0x72, 0x6f, 0x74,
	0x74, 0x6c, 0x69, 0x6e, 0x67, 0x52, 0x0f, 0x72, 0x65, 0x74, 0x72, 0x79, 0x54, 0x68, 0x72, 0x6f,
	0x74, 0x74, 0x6c, 0x69, 0x6e, 0x67, 0x1a, 0x3e, 0x0a, 0x0a, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64,
	0x50, 0x61, 0x74, 0x68, 0x12, 0x18, 0x0a, 0x07, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x07, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x16,
	0x0a, 0x06, 0x6d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x06,
	0x6d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x1a, 0xf1, 0x01, 0x0a, 0x0b, 0x52, 0x65, 0x74, 0x72, 0x79,
	0x50, 0x6f, 0x6c, 0x69, 0x63, 0x79, 0x12, 0x21, 0x0a, 0x0c, 0x6d, 0x61, 0x78, 0x5f, 0x61, 0x74,
	0x74, 0x65, 0x6d, 0x70, 0x74, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0b, 0x6d, 0x61,
	0x78, 0x41, 0x74, 0x74, 0x65, 0x6d, 0x70, 0x74, 0x73, 0x12, 0x27, 0x0a, 0x0f, 0x69, 0x6e, 0x69,
	0x74, 0x69, 0x61, 0x6c, 0x5f, 0x62, 0x61, 0x63, 0x6b, 0x6f, 0x66, 0x66, 0x18, 0x02, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x0e, 0x69, 0x6e, 0x69, 0x74, 0x69, 0x61, 0x6c, 0x42, 0x61, 0x63, 0x6b, 0x6f,
	0x66, 0x66, 0x12, 0x1f, 0x0a, 0x0b, 0x6d, 0x61, 0x78, 0x5f, 0x62, 0x61, 0x63, 0x6b, 0x6f, 0x66,
	0x66, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0a, 0x6d, 0x61, 0x78, 0x42, 0x61, 0x63, 0x6b,
	0x6f, 0x66, 0x66, 0x12, 0x2d, 0x0a, 0x12, 0x62, 0x61, 0x63, 0x6b, 0x6f, 0x66, 0x66, 0x5f, 0x6d,
	0x75, 0x6c, 0x74, 0x69, 0x70, 0x6c, 0x69, 0x65, 0x72, 0x18, 0x04, 0x20, 0x01, 0x28, 0x01, 0x52,
	0x11, 0x62, 0x61, 0x63, 0x6b, 0x6f, 0x66, 0x66, 0x4d, 0x75, 0x6c, 0x74, 0x69, 0x70, 0x6c, 0x69,
	0x65, 0x72, 0x12, 0x46, 0x0a, 0x16, 0x72, 0x65, 0x74, 0x72, 0x79, 0x61, 0x62, 0x6c, 0x65, 0x5f,
	0x73, 0x74, 0x61, 0x74, 0x75, 0x73, 0x5f, 0x63, 0x6f, 0x64, 0x65, 0x73, 0x18, 0x05, 0x20, 0x03,
	0x28, 0x0e, 0x32, 0x10, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x72, 0x70, 0x63, 0x2e,
	0x43, 0x6f, 0x64, 0x65, 0x52, 0x14, 0x72, 0x65, 0x74, 0x72, 0x79, 0x61, 0x62, 0x6c, 0x65, 0x53,
	0x74, 0x61, 0x74, 0x75, 0x73, 0x43, 0x6f, 0x64, 0x65, 0x73, 0x1a, 0x51, 0x0a, 0x0f, 0x52, 0x65,
	0x74, 0x72, 0x79, 0x54, 0x68, 0x72, 0x6f, 0x74, 0x74, 0x6c, 0x69, 0x6e, 0x67, 0x12, 0x1d, 0x0a,
	0x0a, 0x6d, 0x61, 0x78, 0x5f, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x73, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x01, 0x52, 0x09, 0x6d, 0x61, 0x78, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x73, 0x12, 0x1f, 0x0a, 0x0b,
	0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x5f, 0x72, 0x61, 0x74, 0x69, 0x6f, 0x18, 0x02, 0x20, 0x01, 0x28,
	0x01, 0x52, 0x0a, 0x74, 0x6f, 0x6b, 0x65, 0x6e, 0x52, 0x61, 0x74, 0x69, 0x6f, 0x42, 0x43, 0x5a,
	0x41, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x73, 0x79, 0x6c, 0x6b,
	0x2d, 0x62, 0x75, 0x69, 0x6c, 0x64, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2d, 0x69, 0x6f, 0x2f, 0x74,
	0x79, 0x70, 0x65, 0x73, 0x2f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x5f, 0x63, 0x6f, 0x6e,
	0x66, 0x69, 0x67, 0x3b, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x5f, 0x63, 0x6f, 0x6e, 0x66,
	0x69, 0x67, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_sylk_io_service_config_proto_rawDescOnce sync.Once
	file_sylk_io_service_config_proto_rawDescData = file_sylk_io_service_config_proto_rawDesc
)

func file_sylk_io_service_config_proto_rawDescGZIP() []byte {
	file_sylk_io_service_config_proto_rawDescOnce.Do(func() {
		file_sylk_io_service_config_proto_rawDescData = protoimpl.X.CompressGZIP(file_sylk_io_service_config_proto_rawDescData)
	})
	return file_sylk_io_service_config_proto_rawDescData
}

var file_sylk_io_service_config_proto_msgTypes = make([]protoimpl.MessageInfo, 5)
var file_sylk_io_service_config_proto_goTypes = []interface{}{
	(*ServiceConfig)(nil),                // 0: sylk.io.ServiceConfig
	(*MethodConfig)(nil),                 // 1: sylk.io.MethodConfig
	(*MethodConfig_MethodPath)(nil),      // 2: sylk.io.MethodConfig.MethodPath
	(*MethodConfig_RetryPolicy)(nil),     // 3: sylk.io.MethodConfig.RetryPolicy
	(*MethodConfig_RetryThrottling)(nil), // 4: sylk.io.MethodConfig.RetryThrottling
	(code.Code)(0),                       // 5: google.rpc.Code
}
var file_sylk_io_service_config_proto_depIdxs = []int32{
	1, // 0: sylk.io.ServiceConfig.method_config:type_name -> sylk.io.MethodConfig
	2, // 1: sylk.io.MethodConfig.name:type_name -> sylk.io.MethodConfig.MethodPath
	3, // 2: sylk.io.MethodConfig.retry_policy:type_name -> sylk.io.MethodConfig.RetryPolicy
	4, // 3: sylk.io.MethodConfig.retry_throttling:type_name -> sylk.io.MethodConfig.RetryThrottling
	5, // 4: sylk.io.MethodConfig.RetryPolicy.retryable_status_codes:type_name -> google.rpc.Code
	5, // [5:5] is the sub-list for method output_type
	5, // [5:5] is the sub-list for method input_type
	5, // [5:5] is the sub-list for extension type_name
	5, // [5:5] is the sub-list for extension extendee
	0, // [0:5] is the sub-list for field type_name
}

func init() { file_sylk_io_service_config_proto_init() }
func file_sylk_io_service_config_proto_init() {
	if File_sylk_io_service_config_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_sylk_io_service_config_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ServiceConfig); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_sylk_io_service_config_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*MethodConfig); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_sylk_io_service_config_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*MethodConfig_MethodPath); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_sylk_io_service_config_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*MethodConfig_RetryPolicy); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_sylk_io_service_config_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*MethodConfig_RetryThrottling); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_sylk_io_service_config_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   5,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_sylk_io_service_config_proto_goTypes,
		DependencyIndexes: file_sylk_io_service_config_proto_depIdxs,
		MessageInfos:      file_sylk_io_service_config_proto_msgTypes,
	}.Build()
	File_sylk_io_service_config_proto = out.File
	file_sylk_io_service_config_proto_rawDesc = nil
	file_sylk_io_service_config_proto_goTypes = nil
	file_sylk_io_service_config_proto_depIdxs = nil
}