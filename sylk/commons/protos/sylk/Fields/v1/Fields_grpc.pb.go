// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.23.1
// source: sylk/Fields/v1/Fields.proto

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

// FieldsClient is the client API for Fields service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type FieldsClient interface {
	// [sylk] - None
	CreateField(ctx context.Context, in *v1.CreateFieldRequest, opts ...grpc.CallOption) (*v1.CreateFieldResponse, error)
	// [sylk] - None
	GetField(ctx context.Context, in *v1.GetFieldRequest, opts ...grpc.CallOption) (*v1.GetFieldResponse, error)
	// [sylk] - None
	DeleteField(ctx context.Context, in *v1.DeleteFieldRequest, opts ...grpc.CallOption) (*v1.DeleteFieldResponse, error)
	// [sylk] - None
	UpdateField(ctx context.Context, in *v1.UpdateFieldRequest, opts ...grpc.CallOption) (*v1.UpdateFieldResponse, error)
}

type fieldsClient struct {
	cc grpc.ClientConnInterface
}

func NewFieldsClient(cc grpc.ClientConnInterface) FieldsClient {
	return &fieldsClient{cc}
}

func (c *fieldsClient) CreateField(ctx context.Context, in *v1.CreateFieldRequest, opts ...grpc.CallOption) (*v1.CreateFieldResponse, error) {
	out := new(v1.CreateFieldResponse)
	err := c.cc.Invoke(ctx, "/Fields/CreateField", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *fieldsClient) GetField(ctx context.Context, in *v1.GetFieldRequest, opts ...grpc.CallOption) (*v1.GetFieldResponse, error) {
	out := new(v1.GetFieldResponse)
	err := c.cc.Invoke(ctx, "/Fields/GetField", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *fieldsClient) DeleteField(ctx context.Context, in *v1.DeleteFieldRequest, opts ...grpc.CallOption) (*v1.DeleteFieldResponse, error) {
	out := new(v1.DeleteFieldResponse)
	err := c.cc.Invoke(ctx, "/Fields/DeleteField", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *fieldsClient) UpdateField(ctx context.Context, in *v1.UpdateFieldRequest, opts ...grpc.CallOption) (*v1.UpdateFieldResponse, error) {
	out := new(v1.UpdateFieldResponse)
	err := c.cc.Invoke(ctx, "/Fields/UpdateField", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// FieldsServer is the server API for Fields service.
// All implementations must embed UnimplementedFieldsServer
// for forward compatibility
type FieldsServer interface {
	// [sylk] - None
	CreateField(context.Context, *v1.CreateFieldRequest) (*v1.CreateFieldResponse, error)
	// [sylk] - None
	GetField(context.Context, *v1.GetFieldRequest) (*v1.GetFieldResponse, error)
	// [sylk] - None
	DeleteField(context.Context, *v1.DeleteFieldRequest) (*v1.DeleteFieldResponse, error)
	// [sylk] - None
	UpdateField(context.Context, *v1.UpdateFieldRequest) (*v1.UpdateFieldResponse, error)
	mustEmbedUnimplementedFieldsServer()
}

// UnimplementedFieldsServer must be embedded to have forward compatible implementations.
type UnimplementedFieldsServer struct {
}

func (UnimplementedFieldsServer) CreateField(context.Context, *v1.CreateFieldRequest) (*v1.CreateFieldResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateField not implemented")
}
func (UnimplementedFieldsServer) GetField(context.Context, *v1.GetFieldRequest) (*v1.GetFieldResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetField not implemented")
}
func (UnimplementedFieldsServer) DeleteField(context.Context, *v1.DeleteFieldRequest) (*v1.DeleteFieldResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteField not implemented")
}
func (UnimplementedFieldsServer) UpdateField(context.Context, *v1.UpdateFieldRequest) (*v1.UpdateFieldResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateField not implemented")
}
func (UnimplementedFieldsServer) mustEmbedUnimplementedFieldsServer() {}

// UnsafeFieldsServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to FieldsServer will
// result in compilation errors.
type UnsafeFieldsServer interface {
	mustEmbedUnimplementedFieldsServer()
}

func RegisterFieldsServer(s grpc.ServiceRegistrar, srv FieldsServer) {
	s.RegisterService(&Fields_ServiceDesc, srv)
}

func _Fields_CreateField_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.CreateFieldRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(FieldsServer).CreateField(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Fields/CreateField",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(FieldsServer).CreateField(ctx, req.(*v1.CreateFieldRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Fields_GetField_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.GetFieldRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(FieldsServer).GetField(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Fields/GetField",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(FieldsServer).GetField(ctx, req.(*v1.GetFieldRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Fields_DeleteField_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.DeleteFieldRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(FieldsServer).DeleteField(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Fields/DeleteField",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(FieldsServer).DeleteField(ctx, req.(*v1.DeleteFieldRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Fields_UpdateField_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.UpdateFieldRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(FieldsServer).UpdateField(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Fields/UpdateField",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(FieldsServer).UpdateField(ctx, req.(*v1.UpdateFieldRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Fields_ServiceDesc is the grpc.ServiceDesc for Fields service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Fields_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "Fields",
	HandlerType: (*FieldsServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "CreateField",
			Handler:    _Fields_CreateField_Handler,
		},
		{
			MethodName: "GetField",
			Handler:    _Fields_GetField_Handler,
		},
		{
			MethodName: "DeleteField",
			Handler:    _Fields_DeleteField_Handler,
		},
		{
			MethodName: "UpdateField",
			Handler:    _Fields_UpdateField_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "sylk/Fields/v1/Fields.proto",
}