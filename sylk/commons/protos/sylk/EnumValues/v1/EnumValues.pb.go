// sylk.build Generated proto DO NOT EDIT

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v4.23.1
// source: sylk/EnumValues/v1/EnumValues.proto

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

var File_sylk_EnumValues_v1_EnumValues_proto protoreflect.FileDescriptor

var file_sylk_EnumValues_v1_EnumValues_proto_rawDesc = []byte{
	0x0a, 0x23, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65,
	0x73, 0x2f, 0x76, 0x31, 0x2f, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x73, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1d, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b,
	0x41, 0x70, 0x69, 0x2f, 0x76, 0x31, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x32, 0x9b, 0x03, 0x0a, 0x0a, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c,
	0x75, 0x65, 0x73, 0x12, 0x5b, 0x0a, 0x0c, 0x47, 0x65, 0x74, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61,
	0x6c, 0x75, 0x65, 0x12, 0x24, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41,
	0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c,
	0x75, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x25, 0x2e, 0x73, 0x79, 0x6c, 0x6b,
	0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74, 0x45,
	0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65,
	0x12, 0x64, 0x0a, 0x0f, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61,
	0x6c, 0x75, 0x65, 0x12, 0x27, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41,
	0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x45, 0x6e, 0x75, 0x6d,
	0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x28, 0x2e, 0x73,
	0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43,
	0x72, 0x65, 0x61, 0x74, 0x65, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x64, 0x0a, 0x0f, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65,
	0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x12, 0x27, 0x2e, 0x73, 0x79, 0x6c, 0x6b,
	0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x65, 0x6c, 0x65,
	0x74, 0x65, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x1a, 0x28, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70,
	0x69, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x45, 0x6e, 0x75, 0x6d, 0x56,
	0x61, 0x6c, 0x75, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x64, 0x0a, 0x0f,
	0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x12,
	0x27, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c, 0x75,
	0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x28, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e,
	0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74,
	0x65, 0x45, 0x6e, 0x75, 0x6d, 0x56, 0x61, 0x6c, 0x75, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x42, 0x44, 0x5a, 0x42, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d,
	0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2d, 0x62, 0x75, 0x69, 0x6c, 0x64, 0x2f, 0x73, 0x79, 0x6c, 0x6b,
	0x2d, 0x63, 0x6f, 0x72, 0x65, 0x2f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x73, 0x2f, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x45, 0x6e, 0x75, 0x6d, 0x56,
	0x61, 0x6c, 0x75, 0x65, 0x73, 0x2f, 0x76, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var file_sylk_EnumValues_v1_EnumValues_proto_goTypes = []interface{}{
	(*v1.GetEnumValueRequest)(nil),     // 0: sylk.SylkApi.v1.GetEnumValueRequest
	(*v1.CreateEnumValueRequest)(nil),  // 1: sylk.SylkApi.v1.CreateEnumValueRequest
	(*v1.DeleteEnumValueRequest)(nil),  // 2: sylk.SylkApi.v1.DeleteEnumValueRequest
	(*v1.UpdateEnumValueRequest)(nil),  // 3: sylk.SylkApi.v1.UpdateEnumValueRequest
	(*v1.GetEnumValueResponse)(nil),    // 4: sylk.SylkApi.v1.GetEnumValueResponse
	(*v1.CreateEnumValueResponse)(nil), // 5: sylk.SylkApi.v1.CreateEnumValueResponse
	(*v1.DeleteEnumValueResponse)(nil), // 6: sylk.SylkApi.v1.DeleteEnumValueResponse
	(*v1.UpdateEnumValueResponse)(nil), // 7: sylk.SylkApi.v1.UpdateEnumValueResponse
}
var file_sylk_EnumValues_v1_EnumValues_proto_depIdxs = []int32{
	0, // 0: EnumValues.GetEnumValue:input_type -> sylk.SylkApi.v1.GetEnumValueRequest
	1, // 1: EnumValues.CreateEnumValue:input_type -> sylk.SylkApi.v1.CreateEnumValueRequest
	2, // 2: EnumValues.DeleteEnumValue:input_type -> sylk.SylkApi.v1.DeleteEnumValueRequest
	3, // 3: EnumValues.UpdateEnumValue:input_type -> sylk.SylkApi.v1.UpdateEnumValueRequest
	4, // 4: EnumValues.GetEnumValue:output_type -> sylk.SylkApi.v1.GetEnumValueResponse
	5, // 5: EnumValues.CreateEnumValue:output_type -> sylk.SylkApi.v1.CreateEnumValueResponse
	6, // 6: EnumValues.DeleteEnumValue:output_type -> sylk.SylkApi.v1.DeleteEnumValueResponse
	7, // 7: EnumValues.UpdateEnumValue:output_type -> sylk.SylkApi.v1.UpdateEnumValueResponse
	4, // [4:8] is the sub-list for method output_type
	0, // [0:4] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_sylk_EnumValues_v1_EnumValues_proto_init() }
func file_sylk_EnumValues_v1_EnumValues_proto_init() {
	if File_sylk_EnumValues_v1_EnumValues_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_sylk_EnumValues_v1_EnumValues_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   0,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_sylk_EnumValues_v1_EnumValues_proto_goTypes,
		DependencyIndexes: file_sylk_EnumValues_v1_EnumValues_proto_depIdxs,
	}.Build()
	File_sylk_EnumValues_v1_EnumValues_proto = out.File
	file_sylk_EnumValues_v1_EnumValues_proto_rawDesc = nil
	file_sylk_EnumValues_v1_EnumValues_proto_goTypes = nil
	file_sylk_EnumValues_v1_EnumValues_proto_depIdxs = nil
}