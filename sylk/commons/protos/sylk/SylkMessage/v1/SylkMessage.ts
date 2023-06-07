/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { Struct } from "../../../google/protobuf/struct";
import { Timestamp } from "../../../google/protobuf/timestamp";
import { SylkExtensions, sylkExtensionsFromJSON, sylkExtensionsToJSON } from "../../SylkCommons/v1/SylkCommons";
import { SylkField } from "../../SylkField/v1/SylkField";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkMessage.v1.SylkMessageDisplay] - None */
export interface SylkMessageDisplay {
  updatedAt?: Date;
  message?: SylkMessage;
  createdAt?: Date;
}

/** [sylk.SylkMessage.v1.SylkMessage] - None */
export interface SylkMessage {
  extensionType: SylkExtensions;
  name: string;
  uri: string;
  extensions: { [key: string]: { [key: string]: any } };
  fullName: string;
  type: string;
  description: string;
  kind: string;
  fields: SylkField[];
}

export interface SylkMessage_ExtensionsEntry {
  key: string;
  value?: { [key: string]: any };
}

function createBaseSylkMessageDisplay(): SylkMessageDisplay {
  return { updatedAt: undefined, message: undefined, createdAt: undefined };
}

export const SylkMessageDisplay = {
  encode(message: SylkMessageDisplay, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.updatedAt !== undefined) {
      Timestamp.encode(toTimestamp(message.updatedAt), writer.uint32(26).fork()).ldelim();
    }
    if (message.message !== undefined) {
      SylkMessage.encode(message.message, writer.uint32(10).fork()).ldelim();
    }
    if (message.createdAt !== undefined) {
      Timestamp.encode(toTimestamp(message.createdAt), writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkMessageDisplay {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkMessageDisplay();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updatedAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.message = SylkMessage.decode(reader, reader.uint32());
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.createdAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkMessageDisplay {
    return {
      updatedAt: isSet(object.updatedAt) ? fromJsonTimestamp(object.updatedAt) : undefined,
      message: isSet(object.message) ? SylkMessage.fromJSON(object.message) : undefined,
      createdAt: isSet(object.createdAt) ? fromJsonTimestamp(object.createdAt) : undefined,
    };
  },

  toJSON(message: SylkMessageDisplay): unknown {
    const obj: any = {};
    message.updatedAt !== undefined && (obj.updatedAt = message.updatedAt.toISOString());
    message.message !== undefined && (obj.message = message.message ? SylkMessage.toJSON(message.message) : undefined);
    message.createdAt !== undefined && (obj.createdAt = message.createdAt.toISOString());
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkMessageDisplay>, I>>(base?: I): SylkMessageDisplay {
    return SylkMessageDisplay.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkMessageDisplay>, I>>(object: I): SylkMessageDisplay {
    const message = createBaseSylkMessageDisplay();
    message.updatedAt = object.updatedAt ?? undefined;
    message.message = (object.message !== undefined && object.message !== null)
      ? SylkMessage.fromPartial(object.message)
      : undefined;
    message.createdAt = object.createdAt ?? undefined;
    return message;
  },
};

function createBaseSylkMessage(): SylkMessage {
  return {
    extensionType: 0,
    name: "",
    uri: "",
    extensions: {},
    fullName: "",
    type: "",
    description: "",
    kind: "",
    fields: [],
  };
}

export const SylkMessage = {
  encode(message: SylkMessage, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.extensionType !== 0) {
      writer.uint32(72).int32(message.extensionType);
    }
    if (message.name !== "") {
      writer.uint32(18).string(message.name);
    }
    if (message.uri !== "") {
      writer.uint32(10).string(message.uri);
    }
    Object.entries(message.extensions).forEach(([key, value]) => {
      if (value !== undefined) {
        SylkMessage_ExtensionsEntry.encode({ key: key as any, value }, writer.uint32(66).fork()).ldelim();
      }
    });
    if (message.fullName !== "") {
      writer.uint32(26).string(message.fullName);
    }
    if (message.type !== "") {
      writer.uint32(50).string(message.type);
    }
    if (message.description !== "") {
      writer.uint32(34).string(message.description);
    }
    if (message.kind !== "") {
      writer.uint32(58).string(message.kind);
    }
    for (const v of message.fields) {
      SylkField.encode(v!, writer.uint32(42).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkMessage {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkMessage();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 9:
          if (tag !== 72) {
            break;
          }

          message.extensionType = reader.int32() as any;
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.name = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.uri = reader.string();
          continue;
        case 8:
          if (tag !== 66) {
            break;
          }

          const entry8 = SylkMessage_ExtensionsEntry.decode(reader, reader.uint32());
          if (entry8.value !== undefined) {
            message.extensions[entry8.key] = entry8.value;
          }
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.fullName = reader.string();
          continue;
        case 6:
          if (tag !== 50) {
            break;
          }

          message.type = reader.string();
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.description = reader.string();
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.kind = reader.string();
          continue;
        case 5:
          if (tag !== 42) {
            break;
          }

          message.fields.push(SylkField.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkMessage {
    return {
      extensionType: isSet(object.extensionType) ? sylkExtensionsFromJSON(object.extensionType) : 0,
      name: isSet(object.name) ? String(object.name) : "",
      uri: isSet(object.uri) ? String(object.uri) : "",
      extensions: isObject(object.extensions)
        ? Object.entries(object.extensions).reduce<{ [key: string]: { [key: string]: any } }>((acc, [key, value]) => {
          acc[key] = value as { [key: string]: any };
          return acc;
        }, {})
        : {},
      fullName: isSet(object.fullName) ? String(object.fullName) : "",
      type: isSet(object.type) ? String(object.type) : "",
      description: isSet(object.description) ? String(object.description) : "",
      kind: isSet(object.kind) ? String(object.kind) : "",
      fields: Array.isArray(object?.fields) ? object.fields.map((e: any) => SylkField.fromJSON(e)) : [],
    };
  },

  toJSON(message: SylkMessage): unknown {
    const obj: any = {};
    message.extensionType !== undefined && (obj.extensionType = sylkExtensionsToJSON(message.extensionType));
    message.name !== undefined && (obj.name = message.name);
    message.uri !== undefined && (obj.uri = message.uri);
    obj.extensions = {};
    if (message.extensions) {
      Object.entries(message.extensions).forEach(([k, v]) => {
        obj.extensions[k] = v;
      });
    }
    message.fullName !== undefined && (obj.fullName = message.fullName);
    message.type !== undefined && (obj.type = message.type);
    message.description !== undefined && (obj.description = message.description);
    message.kind !== undefined && (obj.kind = message.kind);
    if (message.fields) {
      obj.fields = message.fields.map((e) => e ? SylkField.toJSON(e) : undefined);
    } else {
      obj.fields = [];
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkMessage>, I>>(base?: I): SylkMessage {
    return SylkMessage.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkMessage>, I>>(object: I): SylkMessage {
    const message = createBaseSylkMessage();
    message.extensionType = object.extensionType ?? 0;
    message.name = object.name ?? "";
    message.uri = object.uri ?? "";
    message.extensions = Object.entries(object.extensions ?? {}).reduce<{ [key: string]: { [key: string]: any } }>(
      (acc, [key, value]) => {
        if (value !== undefined) {
          acc[key] = value;
        }
        return acc;
      },
      {},
    );
    message.fullName = object.fullName ?? "";
    message.type = object.type ?? "";
    message.description = object.description ?? "";
    message.kind = object.kind ?? "";
    message.fields = object.fields?.map((e) => SylkField.fromPartial(e)) || [];
    return message;
  },
};

function createBaseSylkMessage_ExtensionsEntry(): SylkMessage_ExtensionsEntry {
  return { key: "", value: undefined };
}

export const SylkMessage_ExtensionsEntry = {
  encode(message: SylkMessage_ExtensionsEntry, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.key !== "") {
      writer.uint32(10).string(message.key);
    }
    if (message.value !== undefined) {
      Struct.encode(Struct.wrap(message.value), writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkMessage_ExtensionsEntry {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkMessage_ExtensionsEntry();
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

  fromJSON(object: any): SylkMessage_ExtensionsEntry {
    return {
      key: isSet(object.key) ? String(object.key) : "",
      value: isObject(object.value) ? object.value : undefined,
    };
  },

  toJSON(message: SylkMessage_ExtensionsEntry): unknown {
    const obj: any = {};
    message.key !== undefined && (obj.key = message.key);
    message.value !== undefined && (obj.value = message.value);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkMessage_ExtensionsEntry>, I>>(base?: I): SylkMessage_ExtensionsEntry {
    return SylkMessage_ExtensionsEntry.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkMessage_ExtensionsEntry>, I>>(object: I): SylkMessage_ExtensionsEntry {
    const message = createBaseSylkMessage_ExtensionsEntry();
    message.key = object.key ?? "";
    message.value = object.value ?? undefined;
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
