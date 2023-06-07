// sylk.build Generated proto DO NOT EDIT

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v4.23.1
// source: sylk/SylkField/v1/SylkField.proto

package v1

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	structpb "google.golang.org/protobuf/types/known/structpb"
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

// [sylk.SylkField.v1.SylkFieldTypes] - None
type SylkFieldTypes int32

const (
	// [sylk.SylkField.v1.SylkFieldTypes] - Default enum value for "sylk.SylkField.v1.SylkFieldTypes"
	SylkFieldTypes_DEFAULT_SYLKFIELDTYPES SylkFieldTypes = 0
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_DOUBLE SylkFieldTypes = 1
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_FLOAT SylkFieldTypes = 2
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_INT64 SylkFieldTypes = 3
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_UINT64 SylkFieldTypes = 4
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_INT32 SylkFieldTypes = 5
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_FIXED64 SylkFieldTypes = 6
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_FIXED32 SylkFieldTypes = 7
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_BOOL SylkFieldTypes = 8
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_STRING SylkFieldTypes = 9
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_GROUP SylkFieldTypes = 10
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_MESSAGE SylkFieldTypes = 11
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_BYTES SylkFieldTypes = 12
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_UINT32 SylkFieldTypes = 13
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_ENUM SylkFieldTypes = 14
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_SFIXED32 SylkFieldTypes = 15
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_SFIXED64 SylkFieldTypes = 16
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_SINT32 SylkFieldTypes = 17
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_SINT64 SylkFieldTypes = 18
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_MAP SylkFieldTypes = 19
	// [sylk.SylkField.v1.SylkFieldTypes] - None
	SylkFieldTypes_TYPE_ONEOF SylkFieldTypes = 20
)

// Enum value maps for SylkFieldTypes.
var (
	SylkFieldTypes_name = map[int32]string{
		0:  "DEFAULT_SYLKFIELDTYPES",
		1:  "TYPE_DOUBLE",
		2:  "TYPE_FLOAT",
		3:  "TYPE_INT64",
		4:  "TYPE_UINT64",
		5:  "TYPE_INT32",
		6:  "TYPE_FIXED64",
		7:  "TYPE_FIXED32",
		8:  "TYPE_BOOL",
		9:  "TYPE_STRING",
		10: "TYPE_GROUP",
		11: "TYPE_MESSAGE",
		12: "TYPE_BYTES",
		13: "TYPE_UINT32",
		14: "TYPE_ENUM",
		15: "TYPE_SFIXED32",
		16: "TYPE_SFIXED64",
		17: "TYPE_SINT32",
		18: "TYPE_SINT64",
		19: "TYPE_MAP",
		20: "TYPE_ONEOF",
	}
	SylkFieldTypes_value = map[string]int32{
		"DEFAULT_SYLKFIELDTYPES": 0,
		"TYPE_DOUBLE":            1,
		"TYPE_FLOAT":             2,
		"TYPE_INT64":             3,
		"TYPE_UINT64":            4,
		"TYPE_INT32":             5,
		"TYPE_FIXED64":           6,
		"TYPE_FIXED32":           7,
		"TYPE_BOOL":              8,
		"TYPE_STRING":            9,
		"TYPE_GROUP":             10,
		"TYPE_MESSAGE":           11,
		"TYPE_BYTES":             12,
		"TYPE_UINT32":            13,
		"TYPE_ENUM":              14,
		"TYPE_SFIXED32":          15,
		"TYPE_SFIXED64":          16,
		"TYPE_SINT32":            17,
		"TYPE_SINT64":            18,
		"TYPE_MAP":               19,
		"TYPE_ONEOF":             20,
	}
)

func (x SylkFieldTypes) Enum() *SylkFieldTypes {
	p := new(SylkFieldTypes)
	*p = x
	return p
}

func (x SylkFieldTypes) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (SylkFieldTypes) Descriptor() protoreflect.EnumDescriptor {
	return file_sylk_SylkField_v1_SylkField_proto_enumTypes[0].Descriptor()
}

func (SylkFieldTypes) Type() protoreflect.EnumType {
	return &file_sylk_SylkField_v1_SylkField_proto_enumTypes[0]
}

func (x SylkFieldTypes) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use SylkFieldTypes.Descriptor instead.
func (SylkFieldTypes) EnumDescriptor() ([]byte, []int) {
	return file_sylk_SylkField_v1_SylkField_proto_rawDescGZIP(), []int{0}
}

// [sylk.SylkField.v1.SylkFieldLabels] - None
type SylkFieldLabels int32

const (
	// [sylk.SylkField.v1.SylkFieldLabels] - Default enum value for "sylk.SylkField.v1.SylkFieldLabels"
	SylkFieldLabels_DEFAULT_SYLKFIELDLABELS SylkFieldLabels = 0
	// [sylk.SylkField.v1.SylkFieldLabels] - None
	SylkFieldLabels_LABEL_OPTIONAL SylkFieldLabels = 1
	// [sylk.SylkField.v1.SylkFieldLabels] - None
	SylkFieldLabels_LABEL_REQUIRED SylkFieldLabels = 2
	// [sylk.SylkField.v1.SylkFieldLabels] - None
	SylkFieldLabels_LABEL_REPEATED SylkFieldLabels = 3
)

// Enum value maps for SylkFieldLabels.
var (
	SylkFieldLabels_name = map[int32]string{
		0: "DEFAULT_SYLKFIELDLABELS",
		1: "LABEL_OPTIONAL",
		2: "LABEL_REQUIRED",
		3: "LABEL_REPEATED",
	}
	SylkFieldLabels_value = map[string]int32{
		"DEFAULT_SYLKFIELDLABELS": 0,
		"LABEL_OPTIONAL":          1,
		"LABEL_REQUIRED":          2,
		"LABEL_REPEATED":          3,
	}
)

func (x SylkFieldLabels) Enum() *SylkFieldLabels {
	p := new(SylkFieldLabels)
	*p = x
	return p
}

func (x SylkFieldLabels) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (SylkFieldLabels) Descriptor() protoreflect.EnumDescriptor {
	return file_sylk_SylkField_v1_SylkField_proto_enumTypes[1].Descriptor()
}

func (SylkFieldLabels) Type() protoreflect.EnumType {
	return &file_sylk_SylkField_v1_SylkField_proto_enumTypes[1]
}

func (x SylkFieldLabels) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use SylkFieldLabels.Descriptor instead.
func (SylkFieldLabels) EnumDescriptor() ([]byte, []int) {
	return file_sylk_SylkField_v1_SylkField_proto_rawDescGZIP(), []int{1}
}

// [sylk.SylkField.v1.SylkFieldDisplay] - None
type SylkFieldDisplay struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	CreatedAt *timestamppb.Timestamp `protobuf:"bytes,2,opt,name=created_at,json=createdAt,proto3" json:"created_at,omitempty"`
	Field     *SylkField             `protobuf:"bytes,1,opt,name=field,proto3" json:"field,omitempty"`
	UpdatedAt *timestamppb.Timestamp `protobuf:"bytes,3,opt,name=updated_at,json=updatedAt,proto3" json:"updated_at,omitempty"`
}

func (x *SylkFieldDisplay) Reset() {
	*x = SylkFieldDisplay{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_SylkField_v1_SylkField_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SylkFieldDisplay) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SylkFieldDisplay) ProtoMessage() {}

func (x *SylkFieldDisplay) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_SylkField_v1_SylkField_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SylkFieldDisplay.ProtoReflect.Descriptor instead.
func (*SylkFieldDisplay) Descriptor() ([]byte, []int) {
	return file_sylk_SylkField_v1_SylkField_proto_rawDescGZIP(), []int{0}
}

func (x *SylkFieldDisplay) GetCreatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.CreatedAt
	}
	return nil
}

func (x *SylkFieldDisplay) GetField() *SylkField {
	if x != nil {
		return x.Field
	}
	return nil
}

func (x *SylkFieldDisplay) GetUpdatedAt() *timestamppb.Timestamp {
	if x != nil {
		return x.UpdatedAt
	}
	return nil
}

// [sylk.SylkField.v1.SylkField] - None
type SylkField struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Type        string                      `protobuf:"bytes,11,opt,name=type,proto3" json:"type,omitempty"`
	Uri         string                      `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
	OneofFields []*SylkOneOfField           `protobuf:"bytes,15,rep,name=oneof_fields,json=oneofFields,proto3" json:"oneof_fields,omitempty"`
	Name        string                      `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Description string                      `protobuf:"bytes,4,opt,name=description,proto3" json:"description,omitempty"`
	EnumType    string                      `protobuf:"bytes,10,opt,name=enum_type,json=enumType,proto3" json:"enum_type,omitempty"`
	FieldType   SylkFieldTypes              `protobuf:"varint,5,opt,name=field_type,json=fieldType,proto3,enum=sylk.SylkField.v1.SylkFieldTypes" json:"field_type,omitempty"`
	MessageType string                      `protobuf:"bytes,9,opt,name=message_type,json=messageType,proto3" json:"message_type,omitempty"`
	Kind        string                      `protobuf:"bytes,12,opt,name=kind,proto3" json:"kind,omitempty"`
	FullName    string                      `protobuf:"bytes,3,opt,name=full_name,json=fullName,proto3" json:"full_name,omitempty"`
	Extensions  map[string]*structpb.Struct `protobuf:"bytes,14,rep,name=extensions,proto3" json:"extensions,omitempty" protobuf_key:"bytes,1,opt,name=key,proto3" protobuf_val:"bytes,2,opt,name=value,proto3"`
	Index       int32                       `protobuf:"varint,13,opt,name=index,proto3" json:"index,omitempty"`
	Label       SylkFieldLabels             `protobuf:"varint,6,opt,name=label,proto3,enum=sylk.SylkField.v1.SylkFieldLabels" json:"label,omitempty"`
	KeyType     SylkFieldTypes              `protobuf:"varint,7,opt,name=key_type,json=keyType,proto3,enum=sylk.SylkField.v1.SylkFieldTypes" json:"key_type,omitempty"`
	ValueType   SylkFieldTypes              `protobuf:"varint,8,opt,name=value_type,json=valueType,proto3,enum=sylk.SylkField.v1.SylkFieldTypes" json:"value_type,omitempty"`
}

func (x *SylkField) Reset() {
	*x = SylkField{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_SylkField_v1_SylkField_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SylkField) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SylkField) ProtoMessage() {}

func (x *SylkField) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_SylkField_v1_SylkField_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SylkField.ProtoReflect.Descriptor instead.
func (*SylkField) Descriptor() ([]byte, []int) {
	return file_sylk_SylkField_v1_SylkField_proto_rawDescGZIP(), []int{1}
}

func (x *SylkField) GetType() string {
	if x != nil {
		return x.Type
	}
	return ""
}

func (x *SylkField) GetUri() string {
	if x != nil {
		return x.Uri
	}
	return ""
}

func (x *SylkField) GetOneofFields() []*SylkOneOfField {
	if x != nil {
		return x.OneofFields
	}
	return nil
}

func (x *SylkField) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *SylkField) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *SylkField) GetEnumType() string {
	if x != nil {
		return x.EnumType
	}
	return ""
}

func (x *SylkField) GetFieldType() SylkFieldTypes {
	if x != nil {
		return x.FieldType
	}
	return SylkFieldTypes_DEFAULT_SYLKFIELDTYPES
}

func (x *SylkField) GetMessageType() string {
	if x != nil {
		return x.MessageType
	}
	return ""
}

func (x *SylkField) GetKind() string {
	if x != nil {
		return x.Kind
	}
	return ""
}

func (x *SylkField) GetFullName() string {
	if x != nil {
		return x.FullName
	}
	return ""
}

func (x *SylkField) GetExtensions() map[string]*structpb.Struct {
	if x != nil {
		return x.Extensions
	}
	return nil
}

func (x *SylkField) GetIndex() int32 {
	if x != nil {
		return x.Index
	}
	return 0
}

func (x *SylkField) GetLabel() SylkFieldLabels {
	if x != nil {
		return x.Label
	}
	return SylkFieldLabels_DEFAULT_SYLKFIELDLABELS
}

func (x *SylkField) GetKeyType() SylkFieldTypes {
	if x != nil {
		return x.KeyType
	}
	return SylkFieldTypes_DEFAULT_SYLKFIELDTYPES
}

func (x *SylkField) GetValueType() SylkFieldTypes {
	if x != nil {
		return x.ValueType
	}
	return SylkFieldTypes_DEFAULT_SYLKFIELDTYPES
}

// [sylk.SylkField.v1.SylkOneOfField] - None
type SylkOneOfField struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	EnumType    string          `protobuf:"bytes,8,opt,name=enum_type,json=enumType,proto3" json:"enum_type,omitempty"`
	FullName    string          `protobuf:"bytes,3,opt,name=full_name,json=fullName,proto3" json:"full_name,omitempty"`
	Uri         string          `protobuf:"bytes,1,opt,name=uri,proto3" json:"uri,omitempty"`
	MessageType string          `protobuf:"bytes,7,opt,name=message_type,json=messageType,proto3" json:"message_type,omitempty"`
	FieldType   SylkFieldTypes  `protobuf:"varint,5,opt,name=field_type,json=fieldType,proto3,enum=sylk.SylkField.v1.SylkFieldTypes" json:"field_type,omitempty"`
	Name        string          `protobuf:"bytes,2,opt,name=name,proto3" json:"name,omitempty"`
	Description string          `protobuf:"bytes,4,opt,name=description,proto3" json:"description,omitempty"`
	Label       SylkFieldLabels `protobuf:"varint,6,opt,name=label,proto3,enum=sylk.SylkField.v1.SylkFieldLabels" json:"label,omitempty"`
}

func (x *SylkOneOfField) Reset() {
	*x = SylkOneOfField{}
	if protoimpl.UnsafeEnabled {
		mi := &file_sylk_SylkField_v1_SylkField_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *SylkOneOfField) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*SylkOneOfField) ProtoMessage() {}

func (x *SylkOneOfField) ProtoReflect() protoreflect.Message {
	mi := &file_sylk_SylkField_v1_SylkField_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use SylkOneOfField.ProtoReflect.Descriptor instead.
func (*SylkOneOfField) Descriptor() ([]byte, []int) {
	return file_sylk_SylkField_v1_SylkField_proto_rawDescGZIP(), []int{2}
}

func (x *SylkOneOfField) GetEnumType() string {
	if x != nil {
		return x.EnumType
	}
	return ""
}

func (x *SylkOneOfField) GetFullName() string {
	if x != nil {
		return x.FullName
	}
	return ""
}

func (x *SylkOneOfField) GetUri() string {
	if x != nil {
		return x.Uri
	}
	return ""
}

func (x *SylkOneOfField) GetMessageType() string {
	if x != nil {
		return x.MessageType
	}
	return ""
}

func (x *SylkOneOfField) GetFieldType() SylkFieldTypes {
	if x != nil {
		return x.FieldType
	}
	return SylkFieldTypes_DEFAULT_SYLKFIELDTYPES
}

func (x *SylkOneOfField) GetName() string {
	if x != nil {
		return x.Name
	}
	return ""
}

func (x *SylkOneOfField) GetDescription() string {
	if x != nil {
		return x.Description
	}
	return ""
}

func (x *SylkOneOfField) GetLabel() SylkFieldLabels {
	if x != nil {
		return x.Label
	}
	return SylkFieldLabels_DEFAULT_SYLKFIELDLABELS
}

var File_sylk_SylkField_v1_SylkField_proto protoreflect.FileDescriptor

var file_sylk_SylkField_v1_SylkField_proto_rawDesc = []byte{
	0x0a, 0x21, 0x73, 0x79, 0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64,
	0x2f, 0x76, 0x31, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x12, 0x11, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69,
	0x65, 0x6c, 0x64, 0x2e, 0x76, 0x31, 0x1a, 0x1f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x74, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d,
	0x70, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1c, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2f, 0x73, 0x74, 0x72, 0x75, 0x63, 0x74, 0x2e,
	0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0xbc, 0x01, 0x0a, 0x10, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69,
	0x65, 0x6c, 0x64, 0x44, 0x69, 0x73, 0x70, 0x6c, 0x61, 0x79, 0x12, 0x39, 0x0a, 0x0a, 0x63, 0x72,
	0x65, 0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a,
	0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66,
	0x2e, 0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x63, 0x72, 0x65, 0x61,
	0x74, 0x65, 0x64, 0x41, 0x74, 0x12, 0x32, 0x0a, 0x05, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x0b, 0x32, 0x1c, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b,
	0x46, 0x69, 0x65, 0x6c, 0x64, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65,
	0x6c, 0x64, 0x52, 0x05, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x12, 0x39, 0x0a, 0x0a, 0x75, 0x70, 0x64,
	0x61, 0x74, 0x65, 0x64, 0x5f, 0x61, 0x74, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x1a, 0x2e,
	0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e,
	0x54, 0x69, 0x6d, 0x65, 0x73, 0x74, 0x61, 0x6d, 0x70, 0x52, 0x09, 0x75, 0x70, 0x64, 0x61, 0x74,
	0x65, 0x64, 0x41, 0x74, 0x22, 0xd6, 0x05, 0x0a, 0x09, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65,
	0x6c, 0x64, 0x12, 0x12, 0x0a, 0x04, 0x74, 0x79, 0x70, 0x65, 0x18, 0x0b, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x04, 0x74, 0x79, 0x70, 0x65, 0x12, 0x10, 0x0a, 0x03, 0x75, 0x72, 0x69, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x03, 0x75, 0x72, 0x69, 0x12, 0x44, 0x0a, 0x0c, 0x6f, 0x6e, 0x65, 0x6f,
	0x66, 0x5f, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x18, 0x0f, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x21,
	0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x2e,
	0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x4f, 0x6e, 0x65, 0x4f, 0x66, 0x46, 0x69, 0x65, 0x6c,
	0x64, 0x52, 0x0b, 0x6f, 0x6e, 0x65, 0x6f, 0x66, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x73, 0x12, 0x12,
	0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6e, 0x61,
	0x6d, 0x65, 0x12, 0x20, 0x0a, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70, 0x74, 0x69, 0x6f,
	0x6e, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70,
	0x74, 0x69, 0x6f, 0x6e, 0x12, 0x1b, 0x0a, 0x09, 0x65, 0x6e, 0x75, 0x6d, 0x5f, 0x74, 0x79, 0x70,
	0x65, 0x18, 0x0a, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x65, 0x6e, 0x75, 0x6d, 0x54, 0x79, 0x70,
	0x65, 0x12, 0x40, 0x0a, 0x0a, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18,
	0x05, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x21, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c,
	0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69,
	0x65, 0x6c, 0x64, 0x54, 0x79, 0x70, 0x65, 0x73, 0x52, 0x09, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x54,
	0x79, 0x70, 0x65, 0x12, 0x21, 0x0a, 0x0c, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x5f, 0x74,
	0x79, 0x70, 0x65, 0x18, 0x09, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x6d, 0x65, 0x73, 0x73, 0x61,
	0x67, 0x65, 0x54, 0x79, 0x70, 0x65, 0x12, 0x12, 0x0a, 0x04, 0x6b, 0x69, 0x6e, 0x64, 0x18, 0x0c,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x04, 0x6b, 0x69, 0x6e, 0x64, 0x12, 0x1b, 0x0a, 0x09, 0x66, 0x75,
	0x6c, 0x6c, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x66,
	0x75, 0x6c, 0x6c, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x4c, 0x0a, 0x0a, 0x65, 0x78, 0x74, 0x65, 0x6e,
	0x73, 0x69, 0x6f, 0x6e, 0x73, 0x18, 0x0e, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x2c, 0x2e, 0x73, 0x79,
	0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x2e, 0x76, 0x31, 0x2e,
	0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x2e, 0x45, 0x78, 0x74, 0x65, 0x6e, 0x73,
	0x69, 0x6f, 0x6e, 0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x52, 0x0a, 0x65, 0x78, 0x74, 0x65, 0x6e,
	0x73, 0x69, 0x6f, 0x6e, 0x73, 0x12, 0x14, 0x0a, 0x05, 0x69, 0x6e, 0x64, 0x65, 0x78, 0x18, 0x0d,
	0x20, 0x01, 0x28, 0x05, 0x52, 0x05, 0x69, 0x6e, 0x64, 0x65, 0x78, 0x12, 0x38, 0x0a, 0x05, 0x6c,
	0x61, 0x62, 0x65, 0x6c, 0x18, 0x06, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x22, 0x2e, 0x73, 0x79, 0x6c,
	0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x2e, 0x76, 0x31, 0x2e, 0x53,
	0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x4c, 0x61, 0x62, 0x65, 0x6c, 0x73, 0x52, 0x05,
	0x6c, 0x61, 0x62, 0x65, 0x6c, 0x12, 0x3c, 0x0a, 0x08, 0x6b, 0x65, 0x79, 0x5f, 0x74, 0x79, 0x70,
	0x65, 0x18, 0x07, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x21, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53,
	0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b,
	0x46, 0x69, 0x65, 0x6c, 0x64, 0x54, 0x79, 0x70, 0x65, 0x73, 0x52, 0x07, 0x6b, 0x65, 0x79, 0x54,
	0x79, 0x70, 0x65, 0x12, 0x40, 0x0a, 0x0a, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x5f, 0x74, 0x79, 0x70,
	0x65, 0x18, 0x08, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x21, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53,
	0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b,
	0x46, 0x69, 0x65, 0x6c, 0x64, 0x54, 0x79, 0x70, 0x65, 0x73, 0x52, 0x09, 0x76, 0x61, 0x6c, 0x75,
	0x65, 0x54, 0x79, 0x70, 0x65, 0x1a, 0x56, 0x0a, 0x0f, 0x45, 0x78, 0x74, 0x65, 0x6e, 0x73, 0x69,
	0x6f, 0x6e, 0x73, 0x45, 0x6e, 0x74, 0x72, 0x79, 0x12, 0x10, 0x0a, 0x03, 0x6b, 0x65, 0x79, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x6b, 0x65, 0x79, 0x12, 0x2d, 0x0a, 0x05, 0x76, 0x61,
	0x6c, 0x75, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x17, 0x2e, 0x67, 0x6f, 0x6f, 0x67,
	0x6c, 0x65, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x75, 0x66, 0x2e, 0x53, 0x74, 0x72, 0x75,
	0x63, 0x74, 0x52, 0x05, 0x76, 0x61, 0x6c, 0x75, 0x65, 0x3a, 0x02, 0x38, 0x01, 0x22, 0xb1, 0x02,
	0x0a, 0x0e, 0x53, 0x79, 0x6c, 0x6b, 0x4f, 0x6e, 0x65, 0x4f, 0x66, 0x46, 0x69, 0x65, 0x6c, 0x64,
	0x12, 0x1b, 0x0a, 0x09, 0x65, 0x6e, 0x75, 0x6d, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x08, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x08, 0x65, 0x6e, 0x75, 0x6d, 0x54, 0x79, 0x70, 0x65, 0x12, 0x1b, 0x0a,
	0x09, 0x66, 0x75, 0x6c, 0x6c, 0x5f, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09,
	0x52, 0x08, 0x66, 0x75, 0x6c, 0x6c, 0x4e, 0x61, 0x6d, 0x65, 0x12, 0x10, 0x0a, 0x03, 0x75, 0x72,
	0x69, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x75, 0x72, 0x69, 0x12, 0x21, 0x0a, 0x0c,
	0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x07, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x0b, 0x6d, 0x65, 0x73, 0x73, 0x61, 0x67, 0x65, 0x54, 0x79, 0x70, 0x65, 0x12,
	0x40, 0x0a, 0x0a, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x5f, 0x74, 0x79, 0x70, 0x65, 0x18, 0x05, 0x20,
	0x01, 0x28, 0x0e, 0x32, 0x21, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x46,
	0x69, 0x65, 0x6c, 0x64, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c,
	0x64, 0x54, 0x79, 0x70, 0x65, 0x73, 0x52, 0x09, 0x66, 0x69, 0x65, 0x6c, 0x64, 0x54, 0x79, 0x70,
	0x65, 0x12, 0x12, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x04, 0x6e, 0x61, 0x6d, 0x65, 0x12, 0x20, 0x0a, 0x0b, 0x64, 0x65, 0x73, 0x63, 0x72, 0x69, 0x70,
	0x74, 0x69, 0x6f, 0x6e, 0x18, 0x04, 0x20, 0x01, 0x28, 0x09, 0x52, 0x0b, 0x64, 0x65, 0x73, 0x63,
	0x72, 0x69, 0x70, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x38, 0x0a, 0x05, 0x6c, 0x61, 0x62, 0x65, 0x6c,
	0x18, 0x06, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x22, 0x2e, 0x73, 0x79, 0x6c, 0x6b, 0x2e, 0x53, 0x79,
	0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x2e, 0x76, 0x31, 0x2e, 0x53, 0x79, 0x6c, 0x6b, 0x46,
	0x69, 0x65, 0x6c, 0x64, 0x4c, 0x61, 0x62, 0x65, 0x6c, 0x73, 0x52, 0x05, 0x6c, 0x61, 0x62, 0x65,
	0x6c, 0x2a, 0xfa, 0x02, 0x0a, 0x0e, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x54,
	0x79, 0x70, 0x65, 0x73, 0x12, 0x1a, 0x0a, 0x16, 0x44, 0x45, 0x46, 0x41, 0x55, 0x4c, 0x54, 0x5f,
	0x53, 0x59, 0x4c, 0x4b, 0x46, 0x49, 0x45, 0x4c, 0x44, 0x54, 0x59, 0x50, 0x45, 0x53, 0x10, 0x00,
	0x12, 0x0f, 0x0a, 0x0b, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x44, 0x4f, 0x55, 0x42, 0x4c, 0x45, 0x10,
	0x01, 0x12, 0x0e, 0x0a, 0x0a, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x46, 0x4c, 0x4f, 0x41, 0x54, 0x10,
	0x02, 0x12, 0x0e, 0x0a, 0x0a, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x49, 0x4e, 0x54, 0x36, 0x34, 0x10,
	0x03, 0x12, 0x0f, 0x0a, 0x0b, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x55, 0x49, 0x4e, 0x54, 0x36, 0x34,
	0x10, 0x04, 0x12, 0x0e, 0x0a, 0x0a, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x49, 0x4e, 0x54, 0x33, 0x32,
	0x10, 0x05, 0x12, 0x10, 0x0a, 0x0c, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x46, 0x49, 0x58, 0x45, 0x44,
	0x36, 0x34, 0x10, 0x06, 0x12, 0x10, 0x0a, 0x0c, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x46, 0x49, 0x58,
	0x45, 0x44, 0x33, 0x32, 0x10, 0x07, 0x12, 0x0d, 0x0a, 0x09, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x42,
	0x4f, 0x4f, 0x4c, 0x10, 0x08, 0x12, 0x0f, 0x0a, 0x0b, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x53, 0x54,
	0x52, 0x49, 0x4e, 0x47, 0x10, 0x09, 0x12, 0x0e, 0x0a, 0x0a, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x47,
	0x52, 0x4f, 0x55, 0x50, 0x10, 0x0a, 0x12, 0x10, 0x0a, 0x0c, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x4d,
	0x45, 0x53, 0x53, 0x41, 0x47, 0x45, 0x10, 0x0b, 0x12, 0x0e, 0x0a, 0x0a, 0x54, 0x59, 0x50, 0x45,
	0x5f, 0x42, 0x59, 0x54, 0x45, 0x53, 0x10, 0x0c, 0x12, 0x0f, 0x0a, 0x0b, 0x54, 0x59, 0x50, 0x45,
	0x5f, 0x55, 0x49, 0x4e, 0x54, 0x33, 0x32, 0x10, 0x0d, 0x12, 0x0d, 0x0a, 0x09, 0x54, 0x59, 0x50,
	0x45, 0x5f, 0x45, 0x4e, 0x55, 0x4d, 0x10, 0x0e, 0x12, 0x11, 0x0a, 0x0d, 0x54, 0x59, 0x50, 0x45,
	0x5f, 0x53, 0x46, 0x49, 0x58, 0x45, 0x44, 0x33, 0x32, 0x10, 0x0f, 0x12, 0x11, 0x0a, 0x0d, 0x54,
	0x59, 0x50, 0x45, 0x5f, 0x53, 0x46, 0x49, 0x58, 0x45, 0x44, 0x36, 0x34, 0x10, 0x10, 0x12, 0x0f,
	0x0a, 0x0b, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x53, 0x49, 0x4e, 0x54, 0x33, 0x32, 0x10, 0x11, 0x12,
	0x0f, 0x0a, 0x0b, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x53, 0x49, 0x4e, 0x54, 0x36, 0x34, 0x10, 0x12,
	0x12, 0x0c, 0x0a, 0x08, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x4d, 0x41, 0x50, 0x10, 0x13, 0x12, 0x0e,
	0x0a, 0x0a, 0x54, 0x59, 0x50, 0x45, 0x5f, 0x4f, 0x4e, 0x45, 0x4f, 0x46, 0x10, 0x14, 0x2a, 0x6a,
	0x0a, 0x0f, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x4c, 0x61, 0x62, 0x65, 0x6c,
	0x73, 0x12, 0x1b, 0x0a, 0x17, 0x44, 0x45, 0x46, 0x41, 0x55, 0x4c, 0x54, 0x5f, 0x53, 0x59, 0x4c,
	0x4b, 0x46, 0x49, 0x45, 0x4c, 0x44, 0x4c, 0x41, 0x42, 0x45, 0x4c, 0x53, 0x10, 0x00, 0x12, 0x12,
	0x0a, 0x0e, 0x4c, 0x41, 0x42, 0x45, 0x4c, 0x5f, 0x4f, 0x50, 0x54, 0x49, 0x4f, 0x4e, 0x41, 0x4c,
	0x10, 0x01, 0x12, 0x12, 0x0a, 0x0e, 0x4c, 0x41, 0x42, 0x45, 0x4c, 0x5f, 0x52, 0x45, 0x51, 0x55,
	0x49, 0x52, 0x45, 0x44, 0x10, 0x02, 0x12, 0x12, 0x0a, 0x0e, 0x4c, 0x41, 0x42, 0x45, 0x4c, 0x5f,
	0x52, 0x45, 0x50, 0x45, 0x41, 0x54, 0x45, 0x44, 0x10, 0x03, 0x42, 0x43, 0x5a, 0x41, 0x67, 0x69,
	0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2d, 0x62, 0x75,
	0x69, 0x6c, 0x64, 0x2f, 0x73, 0x79, 0x6c, 0x6b, 0x2d, 0x63, 0x6f, 0x72, 0x65, 0x2f, 0x73, 0x65,
	0x72, 0x76, 0x69, 0x63, 0x65, 0x73, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x73, 0x2f, 0x73, 0x79,
	0x6c, 0x6b, 0x2f, 0x53, 0x79, 0x6c, 0x6b, 0x46, 0x69, 0x65, 0x6c, 0x64, 0x2f, 0x76, 0x31, 0x62,
	0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_sylk_SylkField_v1_SylkField_proto_rawDescOnce sync.Once
	file_sylk_SylkField_v1_SylkField_proto_rawDescData = file_sylk_SylkField_v1_SylkField_proto_rawDesc
)

func file_sylk_SylkField_v1_SylkField_proto_rawDescGZIP() []byte {
	file_sylk_SylkField_v1_SylkField_proto_rawDescOnce.Do(func() {
		file_sylk_SylkField_v1_SylkField_proto_rawDescData = protoimpl.X.CompressGZIP(file_sylk_SylkField_v1_SylkField_proto_rawDescData)
	})
	return file_sylk_SylkField_v1_SylkField_proto_rawDescData
}

var file_sylk_SylkField_v1_SylkField_proto_enumTypes = make([]protoimpl.EnumInfo, 2)
var file_sylk_SylkField_v1_SylkField_proto_msgTypes = make([]protoimpl.MessageInfo, 4)
var file_sylk_SylkField_v1_SylkField_proto_goTypes = []interface{}{
	(SylkFieldTypes)(0),           // 0: sylk.SylkField.v1.SylkFieldTypes
	(SylkFieldLabels)(0),          // 1: sylk.SylkField.v1.SylkFieldLabels
	(*SylkFieldDisplay)(nil),      // 2: sylk.SylkField.v1.SylkFieldDisplay
	(*SylkField)(nil),             // 3: sylk.SylkField.v1.SylkField
	(*SylkOneOfField)(nil),        // 4: sylk.SylkField.v1.SylkOneOfField
	nil,                           // 5: sylk.SylkField.v1.SylkField.ExtensionsEntry
	(*timestamppb.Timestamp)(nil), // 6: google.protobuf.Timestamp
	(*structpb.Struct)(nil),       // 7: google.protobuf.Struct
}
var file_sylk_SylkField_v1_SylkField_proto_depIdxs = []int32{
	6,  // 0: sylk.SylkField.v1.SylkFieldDisplay.created_at:type_name -> google.protobuf.Timestamp
	3,  // 1: sylk.SylkField.v1.SylkFieldDisplay.field:type_name -> sylk.SylkField.v1.SylkField
	6,  // 2: sylk.SylkField.v1.SylkFieldDisplay.updated_at:type_name -> google.protobuf.Timestamp
	4,  // 3: sylk.SylkField.v1.SylkField.oneof_fields:type_name -> sylk.SylkField.v1.SylkOneOfField
	0,  // 4: sylk.SylkField.v1.SylkField.field_type:type_name -> sylk.SylkField.v1.SylkFieldTypes
	5,  // 5: sylk.SylkField.v1.SylkField.extensions:type_name -> sylk.SylkField.v1.SylkField.ExtensionsEntry
	1,  // 6: sylk.SylkField.v1.SylkField.label:type_name -> sylk.SylkField.v1.SylkFieldLabels
	0,  // 7: sylk.SylkField.v1.SylkField.key_type:type_name -> sylk.SylkField.v1.SylkFieldTypes
	0,  // 8: sylk.SylkField.v1.SylkField.value_type:type_name -> sylk.SylkField.v1.SylkFieldTypes
	0,  // 9: sylk.SylkField.v1.SylkOneOfField.field_type:type_name -> sylk.SylkField.v1.SylkFieldTypes
	1,  // 10: sylk.SylkField.v1.SylkOneOfField.label:type_name -> sylk.SylkField.v1.SylkFieldLabels
	7,  // 11: sylk.SylkField.v1.SylkField.ExtensionsEntry.value:type_name -> google.protobuf.Struct
	12, // [12:12] is the sub-list for method output_type
	12, // [12:12] is the sub-list for method input_type
	12, // [12:12] is the sub-list for extension type_name
	12, // [12:12] is the sub-list for extension extendee
	0,  // [0:12] is the sub-list for field type_name
}

func init() { file_sylk_SylkField_v1_SylkField_proto_init() }
func file_sylk_SylkField_v1_SylkField_proto_init() {
	if File_sylk_SylkField_v1_SylkField_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_sylk_SylkField_v1_SylkField_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SylkFieldDisplay); i {
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
		file_sylk_SylkField_v1_SylkField_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SylkField); i {
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
		file_sylk_SylkField_v1_SylkField_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*SylkOneOfField); i {
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
			RawDescriptor: file_sylk_SylkField_v1_SylkField_proto_rawDesc,
			NumEnums:      2,
			NumMessages:   4,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_sylk_SylkField_v1_SylkField_proto_goTypes,
		DependencyIndexes: file_sylk_SylkField_v1_SylkField_proto_depIdxs,
		EnumInfos:         file_sylk_SylkField_v1_SylkField_proto_enumTypes,
		MessageInfos:      file_sylk_SylkField_v1_SylkField_proto_msgTypes,
	}.Build()
	File_sylk_SylkField_v1_SylkField_proto = out.File
	file_sylk_SylkField_v1_SylkField_proto_rawDesc = nil
	file_sylk_SylkField_v1_SylkField_proto_goTypes = nil
	file_sylk_SylkField_v1_SylkField_proto_depIdxs = nil
}
