/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { Struct } from "../../../google/protobuf/struct";
import { Timestamp } from "../../../google/protobuf/timestamp";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkField.v1.SylkFieldTypes] - None */
export enum SylkFieldTypes {
  /** DEFAULT_SYLKFIELDTYPES - [sylk.SylkField.v1.SylkFieldTypes] - Default enum value for "sylk.SylkField.v1.SylkFieldTypes" */
  DEFAULT_SYLKFIELDTYPES = 0,
  /** TYPE_DOUBLE - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_DOUBLE = 1,
  /** TYPE_FLOAT - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_FLOAT = 2,
  /** TYPE_INT64 - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_INT64 = 3,
  /** TYPE_UINT64 - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_UINT64 = 4,
  /** TYPE_INT32 - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_INT32 = 5,
  /** TYPE_FIXED64 - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_FIXED64 = 6,
  /** TYPE_FIXED32 - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_FIXED32 = 7,
  /** TYPE_BOOL - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_BOOL = 8,
  /** TYPE_STRING - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_STRING = 9,
  /** TYPE_GROUP - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_GROUP = 10,
  /** TYPE_MESSAGE - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_MESSAGE = 11,
  /** TYPE_BYTES - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_BYTES = 12,
  /** TYPE_UINT32 - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_UINT32 = 13,
  /** TYPE_ENUM - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_ENUM = 14,
  /** TYPE_SFIXED32 - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_SFIXED32 = 15,
  /** TYPE_SFIXED64 - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_SFIXED64 = 16,
  /** TYPE_SINT32 - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_SINT32 = 17,
  /** TYPE_SINT64 - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_SINT64 = 18,
  /** TYPE_MAP - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_MAP = 19,
  /** TYPE_ONEOF - [sylk.SylkField.v1.SylkFieldTypes] - None */
  TYPE_ONEOF = 20,
  UNRECOGNIZED = -1,
}

export function sylkFieldTypesFromJSON(object: any): SylkFieldTypes {
  switch (object) {
    case 0:
    case "DEFAULT_SYLKFIELDTYPES":
      return SylkFieldTypes.DEFAULT_SYLKFIELDTYPES;
    case 1:
    case "TYPE_DOUBLE":
      return SylkFieldTypes.TYPE_DOUBLE;
    case 2:
    case "TYPE_FLOAT":
      return SylkFieldTypes.TYPE_FLOAT;
    case 3:
    case "TYPE_INT64":
      return SylkFieldTypes.TYPE_INT64;
    case 4:
    case "TYPE_UINT64":
      return SylkFieldTypes.TYPE_UINT64;
    case 5:
    case "TYPE_INT32":
      return SylkFieldTypes.TYPE_INT32;
    case 6:
    case "TYPE_FIXED64":
      return SylkFieldTypes.TYPE_FIXED64;
    case 7:
    case "TYPE_FIXED32":
      return SylkFieldTypes.TYPE_FIXED32;
    case 8:
    case "TYPE_BOOL":
      return SylkFieldTypes.TYPE_BOOL;
    case 9:
    case "TYPE_STRING":
      return SylkFieldTypes.TYPE_STRING;
    case 10:
    case "TYPE_GROUP":
      return SylkFieldTypes.TYPE_GROUP;
    case 11:
    case "TYPE_MESSAGE":
      return SylkFieldTypes.TYPE_MESSAGE;
    case 12:
    case "TYPE_BYTES":
      return SylkFieldTypes.TYPE_BYTES;
    case 13:
    case "TYPE_UINT32":
      return SylkFieldTypes.TYPE_UINT32;
    case 14:
    case "TYPE_ENUM":
      return SylkFieldTypes.TYPE_ENUM;
    case 15:
    case "TYPE_SFIXED32":
      return SylkFieldTypes.TYPE_SFIXED32;
    case 16:
    case "TYPE_SFIXED64":
      return SylkFieldTypes.TYPE_SFIXED64;
    case 17:
    case "TYPE_SINT32":
      return SylkFieldTypes.TYPE_SINT32;
    case 18:
    case "TYPE_SINT64":
      return SylkFieldTypes.TYPE_SINT64;
    case 19:
    case "TYPE_MAP":
      return SylkFieldTypes.TYPE_MAP;
    case 20:
    case "TYPE_ONEOF":
      return SylkFieldTypes.TYPE_ONEOF;
    case -1:
    case "UNRECOGNIZED":
    default:
      return SylkFieldTypes.UNRECOGNIZED;
  }
}

export function sylkFieldTypesToJSON(object: SylkFieldTypes): string {
  switch (object) {
    case SylkFieldTypes.DEFAULT_SYLKFIELDTYPES:
      return "DEFAULT_SYLKFIELDTYPES";
    case SylkFieldTypes.TYPE_DOUBLE:
      return "TYPE_DOUBLE";
    case SylkFieldTypes.TYPE_FLOAT:
      return "TYPE_FLOAT";
    case SylkFieldTypes.TYPE_INT64:
      return "TYPE_INT64";
    case SylkFieldTypes.TYPE_UINT64:
      return "TYPE_UINT64";
    case SylkFieldTypes.TYPE_INT32:
      return "TYPE_INT32";
    case SylkFieldTypes.TYPE_FIXED64:
      return "TYPE_FIXED64";
    case SylkFieldTypes.TYPE_FIXED32:
      return "TYPE_FIXED32";
    case SylkFieldTypes.TYPE_BOOL:
      return "TYPE_BOOL";
    case SylkFieldTypes.TYPE_STRING:
      return "TYPE_STRING";
    case SylkFieldTypes.TYPE_GROUP:
      return "TYPE_GROUP";
    case SylkFieldTypes.TYPE_MESSAGE:
      return "TYPE_MESSAGE";
    case SylkFieldTypes.TYPE_BYTES:
      return "TYPE_BYTES";
    case SylkFieldTypes.TYPE_UINT32:
      return "TYPE_UINT32";
    case SylkFieldTypes.TYPE_ENUM:
      return "TYPE_ENUM";
    case SylkFieldTypes.TYPE_SFIXED32:
      return "TYPE_SFIXED32";
    case SylkFieldTypes.TYPE_SFIXED64:
      return "TYPE_SFIXED64";
    case SylkFieldTypes.TYPE_SINT32:
      return "TYPE_SINT32";
    case SylkFieldTypes.TYPE_SINT64:
      return "TYPE_SINT64";
    case SylkFieldTypes.TYPE_MAP:
      return "TYPE_MAP";
    case SylkFieldTypes.TYPE_ONEOF:
      return "TYPE_ONEOF";
    case SylkFieldTypes.UNRECOGNIZED:
    default:
      return "UNRECOGNIZED";
  }
}

/** [sylk.SylkField.v1.SylkFieldLabels] - None */
export enum SylkFieldLabels {
  /** DEFAULT_SYLKFIELDLABELS - [sylk.SylkField.v1.SylkFieldLabels] - Default enum value for "sylk.SylkField.v1.SylkFieldLabels" */
  DEFAULT_SYLKFIELDLABELS = 0,
  /** LABEL_OPTIONAL - [sylk.SylkField.v1.SylkFieldLabels] - None */
  LABEL_OPTIONAL = 1,
  /** LABEL_REQUIRED - [sylk.SylkField.v1.SylkFieldLabels] - None */
  LABEL_REQUIRED = 2,
  /** LABEL_REPEATED - [sylk.SylkField.v1.SylkFieldLabels] - None */
  LABEL_REPEATED = 3,
  UNRECOGNIZED = -1,
}

export function sylkFieldLabelsFromJSON(object: any): SylkFieldLabels {
  switch (object) {
    case 0:
    case "DEFAULT_SYLKFIELDLABELS":
      return SylkFieldLabels.DEFAULT_SYLKFIELDLABELS;
    case 1:
    case "LABEL_OPTIONAL":
      return SylkFieldLabels.LABEL_OPTIONAL;
    case 2:
    case "LABEL_REQUIRED":
      return SylkFieldLabels.LABEL_REQUIRED;
    case 3:
    case "LABEL_REPEATED":
      return SylkFieldLabels.LABEL_REPEATED;
    case -1:
    case "UNRECOGNIZED":
    default:
      return SylkFieldLabels.UNRECOGNIZED;
  }
}

export function sylkFieldLabelsToJSON(object: SylkFieldLabels): string {
  switch (object) {
    case SylkFieldLabels.DEFAULT_SYLKFIELDLABELS:
      return "DEFAULT_SYLKFIELDLABELS";
    case SylkFieldLabels.LABEL_OPTIONAL:
      return "LABEL_OPTIONAL";
    case SylkFieldLabels.LABEL_REQUIRED:
      return "LABEL_REQUIRED";
    case SylkFieldLabels.LABEL_REPEATED:
      return "LABEL_REPEATED";
    case SylkFieldLabels.UNRECOGNIZED:
    default:
      return "UNRECOGNIZED";
  }
}

/** [sylk.SylkField.v1.SylkFieldDisplay] - None */
export interface SylkFieldDisplay {
  createdAt?: Date;
  field?: SylkField;
  updatedAt?: Date;
}

/** [sylk.SylkField.v1.SylkField] - None */
export interface SylkField {
  type: string;
  uri: string;
  oneofFields: SylkOneOfField[];
  name: string;
  description: string;
  enumType: string;
  fieldType: SylkFieldTypes;
  messageType: string;
  kind: string;
  fullName: string;
  extensions: { [key: string]: { [key: string]: any } };
  index: number;
  label: SylkFieldLabels;
  keyType: SylkFieldTypes;
  valueType: SylkFieldTypes;
}

export interface SylkField_ExtensionsEntry {
  key: string;
  value?: { [key: string]: any };
}

/** [sylk.SylkField.v1.SylkOneOfField] - None */
export interface SylkOneOfField {
  enumType: string;
  fullName: string;
  uri: string;
  messageType: string;
  fieldType: SylkFieldTypes;
  name: string;
  description: string;
  label: SylkFieldLabels;
}

function createBaseSylkFieldDisplay(): SylkFieldDisplay {
  return { createdAt: undefined, field: undefined, updatedAt: undefined };
}

export const SylkFieldDisplay = {
  encode(message: SylkFieldDisplay, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.createdAt !== undefined) {
      Timestamp.encode(toTimestamp(message.createdAt), writer.uint32(18).fork()).ldelim();
    }
    if (message.field !== undefined) {
      SylkField.encode(message.field, writer.uint32(10).fork()).ldelim();
    }
    if (message.updatedAt !== undefined) {
      Timestamp.encode(toTimestamp(message.updatedAt), writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkFieldDisplay {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkFieldDisplay();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.createdAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.field = SylkField.decode(reader, reader.uint32());
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updatedAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkFieldDisplay {
    return {
      createdAt: isSet(object.createdAt) ? fromJsonTimestamp(object.createdAt) : undefined,
      field: isSet(object.field) ? SylkField.fromJSON(object.field) : undefined,
      updatedAt: isSet(object.updatedAt) ? fromJsonTimestamp(object.updatedAt) : undefined,
    };
  },

  toJSON(message: SylkFieldDisplay): unknown {
    const obj: any = {};
    message.createdAt !== undefined && (obj.createdAt = message.createdAt.toISOString());
    message.field !== undefined && (obj.field = message.field ? SylkField.toJSON(message.field) : undefined);
    message.updatedAt !== undefined && (obj.updatedAt = message.updatedAt.toISOString());
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkFieldDisplay>, I>>(base?: I): SylkFieldDisplay {
    return SylkFieldDisplay.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkFieldDisplay>, I>>(object: I): SylkFieldDisplay {
    const message = createBaseSylkFieldDisplay();
    message.createdAt = object.createdAt ?? undefined;
    message.field = (object.field !== undefined && object.field !== null)
      ? SylkField.fromPartial(object.field)
      : undefined;
    message.updatedAt = object.updatedAt ?? undefined;
    return message;
  },
};

function createBaseSylkField(): SylkField {
  return {
    type: "",
    uri: "",
    oneofFields: [],
    name: "",
    description: "",
    enumType: "",
    fieldType: 0,
    messageType: "",
    kind: "",
    fullName: "",
    extensions: {},
    index: 0,
    label: 0,
    keyType: 0,
    valueType: 0,
  };
}

export const SylkField = {
  encode(message: SylkField, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.type !== "") {
      writer.uint32(90).string(message.type);
    }
    if (message.uri !== "") {
      writer.uint32(10).string(message.uri);
    }
    for (const v of message.oneofFields) {
      SylkOneOfField.encode(v!, writer.uint32(122).fork()).ldelim();
    }
    if (message.name !== "") {
      writer.uint32(18).string(message.name);
    }
    if (message.description !== "") {
      writer.uint32(34).string(message.description);
    }
    if (message.enumType !== "") {
      writer.uint32(82).string(message.enumType);
    }
    if (message.fieldType !== 0) {
      writer.uint32(40).int32(message.fieldType);
    }
    if (message.messageType !== "") {
      writer.uint32(74).string(message.messageType);
    }
    if (message.kind !== "") {
      writer.uint32(98).string(message.kind);
    }
    if (message.fullName !== "") {
      writer.uint32(26).string(message.fullName);
    }
    Object.entries(message.extensions).forEach(([key, value]) => {
      if (value !== undefined) {
        SylkField_ExtensionsEntry.encode({ key: key as any, value }, writer.uint32(114).fork()).ldelim();
      }
    });
    if (message.index !== 0) {
      writer.uint32(104).int32(message.index);
    }
    if (message.label !== 0) {
      writer.uint32(48).int32(message.label);
    }
    if (message.keyType !== 0) {
      writer.uint32(56).int32(message.keyType);
    }
    if (message.valueType !== 0) {
      writer.uint32(64).int32(message.valueType);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkField {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkField();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 11:
          if (tag !== 90) {
            break;
          }

          message.type = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.uri = reader.string();
          continue;
        case 15:
          if (tag !== 122) {
            break;
          }

          message.oneofFields.push(SylkOneOfField.decode(reader, reader.uint32()));
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.name = reader.string();
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.description = reader.string();
          continue;
        case 10:
          if (tag !== 82) {
            break;
          }

          message.enumType = reader.string();
          continue;
        case 5:
          if (tag !== 40) {
            break;
          }

          message.fieldType = reader.int32() as any;
          continue;
        case 9:
          if (tag !== 74) {
            break;
          }

          message.messageType = reader.string();
          continue;
        case 12:
          if (tag !== 98) {
            break;
          }

          message.kind = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.fullName = reader.string();
          continue;
        case 14:
          if (tag !== 114) {
            break;
          }

          const entry14 = SylkField_ExtensionsEntry.decode(reader, reader.uint32());
          if (entry14.value !== undefined) {
            message.extensions[entry14.key] = entry14.value;
          }
          continue;
        case 13:
          if (tag !== 104) {
            break;
          }

          message.index = reader.int32();
          continue;
        case 6:
          if (tag !== 48) {
            break;
          }

          message.label = reader.int32() as any;
          continue;
        case 7:
          if (tag !== 56) {
            break;
          }

          message.keyType = reader.int32() as any;
          continue;
        case 8:
          if (tag !== 64) {
            break;
          }

          message.valueType = reader.int32() as any;
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkField {
    return {
      type: isSet(object.type) ? String(object.type) : "",
      uri: isSet(object.uri) ? String(object.uri) : "",
      oneofFields: Array.isArray(object?.oneofFields)
        ? object.oneofFields.map((e: any) => SylkOneOfField.fromJSON(e))
        : [],
      name: isSet(object.name) ? String(object.name) : "",
      description: isSet(object.description) ? String(object.description) : "",
      enumType: isSet(object.enumType) ? String(object.enumType) : "",
      fieldType: isSet(object.fieldType) ? sylkFieldTypesFromJSON(object.fieldType) : 0,
      messageType: isSet(object.messageType) ? String(object.messageType) : "",
      kind: isSet(object.kind) ? String(object.kind) : "",
      fullName: isSet(object.fullName) ? String(object.fullName) : "",
      extensions: isObject(object.extensions)
        ? Object.entries(object.extensions).reduce<{ [key: string]: { [key: string]: any } }>((acc, [key, value]) => {
          acc[key] = value as { [key: string]: any };
          return acc;
        }, {})
        : {},
      index: isSet(object.index) ? Number(object.index) : 0,
      label: isSet(object.label) ? sylkFieldLabelsFromJSON(object.label) : 0,
      keyType: isSet(object.keyType) ? sylkFieldTypesFromJSON(object.keyType) : 0,
      valueType: isSet(object.valueType) ? sylkFieldTypesFromJSON(object.valueType) : 0,
    };
  },

  toJSON(message: SylkField): unknown {
    const obj: any = {};
    message.type !== undefined && (obj.type = message.type);
    message.uri !== undefined && (obj.uri = message.uri);
    if (message.oneofFields) {
      obj.oneofFields = message.oneofFields.map((e) => e ? SylkOneOfField.toJSON(e) : undefined);
    } else {
      obj.oneofFields = [];
    }
    message.name !== undefined && (obj.name = message.name);
    message.description !== undefined && (obj.description = message.description);
    message.enumType !== undefined && (obj.enumType = message.enumType);
    message.fieldType !== undefined && (obj.fieldType = sylkFieldTypesToJSON(message.fieldType));
    message.messageType !== undefined && (obj.messageType = message.messageType);
    message.kind !== undefined && (obj.kind = message.kind);
    message.fullName !== undefined && (obj.fullName = message.fullName);
    obj.extensions = {};
    if (message.extensions) {
      Object.entries(message.extensions).forEach(([k, v]) => {
        obj.extensions[k] = v;
      });
    }
    message.index !== undefined && (obj.index = Math.round(message.index));
    message.label !== undefined && (obj.label = sylkFieldLabelsToJSON(message.label));
    message.keyType !== undefined && (obj.keyType = sylkFieldTypesToJSON(message.keyType));
    message.valueType !== undefined && (obj.valueType = sylkFieldTypesToJSON(message.valueType));
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkField>, I>>(base?: I): SylkField {
    return SylkField.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkField>, I>>(object: I): SylkField {
    const message = createBaseSylkField();
    message.type = object.type ?? "";
    message.uri = object.uri ?? "";
    message.oneofFields = object.oneofFields?.map((e) => SylkOneOfField.fromPartial(e)) || [];
    message.name = object.name ?? "";
    message.description = object.description ?? "";
    message.enumType = object.enumType ?? "";
    message.fieldType = object.fieldType ?? 0;
    message.messageType = object.messageType ?? "";
    message.kind = object.kind ?? "";
    message.fullName = object.fullName ?? "";
    message.extensions = Object.entries(object.extensions ?? {}).reduce<{ [key: string]: { [key: string]: any } }>(
      (acc, [key, value]) => {
        if (value !== undefined) {
          acc[key] = value;
        }
        return acc;
      },
      {},
    );
    message.index = object.index ?? 0;
    message.label = object.label ?? 0;
    message.keyType = object.keyType ?? 0;
    message.valueType = object.valueType ?? 0;
    return message;
  },
};

function createBaseSylkField_ExtensionsEntry(): SylkField_ExtensionsEntry {
  return { key: "", value: undefined };
}

export const SylkField_ExtensionsEntry = {
  encode(message: SylkField_ExtensionsEntry, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.key !== "") {
      writer.uint32(10).string(message.key);
    }
    if (message.value !== undefined) {
      Struct.encode(Struct.wrap(message.value), writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkField_ExtensionsEntry {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkField_ExtensionsEntry();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.key = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.value = Struct.unwrap(Struct.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkField_ExtensionsEntry {
    return {
      key: isSet(object.key) ? String(object.key) : "",
      value: isObject(object.value) ? object.value : undefined,
    };
  },

  toJSON(message: SylkField_ExtensionsEntry): unknown {
    const obj: any = {};
    message.key !== undefined && (obj.key = message.key);
    message.value !== undefined && (obj.value = message.value);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkField_ExtensionsEntry>, I>>(base?: I): SylkField_ExtensionsEntry {
    return SylkField_ExtensionsEntry.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkField_ExtensionsEntry>, I>>(object: I): SylkField_ExtensionsEntry {
    const message = createBaseSylkField_ExtensionsEntry();
    message.key = object.key ?? "";
    message.value = object.value ?? undefined;
    return message;
  },
};

function createBaseSylkOneOfField(): SylkOneOfField {
  return { enumType: "", fullName: "", uri: "", messageType: "", fieldType: 0, name: "", description: "", label: 0 };
}

export const SylkOneOfField = {
  encode(message: SylkOneOfField, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.enumType !== "") {
      writer.uint32(66).string(message.enumType);
    }
    if (message.fullName !== "") {
      writer.uint32(26).string(message.fullName);
    }
    if (message.uri !== "") {
      writer.uint32(10).string(message.uri);
    }
    if (message.messageType !== "") {
      writer.uint32(58).string(message.messageType);
    }
    if (message.fieldType !== 0) {
      writer.uint32(40).int32(message.fieldType);
    }
    if (message.name !== "") {
      writer.uint32(18).string(message.name);
    }
    if (message.description !== "") {
      writer.uint32(34).string(message.description);
    }
    if (message.label !== 0) {
      writer.uint32(48).int32(message.label);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkOneOfField {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkOneOfField();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 8:
          if (tag !== 66) {
            break;
          }

          message.enumType = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.fullName = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.uri = reader.string();
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.messageType = reader.string();
          continue;
        case 5:
          if (tag !== 40) {
            break;
          }

          message.fieldType = reader.int32() as any;
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.name = reader.string();
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.description = reader.string();
          continue;
        case 6:
          if (tag !== 48) {
            break;
          }

          message.label = reader.int32() as any;
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkOneOfField {
    return {
      enumType: isSet(object.enumType) ? String(object.enumType) : "",
      fullName: isSet(object.fullName) ? String(object.fullName) : "",
      uri: isSet(object.uri) ? String(object.uri) : "",
      messageType: isSet(object.messageType) ? String(object.messageType) : "",
      fieldType: isSet(object.fieldType) ? sylkFieldTypesFromJSON(object.fieldType) : 0,
      name: isSet(object.name) ? String(object.name) : "",
      description: isSet(object.description) ? String(object.description) : "",
      label: isSet(object.label) ? sylkFieldLabelsFromJSON(object.label) : 0,
    };
  },

  toJSON(message: SylkOneOfField): unknown {
    const obj: any = {};
    message.enumType !== undefined && (obj.enumType = message.enumType);
    message.fullName !== undefined && (obj.fullName = message.fullName);
    message.uri !== undefined && (obj.uri = message.uri);
    message.messageType !== undefined && (obj.messageType = message.messageType);
    message.fieldType !== undefined && (obj.fieldType = sylkFieldTypesToJSON(message.fieldType));
    message.name !== undefined && (obj.name = message.name);
    message.description !== undefined && (obj.description = message.description);
    message.label !== undefined && (obj.label = sylkFieldLabelsToJSON(message.label));
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkOneOfField>, I>>(base?: I): SylkOneOfField {
    return SylkOneOfField.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkOneOfField>, I>>(object: I): SylkOneOfField {
    const message = createBaseSylkOneOfField();
    message.enumType = object.enumType ?? "";
    message.fullName = object.fullName ?? "";
    message.uri = object.uri ?? "";
    message.messageType = object.messageType ?? "";
    message.fieldType = object.fieldType ?? 0;
    message.name = object.name ?? "";
    message.description = object.description ?? "";
    message.label = object.label ?? 0;
    return message;
  },
};

type Builtin = Date | Function | Uint8Array | string | number | boolean | undefined;

type DeepPartial<T> = T extends Builtin ? T
  : T extends Array<infer U> ? Array<DeepPartial<U>> : T extends ReadonlyArray<infer U> ? ReadonlyArray<DeepPartial<U>>
  : T extends {} ? { [K in keyof T]?: DeepPartial<T[K]> }
  : Partial<T>;

type KeysOfUnion<T> = T extends T ? keyof T : never;
type Exact<P, I extends P> = P extends Builtin ? P
  : P & { [K in keyof P]: Exact<P[K], I[K]> } & { [K in Exclude<keyof I, KeysOfUnion<P>>]: never };

function toTimestamp(date: Date): Timestamp {
  const seconds = date.getTime() / 1_000;
  const nanos = (date.getTime() % 1_000) * 1_000_000;
  return { seconds, nanos };
}

function fromTimestamp(t: Timestamp): Date {
  let millis = (t.seconds || 0) * 1_000;
  millis += (t.nanos || 0) / 1_000_000;
  return new Date(millis);
}

function fromJsonTimestamp(o: any): Date {
  if (o instanceof Date) {
    return o;
  } else if (typeof o === "string") {
    return new Date(o);
  } else {
    return fromTimestamp(Timestamp.fromJSON(o));
  }
}

function isObject(value: any): boolean {
  return typeof value === "object" && value !== null;
}

function isSet(value: any): boolean {
  return value !== null && value !== undefined;
}
