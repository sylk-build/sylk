// sylk.build Generated proto DO NOT EDIT

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v4.23.1
// source: sylk/Packages/v1/Packages.proto

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

var File_sylk_Packages_v1_Packages_proto protoreflect.FileDescriptor

var file_sylk_Packages_v1_Packages_proto_rawDesc = []byte{
	0x0a, 0x1f, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x2f,
	0x76, 0x31, 0x2f, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x1a, 0x1d, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2f,
	0x76, 0x31, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x32, 0xde, 0x03, 0x0a, 0x08, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x12, 0x55, 0x0a,
	0x0a, 0x47, 0x65, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x12, 0x22, 0x2e, 0x73, 0x79,
	0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65,
	0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x23, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76,
	0x31, 0x2e, 0x47, 0x65, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x5e, 0x0a, 0x0d, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x50, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x12, 0x25, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c,
	0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43, 0x72, 0x65, 0x61, 0x74, 0x65, 0x50, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x26, 0x2e, 0x73,
	0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x43,
	0x72, 0x65, 0x61, 0x74, 0x65, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x5e, 0x0a, 0x0d, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x50, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x12, 0x25, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c,
	0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x44, 0x65, 0x6c, 0x65, 0x74, 0x65, 0x50, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x26, 0x2e, 0x73,
	0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x44,
	0x65, 0x6c, 0x65, 0x74, 0x65, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x5e, 0x0a, 0x0d, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x50, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x12, 0x25, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c,
	0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x55, 0x70, 0x64, 0x61, 0x74, 0x65, 0x50, 0x61,
	0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x26, 0x2e, 0x73,
	0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x55,
	0x70, 0x64, 0x61, 0x74, 0x65, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70,
	0x6f, 0x6e, 0x73, 0x65, 0x12, 0x5b, 0x0a, 0x0c, 0x4c, 0x69, 0x73, 0x74, 0x50, 0x61, 0x63, 0x6b,
	0x61, 0x67, 0x65, 0x73, 0x12, 0x24, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b,
	0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x4c, 0x69, 0x73, 0x74, 0x50, 0x61, 0x63, 0x6b, 0x61,
	0x67, 0x65, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x23, 0x2e, 0x73, 0x79, 0x6c,
	0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x41, 0x70, 0x69, 0x2e, 0x76, 0x31, 0x2e, 0x47, 0x65, 0x74,
	0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x30,
	0x01, 0x42, 0x42, 0x5a, 0x40, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f,
	0x73, 0x79, 0x6c, 0x6b, 0x2d, 0x62, 0x75, 0x69, 0x6c, 0x64, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2d,
	0x63, 0x6f, 0x72, 0x65, 0x2f, 0x73, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x73, 0x2f, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67,
	0x65, 0x73, 0x2f, 0x76, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var file_sylk_Packages_v1_Packages_proto_goTypes = []interface{}{
	(*v1.GetPackageRequest)(nil),     // 0: sylk.SylkApi.v1.GetPackageRequest
	(*v1.CreatePackageRequest)(nil),  // 1: sylk.SylkApi.v1.CreatePackageRequest
	(*v1.DeletePackageRequest)(nil),  // 2: sylk.SylkApi.v1.DeletePackageRequest
	(*v1.UpdatePackageRequest)(nil),  // 3: sylk.SylkApi.v1.UpdatePackageRequest
	(*v1.ListPackagesRequest)(nil),   // 4: sylk.SylkApi.v1.ListPackagesRequest
	(*v1.GetPackageResponse)(nil),    // 5: sylk.SylkApi.v1.GetPackageResponse
	(*v1.CreatePackageResponse)(nil), // 6: sylk.SylkApi.v1.CreatePackageResponse
	(*v1.DeletePackageResponse)(nil), // 7: sylk.SylkApi.v1.DeletePackageResponse
	(*v1.UpdatePackageResponse)(nil), // 8: sylk.SylkApi.v1.UpdatePackageResponse
}
var file_sylk_Packages_v1_Packages_proto_depIdxs = []int32{
	0, // 0: Packages.GetPackage:input_type -> sylk.SylkApi.v1.GetPackageRequest
	1, // 1: Packages.CreatePackage:input_type -> sylk.SylkApi.v1.CreatePackageRequest
	2, // 2: Packages.DeletePackage:input_type -> sylk.SylkApi.v1.DeletePackageRequest
	3, // 3: Packages.UpdatePackage:input_type -> sylk.SylkApi.v1.UpdatePackageRequest
	4, // 4: Packages.ListPackages:input_type -> sylk.SylkApi.v1.ListPackagesRequest
	5, // 5: Packages.GetPackage:output_type -> sylk.SylkApi.v1.GetPackageResponse
	6, // 6: Packages.CreatePackage:output_type -> sylk.SylkApi.v1.CreatePackageResponse
	7, // 7: Packages.DeletePackage:output_type -> sylk.SylkApi.v1.DeletePackageResponse
	8, // 8: Packages.UpdatePackage:output_type -> sylk.SylkApi.v1.UpdatePackageResponse
	5, // 9: Packages.ListPackages:output_type -> sylk.SylkApi.v1.GetPackageResponse
	5, // [5:10] is the sub-list for method output_type
	0, // [0:5] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_sylk_Packages_v1_Packages_proto_init() }
func file_sylk_Packages_v1_Packages_proto_init() {
	if File_sylk_Packages_v1_Packages_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_sylk_Packages_v1_Packages_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   0,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_sylk_Packages_v1_Packages_proto_goTypes,
		DependencyIndexes: file_sylk_Packages_v1_Packages_proto_depIdxs,
	}.Build()
	File_sylk_Packages_v1_Packages_proto = out.File
	file_sylk_Packages_v1_Packages_proto_rawDesc = nil
	file_sylk_Packages_v1_Packages_proto_goTypes = nil
	file_sylk_Packages_v1_Packages_proto_depIdxs = nil
}