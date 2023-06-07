/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { Struct } from "../../../google/protobuf/struct";
import { Timestamp } from "../../../google/protobuf/timestamp";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkMethod.v1.SylkMethodDisplay] - None */
export interface SylkMethodDisplay {
  createdAt?: Date;
  method?: SylkMethod;
  updatedAt?: Date;
}

/** [sylk.SylkMethod.v1.SylkMethod] - None */
export interface SylkMethod {
  clientStreaming: boolean;
  fullName: string;
  type: string;
  name: string;
  serverStreaming: boolean;
  description: string;
  kind: string;
  extensions: { [key: string]: { [key: string]: any } };
  inputType: string;
  outputType: string;
  uri: string;
}

export interface SylkMethod_ExtensionsEntry {
  key: string;
  value?: { [key: string]: any };
}

function createBaseSylkMethodDisplay(): SylkMethodDisplay {
  return { createdAt: undefined, method: undefined, updatedAt: undefined };
}

export const SylkMethodDisplay = {
  encode(message: SylkMethodDisplay, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.createdAt !== undefined) {
      Timestamp.encode(toTimestamp(message.createdAt), writer.uint32(18).fork()).ldelim();
    }
    if (message.method !== undefined) {
      SylkMethod.encode(message.method, writer.uint32(10).fork()).ldelim();
    }
    if (message.updatedAt !== undefined) {
      Timestamp.encode(toTimestamp(message.updatedAt), writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkMethodDisplay {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkMethodDisplay();
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

          message.method = SylkMethod.decode(reader, reader.uint32());
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

  fromJSON(object: any): SylkMethodDisplay {
    return {
      createdAt: isSet(object.createdAt) ? fromJsonTimestamp(object.createdAt) : undefined,
      method: isSet(object.method) ? SylkMethod.fromJSON(object.method) : undefined,
      updatedAt: isSet(object.updatedAt) ? fromJsonTimestamp(object.updatedAt) : undefined,
    };
  },

  toJSON(message: SylkMethodDisplay): unknown {
    const obj: any = {};
    message.createdAt !== undefined && (obj.createdAt = message.createdAt.toISOString());
    message.method !== undefined && (obj.method = message.method ? SylkMethod.toJSON(message.method) : undefined);
    message.updatedAt !== undefined && (obj.updatedAt = message.updatedAt.toISOString());
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkMethodDisplay>, I>>(base?: I): SylkMethodDisplay {
    return SylkMethodDisplay.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkMethodDisplay>, I>>(object: I): SylkMethodDisplay {
    const message = createBaseSylkMethodDisplay();
    message.createdAt = object.createdAt ?? undefined;
    message.method = (object.method !== undefined && object.method !== null)
      ? SylkMethod.fromPartial(object.method)
      : undefined;
    message.updatedAt = object.updatedAt ?? undefined;
    return message;
  },
};

function createBaseSylkMethod(): SylkMethod {
  return {
    clientStreaming: false,
    fullName: "",
    type: "",
    name: "",
    serverStreaming: false,
    description: "",
    kind: "",
    extensions: {},
    inputType: "",
    outputType: "",
    uri: "",
  };
}

export const SylkMethod = {
  encode(message: SylkMethod, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.clientStreaming === true) {
      writer.uint32(56).bool(message.clientStreaming);
    }
    if (message.fullName !== "") {
      writer.uint32(26).string(message.fullName);
    }
    if (message.type !== "") {
      writer.uint32(74).string(message.type);
    }
    if (message.name !== "") {
      writer.uint32(18).string(message.name);
    }
    if (message.serverStreaming === true) {
      writer.uint32(64).bool(message.serverStreaming);
    }
    if (message.description !== "") {
      writer.uint32(34).string(message.description);
    }
    if (message.kind !== "") {
      writer.uint32(82).string(message.kind);
    }
    Object.entries(message.extensions).forEach(([key, value]) => {
      if (value !== undefined) {
        SylkMethod_ExtensionsEntry.encode({ key: key as any, value }, writer.uint32(90).fork()).ldelim();
      }
    });
    if (message.inputType !== "") {
      writer.uint32(42).string(message.inputType);
    }
    if (message.outputType !== "") {
      writer.uint32(50).string(message.outputType);
    }
    if (message.uri !== "") {
      writer.uint32(10).string(message.uri);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkMethod {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkMethod();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 7:
          if (tag !== 56) {
            break;
          }

          message.clientStreaming = reader.bool();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.fullName = reader.string();
          continue;
        case 9:
          if (tag !== 74) {
            break;
          }

          message.type = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.name = reader.string();
          continue;
        case 8:
          if (tag !== 64) {
            break;
          }

          message.serverStreaming = reader.bool();
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

          message.kind = reader.string();
          continue;
        case 11:
          if (tag !== 90) {
            break;
          }

          const entry11 = SylkMethod_ExtensionsEntry.decode(reader, reader.uint32());
          if (entry11.value !== undefined) {
            message.extensions[entry11.key] = entry11.value;
          }
          continue;
        case 5:
          if (tag !== 42) {
            break;
          }

          message.inputType = reader.string();
          continue;
        case 6:
          if (tag !== 50) {
            break;
          }

          message.outputType = reader.string();
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

  fromJSON(object: any): SylkMethod {
    return {
      clientStreaming: isSet(object.clientStreaming) ? Boolean(object.clientStreaming) : false,
      fullName: isSet(object.fullName) ? String(object.fullName) : "",
      type: isSet(object.type) ? String(object.type) : "",
      name: isSet(object.name) ? String(object.name) : "",
      serverStreaming: isSet(object.serverStreaming) ? Boolean(object.serverStreaming) : false,
      description: isSet(object.description) ? String(object.description) : "",
      kind: isSet(object.kind) ? String(object.kind) : "",
      extensions: isObject(object.extensions)
        ? Object.entries(object.extensions).reduce<{ [key: string]: { [key: string]: any } }>((acc, [key, value]) => {
          acc[key] = value as { [key: string]: any };
          return acc;
        }, {})
        : {},
      inputType: isSet(object.inputType) ? String(object.inputType) : "",
      outputType: isSet(object.outputType) ? String(object.outputType) : "",
      uri: isSet(object.uri) ? String(object.uri) : "",
    };
  },

  toJSON(message: SylkMethod): unknown {
    const obj: any = {};
    message.clientStreaming !== undefined && (obj.clientStreaming = message.clientStreaming);
    message.fullName !== undefined && (obj.fullName = message.fullName);
    message.type !== undefined && (obj.type = message.type);
    message.name !== undefined && (obj.name = message.name);
    message.serverStreaming !== undefined && (obj.serverStreaming = message.serverStreaming);
    message.description !== undefined && (obj.description = message.description);
    message.kind !== undefined && (obj.kind = message.kind);
    obj.extensions = {};
    if (message.extensions) {
      Object.entries(message.extensions).forEach(([k, v]) => {
        obj.extensions[k] = v;
      });
    }
    message.inputType !== undefined && (obj.inputType = message.inputType);
    message.outputType !== undefined && (obj.outputType = message.outputType);
    message.uri !== undefined && (obj.uri = message.uri);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkMethod>, I>>(base?: I): SylkMethod {
    return SylkMethod.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkMethod>, I>>(object: I): SylkMethod {
    const message = createBaseSylkMethod();
    message.clientStreaming = object.clientStreaming ?? false;
    message.fullName = object.fullName ?? "";
    message.type = object.type ?? "";
    message.name = object.name ?? "";
    message.serverStreaming = object.serverStreaming ?? false;
    message.description = object.description ?? "";
    message.kind = object.kind ?? "";
    message.extensions = Object.entries(object.extensions ?? {}).reduce<{ [key: string]: { [key: string]: any } }>(
      (acc, [key, value]) => {
        if (value !== undefined) {
          acc[key] = value;
        }
        return acc;
      },
      {},
    );
    message.inputType = object.inputType ?? "";
    message.outputType = object.outputType ?? "";
    message.uri = object.uri ?? "";
    return message;
  },
};

function createBaseSylkMethod_ExtensionsEntry(): SylkMethod_ExtensionsEntry {
  return { key: "", value: undefined };
}

export const SylkMethod_ExtensionsEntry = {
  encode(message: SylkMethod_ExtensionsEntry, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.key !== "") {
      writer.uint32(10).string(message.key);
    }
    if (message.value !== undefined) {
      Struct.encode(Struct.wrap(message.value), writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkMethod_ExtensionsEntry {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkMethod_ExtensionsEntry();
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

  fromJSON(object: any): SylkMethod_ExtensionsEntry {
    return {
      key: isSet(object.key) ? String(object.key) : "",
      value: isObject(object.value) ? object.value : undefined,
    };
  },

  toJSON(message: SylkMethod_ExtensionsEntry): unknown {
    const obj: any = {};
    message.key !== undefined && (obj.key = message.key);
    message.value !== undefined && (obj.value = message.value);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkMethod_ExtensionsEntry>, I>>(base?: I): SylkMethod_ExtensionsEntry {
    return SylkMethod_ExtensionsEntry.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkMethod_ExtensionsEntry>, I>>(object: I): SylkMethod_ExtensionsEntry {
    const message = createBaseSylkMethod_ExtensionsEntry();
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
