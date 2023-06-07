/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { Struct } from "../../../google/protobuf/struct";
import { Timestamp } from "../../../google/protobuf/timestamp";
import { SylkMethod } from "../../SylkMethod/v1/SylkMethod";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkService.v1.SylkServiceDisplay] - None */
export interface SylkServiceDisplay {
  updatedAt?: Date;
  service?: SylkService;
  createdAt?: Date;
}

/** [sylk.SylkService.v1.SylkService] - None */
export interface SylkService {
  dependencies: string[];
  description: string;
  uri: string;
  name: string;
  fullName: string;
  type: string;
  methods: SylkMethod[];
  extensions: { [key: string]: { [key: string]: any } };
}

export interface SylkService_ExtensionsEntry {
  key: string;
  value?: { [key: string]: any };
}

function createBaseSylkServiceDisplay(): SylkServiceDisplay {
  return { updatedAt: undefined, service: undefined, createdAt: undefined };
}

export const SylkServiceDisplay = {
  encode(message: SylkServiceDisplay, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.updatedAt !== undefined) {
      Timestamp.encode(toTimestamp(message.updatedAt), writer.uint32(26).fork()).ldelim();
    }
    if (message.service !== undefined) {
      SylkService.encode(message.service, writer.uint32(10).fork()).ldelim();
    }
    if (message.createdAt !== undefined) {
      Timestamp.encode(toTimestamp(message.createdAt), writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkServiceDisplay {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkServiceDisplay();
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

          message.service = SylkService.decode(reader, reader.uint32());
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

  fromJSON(object: any): SylkServiceDisplay {
    return {
      updatedAt: isSet(object.updatedAt) ? fromJsonTimestamp(object.updatedAt) : undefined,
      service: isSet(object.service) ? SylkService.fromJSON(object.service) : undefined,
      createdAt: isSet(object.createdAt) ? fromJsonTimestamp(object.createdAt) : undefined,
    };
  },

  toJSON(message: SylkServiceDisplay): unknown {
    const obj: any = {};
    message.updatedAt !== undefined && (obj.updatedAt = message.updatedAt.toISOString());
    message.service !== undefined && (obj.service = message.service ? SylkService.toJSON(message.service) : undefined);
    message.createdAt !== undefined && (obj.createdAt = message.createdAt.toISOString());
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkServiceDisplay>, I>>(base?: I): SylkServiceDisplay {
    return SylkServiceDisplay.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkServiceDisplay>, I>>(object: I): SylkServiceDisplay {
    const message = createBaseSylkServiceDisplay();
    message.updatedAt = object.updatedAt ?? undefined;
    message.service = (object.service !== undefined && object.service !== null)
      ? SylkService.fromPartial(object.service)
      : undefined;
    message.createdAt = object.createdAt ?? undefined;
    return message;
  },
};

function createBaseSylkService(): SylkService {
  return { dependencies: [], description: "", uri: "", name: "", fullName: "", type: "", methods: [], extensions: {} };
}

export const SylkService = {
  encode(message: SylkService, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    for (const v of message.dependencies) {
      writer.uint32(58).string(v!);
    }
    if (message.description !== "") {
      writer.uint32(34).string(message.description);
    }
    if (message.uri !== "") {
      writer.uint32(10).string(message.uri);
    }
    if (message.name !== "") {
      writer.uint32(18).string(message.name);
    }
    if (message.fullName !== "") {
      writer.uint32(26).string(message.fullName);
    }
    if (message.type !== "") {
      writer.uint32(50).string(message.type);
    }
    for (const v of message.methods) {
      SylkMethod.encode(v!, writer.uint32(42).fork()).ldelim();
    }
    Object.entries(message.extensions).forEach(([key, value]) => {
      if (value !== undefined) {
        SylkService_ExtensionsEntry.encode({ key: key as any, value }, writer.uint32(66).fork()).ldelim();
      }
    });
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkService {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkService();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 7:
          if (tag !== 58) {
            break;
          }

          message.dependencies.push(reader.string());
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.description = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.uri = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.name = reader.string();
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
        case 5:
          if (tag !== 42) {
            break;
          }

          message.methods.push(SylkMethod.decode(reader, reader.uint32()));
          continue;
        case 8:
          if (tag !== 66) {
            break;
          }

          const entry8 = SylkService_ExtensionsEntry.decode(reader, reader.uint32());
          if (entry8.value !== undefined) {
            message.extensions[entry8.key] = entry8.value;
          }
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkService {
    return {
      dependencies: Array.isArray(object?.dependencies) ? object.dependencies.map((e: any) => String(e)) : [],
      description: isSet(object.description) ? String(object.description) : "",
      uri: isSet(object.uri) ? String(object.uri) : "",
      name: isSet(object.name) ? String(object.name) : "",
      fullName: isSet(object.fullName) ? String(object.fullName) : "",
      type: isSet(object.type) ? String(object.type) : "",
      methods: Array.isArray(object?.methods) ? object.methods.map((e: any) => SylkMethod.fromJSON(e)) : [],
      extensions: isObject(object.extensions)
        ? Object.entries(object.extensions).reduce<{ [key: string]: { [key: string]: any } }>((acc, [key, value]) => {
          acc[key] = value as { [key: string]: any };
          return acc;
        }, {})
        : {},
    };
  },

  toJSON(message: SylkService): unknown {
    const obj: any = {};
    if (message.dependencies) {
      obj.dependencies = message.dependencies.map((e) => e);
    } else {
      obj.dependencies = [];
    }
    message.description !== undefined && (obj.description = message.description);
    message.uri !== undefined && (obj.uri = message.uri);
    message.name !== undefined && (obj.name = message.name);
    message.fullName !== undefined && (obj.fullName = message.fullName);
    message.type !== undefined && (obj.type = message.type);
    if (message.methods) {
      obj.methods = message.methods.map((e) => e ? SylkMethod.toJSON(e) : undefined);
    } else {
      obj.methods = [];
    }
    obj.extensions = {};
    if (message.extensions) {
      Object.entries(message.extensions).forEach(([k, v]) => {
        obj.extensions[k] = v;
      });
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkService>, I>>(base?: I): SylkService {
    return SylkService.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkService>, I>>(object: I): SylkService {
    const message = createBaseSylkService();
    message.dependencies = object.dependencies?.map((e) => e) || [];
    message.description = object.description ?? "";
    message.uri = object.uri ?? "";
    message.name = object.name ?? "";
    message.fullName = object.fullName ?? "";
    message.type = object.type ?? "";
    message.methods = object.methods?.map((e) => SylkMethod.fromPartial(e)) || [];
    message.extensions = Object.entries(object.extensions ?? {}).reduce<{ [key: string]: { [key: string]: any } }>(
      (acc, [key, value]) => {
        if (value !== undefined) {
          acc[key] = value;
        }
        return acc;
      },
      {},
    );
    return message;
  },
};

function createBaseSylkService_ExtensionsEntry(): SylkService_ExtensionsEntry {
  return { key: "", value: undefined };
}

export const SylkService_ExtensionsEntry = {
  encode(message: SylkService_ExtensionsEntry, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.key !== "") {
      writer.uint32(10).string(message.key);
    }
    if (message.value !== undefined) {
      Struct.encode(Struct.wrap(message.value), writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkService_ExtensionsEntry {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkService_ExtensionsEntry();
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

  fromJSON(object: any): SylkService_ExtensionsEntry {
    return {
      key: isSet(object.key) ? String(object.key) : "",
      value: isObject(object.value) ? object.value : undefined,
    };
  },

  toJSON(message: SylkService_ExtensionsEntry): unknown {
    const obj: any = {};
    message.key !== undefined && (obj.key = message.key);
    message.value !== undefined && (obj.value = message.value);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkService_ExtensionsEntry>, I>>(base?: I): SylkService_ExtensionsEntry {
    return SylkService_ExtensionsEntry.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkService_ExtensionsEntry>, I>>(object: I): SylkService_ExtensionsEntry {
    const message = createBaseSylkService_ExtensionsEntry();
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
