/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { Timestamp } from "../../../google/protobuf/timestamp";
import { SylkEnumValue } from "../../SylkEnumValue/v1/SylkEnumValue";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkEnum.v1.SylkEnumDisplay] - None */
export interface SylkEnumDisplay {
  updatedAt?: Date;
  enum?: SylkEnum;
  createdAt?: Date;
}

/** [sylk.SylkEnum.v1.SylkEnum] - None */
export interface SylkEnum {
  type: string;
  kind: string;
  description: string;
  values: SylkEnumValue[];
  name: string;
  uri: string;
  fullName: string;
}

function createBaseSylkEnumDisplay(): SylkEnumDisplay {
  return { updatedAt: undefined, enum: undefined, createdAt: undefined };
}

export const SylkEnumDisplay = {
  encode(message: SylkEnumDisplay, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.updatedAt !== undefined) {
      Timestamp.encode(toTimestamp(message.updatedAt), writer.uint32(26).fork()).ldelim();
    }
    if (message.enum !== undefined) {
      SylkEnum.encode(message.enum, writer.uint32(10).fork()).ldelim();
    }
    if (message.createdAt !== undefined) {
      Timestamp.encode(toTimestamp(message.createdAt), writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkEnumDisplay {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkEnumDisplay();
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

          message.enum = SylkEnum.decode(reader, reader.uint32());
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

  fromJSON(object: any): SylkEnumDisplay {
    return {
      updatedAt: isSet(object.updatedAt) ? fromJsonTimestamp(object.updatedAt) : undefined,
      enum: isSet(object.enum) ? SylkEnum.fromJSON(object.enum) : undefined,
      createdAt: isSet(object.createdAt) ? fromJsonTimestamp(object.createdAt) : undefined,
    };
  },

  toJSON(message: SylkEnumDisplay): unknown {
    const obj: any = {};
    message.updatedAt !== undefined && (obj.updatedAt = message.updatedAt.toISOString());
    message.enum !== undefined && (obj.enum = message.enum ? SylkEnum.toJSON(message.enum) : undefined);
    message.createdAt !== undefined && (obj.createdAt = message.createdAt.toISOString());
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkEnumDisplay>, I>>(base?: I): SylkEnumDisplay {
    return SylkEnumDisplay.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkEnumDisplay>, I>>(object: I): SylkEnumDisplay {
    const message = createBaseSylkEnumDisplay();
    message.updatedAt = object.updatedAt ?? undefined;
    message.enum = (object.enum !== undefined && object.enum !== null) ? SylkEnum.fromPartial(object.enum) : undefined;
    message.createdAt = object.createdAt ?? undefined;
    return message;
  },
};

function createBaseSylkEnum(): SylkEnum {
  return { type: "", kind: "", description: "", values: [], name: "", uri: "", fullName: "" };
}

export const SylkEnum = {
  encode(message: SylkEnum, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.type !== "") {
      writer.uint32(50).string(message.type);
    }
    if (message.kind !== "") {
      writer.uint32(58).string(message.kind);
    }
    if (message.description !== "") {
      writer.uint32(34).string(message.description);
    }
    for (const v of message.values) {
      SylkEnumValue.encode(v!, writer.uint32(42).fork()).ldelim();
    }
    if (message.name !== "") {
      writer.uint32(18).string(message.name);
    }
    if (message.uri !== "") {
      writer.uint32(10).string(message.uri);
    }
    if (message.fullName !== "") {
      writer.uint32(26).string(message.fullName);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkEnum {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkEnum();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 6:
          if (tag !== 50) {
            break;
          }

          message.type = reader.string();
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.kind = reader.string();
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.description = reader.string();
          continue;
        case 5:
          if (tag !== 42) {
            break;
          }

          message.values.push(SylkEnumValue.decode(reader, reader.uint32()));
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
        case 3:
          if (tag !== 26) {
            break;
          }

          message.fullName = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkEnum {
    return {
      type: isSet(object.type) ? String(object.type) : "",
      kind: isSet(object.kind) ? String(object.kind) : "",
      description: isSet(object.description) ? String(object.description) : "",
      values: Array.isArray(object?.values) ? object.values.map((e: any) => SylkEnumValue.fromJSON(e)) : [],
      name: isSet(object.name) ? String(object.name) : "",
      uri: isSet(object.uri) ? String(object.uri) : "",
      fullName: isSet(object.fullName) ? String(object.fullName) : "",
    };
  },

  toJSON(message: SylkEnum): unknown {
    const obj: any = {};
    message.type !== undefined && (obj.type = message.type);
    message.kind !== undefined && (obj.kind = message.kind);
    message.description !== undefined && (obj.description = message.description);
    if (message.values) {
      obj.values = message.values.map((e) => e ? SylkEnumValue.toJSON(e) : undefined);
    } else {
      obj.values = [];
    }
    message.name !== undefined && (obj.name = message.name);
    message.uri !== undefined && (obj.uri = message.uri);
    message.fullName !== undefined && (obj.fullName = message.fullName);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkEnum>, I>>(base?: I): SylkEnum {
    return SylkEnum.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkEnum>, I>>(object: I): SylkEnum {
    const message = createBaseSylkEnum();
    message.type = object.type ?? "";
    message.kind = object.kind ?? "";
    message.description = object.description ?? "";
    message.values = object.values?.map((e) => SylkEnumValue.fromPartial(e)) || [];
    message.name = object.name ?? "";
    message.uri = object.uri ?? "";
    message.fullName = object.fullName ?? "";
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

function isSet(value: any): boolean {
  return value !== null && value !== undefined;
}
