/* eslint-disable */
import _m0 from "protobufjs/minimal";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkClient.v1.SylkClientLanguages] - None */
export enum SylkClientLanguages {
  /** DEFAULT_SYLKCLIENTLANGUAGES - [sylk.SylkClient.v1.SylkClientLanguages] - Default enum value for "sylk.SylkClient.v1.SylkClientLanguages" */
  DEFAULT_SYLKCLIENTLANGUAGES = 0,
  /** python - [sylk.SylkClient.v1.SylkClientLanguages] - None */
  python = 1,
  /** nodejs - [sylk.SylkClient.v1.SylkClientLanguages] - None */
  nodejs = 2,
  /** typescript - [sylk.SylkClient.v1.SylkClientLanguages] - None */
  typescript = 3,
  /** go - [sylk.SylkClient.v1.SylkClientLanguages] - None */
  go = 4,
  UNRECOGNIZED = -1,
}

export function sylkClientLanguagesFromJSON(object: any): SylkClientLanguages {
  switch (object) {
    case 0:
    case "DEFAULT_SYLKCLIENTLANGUAGES":
      return SylkClientLanguages.DEFAULT_SYLKCLIENTLANGUAGES;
    case 1:
    case "python":
      return SylkClientLanguages.python;
    case 2:
    case "nodejs":
      return SylkClientLanguages.nodejs;
    case 3:
    case "typescript":
      return SylkClientLanguages.typescript;
    case 4:
    case "go":
      return SylkClientLanguages.go;
    case -1:
    case "UNRECOGNIZED":
    default:
      return SylkClientLanguages.UNRECOGNIZED;
  }
}

export function sylkClientLanguagesToJSON(object: SylkClientLanguages): string {
  switch (object) {
    case SylkClientLanguages.DEFAULT_SYLKCLIENTLANGUAGES:
      return "DEFAULT_SYLKCLIENTLANGUAGES";
    case SylkClientLanguages.python:
      return "python";
    case SylkClientLanguages.nodejs:
      return "nodejs";
    case SylkClientLanguages.typescript:
      return "typescript";
    case SylkClientLanguages.go:
      return "go";
    case SylkClientLanguages.UNRECOGNIZED:
    default:
      return "UNRECOGNIZED";
  }
}

/** [sylk.SylkClient.v1.SylkClient] - None */
export interface SylkClient {
  outDir: string;
  language: SylkClientLanguages;
}

function createBaseSylkClient(): SylkClient {
  return { outDir: "", language: 0 };
}

export const SylkClient = {
  encode(message: SylkClient, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.outDir !== "") {
      writer.uint32(18).string(message.outDir);
    }
    if (message.language !== 0) {
      writer.uint32(8).int32(message.language);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkClient {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkClient();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.outDir = reader.string();
          continue;
        case 1:
          if (tag !== 8) {
            break;
          }

          message.language = reader.int32() as any;
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkClient {
    return {
      outDir: isSet(object.outDir) ? String(object.outDir) : "",
      language: isSet(object.language) ? sylkClientLanguagesFromJSON(object.language) : 0,
    };
  },

  toJSON(message: SylkClient): unknown {
    const obj: any = {};
    message.outDir !== undefined && (obj.outDir = message.outDir);
    message.language !== undefined && (obj.language = sylkClientLanguagesToJSON(message.language));
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkClient>, I>>(base?: I): SylkClient {
    return SylkClient.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkClient>, I>>(object: I): SylkClient {
    const message = createBaseSylkClient();
    message.outDir = object.outDir ?? "";
    message.language = object.language ?? 0;
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
