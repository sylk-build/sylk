// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.23.1
// source: sylk/Enums/v1/Enums.proto

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

// EnumsClient is the client API for Enums service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type EnumsClient interface {
	// [sylk] - None
	GetEnum(ctx context.Context, in *v1.GetEnumRequest, opts ...grpc.CallOption) (*v1.GetEnumResponse, error)
	// [sylk] - None
	UpdateEnum(ctx context.Context, in *v1.UpdateEnumRequest, opts ...grpc.CallOption) (*v1.UpdateEnumResponse, error)
	// [sylk] - None
	DeleteEnum(ctx context.Context, in *v1.DeleteEnumRequest, opts ...grpc.CallOption) (*v1.DeleteEnumResponse, error)
	// [sylk] - None
	CreateEnum(ctx context.Context, in *v1.CreateEnumRequest, opts ...grpc.CallOption) (*v1.CreateEnumResponse, error)
}

type enumsClient struct {
	cc grpc.ClientConnInterface
}

func NewEnumsClient(cc grpc.ClientConnInterface) EnumsClient {
	return &enumsClient{cc}
}

func (c *enumsClient) GetEnum(ctx context.Context, in *v1.GetEnumRequest, opts ...grpc.CallOption) (*v1.GetEnumResponse, error) {
	out := new(v1.GetEnumResponse)
	err := c.cc.Invoke(ctx, "/Enums/GetEnum", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enumsClient) UpdateEnum(ctx context.Context, in *v1.UpdateEnumRequest, opts ...grpc.CallOption) (*v1.UpdateEnumResponse, error) {
	out := new(v1.UpdateEnumResponse)
	err := c.cc.Invoke(ctx, "/Enums/UpdateEnum", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enumsClient) DeleteEnum(ctx context.Context, in *v1.DeleteEnumRequest, opts ...grpc.CallOption) (*v1.DeleteEnumResponse, error) {
	out := new(v1.DeleteEnumResponse)
	err := c.cc.Invoke(ctx, "/Enums/DeleteEnum", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *enumsClient) CreateEnum(ctx context.Context, in *v1.CreateEnumRequest, opts ...grpc.CallOption) (*v1.CreateEnumResponse, error) {
	out := new(v1.CreateEnumResponse)
	err := c.cc.Invoke(ctx, "/Enums/CreateEnum", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// EnumsServer is the server API for Enums service.
// All implementations must embed UnimplementedEnumsServer
// for forward compatibility
type EnumsServer interface {
	// [sylk] - None
	GetEnum(context.Context, *v1.GetEnumRequest) (*v1.GetEnumResponse, error)
	// [sylk] - None
	UpdateEnum(context.Context, *v1.UpdateEnumRequest) (*v1.UpdateEnumResponse, error)
	// [sylk] - None
	DeleteEnum(context.Context, *v1.DeleteEnumRequest) (*v1.DeleteEnumResponse, error)
	// [sylk] - None
	CreateEnum(context.Context, *v1.CreateEnumRequest) (*v1.CreateEnumResponse, error)
	mustEmbedUnimplementedEnumsServer()
}

// UnimplementedEnumsServer must be embedded to have forward compatible implementations.
type UnimplementedEnumsServer struct {
}

func (UnimplementedEnumsServer) GetEnum(context.Context, *v1.GetEnumRequest) (*v1.GetEnumResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetEnum not implemented")
}
func (UnimplementedEnumsServer) UpdateEnum(context.Context, *v1.UpdateEnumRequest) (*v1.UpdateEnumResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateEnum not implemented")
}
func (UnimplementedEnumsServer) DeleteEnum(context.Context, *v1.DeleteEnumRequest) (*v1.DeleteEnumResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteEnum not implemented")
}
func (UnimplementedEnumsServer) CreateEnum(context.Context, *v1.CreateEnumRequest) (*v1.CreateEnumResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateEnum not implemented")
}
func (UnimplementedEnumsServer) mustEmbedUnimplementedEnumsServer() {}

// UnsafeEnumsServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to EnumsServer will
// result in compilation errors.
type UnsafeEnumsServer interface {
	mustEmbedUnimplementedEnumsServer()
}

func RegisterEnumsServer(s grpc.ServiceRegistrar, srv EnumsServer) {
	s.RegisterService(&Enums_ServiceDesc, srv)
}

func _Enums_GetEnum_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.GetEnumRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnumsServer).GetEnum(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Enums/GetEnum",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnumsServer).GetEnum(ctx, req.(*v1.GetEnumRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Enums_UpdateEnum_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.UpdateEnumRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnumsServer).UpdateEnum(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Enums/UpdateEnum",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnumsServer).UpdateEnum(ctx, req.(*v1.UpdateEnumRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Enums_DeleteEnum_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.DeleteEnumRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnumsServer).DeleteEnum(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Enums/DeleteEnum",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnumsServer).DeleteEnum(ctx, req.(*v1.DeleteEnumRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Enums_CreateEnum_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.CreateEnumRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(EnumsServer).CreateEnum(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Enums/CreateEnum",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(EnumsServer).CreateEnum(ctx, req.(*v1.CreateEnumRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Enums_ServiceDesc is the grpc.ServiceDesc for Enums service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Enums_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "Enums",
	HandlerType: (*EnumsServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetEnum",
			Handler:    _Enums_GetEnum_Handler,
		},
		{
			MethodName: "UpdateEnum",
			Handler:    _Enums_UpdateEnum_Handler,
		},
		{
			MethodName: "DeleteEnum",
			Handler:    _Enums_DeleteEnum_Handler,
		},
		{
			MethodName: "CreateEnum",
			Handler:    _Enums_CreateEnum_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "sylk/Enums/v1/Enums.proto",
}
