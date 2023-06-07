// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.23.1
// source: sylk/Messages/v1/Messages.proto

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

// MessagesClient is the client API for Messages service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type MessagesClient interface {
	// [sylk] - None
	GetMessage(ctx context.Context, in *v1.GetMessageRequest, opts ...grpc.CallOption) (*v1.GetMessageResponse, error)
	// [sylk] - None
	UpdateMessage(ctx context.Context, in *v1.UpdateMessageRequest, opts ...grpc.CallOption) (*v1.UpdateMessageResponse, error)
	// [sylk] - None
	CreateMessage(ctx context.Context, in *v1.CreateMessageRequest, opts ...grpc.CallOption) (*v1.CreateMessageResponse, error)
	// [sylk] - None
	DeleteMessage(ctx context.Context, in *v1.DeleteMessageRequest, opts ...grpc.CallOption) (*v1.DeleteMessageResponse, error)
}

type messagesClient struct {
	cc grpc.ClientConnInterface
}

func NewMessagesClient(cc grpc.ClientConnInterface) MessagesClient {
	return &messagesClient{cc}
}

func (c *messagesClient) GetMessage(ctx context.Context, in *v1.GetMessageRequest, opts ...grpc.CallOption) (*v1.GetMessageResponse, error) {
	out := new(v1.GetMessageResponse)
	err := c.cc.Invoke(ctx, "/Messages/GetMessage", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *messagesClient) UpdateMessage(ctx context.Context, in *v1.UpdateMessageRequest, opts ...grpc.CallOption) (*v1.UpdateMessageResponse, error) {
	out := new(v1.UpdateMessageResponse)
	err := c.cc.Invoke(ctx, "/Messages/UpdateMessage", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *messagesClient) CreateMessage(ctx context.Context, in *v1.CreateMessageRequest, opts ...grpc.CallOption) (*v1.CreateMessageResponse, error) {
	out := new(v1.CreateMessageResponse)
	err := c.cc.Invoke(ctx, "/Messages/CreateMessage", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *messagesClient) DeleteMessage(ctx context.Context, in *v1.DeleteMessageRequest, opts ...grpc.CallOption) (*v1.DeleteMessageResponse, error) {
	out := new(v1.DeleteMessageResponse)
	err := c.cc.Invoke(ctx, "/Messages/DeleteMessage", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// MessagesServer is the server API for Messages service.
// All implementations must embed UnimplementedMessagesServer
// for forward compatibility
type MessagesServer interface {
	// [sylk] - None
	GetMessage(context.Context, *v1.GetMessageRequest) (*v1.GetMessageResponse, error)
	// [sylk] - None
	UpdateMessage(context.Context, *v1.UpdateMessageRequest) (*v1.UpdateMessageResponse, error)
	// [sylk] - None
	CreateMessage(context.Context, *v1.CreateMessageRequest) (*v1.CreateMessageResponse, error)
	// [sylk] - None
	DeleteMessage(context.Context, *v1.DeleteMessageRequest) (*v1.DeleteMessageResponse, error)
	mustEmbedUnimplementedMessagesServer()
}

// UnimplementedMessagesServer must be embedded to have forward compatible implementations.
type UnimplementedMessagesServer struct {
}

func (UnimplementedMessagesServer) GetMessage(context.Context, *v1.GetMessageRequest) (*v1.GetMessageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetMessage not implemented")
}
func (UnimplementedMessagesServer) UpdateMessage(context.Context, *v1.UpdateMessageRequest) (*v1.UpdateMessageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateMessage not implemented")
}
func (UnimplementedMessagesServer) CreateMessage(context.Context, *v1.CreateMessageRequest) (*v1.CreateMessageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method CreateMessage not implemented")
}
func (UnimplementedMessagesServer) DeleteMessage(context.Context, *v1.DeleteMessageRequest) (*v1.DeleteMessageResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DeleteMessage not implemented")
}
func (UnimplementedMessagesServer) mustEmbedUnimplementedMessagesServer() {}

// UnsafeMessagesServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to MessagesServer will
// result in compilation errors.
type UnsafeMessagesServer interface {
	mustEmbedUnimplementedMessagesServer()
}

func RegisterMessagesServer(s grpc.ServiceRegistrar, srv MessagesServer) {
	s.RegisterService(&Messages_ServiceDesc, srv)
}

func _Messages_GetMessage_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.GetMessageRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MessagesServer).GetMessage(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Messages/GetMessage",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MessagesServer).GetMessage(ctx, req.(*v1.GetMessageRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Messages_UpdateMessage_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.UpdateMessageRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MessagesServer).UpdateMessage(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Messages/UpdateMessage",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MessagesServer).UpdateMessage(ctx, req.(*v1.UpdateMessageRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Messages_CreateMessage_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.CreateMessageRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MessagesServer).CreateMessage(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Messages/CreateMessage",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MessagesServer).CreateMessage(ctx, req.(*v1.CreateMessageRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Messages_DeleteMessage_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.DeleteMessageRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(MessagesServer).DeleteMessage(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Messages/DeleteMessage",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(MessagesServer).DeleteMessage(ctx, req.(*v1.DeleteMessageRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Messages_ServiceDesc is the grpc.ServiceDesc for Messages service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Messages_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "Messages",
	HandlerType: (*MessagesServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "GetMessage",
			Handler:    _Messages_GetMessage_Handler,
		},
		{
			MethodName: "UpdateMessage",
			Handler:    _Messages_UpdateMessage_Handler,
		},
		{
			MethodName: "CreateMessage",
			Handler:    _Messages_CreateMessage_Handler,
		},
		{
			MethodName: "DeleteMessage",
			Handler:    _Messages_DeleteMessage_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "sylk/Messages/v1/Messages.proto",
}
