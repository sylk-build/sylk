/* eslint-disable */
import _m0 from "protobufjs/minimal";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkConfigs.v1.SylkTemplateConfigs] - None */
export interface SylkTemplateConfigs {
  include: string[];
  exclude: string[];
  name: string;
  description: string;
  outPath: string;
  includeCode: boolean;
  author: string;
}

/** [sylk.SylkConfigs.v1.SylkProjectConfigs] - None */
export interface SylkProjectConfigs {
  description: string;
  host: string;
  template?: SylkTemplateConfigs;
  port: number;
  currentVersion: string;
  plugins: string[];
  protoBasePath: string;
  protoCompiledPath: string;
}

/** [sylk.SylkConfigs.v1.SylkCliConfigs] - None */
export interface SylkCliConfigs {
  sylkTemplates: string[];
  port: number;
  token: string;
  analytics: boolean;
  firstRun: boolean;
  host: string;
  plugins: string[];
}

function createBaseSylkTemplateConfigs(): SylkTemplateConfigs {
  return { include: [], exclude: [], name: "", description: "", outPath: "", includeCode: false, author: "" };
}

export const SylkTemplateConfigs = {
  encode(message: SylkTemplateConfigs, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    for (const v of message.include) {
      writer.uint32(26).string(v!);
    }
    for (const v of message.exclude) {
      writer.uint32(18).string(v!);
    }
    if (message.name !== "") {
      writer.uint32(42).string(message.name);
    }
    if (message.description !== "") {
      writer.uint32(34).string(message.description);
    }
    if (message.outPath !== "") {
      writer.uint32(50).string(message.outPath);
    }
    if (message.includeCode === true) {
      writer.uint32(8).bool(message.includeCode);
    }
    if (message.author !== "") {
      writer.uint32(58).string(message.author);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkTemplateConfigs {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkTemplateConfigs();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 26) {
            break;
          }

          message.include.push(reader.string());
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.exclude.push(reader.string());
          continue;
        case 5:
          if (tag !== 42) {
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
          if (tag !== 50) {
            break;
          }

          message.outPath = reader.string();
          continue;
        case 1:
          if (tag !== 8) {
            break;
          }

          message.includeCode = reader.bool();
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.author = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkTemplateConfigs {
    return {
      include: Array.isArray(object?.include) ? object.include.map((e: any) => String(e)) : [],
      exclude: Array.isArray(object?.exclude) ? object.exclude.map((e: any) => String(e)) : [],
      name: isSet(object.name) ? String(object.name) : "",
      description: isSet(object.description) ? String(object.description) : "",
      outPath: isSet(object.outPath) ? String(object.outPath) : "",
      includeCode: isSet(object.includeCode) ? Boolean(object.includeCode) : false,
      author: isSet(object.author) ? String(object.author) : "",
    };
  },

  toJSON(message: SylkTemplateConfigs): unknown {
    const obj: any = {};
    if (message.include) {
      obj.include = message.include.map((e) => e);
    } else {
      obj.include = [];
    }
    if (message.exclude) {
      obj.exclude = message.exclude.map((e) => e);
    } else {
      obj.exclude = [];
    }
    message.name !== undefined && (obj.name = message.name);
    message.description !== undefined && (obj.description = message.description);
    message.outPath !== undefined && (obj.outPath = message.outPath);
    message.includeCode !== undefined && (obj.includeCode = message.includeCode);
    message.author !== undefined && (obj.author = message.author);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkTemplateConfigs>, I>>(base?: I): SylkTemplateConfigs {
    return SylkTemplateConfigs.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkTemplateConfigs>, I>>(object: I): SylkTemplateConfigs {
    const message = createBaseSylkTemplateConfigs();
    message.include = object.include?.map((e) => e) || [];
    message.exclude = object.exclude?.map((e) => e) || [];
    message.name = object.name ?? "";
    message.description = object.description ?? "";
    message.outPath = object.outPath ?? "";
    message.includeCode = object.includeCode ?? false;
    message.author = object.author ?? "";
    return message;
  },
};

function createBaseSylkProjectConfigs(): SylkProjectConfigs {
  return {
    description: "",
    host: "",
    template: undefined,
    port: 0,
    currentVersion: "",
    plugins: [],
    protoBasePath: "",
    protoCompiledPath: "",
  };
}

export const SylkProjectConfigs = {
  encode(message: SylkProjectConfigs, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.description !== "") {
      writer.uint32(26).string(message.description);
    }
    if (message.host !== "") {
      writer.uint32(10).string(message.host);
    }
    if (message.template !== undefined) {
      SylkTemplateConfigs.encode(message.template, writer.uint32(42).fork()).ldelim();
    }
    if (message.port !== 0) {
      writer.uint32(16).int32(message.port);
    }
    if (message.currentVersion !== "") {
      writer.uint32(34).string(message.currentVersion);
    }
    for (const v of message.plugins) {
      writer.uint32(50).string(v!);
    }
    if (message.protoBasePath !== "") {
      writer.uint32(58).string(message.protoBasePath);
    }
    if (message.protoCompiledPath !== "") {
      writer.uint32(66).string(message.protoCompiledPath);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkProjectConfigs {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkProjectConfigs();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 26) {
            break;
          }

          message.description = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.host = reader.string();
          continue;
        case 5:
          if (tag !== 42) {
            break;
          }

          message.template = SylkTemplateConfigs.decode(reader, reader.uint32());
          continue;
        case 2:
          if (tag !== 16) {
            break;
          }

          message.port = reader.int32();
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.currentVersion = reader.string();
          continue;
        case 6:
          if (tag !== 50) {
            break;
          }

          message.plugins.push(reader.string());
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.protoBasePath = reader.string();
          continue;
        case 8:
          if (tag !== 66) {
            break;
          }

          message.protoCompiledPath = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkProjectConfigs {
    return {
      description: isSet(object.description) ? String(object.description) : "",
      host: isSet(object.host) ? String(object.host) : "",
      template: isSet(object.template) ? SylkTemplateConfigs.fromJSON(object.template) : undefined,
      port: isSet(object.port) ? Number(object.port) : 0,
      currentVersion: isSet(object.currentVersion) ? String(object.currentVersion) : "",
      plugins: Array.isArray(object?.plugins) ? object.plugins.map((e: any) => String(e)) : [],
      protoBasePath: isSet(object.protoBasePath) ? String(object.protoBasePath) : "",
      protoCompiledPath: isSet(object.protoCompiledPath) ? String(object.protoCompiledPath) : "",
    };
  },

  toJSON(message: SylkProjectConfigs): unknown {
    const obj: any = {};
    message.description !== undefined && (obj.description = message.description);
    message.host !== undefined && (obj.host = message.host);
    message.template !== undefined &&
      (obj.template = message.template ? SylkTemplateConfigs.toJSON(message.template) : undefined);
    message.port !== undefined && (obj.port = Math.round(message.port));
    message.currentVersion !== undefined && (obj.currentVersion = message.currentVersion);
    if (message.plugins) {
      obj.plugins = message.plugins.map((e) => e);
    } else {
      obj.plugins = [];
    }
    message.protoBasePath !== undefined && (obj.protoBasePath = message.protoBasePath);
    message.protoCompiledPath !== undefined && (obj.protoCompiledPath = message.protoCompiledPath);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkProjectConfigs>, I>>(base?: I): SylkProjectConfigs {
    return SylkProjectConfigs.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkProjectConfigs>, I>>(object: I): SylkProjectConfigs {
    const message = createBaseSylkProjectConfigs();
    message.description = object.description ?? "";
    message.host = object.host ?? "";
    message.template = (object.template !== undefined && object.template !== null)
      ? SylkTemplateConfigs.fromPartial(object.template)
      : undefined;
    message.port = object.port ?? 0;
    message.currentVersion = object.currentVersion ?? "";
    message.plugins = object.plugins?.map((e) => e) || [];
    message.protoBasePath = object.protoBasePath ?? "";
    message.protoCompiledPath = object.protoCompiledPath ?? "";
    return message;
  },
};

function createBaseSylkCliConfigs(): SylkCliConfigs {
  return { sylkTemplates: [], port: 0, token: "", analytics: false, firstRun: false, host: "", plugins: [] };
}

export const SylkCliConfigs = {
  encode(message: SylkCliConfigs, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    for (const v of message.sylkTemplates) {
      writer.uint32(50).string(v!);
    }
    if (message.port !== 0) {
      writer.uint32(16).int32(message.port);
    }
    if (message.token !== "") {
      writer.uint32(26).string(message.token);
    }
    if (message.analytics === true) {
      writer.uint32(32).bool(message.analytics);
    }
    if (message.firstRun === true) {
      writer.uint32(40).bool(message.firstRun);
    }
    if (message.host !== "") {
      writer.uint32(10).string(message.host);
    }
    for (const v of message.plugins) {
      writer.uint32(58).string(v!);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkCliConfigs {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkCliConfigs();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 6:
          if (tag !== 50) {
            break;
          }

          message.sylkTemplates.push(reader.string());
          continue;
        case 2:
          if (tag !== 16) {
            break;
          }

          message.port = reader.int32();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.token = reader.string();
          continue;
        case 4:
          if (tag !== 32) {
            break;
          }

          message.analytics = reader.bool();
          continue;
        case 5:
          if (tag !== 40) {
            break;
          }

          message.firstRun = reader.bool();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.host = reader.string();
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.plugins.push(reader.string());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkCliConfigs {
    return {
      sylkTemplates: Array.isArray(object?.sylkTemplates) ? object.sylkTemplates.map((e: any) => String(e)) : [],
      port: isSet(object.port) ? Number(object.port) : 0,
      token: isSet(object.token) ? String(object.token) : "",
      analytics: isSet(object.analytics) ? Boolean(object.analytics) : false,
      firstRun: isSet(object.firstRun) ? Boolean(object.firstRun) : false,
      host: isSet(object.host) ? String(object.host) : "",
      plugins: Array.isArray(object?.plugins) ? object.plugins.map((e: any) => String(e)) : [],
    };
  },

  toJSON(message: SylkCliConfigs): unknown {
    const obj: any = {};
    if (message.sylkTemplates) {
      obj.sylkTemplates = message.sylkTemplates.map((e) => e);
    } else {
      obj.sylkTemplates = [];
    }
    message.port !== undefined && (obj.port = Math.round(message.port));
    message.token !== undefined && (obj.token = message.token);
    message.analytics !== undefined && (obj.analytics = message.analytics);
    message.firstRun !== undefined && (obj.firstRun = message.firstRun);
    message.host !== undefined && (obj.host = message.host);
    if (message.plugins) {
      obj.plugins = message.plugins.map((e) => e);
    } else {
      obj.plugins = [];
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkCliConfigs>, I>>(base?: I): SylkCliConfigs {
    return SylkCliConfigs.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkCliConfigs>, I>>(object: I): SylkCliConfigs {
    const message = createBaseSylkCliConfigs();
    message.sylkTemplates = object.sylkTemplates?.map((e) => e) || [];
    message.port = object.port ?? 0;
    message.token = object.token ?? "";
    message.analytics = object.analytics ?? false;
    message.firstRun = object.firstRun ?? false;
    message.host = object.host ?? "";
    message.plugins = object.plugins?.map((e) => e) || [];
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

function isSet(value: any): boolean {
  return value !== null && value !== undefined;
}
