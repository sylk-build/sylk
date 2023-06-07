/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { Timestamp } from "../../../google/protobuf/timestamp";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkEnumValue.v1.SylkEnumValueDisplay] - None */
export interface SylkEnumValueDisplay {
  enumValue?: SylkEnumValue;
  updatedAt?: Date;
  createdAt?: Date;
}

/** [sylk.SylkEnumValue.v1.SylkEnumValue] - None */
export interface SylkEnumValue {
  kind: string;
  description: string;
  index: number;
  uri: string;
  name: string;
  number: number;
  fullName: string;
  type: string;
}

function createBaseSylkEnumValueDisplay(): SylkEnumValueDisplay {
  return { enumValue: undefined, updatedAt: undefined, createdAt: undefined };
}

export const SylkEnumValueDisplay = {
  encode(message: SylkEnumValueDisplay, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.enumValue !== undefined) {
      SylkEnumValue.encode(message.enumValue, writer.uint32(10).fork()).ldelim();
    }
    if (message.updatedAt !== undefined) {
      Timestamp.encode(toTimestamp(message.updatedAt), writer.uint32(26).fork()).ldelim();
    }
    if (message.createdAt !== undefined) {
      Timestamp.encode(toTimestamp(message.createdAt), writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkEnumValueDisplay {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkEnumValueDisplay();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.enumValue = SylkEnumValue.decode(reader, reader.uint32());
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updatedAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
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

  fromJSON(object: any): SylkEnumValueDisplay {
    return {
      enumValue: isSet(object.enumValue) ? SylkEnumValue.fromJSON(object.enumValue) : undefined,
      updatedAt: isSet(object.updatedAt) ? fromJsonTimestamp(object.updatedAt) : undefined,
      createdAt: isSet(object.createdAt) ? fromJsonTimestamp(object.createdAt) : undefined,
    };
  },

  toJSON(message: SylkEnumValueDisplay): unknown {
    const obj: any = {};
    message.enumValue !== undefined &&
      (obj.enumValue = message.enumValue ? SylkEnumValue.toJSON(message.enumValue) : undefined);
    message.updatedAt !== undefined && (obj.updatedAt = message.updatedAt.toISOString());
    message.createdAt !== undefined && (obj.createdAt = message.createdAt.toISOString());
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkEnumValueDisplay>, I>>(base?: I): SylkEnumValueDisplay {
    return SylkEnumValueDisplay.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkEnumValueDisplay>, I>>(object: I): SylkEnumValueDisplay {
    const message = createBaseSylkEnumValueDisplay();
    message.enumValue = (object.enumValue !== undefined && object.enumValue !== null)
      ? SylkEnumValue.fromPartial(object.enumValue)
      : undefined;
    message.updatedAt = object.updatedAt ?? undefined;
    message.createdAt = object.createdAt ?? undefined;
    return message;
  },
};

function createBaseSylkEnumValue(): SylkEnumValue {
  return { kind: "", description: "", index: 0, uri: "", name: "", number: 0, fullName: "", type: "" };
}

export const SylkEnumValue = {
  encode(message: SylkEnumValue, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.kind !== "") {
      writer.uint32(66).string(message.kind);
    }
    if (message.description !== "") {
      writer.uint32(50).string(message.description);
    }
    if (message.index !== 0) {
      writer.uint32(32).int32(message.index);
    }
    if (message.uri !== "") {
      writer.uint32(10).string(message.uri);
    }
    if (message.name !== "") {
      writer.uint32(18).string(message.name);
    }
    if (message.number !== 0) {
      writer.uint32(40).int32(message.number);
    }
    if (message.fullName !== "") {
      writer.uint32(26).string(message.fullName);
    }
    if (message.type !== "") {
      writer.uint32(58).string(message.type);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkEnumValue {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkEnumValue();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 8:
          if (tag !== 66) {
            break;
          }

          message.kind = reader.string();
          continue;
        case 6:
          if (tag !== 50) {
            break;
          }

          message.description = reader.string();
          continue;
        case 4:
          if (tag !== 32) {
            break;
          }

          message.index = reader.int32();
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
        case 5:
          if (tag !== 40) {
            break;
          }

          message.number = reader.int32();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.fullName = reader.string();
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.type = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkEnumValue {
    return {
      kind: isSet(object.kind) ? String(object.kind) : "",
      description: isSet(object.description) ? String(object.description) : "",
      index: isSet(object.index) ? Number(object.index) : 0,
      uri: isSet(object.uri) ? String(object.uri) : "",
      name: isSet(object.name) ? String(object.name) : "",
      number: isSet(object.number) ? Number(object.number) : 0,
      fullName: isSet(object.fullName) ? String(object.fullName) : "",
      type: isSet(object.type) ? String(object.type) : "",
    };
  },

  toJSON(message: SylkEnumValue): unknown {
    const obj: any = {};
    message.kind !== undefined && (obj.kind = message.kind);
    message.description !== undefined && (obj.description = message.description);
    message.index !== undefined && (obj.index = Math.round(message.index));
    message.uri !== undefined && (obj.uri = message.uri);
    message.name !== undefined && (obj.name = message.name);
    message.number !== undefined && (obj.number = Math.round(message.number));
    message.fullName !== undefined && (obj.fullName = message.fullName);
    message.type !== undefined && (obj.type = message.type);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkEnumValue>, I>>(base?: I): SylkEnumValue {
    return SylkEnumValue.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkEnumValue>, I>>(object: I): SylkEnumValue {
    const message = createBaseSylkEnumValue();
    message.kind = object.kind ?? "";
    message.description = object.description ?? "";
    message.index = object.index ?? 0;
    message.uri = object.uri ?? "";
    message.name = object.name ?? "";
    message.number = object.number ?? 0;
    message.fullName = object.fullName ?? "";
    message.type = object.type ?? "";
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
