/* eslint-disable */
import _m0 from "protobufjs/minimal";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkServer.v1.SylkServerLanguages] - None */
export enum SylkServerLanguages {
  /** DEFAULT_SYLKSERVERLANGUAGES - [sylk.SylkServer.v1.SylkServerLanguages] - Default enum value for "sylk.SylkServer.v1.SylkServerLanguages" */
  DEFAULT_SYLKSERVERLANGUAGES = 0,
  /** python - [sylk.SylkServer.v1.SylkServerLanguages] - None */
  python = 1,
  /** nodejs - [sylk.SylkServer.v1.SylkServerLanguages] - None */
  nodejs = 2,
  /** typescript - [sylk.SylkServer.v1.SylkServerLanguages] - None */
  typescript = 3,
  /** go - [sylk.SylkServer.v1.SylkServerLanguages] - None */
  go = 4,
  UNRECOGNIZED = -1,
}

export function sylkServerLanguagesFromJSON(object: any): SylkServerLanguages {
  switch (object) {
    case 0:
    case "DEFAULT_SYLKSERVERLANGUAGES":
      return SylkServerLanguages.DEFAULT_SYLKSERVERLANGUAGES;
    case 1:
    case "python":
      return SylkServerLanguages.python;
    case 2:
    case "nodejs":
      return SylkServerLanguages.nodejs;
    case 3:
    case "typescript":
      return SylkServerLanguages.typescript;
    case 4:
    case "go":
      return SylkServerLanguages.go;
    case -1:
    case "UNRECOGNIZED":
    default:
      return SylkServerLanguages.UNRECOGNIZED;
  }
}

export function sylkServerLanguagesToJSON(object: SylkServerLanguages): string {
  switch (object) {
    case SylkServerLanguages.DEFAULT_SYLKSERVERLANGUAGES:
      return "DEFAULT_SYLKSERVERLANGUAGES";
    case SylkServerLanguages.python:
      return "python";
    case SylkServerLanguages.nodejs:
      return "nodejs";
    case SylkServerLanguages.typescript:
      return "typescript";
    case SylkServerLanguages.go:
      return "go";
    case SylkServerLanguages.UNRECOGNIZED:
    default:
      return "UNRECOGNIZED";
  }
}

/** [sylk.SylkServer.v1.SylkServer] - None */
export interface SylkServer {
  language: SylkServerLanguages;
}

function createBaseSylkServer(): SylkServer {
  return { language: 0 };
}

export const SylkServer = {
  encode(message: SylkServer, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.language !== 0) {
      writer.uint32(8).int32(message.language);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkServer {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkServer();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
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

  fromJSON(object: any): SylkServer {
    return { language: isSet(object.language) ? sylkServerLanguagesFromJSON(object.language) : 0 };
  },

  toJSON(message: SylkServer): unknown {
    const obj: any = {};
    message.language !== undefined && (obj.language = sylkServerLanguagesToJSON(message.language));
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkServer>, I>>(base?: I): SylkServer {
    return SylkServer.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkServer>, I>>(object: I): SylkServer {
    const message = createBaseSylkServer();
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
