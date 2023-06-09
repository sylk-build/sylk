// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.23.1
// source: sylk/EnumValues/v1/EnumValues.proto

package v1

import (
	context "context"
	v1 "github.com/sylk-build/sylk-core/services/protos/sylk/SylkApi/v1"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
)

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
// Requires gRPC-Go v1.32.0 or later.
const _ = grpc.SupportPackageIsVersion7

// EnumValuesClient is the client API for EnumValues service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type EnumValuesClient interface {
	// [sylk] - None
	GetEnumValue(ctx context.Context, in *v1.GetEnumValueRequest, opts ...grpc.CallOption) (*v1.GetEnumValueResponse, error)
	// [sylk] - None
	CreateEnumValue(ctx context.Context, in *v1.CreateEnumValueRequest, opts ...grpc.CallOption) (*v1.CreateEnumValueResponse, error)
	// [sylk] - None
	DeleteEnumValue(ctx context.Context, in *v1.DeleteEnumValueRequest, opts ...grpc.CallOption) (*v1.DeleteEnumValueResponse, error)
	// [sylk] - None
	UpdateEnumValue(ctx context.Context, in *v1.UpdateEnumValueRequest, opts ...grpc.CallOption) (*v1.UpdateEnumValueResponse, error)
}

type enumValuesClient struct {
	cc grpc.ClientConnInterface
}

func NewEnumValuesClient(cc grpc.ClientConnInterface) EnumValuesClient {
	return &enumValuesClient{cc}
}

func (c *enumValuesClient) GetEnumValue(ctx context.Context, in *v1.GetEnumValueRequest, opts ...grpc.CallOption) (*v1.GetEnumValueResponse, error) {
	out := new(v1.GetEnumValueResponse)
	err := c.cc.Invoke(ctx, "/EnumValues/GetEnumValue", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enumValuesClient) CreateEnumValue(ctx context.Context, in *v1.CreateEnumValueRequest, opts ...grpc.CallOption) (*v1.CreateEnumValueResponse, error) {
	out := new(v1.CreateEnumValueResponse)
	err := c.cc.Invoke(ctx, "/EnumValues/CreateEnumValue", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enumValuesClient) DeleteEnumValue(ctx context.Context, in *v1.DeleteEnumValueRequest, opts ...grpc.CallOption) (*v1.DeleteEnumValueResponse, error) {
	out := new(v1.DeleteEnumValueResponse)
	err := c.cc.Invoke(ctx, "/EnumValues/DeleteEnumValue", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enumValuesClient) UpdateEnumValue(ctx context.Context, in *v1.UpdateEnumValueRequest, opts ...grpc.CallOption) (*v1.UpdateEnumValueResponse, error) {
	out := new(v1.UpdateEnumValueResponse)
	err := c.cc.Invoke(ctx, "/EnumValues/UpdateEnumValue", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EnumValuesServer is the server API for EnumValues service.
// All implementations must embed UnimplementedEnumValuesServer
// for forward compatibility
type EnumValuesServer interface {
	// [sylk] - None
	GetEnumValue(context.Context, *v1.GetEnumValueRequest) (*v1.GetEnumValueResponse, error)
	// [sylk] - None
	CreateEnumValue(context.Context, *v1.CreateEnumValueRequest) (*v1.CreateEnumValueResponse, error)
	// [sylk] - None
	DeleteEnumValue(context.Context, *v1.DeleteEnumValueRequest) (*v1.DeleteEnumValueResponse, error)
	// [sylk] - None
	UpdateEnumValue(context.Context, *v1.UpdateEnumValueRequest) (*v1.UpdateEnumValueResponse, error)
	mustEmbedUnimplementedEnumValuesServer()
}

// UnimplementedEnumValuesServer must be embedded to have forward compatible implementations.
type UnimplementedEnumValuesServer struct {
}

func (UnimplementedEnumValuesServer) GetEnumValue(context.Context, *v1.GetEnumValueRequest) (*v1.GetEnumValueResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetEnumValue not implemented")
}
func (UnimplementedEnumValuesServer) CreateEnumValue(context.Context, *v1.CreateEnumValueRequest) (*v1.CreateEnumValueResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateEnumValue not implemented")
}
func (UnimplementedEnumValuesServer) DeleteEnumValue(context.Context, *v1.DeleteEnumValueRequest) (*v1.DeleteEnumValueResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteEnumValue not implemented")
}
func (UnimplementedEnumValuesServer) UpdateEnumValue(context.Context, *v1.UpdateEnumValueRequest) (*v1.UpdateEnumValueResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateEnumValue not implemented")
}
func (UnimplementedEnumValuesServer) mustEmbedUnimplementedEnumValuesServer() {}

// UnsafeEnumValuesServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to EnumValuesServer will
// result in compilation errors.
type UnsafeEnumValuesServer interface {
	mustEmbedUnimplementedEnumValuesServer()
}

func RegisterEnumValuesServer(s grpc.ServiceRegistrar, srv EnumValuesServer) {
	s.RegisterService(&EnumValues_ServiceDesc, srv)
}

func _EnumValues_GetEnumValue_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.GetEnumValueRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnumValuesServer).GetEnumValue(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/EnumValues/GetEnumValue",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnumValuesServer).GetEnumValue(ctx, req.(*v1.GetEnumValueRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnumValues_CreateEnumValue_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.CreateEnumValueRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnumValuesServer).CreateEnumValue(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/EnumValues/CreateEnumValue",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnumValuesServer).CreateEnumValue(ctx, req.(*v1.CreateEnumValueRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnumValues_DeleteEnumValue_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.DeleteEnumValueRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnumValuesServer).DeleteEnumValue(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/EnumValues/DeleteEnumValue",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnumValuesServer).DeleteEnumValue(ctx, req.(*v1.DeleteEnumValueRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _EnumValues_UpdateEnumValue_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.UpdateEnumValueRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnumValuesServer).UpdateEnumValue(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/EnumValues/UpdateEnumValue",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnumValuesServer).UpdateEnumValue(ctx, req.(*v1.UpdateEnumValueRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// EnumValues_ServiceDesc is the grpc.ServiceDesc for EnumValues service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var EnumValues_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "EnumValues",
	HandlerType: (*EnumValuesServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetEnumValue",
			Handler:    _EnumValues_GetEnumValue_Handler,
		},
		{
			MethodName: "CreateEnumValue",
			Handler:    _EnumValues_CreateEnumValue_Handler,
		},
		{
			MethodName: "DeleteEnumValue",
			Handler:    _EnumValues_DeleteEnumValue_Handler,
		},
		{
			MethodName: "UpdateEnumValue",
			Handler:    _EnumValues_UpdateEnumValue_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "sylk/EnumValues/v1/EnumValues.proto",
}
