/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { Struct } from "../../../google/protobuf/struct";
import { Timestamp } from "../../../google/protobuf/timestamp";
import { SylkEnum } from "../../SylkEnum/v1/SylkEnum";
import { SylkMessage } from "../../SylkMessage/v1/SylkMessage";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkPackage.v1.SylkPackageDisplay] - None */
export interface SylkPackageDisplay {
  package?: SylkPackage;
  createdAt?: Date;
  updatedAt?: Date;
}

/** [sylk.SylkPackage.v1.SylkPackage] - None */
export interface SylkPackage {
  messages: SylkMessage[];
  extensions: { [key: string]: { [key: string]: any } };
  type: string;
  description: string;
  enums: SylkEnum[];
  package: string;
  dependencies: string[];
  name: string;
  uri: string;
}

export interface SylkPackage_ExtensionsEntry {
  key: string;
  value?: { [key: string]: any };
}

function createBaseSylkPackageDisplay(): SylkPackageDisplay {
  return { package: undefined, createdAt: undefined, updatedAt: undefined };
}

export const SylkPackageDisplay = {
  encode(message: SylkPackageDisplay, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.package !== undefined) {
      SylkPackage.encode(message.package, writer.uint32(10).fork()).ldelim();
    }
    if (message.createdAt !== undefined) {
      Timestamp.encode(toTimestamp(message.createdAt), writer.uint32(18).fork()).ldelim();
    }
    if (message.updatedAt !== undefined) {
      Timestamp.encode(toTimestamp(message.updatedAt), writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkPackageDisplay {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkPackageDisplay();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.package = SylkPackage.decode(reader, reader.uint32());
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.createdAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
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

  fromJSON(object: any): SylkPackageDisplay {
    return {
      package: isSet(object.package) ? SylkPackage.fromJSON(object.package) : undefined,
      createdAt: isSet(object.createdAt) ? fromJsonTimestamp(object.createdAt) : undefined,
      updatedAt: isSet(object.updatedAt) ? fromJsonTimestamp(object.updatedAt) : undefined,
    };
  },

  toJSON(message: SylkPackageDisplay): unknown {
    const obj: any = {};
    message.package !== undefined && (obj.package = message.package ? SylkPackage.toJSON(message.package) : undefined);
    message.createdAt !== undefined && (obj.createdAt = message.createdAt.toISOString());
    message.updatedAt !== undefined && (obj.updatedAt = message.updatedAt.toISOString());
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkPackageDisplay>, I>>(base?: I): SylkPackageDisplay {
    return SylkPackageDisplay.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkPackageDisplay>, I>>(object: I): SylkPackageDisplay {
    const message = createBaseSylkPackageDisplay();
    message.package = (object.package !== undefined && object.package !== null)
      ? SylkPackage.fromPartial(object.package)
      : undefined;
    message.createdAt = object.createdAt ?? undefined;
    message.updatedAt = object.updatedAt ?? undefined;
    return message;
  },
};

function createBaseSylkPackage(): SylkPackage {
  return {
    messages: [],
    extensions: {},
    type: "",
    description: "",
    enums: [],
    package: "",
    dependencies: [],
    name: "",
    uri: "",
  };
}

export const SylkPackage = {
  encode(message: SylkPackage, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    for (const v of message.messages) {
      SylkMessage.encode(v!, writer.uint32(34).fork()).ldelim();
    }
    Object.entries(message.extensions).forEach(([key, value]) => {
      if (value !== undefined) {
        SylkPackage_ExtensionsEntry.encode({ key: key as any, value }, writer.uint32(74).fork()).ldelim();
      }
    });
    if (message.type !== "") {
      writer.uint32(58).string(message.type);
    }
    if (message.description !== "") {
      writer.uint32(50).string(message.description);
    }
    for (const v of message.enums) {
      SylkEnum.encode(v!, writer.uint32(42).fork()).ldelim();
    }
    if (message.package !== "") {
      writer.uint32(26).string(message.package);
    }
    for (const v of message.dependencies) {
      writer.uint32(66).string(v!);
    }
    if (message.name !== "") {
      writer.uint32(18).string(message.name);
    }
    if (message.uri !== "") {
      writer.uint32(10).string(message.uri);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkPackage {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkPackage();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 4:
          if (tag !== 34) {
            break;
          }

          message.messages.push(SylkMessage.decode(reader, reader.uint32()));
          continue;
        case 9:
          if (tag !== 74) {
            break;
          }

          const entry9 = SylkPackage_ExtensionsEntry.decode(reader, reader.uint32());
          if (entry9.value !== undefined) {
            message.extensions[entry9.key] = entry9.value;
          }
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.type = reader.string();
          continue;
        case 6:
          if (tag !== 50) {
            break;
          }

          message.description = reader.string();
          continue;
        case 5:
          if (tag !== 42) {
            break;
          }

          message.enums.push(SylkEnum.decode(reader, reader.uint32()));
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.package = reader.string();
          continue;
        case 8:
          if (tag !== 66) {
            break;
          }

          message.dependencies.push(reader.string());
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
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkPackage {
    return {
      messages: Array.isArray(object?.messages) ? object.messages.map((e: any) => SylkMessage.fromJSON(e)) : [],
      extensions: isObject(object.extensions)
        ? Object.entries(object.extensions).reduce<{ [key: string]: { [key: string]: any } }>((acc, [key, value]) => {
          acc[key] = value as { [key: string]: any };
          return acc;
        }, {})
        : {},
      type: isSet(object.type) ? String(object.type) : "",
      description: isSet(object.description) ? String(object.description) : "",
      enums: Array.isArray(object?.enums) ? object.enums.map((e: any) => SylkEnum.fromJSON(e)) : [],
      package: isSet(object.package) ? String(object.package) : "",
      dependencies: Array.isArray(object?.dependencies) ? object.dependencies.map((e: any) => String(e)) : [],
      name: isSet(object.name) ? String(object.name) : "",
      uri: isSet(object.uri) ? String(object.uri) : "",
    };
  },

  toJSON(message: SylkPackage): unknown {
    const obj: any = {};
    if (message.messages) {
      obj.messages = message.messages.map((e) => e ? SylkMessage.toJSON(e) : undefined);
    } else {
      obj.messages = [];
    }
    obj.extensions = {};
    if (message.extensions) {
      Object.entries(message.extensions).forEach(([k, v]) => {
        obj.extensions[k] = v;
      });
    }
    message.type !== undefined && (obj.type = message.type);
    message.description !== undefined && (obj.description = message.description);
    if (message.enums) {
      obj.enums = message.enums.map((e) => e ? SylkEnum.toJSON(e) : undefined);
    } else {
      obj.enums = [];
    }
    message.package !== undefined && (obj.package = message.package);
    if (message.dependencies) {
      obj.dependencies = message.dependencies.map((e) => e);
    } else {
      obj.dependencies = [];
    }
    message.name !== undefined && (obj.name = message.name);
    message.uri !== undefined && (obj.uri = message.uri);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkPackage>, I>>(base?: I): SylkPackage {
    return SylkPackage.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkPackage>, I>>(object: I): SylkPackage {
    const message = createBaseSylkPackage();
    message.messages = object.messages?.map((e) => SylkMessage.fromPartial(e)) || [];
    message.extensions = Object.entries(object.extensions ?? {}).reduce<{ [key: string]: { [key: string]: any } }>(
      (acc, [key, value]) => {
        if (value !== undefined) {
          acc[key] = value;
        }
        return acc;
      },
      {},
    );
    message.type = object.type ?? "";
    message.description = object.description ?? "";
    message.enums = object.enums?.map((e) => SylkEnum.fromPartial(e)) || [];
    message.package = object.package ?? "";
    message.dependencies = object.dependencies?.map((e) => e) || [];
    message.name = object.name ?? "";
    message.uri = object.uri ?? "";
    return message;
  },
};

function createBaseSylkPackage_ExtensionsEntry(): SylkPackage_ExtensionsEntry {
  return { key: "", value: undefined };
}

export const SylkPackage_ExtensionsEntry = {
  encode(message: SylkPackage_ExtensionsEntry, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.key !== "") {
      writer.uint32(10).string(message.key);
    }
    if (message.value !== undefined) {
      Struct.encode(Struct.wrap(message.value), writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkPackage_ExtensionsEntry {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkPackage_ExtensionsEntry();
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

  fromJSON(object: any): SylkPackage_ExtensionsEntry {
    return {
      key: isSet(object.key) ? String(object.key) : "",
      value: isObject(object.value) ? object.value : undefined,
    };
  },

  toJSON(message: SylkPackage_ExtensionsEntry): unknown {
    const obj: any = {};
    message.key !== undefined && (obj.key = message.key);
    message.value !== undefined && (obj.value = message.value);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkPackage_ExtensionsEntry>, I>>(base?: I): SylkPackage_ExtensionsEntry {
    return SylkPackage_ExtensionsEntry.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkPackage_ExtensionsEntry>, I>>(object: I): SylkPackage_ExtensionsEntry {
    const message = createBaseSylkPackage_ExtensionsEntry();
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
