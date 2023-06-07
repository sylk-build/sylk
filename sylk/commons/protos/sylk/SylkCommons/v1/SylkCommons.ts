/* eslint-disable */
import _m0 from "protobufjs/minimal";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkCommons.v1.SylkExtensions] - None */
export enum SylkExtensions {
  /** DEFAULT_SYLKEXTENSIONS - [sylk.SylkCommons.v1.SylkExtensions] - sylk.descriptor/enum_value */
  DEFAULT_SYLKEXTENSIONS = 0,
  /** FileOptions - [sylk.SylkCommons.v1.SylkExtensions] - None */
  FileOptions = 1,
  /** MessageOptions - [sylk.SylkCommons.v1.SylkExtensions] - None */
  MessageOptions = 2,
  /** FieldOptions - [sylk.SylkCommons.v1.SylkExtensions] - None */
  FieldOptions = 3,
  /** ServiceOptions - [sylk.SylkCommons.v1.SylkExtensions] - None */
  ServiceOptions = 4,
  /** MethodOptions - [sylk.SylkCommons.v1.SylkExtensions] - None */
  MethodOptions = 5,
  UNRECOGNIZED = -1,
}

export function sylkExtensionsFromJSON(object: any): SylkExtensions {
  switch (object) {
    case 0:
    case "DEFAULT_SYLKEXTENSIONS":
      return SylkExtensions.DEFAULT_SYLKEXTENSIONS;
    case 1:
    case "FileOptions":
      return SylkExtensions.FileOptions;
    case 2:
    case "MessageOptions":
      return SylkExtensions.MessageOptions;
    case 3:
    case "FieldOptions":
      return SylkExtensions.FieldOptions;
    case 4:
    case "ServiceOptions":
      return SylkExtensions.ServiceOptions;
    case 5:
    case "MethodOptions":
      return SylkExtensions.MethodOptions;
    case -1:
    case "UNRECOGNIZED":
    default:
      return SylkExtensions.UNRECOGNIZED;
  }
}

export function sylkExtensionsToJSON(object: SylkExtensions): string {
  switch (object) {
    case SylkExtensions.DEFAULT_SYLKEXTENSIONS:
      return "DEFAULT_SYLKEXTENSIONS";
    case SylkExtensions.FileOptions:
      return "FileOptions";
    case SylkExtensions.MessageOptions:
      return "MessageOptions";
    case SylkExtensions.FieldOptions:
      return "FieldOptions";
    case SylkExtensions.ServiceOptions:
      return "ServiceOptions";
    case SylkExtensions.MethodOptions:
      return "MethodOptions";
    case SylkExtensions.UNRECOGNIZED:
    default:
      return "UNRECOGNIZED";
  }
}

/** [sylk.SylkCommons.v1.SylkContext] - None */
export interface SylkContext {
  files: SylkFileContext[];
}

/** [sylk.SylkCommons.v1.SylkFileContext] - None */
export interface SylkFileContext {
  file: string;
  code: Buffer;
  methods: SylkMethodContext[];
}

/** [sylk.SylkCommons.v1.SylkMethodContext] - None */
export interface SylkMethodContext {
  code: string;
  type: string;
  name: string;
}

function createBaseSylkContext(): SylkContext {
  return { files: [] };
}

export const SylkContext = {
  encode(message: SylkContext, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    for (const v of message.files) {
      SylkFileContext.encode(v!, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkContext {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkContext();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.files.push(SylkFileContext.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkContext {
    return { files: Array.isArray(object?.files) ? object.files.map((e: any) => SylkFileContext.fromJSON(e)) : [] };
  },

  toJSON(message: SylkContext): unknown {
    const obj: any = {};
    if (message.files) {
      obj.files = message.files.map((e) => e ? SylkFileContext.toJSON(e) : undefined);
    } else {
      obj.files = [];
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkContext>, I>>(base?: I): SylkContext {
    return SylkContext.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkContext>, I>>(object: I): SylkContext {
    const message = createBaseSylkContext();
    message.files = object.files?.map((e) => SylkFileContext.fromPartial(e)) || [];
    return message;
  },
};

function createBaseSylkFileContext(): SylkFileContext {
  return { file: "", code: Buffer.alloc(0), methods: [] };
}

export const SylkFileContext = {
  encode(message: SylkFileContext, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.file !== "") {
      writer.uint32(10).string(message.file);
    }
    if (message.code.length !== 0) {
      writer.uint32(26).bytes(message.code);
    }
    for (const v of message.methods) {
      SylkMethodContext.encode(v!, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkFileContext {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkFileContext();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.file = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.code = reader.bytes() as Buffer;
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.methods.push(SylkMethodContext.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkFileContext {
    return {
      file: isSet(object.file) ? String(object.file) : "",
      code: isSet(object.code) ? Buffer.from(bytesFromBase64(object.code)) : Buffer.alloc(0),
      methods: Array.isArray(object?.methods) ? object.methods.map((e: any) => SylkMethodContext.fromJSON(e)) : [],
    };
  },

  toJSON(message: SylkFileContext): unknown {
    const obj: any = {};
    message.file !== undefined && (obj.file = message.file);
    message.code !== undefined &&
      (obj.code = base64FromBytes(message.code !== undefined ? message.code : Buffer.alloc(0)));
    if (message.methods) {
      obj.methods = message.methods.map((e) => e ? SylkMethodContext.toJSON(e) : undefined);
    } else {
      obj.methods = [];
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkFileContext>, I>>(base?: I): SylkFileContext {
    return SylkFileContext.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkFileContext>, I>>(object: I): SylkFileContext {
    const message = createBaseSylkFileContext();
    message.file = object.file ?? "";
    message.code = object.code ?? Buffer.alloc(0);
    message.methods = object.methods?.map((e) => SylkMethodContext.fromPartial(e)) || [];
    return message;
  },
};

function createBaseSylkMethodContext(): SylkMethodContext {
  return { code: "", type: "", name: "" };
}

export const SylkMethodContext = {
  encode(message: SylkMethodContext, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.code !== "") {
      writer.uint32(18).string(message.code);
    }
    if (message.type !== "") {
      writer.uint32(26).string(message.type);
    }
    if (message.name !== "") {
      writer.uint32(10).string(message.name);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkMethodContext {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkMethodContext();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.code = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.type = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.name = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkMethodContext {
    return {
      code: isSet(object.code) ? String(object.code) : "",
      type: isSet(object.type) ? String(object.type) : "",
      name: isSet(object.name) ? String(object.name) : "",
    };
  },

  toJSON(message: SylkMethodContext): unknown {
    const obj: any = {};
    message.code !== undefined && (obj.code = message.code);
    message.type !== undefined && (obj.type = message.type);
    message.name !== undefined && (obj.name = message.name);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkMethodContext>, I>>(base?: I): SylkMethodContext {
    return SylkMethodContext.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkMethodContext>, I>>(object: I): SylkMethodContext {
    const message = createBaseSylkMethodContext();
    message.code = object.code ?? "";
    message.type = object.type ?? "";
    message.name = object.name ?? "";
    return message;
  },
};

declare var self: any | undefined;
declare var window: any | undefined;
declare var global: any | undefined;
var tsProtoGlobalThis: any = (() => {
  if (typeof globalThis !== "undefined") {
    return globalThis;
  }
  if (typeof self !== "undefined") {
    return self;
  }
  if (typeof window !== "undefined") {
    return window;
  }
  if (typeof global !== "undefined") {
    return global;
  }
  throw "Unable to locate global object";
})();

function bytesFromBase64(b64: string): Uint8Array {
  if (tsProtoGlobalThis.Buffer) {
    return Uint8Array.from(tsProtoGlobalThis.Buffer.from(b64, "base64"));
  } else {
    const bin = tsProtoGlobalThis.atob(b64);
    const arr = new Uint8Array(bin.length);
    for (let i = 0; i < bin.length; ++i) {
      arr[i] = bin.charCodeAt(i);
    }
    return arr;
  }
}

function base64FromBytes(arr: Uint8Array): string {
  if (tsProtoGlobalThis.Buffer) {
    return tsProtoGlobalThis.Buffer.from(arr).toString("base64");
  } else {
    const bin: string[] = [];
    arr.forEach((byte) => {
      bin.push(String.fromCharCode(byte));
    });
    return tsProtoGlobalThis.btoa(bin.join(""));
  }
}

type Builtin = Date | Function | Uint8Array | string | number | boolean | undefined;

type DeepPartial<T> = T extends Builtin ? T
  : T extends Array<infer U> ? Array<DeepPartial<U>> : T extends ReadonlyArray<infer U> ? ReadonlyArray<DeepPartial<U>>
  : T extends {} ? { [K in keyof T]?: DeepPartial<T[K]> }
  : Partial<T>;

type KeysOfUnion<T> = T extends T ? keyof T : never;
type Exact<P, I extends P> = P extends Builtin ? P
  : P & { [K in keyof P]: Exact<P[K], I[K]> } & { [K in Exclude<keyof I, KeysOfUnion<P>>]: never };

function isSet(value: any): boolean {
  return value !== null && value !== undefined;
}
