// sylk.build Generated proto DO NOT EDIT

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v4.23.1
// source: sylk/SylkOrganization/v1/SylkOrganization.proto

package v1

import (
	v1 "github.com/sylk-build/sylk-core/services/protos/sylk/SylkProject/v1"
	v11 "github.com/sylk-build/sylk-core/services/protos/sylk/SylkUser/v1"
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

// [sylk.SylkOrganization.v1.SylkOrganizationDisplay] - None
type SylkOrganizationDisplay struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Organization *SylkOrganization        `protobuf:"bytes,1,opt,name=organization,proto3" json:"organization,omitempty"`
	Projects     []*v1.SylkProjectDisplay `protobuf:"bytes,3,rep,name=projects,proto3" json:"projects,omitempty"`
	Users        []*v11.SylkUserDisplay   `protobuf:"bytes,2,rep,name=users,proto3" json:"users,omitempty"`
}

func (x *SylkOrganizationDisplay) Reset() {
	*x = SylkOrganizationDisplay{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_SylkOrganization_v1_SylkOrganization_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SylkOrganizationDisplay) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SylkOrganizationDisplay) ProtoMessage() {}

func (x *SylkOrganizationDisplay) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_SylkOrganization_v1_SylkOrganization_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SylkOrganizationDisplay.ProtoReflect.Descriptor instead.
func (*SylkOrganizationDisplay) Descriptor() ([]byte, []int) {
	return file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDescGZIP(), []int{0}
}

func (x *SylkOrganizationDisplay) GetOrganization() *SylkOrganization {
	if x != nil {
		return x.Organization
	}
	return nil
}

func (x *SylkOrganizationDisplay) GetProjects() []*v1.SylkProjectDisplay {
	if x != nil {
		return x.Projects
	}
	return nil
}

func (x *SylkOrganizationDisplay) GetUsers() []*v11.SylkUserDisplay {
	if x != nil {
		return x.Users
	}
	return nil
}

// [sylk.SylkOrganization.v1.SylkOrganization] - None
type SylkOrganization struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	OrgId  string `protobuf:"bytes,1,opt,name=orgId,proto3" json:"orgId,omitempty"`
	Name   string `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Owner  string `protobuf:"bytes,4,opt,name=owner,proto3" json:"owner,omitempty"`
	Domain string `protobuf:"bytes,3,opt,name=domain,proto3" json:"domain,omitempty"`
}

func (x *SylkOrganization) Reset() {
	*x = SylkOrganization{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_SylkOrganization_v1_SylkOrganization_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SylkOrganization) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SylkOrganization) ProtoMessage() {}

func (x *SylkOrganization) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_SylkOrganization_v1_SylkOrganization_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SylkOrganization.ProtoReflect.Descriptor instead.
func (*SylkOrganization) Descriptor() ([]byte, []int) {
	return file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDescGZIP(), []int{1}
}

func (x *SylkOrganization) GetOrgId() string {
	if x != nil {
		return x.OrgId
	}
	return ""
}

func (x *SylkOrganization) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *SylkOrganization) GetOwner() string {
	if x != nil {
		return x.Owner
	}
	return ""
}

func (x *SylkOrganization) GetDomain() string {
	if x != nil {
		return x.Domain
	}
	return ""
}

var File_sylk_SylkOrganization_v1_SylkOrganization_proto protoreflect.FileDescriptor

var file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDesc = []byte{
	0x0a, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x4f, 0x72, 0x67, 0x61, 0x6e,
	0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2f, 0x76, 0x31, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x4f,
	0x72, 0x67, 0x61, 0x6e, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x12, 0x18, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x4f, 0x72, 0x67, 0x61,
	0x6e, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x76, 0x31, 0x1a, 0x25, 0x73, 0x79, 0x6c,
	0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x2f, 0x76, 0x31,
	0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x1a, 0x1f, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x55, 0x73, 0x65,
	0x72, 0x2f, 0x76, 0x31, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x55, 0x73, 0x65, 0x72, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x22, 0xe7, 0x01, 0x0a, 0x17, 0x53, 0x79, 0x6c, 0x6b, 0x4f, 0x72, 0x67, 0x61,
	0x6e, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x44, 0x69, 0x73, 0x70, 0x6c, 0x61, 0x79, 0x12,
	0x4e, 0x0a, 0x0c, 0x6f, 0x72, 0x67, 0x61, 0x6e, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x2a, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c,
	0x6b, 0x4f, 0x72, 0x67, 0x61, 0x6e, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x2e, 0x76, 0x31,
	0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x4f, 0x72, 0x67, 0x61, 0x6e, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x52, 0x0c, 0x6f, 0x72, 0x67, 0x61, 0x6e, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f, 0x6e, 0x12,
	0x43, 0x0a, 0x08, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x73, 0x18, 0x03, 0x20, 0x03, 0x28,
	0x0b, 0x32, 0x27, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f,
	0x6a, 0x65, 0x63, 0x74, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a,
	0x65, 0x63, 0x74, 0x44, 0x69, 0x73, 0x70, 0x6c, 0x61, 0x79, 0x52, 0x08, 0x70, 0x72, 0x6f, 0x6a,
	0x65, 0x63, 0x74, 0x73, 0x12, 0x37, 0x0a, 0x05, 0x75, 0x73, 0x65, 0x72, 0x73, 0x18, 0x02, 0x20,
	0x03, 0x28, 0x0b, 0x32, 0x21, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x55,
	0x73, 0x65, 0x72, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x55, 0x73, 0x65, 0x72, 0x44,
	0x69, 0x73, 0x70, 0x6c, 0x61, 0x79, 0x52, 0x05, 0x75, 0x73, 0x65, 0x72, 0x73, 0x22, 0x6a, 0x0a,
	0x10, 0x53, 0x79, 0x6c, 0x6b, 0x4f, 0x72, 0x67, 0x61, 0x6e, 0x69, 0x7a, 0x61, 0x74, 0x69, 0x6f,
	0x6e, 0x12, 0x14, 0x0a, 0x05, 0x6f, 0x72, 0x67, 0x49, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x05, 0x6f, 0x72, 0x67, 0x49, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18,
	0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x14, 0x0a, 0x05, 0x6f,
	0x77, 0x6e, 0x65, 0x72, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x6f, 0x77, 0x6e, 0x65,
	0x72, 0x12, 0x16, 0x0a, 0x06, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x18, 0x03, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x06, 0x64, 0x6f, 0x6d, 0x61, 0x69, 0x6e, 0x42, 0x4a, 0x5a, 0x48, 0x67, 0x69, 0x74,
	0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2d, 0x62, 0x75, 0x69,
	0x6c, 0x64, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2d, 0x63, 0x6f, 0x72, 0x65, 0x2f, 0x73, 0x65, 0x72,
	0x76, 0x69, 0x63, 0x65, 0x73, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x73, 0x79, 0x6c,
	0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x4f, 0x72, 0x67, 0x61, 0x6e, 0x69, 0x7a, 0x61, 0x74, 0x69,
	0x6f, 0x6e, 0x2f, 0x76, 0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDescOnce sync.Once
	file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDescData = file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDesc
)

func file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDescGZIP() []byte {
	file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDescOnce.Do(func() {
		file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDescData = protoimpl.X.CompressGZIP(file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDescData)
	})
	return file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDescData
}

var file_sylk_SylkOrganization_v1_SylkOrganization_proto_msgTypes = make([]protoimpl.MessageInfo, 2)
var file_sylk_SylkOrganization_v1_SylkOrganization_proto_goTypes = []interface{}{
	(*SylkOrganizationDisplay)(nil), // 0: sylk.SylkOrganization.v1.SylkOrganizationDisplay
	(*SylkOrganization)(nil),        // 1: sylk.SylkOrganization.v1.SylkOrganization
	(*v1.SylkProjectDisplay)(nil),   // 2: sylk.SylkProject.v1.SylkProjectDisplay
	(*v11.SylkUserDisplay)(nil),     // 3: sylk.SylkUser.v1.SylkUserDisplay
}
var file_sylk_SylkOrganization_v1_SylkOrganization_proto_depIdxs = []int32{
	1, // 0: sylk.SylkOrganization.v1.SylkOrganizationDisplay.organization:type_name -> sylk.SylkOrganization.v1.SylkOrganization
	2, // 1: sylk.SylkOrganization.v1.SylkOrganizationDisplay.projects:type_name -> sylk.SylkProject.v1.SylkProjectDisplay
	3, // 2: sylk.SylkOrganization.v1.SylkOrganizationDisplay.users:type_name -> sylk.SylkUser.v1.SylkUserDisplay
	3, // [3:3] is the sub-list for method output_type
	3, // [3:3] is the sub-list for method input_type
	3, // [3:3] is the sub-list for extension type_name
	3, // [3:3] is the sub-list for extension extendee
	0, // [0:3] is the sub-list for field type_name
}

func init() { file_sylk_SylkOrganization_v1_SylkOrganization_proto_init() }
func file_sylk_SylkOrganization_v1_SylkOrganization_proto_init() {
	if File_sylk_SylkOrganization_v1_SylkOrganization_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_sylk_SylkOrganization_v1_SylkOrganization_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SylkOrganizationDisplay); i {
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
		file_sylk_SylkOrganization_v1_SylkOrganization_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SylkOrganization); i {
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
			RawDescriptor: file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   2,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_sylk_SylkOrganization_v1_SylkOrganization_proto_goTypes,
		DependencyIndexes: file_sylk_SylkOrganization_v1_SylkOrganization_proto_depIdxs,
		MessageInfos:      file_sylk_SylkOrganization_v1_SylkOrganization_proto_msgTypes,
	}.Build()
	File_sylk_SylkOrganization_v1_SylkOrganization_proto = out.File
	file_sylk_SylkOrganization_v1_SylkOrganization_proto_rawDesc = nil
	file_sylk_SylkOrganization_v1_SylkOrganization_proto_goTypes = nil
	file_sylk_SylkOrganization_v1_SylkOrganization_proto_depIdxs = nil
}
