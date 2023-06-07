// sylk.build Generated proto DO NOT EDIT

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v4.23.1
// source: sylk/SylkProject/v1/SylkProject.proto

package v1

import (
	v11 "github.com/sylk-build/sylk-core/services/protos/sylk/SylkClient/v1"
	v12 "github.com/sylk-build/sylk-core/services/protos/sylk/SylkServer/v1"
	v1 "github.com/sylk-build/sylk-core/services/protos/sylk/SylkUser/v1"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	anypb "google.golang.org/protobuf/types/known/anypb"
	timestamppb "google.golang.org/protobuf/types/known/timestamppb"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// [sylk.SylkProject.v1.SylkProjectDisplay] - None
type SylkProjectDisplay struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Owner       string                      `protobuf:"bytes,4,opt,name=owner,proto3" json:"owner,omitempty"`
	UpdatedAt   *timestamppb.Timestamp      `protobuf:"bytes,3,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
	NumMethods  int32                       `protobuf:"varint,6,opt,name=numMethods,proto3" json:"numMethods,omitempty"`
	CreatedAt   *timestamppb.Timestamp      `protobuf:"bytes,2,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	Members     map[string]v1.SylkUserRoles `protobuf:"bytes,5,rep,name=members,proto3" json:"members,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"varint,2,opt,name=value,proto3,enum=sylk.SylkUser.v1.SylkUserRoles"`
	NumServices int32                       `protobuf:"varint,7,opt,name=numServices,proto3" json:"numServices,omitempty"`
	NumMessages int32                       `protobuf:"varint,9,opt,name=numMessages,proto3" json:"numMessages,omitempty"`
	NumPackages int32                       `protobuf:"varint,8,opt,name=numPackages,proto3" json:"numPackages,omitempty"`
	Project     *SylkProject                `protobuf:"bytes,1,opt,name=project,proto3" json:"project,omitempty"`
}

func (x *SylkProjectDisplay) Reset() {
	*x = SylkProjectDisplay{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_SylkProject_v1_SylkProject_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SylkProjectDisplay) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SylkProjectDisplay) ProtoMessage() {}

func (x *SylkProjectDisplay) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_SylkProject_v1_SylkProject_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SylkProjectDisplay.ProtoReflect.Descriptor instead.
func (*SylkProjectDisplay) Descriptor() ([]byte, []int) {
	return file_sylk_SylkProject_v1_SylkProject_proto_rawDescGZIP(), []int{0}
}

func (x *SylkProjectDisplay) GetOwner() string {
	if x != nil {
		return x.Owner
	}
	return ""
}

func (x *SylkProjectDisplay) GetUpdatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.UpdatedAt
	}
	return nil
}

func (x *SylkProjectDisplay) GetNumMethods() int32 {
	if x != nil {
		return x.NumMethods
	}
	return 0
}

func (x *SylkProjectDisplay) GetCreatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.CreatedAt
	}
	return nil
}

func (x *SylkProjectDisplay) GetMembers() map[string]v1.SylkUserRoles {
	if x != nil {
		return x.Members
	}
	return nil
}

func (x *SylkProjectDisplay) GetNumServices() int32 {
	if x != nil {
		return x.NumServices
	}
	return 0
}

func (x *SylkProjectDisplay) GetNumMessages() int32 {
	if x != nil {
		return x.NumMessages
	}
	return 0
}

func (x *SylkProjectDisplay) GetNumPackages() int32 {
	if x != nil {
		return x.NumPackages
	}
	return 0
}

func (x *SylkProjectDisplay) GetProject() *SylkProject {
	if x != nil {
		return x.Project
	}
	return nil
}

// [sylk.SylkProject.v1.SylkProject] - None
type SylkProject struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Description string            `protobuf:"bytes,8,opt,name=description,proto3" json:"description,omitempty"`
	JavaPackage string            `protobuf:"bytes,6,opt,name=java_package,json=javaPackage,proto3" json:"java_package,omitempty"`
	GoPackage   string            `protobuf:"bytes,5,opt,name=go_package,json=goPackage,proto3" json:"go_package,omitempty"`
	Name        string            `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Uri         string            `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
	Clients     []*v11.SylkClient `protobuf:"bytes,4,rep,name=clients,proto3" json:"clients,omitempty"`
	Server      *v12.SylkServer   `protobuf:"bytes,7,opt,name=server,proto3" json:"server,omitempty"`
	PackageName string            `protobuf:"bytes,3,opt,name=package_name,json=packageName,proto3" json:"package_name,omitempty"`
	Extensions  []*anypb.Any      `protobuf:"bytes,9,rep,name=extensions,proto3" json:"extensions,omitempty"`
}

func (x *SylkProject) Reset() {
	*x = SylkProject{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_SylkProject_v1_SylkProject_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SylkProject) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SylkProject) ProtoMessage() {}

func (x *SylkProject) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_SylkProject_v1_SylkProject_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SylkProject.ProtoReflect.Descriptor instead.
func (*SylkProject) Descriptor() ([]byte, []int) {
	return file_sylk_SylkProject_v1_SylkProject_proto_rawDescGZIP(), []int{1}
}

func (x *SylkProject) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *SylkProject) GetJavaPackage() string {
	if x != nil {
		return x.JavaPackage
	}
	return ""
}

func (x *SylkProject) GetGoPackage() string {
	if x != nil {
		return x.GoPackage
	}
	return ""
}

func (x *SylkProject) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *SylkProject) GetUri() string {
	if x != nil {
		return x.Uri
	}
	return ""
}

func (x *SylkProject) GetClients() []*v11.SylkClient {
	if x != nil {
		return x.Clients
	}
	return nil
}

func (x *SylkProject) GetServer() *v12.SylkServer {
	if x != nil {
		return x.Server
	}
	return nil
}

func (x *SylkProject) GetPackageName() string {
	if x != nil {
		return x.PackageName
	}
	return ""
}

func (x *SylkProject) GetExtensions() []*anypb.Any {
	if x != nil {
		return x.Extensions
	}
	return nil
}

var File_sylk_SylkProject_v1_SylkProject_proto protoreflect.FileDescriptor

var file_sylk_SylkProject_v1_SylkProject_proto_rawDesc = []byte{
	0x0a, 0x25, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a, 0x65,
	0x63, 0x74, 0x2f, 0x76, 0x31, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63,
	0x74, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x13, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79,
	0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x2e, 0x76, 0x31, 0x1a, 0x1f, 0x67, 0x6f,
	0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69,
	0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1f, 0x73,
	0x79, 0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x55, 0x73, 0x65, 0x72, 0x2f, 0x76, 0x31, 0x2f,
	0x53, 0x79, 0x6c, 0x6b, 0x55, 0x73, 0x65, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x23,
	0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x43, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2f,
	0x76, 0x31, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x43, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x1a, 0x23, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x53, 0x65,
	0x72, 0x76, 0x65, 0x72, 0x2f, 0x76, 0x31, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x53, 0x65, 0x72, 0x76,
	0x65, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x19, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65,
	0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x61, 0x6e, 0x79, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x22, 0x8f, 0x04, 0x0a, 0x12, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a,
	0x65, 0x63, 0x74, 0x44, 0x69, 0x73, 0x70, 0x6c, 0x61, 0x79, 0x12, 0x14, 0x0a, 0x05, 0x6f, 0x77,
	0x6e, 0x65, 0x72, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x05, 0x6f, 0x77, 0x6e, 0x65, 0x72,
	0x12, 0x39, 0x0a, 0x0a, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x03,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70,
	0x52, 0x09, 0x75, 0x70, 0x64, 0x61, 0x74, 0x65, 0x64, 0x41, 0x74, 0x12, 0x1e, 0x0a, 0x0a, 0x6e,
	0x75, 0x6d, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x73, 0x18, 0x06, 0x20, 0x01, 0x28, 0x05, 0x52,
	0x0a, 0x6e, 0x75, 0x6d, 0x4d, 0x65, 0x74, 0x68, 0x6f, 0x64, 0x73, 0x12, 0x39, 0x0a, 0x0a, 0x63,
	0x72, 0x65, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32,
	0x1a, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75,
	0x66, 0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x63, 0x72, 0x65,
	0x61, 0x74, 0x65, 0x64, 0x41, 0x74, 0x12, 0x4e, 0x0a, 0x07, 0x6d, 0x65, 0x6d, 0x62, 0x65, 0x72,
	0x73, 0x18, 0x05, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x34, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53,
	0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79,
	0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x44, 0x69, 0x73, 0x70, 0x6c, 0x61, 0x79,
	0x2e, 0x4d, 0x65, 0x6d, 0x62, 0x65, 0x72, 0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x07, 0x6d,
	0x65, 0x6d, 0x62, 0x65, 0x72, 0x73, 0x12, 0x20, 0x0a, 0x0b, 0x6e, 0x75, 0x6d, 0x53, 0x65, 0x72,
	0x76, 0x69, 0x63, 0x65, 0x73, 0x18, 0x07, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0b, 0x6e, 0x75, 0x6d,
	0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x73, 0x12, 0x20, 0x0a, 0x0b, 0x6e, 0x75, 0x6d, 0x4d,
	0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x73, 0x18, 0x09, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0b, 0x6e,
	0x75, 0x6d, 0x4d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x73, 0x12, 0x20, 0x0a, 0x0b, 0x6e, 0x75,
	0x6d, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x18, 0x08, 0x20, 0x01, 0x28, 0x05, 0x52,
	0x0b, 0x6e, 0x75, 0x6d, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x73, 0x12, 0x3a, 0x0a, 0x07,
	0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x20, 0x2e,
	0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74,
	0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x52,
	0x07, 0x70, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x1a, 0x5b, 0x0a, 0x0c, 0x4d, 0x65, 0x6d, 0x62,
	0x65, 0x72, 0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x35, 0x0a, 0x05, 0x76, 0x61,
	0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x1f, 0x2e, 0x73, 0x79, 0x6c, 0x6b,
	0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x55, 0x73, 0x65, 0x72, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c,
	0x6b, 0x55, 0x73, 0x65, 0x72, 0x52, 0x6f, 0x6c, 0x65, 0x73, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75,
	0x65, 0x3a, 0x02, 0x38, 0x01, 0x22, 0xe2, 0x02, 0x0a, 0x0b, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72,
	0x6f, 0x6a, 0x65, 0x63, 0x74, 0x12, 0x20, 0x0a, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70,
	0x74, 0x69, 0x6f, 0x6e, 0x18, 0x08, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x65, 0x73, 0x63,
	0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x21, 0x0a, 0x0c, 0x6a, 0x61, 0x76, 0x61, 0x5f,
	0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x18, 0x06, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x6a,
	0x61, 0x76, 0x61, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x12, 0x1d, 0x0a, 0x0a, 0x67, 0x6f,
	0x5f, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x18, 0x05, 0x20, 0x01, 0x28, 0x09, 0x52, 0x09,
	0x67, 0x6f, 0x50, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d,
	0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x10, 0x0a,
	0x03, 0x75, 0x72, 0x69, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x75, 0x72, 0x69, 0x12,
	0x38, 0x0a, 0x07, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x73, 0x18, 0x04, 0x20, 0x03, 0x28, 0x0b,
	0x32, 0x1e, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x43, 0x6c, 0x69, 0x65,
	0x6e, 0x74, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x43, 0x6c, 0x69, 0x65, 0x6e, 0x74,
	0x52, 0x07, 0x63, 0x6c, 0x69, 0x65, 0x6e, 0x74, 0x73, 0x12, 0x36, 0x0a, 0x06, 0x73, 0x65, 0x72,
	0x76, 0x65, 0x72, 0x18, 0x07, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1e, 0x2e, 0x73, 0x79, 0x6c, 0x6b,
	0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x53, 0x65, 0x72, 0x76, 0x65, 0x72, 0x2e, 0x76, 0x31, 0x2e, 0x53,
	0x79, 0x6c, 0x6b, 0x53, 0x65, 0x72, 0x76, 0x65, 0x72, 0x52, 0x06, 0x73, 0x65, 0x72, 0x76, 0x65,
	0x72, 0x12, 0x21, 0x0a, 0x0c, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65, 0x5f, 0x6e, 0x61, 0x6d,
	0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x70, 0x61, 0x63, 0x6b, 0x61, 0x67, 0x65,
	0x4e, 0x61, 0x6d, 0x65, 0x12, 0x34, 0x0a, 0x0a, 0x65, 0x78, 0x74, 0x65, 0x6e, 0x73, 0x69, 0x6f,
	0x6e, 0x73, 0x18, 0x09, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x14, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c,
	0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x41, 0x6e, 0x79, 0x52, 0x0a,
	0x65, 0x78, 0x74, 0x65, 0x6e, 0x73, 0x69, 0x6f, 0x6e, 0x73, 0x42, 0x45, 0x5a, 0x43, 0x67, 0x69,
	0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2d, 0x62, 0x75,
	0x69, 0x6c, 0x64, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2d, 0x63, 0x6f, 0x72, 0x65, 0x2f, 0x73, 0x65,
	0x72, 0x76, 0x69, 0x63, 0x65, 0x73, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x73, 0x79,
	0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x50, 0x72, 0x6f, 0x6a, 0x65, 0x63, 0x74, 0x2f, 0x76,
	0x31, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_sylk_SylkProject_v1_SylkProject_proto_rawDescOnce sync.Once
	file_sylk_SylkProject_v1_SylkProject_proto_rawDescData = file_sylk_SylkProject_v1_SylkProject_proto_rawDesc
)

func file_sylk_SylkProject_v1_SylkProject_proto_rawDescGZIP() []byte {
	file_sylk_SylkProject_v1_SylkProject_proto_rawDescOnce.Do(func() {
		file_sylk_SylkProject_v1_SylkProject_proto_rawDescData = protoimpl.X.CompressGZIP(file_sylk_SylkProject_v1_SylkProject_proto_rawDescData)
	})
	return file_sylk_SylkProject_v1_SylkProject_proto_rawDescData
}

var file_sylk_SylkProject_v1_SylkProject_proto_msgTypes = make([]protoimpl.MessageInfo, 3)
var file_sylk_SylkProject_v1_SylkProject_proto_goTypes = []interface{}{
	(*SylkProjectDisplay)(nil),    // 0: sylk.SylkProject.v1.SylkProjectDisplay
	(*SylkProject)(nil),           // 1: sylk.SylkProject.v1.SylkProject
	nil,                           // 2: sylk.SylkProject.v1.SylkProjectDisplay.MembersEntry
	(*timestamppb.Timestamp)(nil), // 3: google.protobuf.Timestamp
	(*v11.SylkClient)(nil),        // 4: sylk.SylkClient.v1.SylkClient
	(*v12.SylkServer)(nil),        // 5: sylk.SylkServer.v1.SylkServer
	(*anypb.Any)(nil),             // 6: google.protobuf.Any
	(v1.SylkUserRoles)(0),         // 7: sylk.SylkUser.v1.SylkUserRoles
}
var file_sylk_SylkProject_v1_SylkProject_proto_depIdxs = []int32{
	3, // 0: sylk.SylkProject.v1.SylkProjectDisplay.updated_at:type_name -> google.protobuf.Timestamp
	3, // 1: sylk.SylkProject.v1.SylkProjectDisplay.created_at:type_name -> google.protobuf.Timestamp
	2, // 2: sylk.SylkProject.v1.SylkProjectDisplay.members:type_name -> sylk.SylkProject.v1.SylkProjectDisplay.MembersEntry
	1, // 3: sylk.SylkProject.v1.SylkProjectDisplay.project:type_name -> sylk.SylkProject.v1.SylkProject
	4, // 4: sylk.SylkProject.v1.SylkProject.clients:type_name -> sylk.SylkClient.v1.SylkClient
	5, // 5: sylk.SylkProject.v1.SylkProject.server:type_name -> sylk.SylkServer.v1.SylkServer
	6, // 6: sylk.SylkProject.v1.SylkProject.extensions:type_name -> google.protobuf.Any
	7, // 7: sylk.SylkProject.v1.SylkProjectDisplay.MembersEntry.value:type_name -> sylk.SylkUser.v1.SylkUserRoles
	8, // [8:8] is the sub-list for method output_type
	8, // [8:8] is the sub-list for method input_type
	8, // [8:8] is the sub-list for extension type_name
	8, // [8:8] is the sub-list for extension extendee
	0, // [0:8] is the sub-list for field type_name
}

func init() { file_sylk_SylkProject_v1_SylkProject_proto_init() }
func file_sylk_SylkProject_v1_SylkProject_proto_init() {
	if File_sylk_SylkProject_v1_SylkProject_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_sylk_SylkProject_v1_SylkProject_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SylkProjectDisplay); i {
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
		file_sylk_SylkProject_v1_SylkProject_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SylkProject); i {
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
			RawDescriptor: file_sylk_SylkProject_v1_SylkProject_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   3,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_sylk_SylkProject_v1_SylkProject_proto_goTypes,
		DependencyIndexes: file_sylk_SylkProject_v1_SylkProject_proto_depIdxs,
		MessageInfos:      file_sylk_SylkProject_v1_SylkProject_proto_msgTypes,
	}.Build()
	File_sylk_SylkProject_v1_SylkProject_proto = out.File
	file_sylk_SylkProject_v1_SylkProject_proto_rawDesc = nil
	file_sylk_SylkProject_v1_SylkProject_proto_goTypes = nil
	file_sylk_SylkProject_v1_SylkProject_proto_depIdxs = nil
}