// sylk.build Generated proto DO NOT EDIT

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v4.23.1
// source: sylk/Users/v1/Users.proto

package v1

import (
	v1 "github.com/sylk-build/sylk-core/services/protos/sylk/SylkApi/v1"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

var File_sylk_Users_v1_Users_proto protoreflect.FileDescriptor

var file_sylk_Users_v1_Users_proto_rawDesc = []byte{
	0x0a, 0x19, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x55, 0x73, 0x65, 0x72, 0x73, 0x2f, 0x76, 0x31, 0x2f,
	0x55, 0x73, 0x65, 0x72, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1d, 0x73, 0x79, 0x6c,
	0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x53, 0x79, 0x6c,
	0x6b, 0x41, 0x70, 0x69, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x32, 0xa7, 0x05, 0x0a, 0x05, 0x55,
	0x73, 0x65, 0x72, 0x73, 0x12, 0x55, 0x0a, 0x0a, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x55, 0x73,
	0x65, 0x72, 0x12, 0x22, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70,
	0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x55, 0x73, 0x65, 0x72, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x23, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79,
	0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x55,
	0x73, 0x65, 0x72, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x61, 0x0a, 0x0e, 0x47,
	0x65, 0x74, 0x41, 0x63, 0x63, 0x65, 0x73, 0x73, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x12, 0x26, 0x2e,
	0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e,
	0x47, 0x65, 0x74, 0x41, 0x63, 0x63, 0x65, 0x73, 0x73, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x27, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c,
	0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x41, 0x63, 0x63, 0x65, 0x73,
	0x73, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x6a,
	0x0a, 0x11, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x41, 0x63, 0x63, 0x65, 0x73, 0x73, 0x54, 0x6f,
	0x6b, 0x65, 0x6e, 0x12, 0x29, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41,
	0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x41, 0x63, 0x63, 0x65,
	0x73, 0x73, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x2a,
	0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31,
	0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x41, 0x63, 0x63, 0x65, 0x73, 0x73, 0x54, 0x6f, 0x6b,
	0x65, 0x6e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x4c, 0x0a, 0x07, 0x47, 0x65,
	0x74, 0x55, 0x73, 0x65, 0x72, 0x12, 0x1f, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c,
	0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x55, 0x73, 0x65, 0x72, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x20, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79,
	0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x55, 0x73, 0x65, 0x72,
	0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x67, 0x0a, 0x10, 0x4c, 0x69, 0x73, 0x74,
	0x41, 0x63, 0x63, 0x65, 0x73, 0x73, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x73, 0x12, 0x28, 0x2e, 0x73,
	0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x4c,
	0x69, 0x73, 0x74, 0x41, 0x63, 0x63, 0x65, 0x73, 0x73, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x73, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x27, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79,
	0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x41, 0x63, 0x63, 0x65,
	0x73, 0x73, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x30,
	0x01, 0x12, 0x6a, 0x0a, 0x11, 0x52, 0x65, 0x76, 0x6f, 0x6b, 0x65, 0x41, 0x63, 0x63, 0x65, 0x73,
	0x73, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x12, 0x29, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79,
	0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x52, 0x65, 0x76, 0x6f, 0x6b, 0x65, 0x41,
	0x63, 0x63, 0x65, 0x73, 0x73, 0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x1a, 0x2a, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69,
	0x2e, 0x76, 0x31, 0x2e, 0x52, 0x65, 0x76, 0x6f, 0x6b, 0x65, 0x41, 0x63, 0x63, 0x65, 0x73, 0x73,
	0x54, 0x6f, 0x6b, 0x65, 0x6e, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x55, 0x0a,
	0x0a, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x55, 0x73, 0x65, 0x72, 0x12, 0x22, 0x2e, 0x73, 0x79,
	0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x55, 0x70,
	0x64, 0x61, 0x74, 0x65, 0x55, 0x73, 0x65, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x23, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x55, 0x73, 0x65, 0x72, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x42, 0x3f, 0x5a, 0x3d, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63,
	0x6f, 0x6d, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2d, 0x62, 0x75, 0x69, 0x6c, 0x64, 0x2f, 0x73, 0x79,
	0x6c, 0x6b, 0x2d, 0x63, 0x6f, 0x72, 0x65, 0x2f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x73,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x55, 0x73, 0x65,
	0x72, 0x73, 0x2f, 0x76, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var file_sylk_Users_v1_Users_proto_goTypes = []interface{}{
	(*v1.CreateUserRequest)(nil),         // 0: sylk.SylkApi.v1.CreateUserRequest
	(*v1.GetAccessTokenRequest)(nil),     // 1: sylk.SylkApi.v1.GetAccessTokenRequest
	(*v1.CreateAccessTokenRequest)(nil),  // 2: sylk.SylkApi.v1.CreateAccessTokenRequest
	(*v1.GetUserRequest)(nil),            // 3: sylk.SylkApi.v1.GetUserRequest
	(*v1.ListAccessTokensRequest)(nil),   // 4: sylk.SylkApi.v1.ListAccessTokensRequest
	(*v1.RevokeAccessTokenRequest)(nil),  // 5: sylk.SylkApi.v1.RevokeAccessTokenRequest
	(*v1.UpdateUserRequest)(nil),         // 6: sylk.SylkApi.v1.UpdateUserRequest
	(*v1.CreateUserResponse)(nil),        // 7: sylk.SylkApi.v1.CreateUserResponse
	(*v1.GetAccessTokenResponse)(nil),    // 8: sylk.SylkApi.v1.GetAccessTokenResponse
	(*v1.CreateAccessTokenResponse)(nil), // 9: sylk.SylkApi.v1.CreateAccessTokenResponse
	(*v1.GetUserResponse)(nil),           // 10: sylk.SylkApi.v1.GetUserResponse
	(*v1.RevokeAccessTokenResponse)(nil), // 11: sylk.SylkApi.v1.RevokeAccessTokenResponse
	(*v1.UpdateUserResponse)(nil),        // 12: sylk.SylkApi.v1.UpdateUserResponse
}
var file_sylk_Users_v1_Users_proto_depIdxs = []int32{
	0,  // 0: Users.CreateUser:input_type -> sylk.SylkApi.v1.CreateUserRequest
	1,  // 1: Users.GetAccessToken:input_type -> sylk.SylkApi.v1.GetAccessTokenRequest
	2,  // 2: Users.CreateAccessToken:input_type -> sylk.SylkApi.v1.CreateAccessTokenRequest
	3,  // 3: Users.GetUser:input_type -> sylk.SylkApi.v1.GetUserRequest
	4,  // 4: Users.ListAccessTokens:input_type -> sylk.SylkApi.v1.ListAccessTokensRequest
	5,  // 5: Users.RevokeAccessToken:input_type -> sylk.SylkApi.v1.RevokeAccessTokenRequest
	6,  // 6: Users.UpdateUser:input_type -> sylk.SylkApi.v1.UpdateUserRequest
	7,  // 7: Users.CreateUser:output_type -> sylk.SylkApi.v1.CreateUserResponse
	8,  // 8: Users.GetAccessToken:output_type -> sylk.SylkApi.v1.GetAccessTokenResponse
	9,  // 9: Users.CreateAccessToken:output_type -> sylk.SylkApi.v1.CreateAccessTokenResponse
	10, // 10: Users.GetUser:output_type -> sylk.SylkApi.v1.GetUserResponse
	8,  // 11: Users.ListAccessTokens:output_type -> sylk.SylkApi.v1.GetAccessTokenResponse
	11, // 12: Users.RevokeAccessToken:output_type -> sylk.SylkApi.v1.RevokeAccessTokenResponse
	12, // 13: Users.UpdateUser:output_type -> sylk.SylkApi.v1.UpdateUserResponse
	7,  // [7:14] is the sub-list for method output_type
	0,  // [0:7] is the sub-list for method input_type
	0,  // [0:0] is the sub-list for extension type_name
	0,  // [0:0] is the sub-list for extension extendee
	0,  // [0:0] is the sub-list for field type_name
}

func init() { file_sylk_Users_v1_Users_proto_init() }
func file_sylk_Users_v1_Users_proto_init() {
	if File_sylk_Users_v1_Users_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_sylk_Users_v1_Users_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   0,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_sylk_Users_v1_Users_proto_goTypes,
		DependencyIndexes: file_sylk_Users_v1_Users_proto_depIdxs,
	}.Build()
	File_sylk_Users_v1_Users_proto = out.File
	file_sylk_Users_v1_Users_proto_rawDesc = nil
	file_sylk_Users_v1_Users_proto_goTypes = nil
	file_sylk_Users_v1_Users_proto_depIdxs = nil
}
