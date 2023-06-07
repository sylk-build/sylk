// Code generated by protoc-gen-go-grpc. DO NOT EDIT.
// versions:
// - protoc-gen-go-grpc v1.2.0
// - protoc             v4.23.1
// source: sylk/Organizations/v1/Organizations.proto

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

// OrganizationsClient is the client API for Organizations service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://pkg.go.dev/google.golang.org/grpc/?tab=doc#ClientConn.NewStream.
type OrganizationsClient interface {
	// [sylk] - None
	AcceprUserInvite(ctx context.Context, in *v1.AcceptUserInviteRequest, opts ...grpc.CallOption) (*v1.AcceptUserInviteResponse, error)
	// [sylk] - None
	GetOrganization(ctx context.Context, in *v1.GetOrganizationRequest, opts ...grpc.CallOption) (*v1.GetOrganizationResponse, error)
	// [sylk] - None
	UpdateOrganization(ctx context.Context, in *v1.UpdateOrganizationRequest, opts ...grpc.CallOption) (*v1.UpdateOrganizationResponse, error)
	// [sylk] - None
	ListOrganizations(ctx context.Context, in *v1.ListOrganizationsRequest, opts ...grpc.CallOption) (Organizations_ListOrganizationsClient, error)
	// [sylk] - None
	AddUser(ctx context.Context, in *v1.AddUserRequest, opts ...grpc.CallOption) (*v1.AddUserResponse, error)
	// [sylk] - None
	UpdateUserStatus(ctx context.Context, in *v1.UpdateUserStatusRequest, opts ...grpc.CallOption) (*v1.UpdateUserStatusResponse, error)
	// [sylk] - None
	RemoveUser(ctx context.Context, in *v1.RemoveUserRequest, opts ...grpc.CallOption) (*v1.RemoveUserResponse, error)
	// [sylk] - None
	UpdateUserRole(ctx context.Context, in *v1.UpdateUserRoleRequest, opts ...grpc.CallOption) (*v1.UpdateUserRoleResponse, error)
}

type organizationsClient struct {
	cc grpc.ClientConnInterface
}

func NewOrganizationsClient(cc grpc.ClientConnInterface) OrganizationsClient {
	return &organizationsClient{cc}
}

func (c *organizationsClient) AcceprUserInvite(ctx context.Context, in *v1.AcceptUserInviteRequest, opts ...grpc.CallOption) (*v1.AcceptUserInviteResponse, error) {
	out := new(v1.AcceptUserInviteResponse)
	err := c.cc.Invoke(ctx, "/Organizations/AcceprUserInvite", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *organizationsClient) GetOrganization(ctx context.Context, in *v1.GetOrganizationRequest, opts ...grpc.CallOption) (*v1.GetOrganizationResponse, error) {
	out := new(v1.GetOrganizationResponse)
	err := c.cc.Invoke(ctx, "/Organizations/GetOrganization", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *organizationsClient) UpdateOrganization(ctx context.Context, in *v1.UpdateOrganizationRequest, opts ...grpc.CallOption) (*v1.UpdateOrganizationResponse, error) {
	out := new(v1.UpdateOrganizationResponse)
	err := c.cc.Invoke(ctx, "/Organizations/UpdateOrganization", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *organizationsClient) ListOrganizations(ctx context.Context, in *v1.ListOrganizationsRequest, opts ...grpc.CallOption) (Organizations_ListOrganizationsClient, error) {
	stream, err := c.cc.NewStream(ctx, &Organizations_ServiceDesc.Streams[0], "/Organizations/ListOrganizations", opts...)
	if err != nil {
		return nil, err
	}
	x := &organizationsListOrganizationsClient{stream}
	if err := x.ClientStream.SendMsg(in); err != nil {
		return nil, err
	}
	if err := x.ClientStream.CloseSend(); err != nil {
		return nil, err
	}
	return x, nil
}

type Organizations_ListOrganizationsClient interface {
	Recv() (*v1.GetOrganizationResponse, error)
	grpc.ClientStream
}

type organizationsListOrganizationsClient struct {
	grpc.ClientStream
}

func (x *organizationsListOrganizationsClient) Recv() (*v1.GetOrganizationResponse, error) {
	m := new(v1.GetOrganizationResponse)
	if err := x.ClientStream.RecvMsg(m); err != nil {
		return nil, err
	}
	return m, nil
}

func (c *organizationsClient) AddUser(ctx context.Context, in *v1.AddUserRequest, opts ...grpc.CallOption) (*v1.AddUserResponse, error) {
	out := new(v1.AddUserResponse)
	err := c.cc.Invoke(ctx, "/Organizations/AddUser", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *organizationsClient) UpdateUserStatus(ctx context.Context, in *v1.UpdateUserStatusRequest, opts ...grpc.CallOption) (*v1.UpdateUserStatusResponse, error) {
	out := new(v1.UpdateUserStatusResponse)
	err := c.cc.Invoke(ctx, "/Organizations/UpdateUserStatus", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *organizationsClient) RemoveUser(ctx context.Context, in *v1.RemoveUserRequest, opts ...grpc.CallOption) (*v1.RemoveUserResponse, error) {
	out := new(v1.RemoveUserResponse)
	err := c.cc.Invoke(ctx, "/Organizations/RemoveUser", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *organizationsClient) UpdateUserRole(ctx context.Context, in *v1.UpdateUserRoleRequest, opts ...grpc.CallOption) (*v1.UpdateUserRoleResponse, error) {
	out := new(v1.UpdateUserRoleResponse)
	err := c.cc.Invoke(ctx, "/Organizations/UpdateUserRole", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// OrganizationsServer is the server API for Organizations service.
// All implementations must embed UnimplementedOrganizationsServer
// for forward compatibility
type OrganizationsServer interface {
	// [sylk] - None
	AcceprUserInvite(context.Context, *v1.AcceptUserInviteRequest) (*v1.AcceptUserInviteResponse, error)
	// [sylk] - None
	GetOrganization(context.Context, *v1.GetOrganizationRequest) (*v1.GetOrganizationResponse, error)
	// [sylk] - None
	UpdateOrganization(context.Context, *v1.UpdateOrganizationRequest) (*v1.UpdateOrganizationResponse, error)
	// [sylk] - None
	ListOrganizations(*v1.ListOrganizationsRequest, Organizations_ListOrganizationsServer) error
	// [sylk] - None
	AddUser(context.Context, *v1.AddUserRequest) (*v1.AddUserResponse, error)
	// [sylk] - None
	UpdateUserStatus(context.Context, *v1.UpdateUserStatusRequest) (*v1.UpdateUserStatusResponse, error)
	// [sylk] - None
	RemoveUser(context.Context, *v1.RemoveUserRequest) (*v1.RemoveUserResponse, error)
	// [sylk] - None
	UpdateUserRole(context.Context, *v1.UpdateUserRoleRequest) (*v1.UpdateUserRoleResponse, error)
	mustEmbedUnimplementedOrganizationsServer()
}

// UnimplementedOrganizationsServer must be embedded to have forward compatible implementations.
type UnimplementedOrganizationsServer struct {
}

func (UnimplementedOrganizationsServer) AcceprUserInvite(context.Context, *v1.AcceptUserInviteRequest) (*v1.AcceptUserInviteResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AcceprUserInvite not implemented")
}
func (UnimplementedOrganizationsServer) GetOrganization(context.Context, *v1.GetOrganizationRequest) (*v1.GetOrganizationResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method GetOrganization not implemented")
}
func (UnimplementedOrganizationsServer) UpdateOrganization(context.Context, *v1.UpdateOrganizationRequest) (*v1.UpdateOrganizationResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateOrganization not implemented")
}
func (UnimplementedOrganizationsServer) ListOrganizations(*v1.ListOrganizationsRequest, Organizations_ListOrganizationsServer) error {
	return status.Errorf(codes.Unimplemented, "method ListOrganizations not implemented")
}
func (UnimplementedOrganizationsServer) AddUser(context.Context, *v1.AddUserRequest) (*v1.AddUserResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method AddUser not implemented")
}
func (UnimplementedOrganizationsServer) UpdateUserStatus(context.Context, *v1.UpdateUserStatusRequest) (*v1.UpdateUserStatusResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateUserStatus not implemented")
}
func (UnimplementedOrganizationsServer) RemoveUser(context.Context, *v1.RemoveUserRequest) (*v1.RemoveUserResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method RemoveUser not implemented")
}
func (UnimplementedOrganizationsServer) UpdateUserRole(context.Context, *v1.UpdateUserRoleRequest) (*v1.UpdateUserRoleResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method UpdateUserRole not implemented")
}
func (UnimplementedOrganizationsServer) mustEmbedUnimplementedOrganizationsServer() {}

// UnsafeOrganizationsServer may be embedded to opt out of forward compatibility for this service.
// Use of this interface is not recommended, as added methods to OrganizationsServer will
// result in compilation errors.
type UnsafeOrganizationsServer interface {
	mustEmbedUnimplementedOrganizationsServer()
}

func RegisterOrganizationsServer(s grpc.ServiceRegistrar, srv OrganizationsServer) {
	s.RegisterService(&Organizations_ServiceDesc, srv)
}

func _Organizations_AcceprUserInvite_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.AcceptUserInviteRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(OrganizationsServer).AcceprUserInvite(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Organizations/AcceprUserInvite",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(OrganizationsServer).AcceprUserInvite(ctx, req.(*v1.AcceptUserInviteRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Organizations_GetOrganization_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.GetOrganizationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(OrganizationsServer).GetOrganization(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Organizations/GetOrganization",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(OrganizationsServer).GetOrganization(ctx, req.(*v1.GetOrganizationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Organizations_UpdateOrganization_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.UpdateOrganizationRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(OrganizationsServer).UpdateOrganization(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Organizations/UpdateOrganization",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(OrganizationsServer).UpdateOrganization(ctx, req.(*v1.UpdateOrganizationRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Organizations_ListOrganizations_Handler(srv interface{}, stream grpc.ServerStream) error {
	m := new(v1.ListOrganizationsRequest)
	if err := stream.RecvMsg(m); err != nil {
		return err
	}
	return srv.(OrganizationsServer).ListOrganizations(m, &organizationsListOrganizationsServer{stream})
}

type Organizations_ListOrganizationsServer interface {
	Send(*v1.GetOrganizationResponse) error
	grpc.ServerStream
}

type organizationsListOrganizationsServer struct {
	grpc.ServerStream
}

func (x *organizationsListOrganizationsServer) Send(m *v1.GetOrganizationResponse) error {
	return x.ServerStream.SendMsg(m)
}

func _Organizations_AddUser_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.AddUserRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(OrganizationsServer).AddUser(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Organizations/AddUser",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(OrganizationsServer).AddUser(ctx, req.(*v1.AddUserRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Organizations_UpdateUserStatus_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.UpdateUserStatusRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(OrganizationsServer).UpdateUserStatus(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Organizations/UpdateUserStatus",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(OrganizationsServer).UpdateUserStatus(ctx, req.(*v1.UpdateUserStatusRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Organizations_RemoveUser_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.RemoveUserRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(OrganizationsServer).RemoveUser(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Organizations/RemoveUser",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(OrganizationsServer).RemoveUser(ctx, req.(*v1.RemoveUserRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Organizations_UpdateUserRole_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(v1.UpdateUserRoleRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(OrganizationsServer).UpdateUserRole(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/Organizations/UpdateUserRole",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(OrganizationsServer).UpdateUserRole(ctx, req.(*v1.UpdateUserRoleRequest))
	}
	return interceptor(ctx, in, info, handler)
}

// Organizations_ServiceDesc is the grpc.ServiceDesc for Organizations service.
// It's only intended for direct use with grpc.RegisterService,
// and not to be introspected or modified (even as a copy)
var Organizations_ServiceDesc = grpc.ServiceDesc{
	ServiceName: "Organizations",
	HandlerType: (*OrganizationsServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "AcceprUserInvite",
			Handler:    _Organizations_AcceprUserInvite_Handler,
		},
		{
			MethodName: "GetOrganization",
			Handler:    _Organizations_GetOrganization_Handler,
		},
		{
			MethodName: "UpdateOrganization",
			Handler:    _Organizations_UpdateOrganization_Handler,
		},
		{
			MethodName: "AddUser",
			Handler:    _Organizations_AddUser_Handler,
		},
		{
			MethodName: "UpdateUserStatus",
			Handler:    _Organizations_UpdateUserStatus_Handler,
		},
		{
			MethodName: "RemoveUser",
			Handler:    _Organizations_RemoveUser_Handler,
		},
		{
			MethodName: "UpdateUserRole",
			Handler:    _Organizations_UpdateUserRole_Handler,
		},
	},
	Streams: []grpc.StreamDesc{
		{
			StreamName:    "ListOrganizations",
			Handler:       _Organizations_ListOrganizations_Handler,
			ServerStreams: true,
		},
	},
	Metadata: "sylk/Organizations/v1/Organizations.proto",
}
