/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { Any } from "../../../google/protobuf/any";
import { Timestamp } from "../../../google/protobuf/timestamp";
import { SylkClient } from "../../SylkClient/v1/SylkClient";
import { SylkServer } from "../../SylkServer/v1/SylkServer";
import { SylkUserRoles, sylkUserRolesFromJSON, sylkUserRolesToJSON } from "../../SylkUser/v1/SylkUser";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkProject.v1.SylkProjectDisplay] - None */
export interface SylkProjectDisplay {
  owner: string;
  updatedAt?: Date;
  numMethods: number;
  createdAt?: Date;
  members: { [key: string]: SylkUserRoles };
  numServices: number;
  numMessages: number;
  numPackages: number;
  project?: SylkProject;
}

export interface SylkProjectDisplay_MembersEntry {
  key: string;
  value: SylkUserRoles;
}

/** [sylk.SylkProject.v1.SylkProject] - None */
export interface SylkProject {
  description: string;
  javaPackage: string;
  goPackage: string;
  name: string;
  uri: string;
  clients: SylkClient[];
  server?: SylkServer;
  packageName: string;
  extensions: Any[];
}

function createBaseSylkProjectDisplay(): SylkProjectDisplay {
  return {
    owner: "",
    updatedAt: undefined,
    numMethods: 0,
    createdAt: undefined,
    members: {},
    numServices: 0,
    numMessages: 0,
    numPackages: 0,
    project: undefined,
  };
}

export const SylkProjectDisplay = {
  encode(message: SylkProjectDisplay, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.owner !== "") {
      writer.uint32(34).string(message.owner);
    }
    if (message.updatedAt !== undefined) {
      Timestamp.encode(toTimestamp(message.updatedAt), writer.uint32(26).fork()).ldelim();
    }
    if (message.numMethods !== 0) {
      writer.uint32(48).int32(message.numMethods);
    }
    if (message.createdAt !== undefined) {
      Timestamp.encode(toTimestamp(message.createdAt), writer.uint32(18).fork()).ldelim();
    }
    Object.entries(message.members).forEach(([key, value]) => {
      SylkProjectDisplay_MembersEntry.encode({ key: key as any, value }, writer.uint32(42).fork()).ldelim();
    });
    if (message.numServices !== 0) {
      writer.uint32(56).int32(message.numServices);
    }
    if (message.numMessages !== 0) {
      writer.uint32(72).int32(message.numMessages);
    }
    if (message.numPackages !== 0) {
      writer.uint32(64).int32(message.numPackages);
    }
    if (message.project !== undefined) {
      SylkProject.encode(message.project, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkProjectDisplay {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkProjectDisplay();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 4:
          if (tag !== 34) {
            break;
          }

          message.owner = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updatedAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
          continue;
        case 6:
          if (tag !== 48) {
            break;
          }

          message.numMethods = reader.int32();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.createdAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
          continue;
        case 5:
          if (tag !== 42) {
            break;
          }

          const entry5 = SylkProjectDisplay_MembersEntry.decode(reader, reader.uint32());
          if (entry5.value !== undefined) {
            message.members[entry5.key] = entry5.value;
          }
          continue;
        case 7:
          if (tag !== 56) {
            break;
          }

          message.numServices = reader.int32();
          continue;
        case 9:
          if (tag !== 72) {
            break;
          }

          message.numMessages = reader.int32();
          continue;
        case 8:
          if (tag !== 64) {
            break;
          }

          message.numPackages = reader.int32();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.project = SylkProject.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkProjectDisplay {
    return {
      owner: isSet(object.owner) ? String(object.owner) : "",
      updatedAt: isSet(object.updatedAt) ? fromJsonTimestamp(object.updatedAt) : undefined,
      numMethods: isSet(object.numMethods) ? Number(object.numMethods) : 0,
      createdAt: isSet(object.createdAt) ? fromJsonTimestamp(object.createdAt) : undefined,
      members: isObject(object.members)
        ? Object.entries(object.members).reduce<{ [key: string]: SylkUserRoles }>((acc, [key, value]) => {
          acc[key] = sylkUserRolesFromJSON(value);
          return acc;
        }, {})
        : {},
      numServices: isSet(object.numServices) ? Number(object.numServices) : 0,
      numMessages: isSet(object.numMessages) ? Number(object.numMessages) : 0,
      numPackages: isSet(object.numPackages) ? Number(object.numPackages) : 0,
      project: isSet(object.project) ? SylkProject.fromJSON(object.project) : undefined,
    };
  },

  toJSON(message: SylkProjectDisplay): unknown {
    const obj: any = {};
    message.owner !== undefined && (obj.owner = message.owner);
    message.updatedAt !== undefined && (obj.updatedAt = message.updatedAt.toISOString());
    message.numMethods !== undefined && (obj.numMethods = Math.round(message.numMethods));
    message.createdAt !== undefined && (obj.createdAt = message.createdAt.toISOString());
    obj.members = {};
    if (message.members) {
      Object.entries(message.members).forEach(([k, v]) => {
        obj.members[k] = sylkUserRolesToJSON(v);
      });
    }
    message.numServices !== undefined && (obj.numServices = Math.round(message.numServices));
    message.numMessages !== undefined && (obj.numMessages = Math.round(message.numMessages));
    message.numPackages !== undefined && (obj.numPackages = Math.round(message.numPackages));
    message.project !== undefined && (obj.project = message.project ? SylkProject.toJSON(message.project) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkProjectDisplay>, I>>(base?: I): SylkProjectDisplay {
    return SylkProjectDisplay.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkProjectDisplay>, I>>(object: I): SylkProjectDisplay {
    const message = createBaseSylkProjectDisplay();
    message.owner = object.owner ?? "";
    message.updatedAt = object.updatedAt ?? undefined;
    message.numMethods = object.numMethods ?? 0;
    message.createdAt = object.createdAt ?? undefined;
    message.members = Object.entries(object.members ?? {}).reduce<{ [key: string]: SylkUserRoles }>(
      (acc, [key, value]) => {
        if (value !== undefined) {
          acc[key] = value as SylkUserRoles;
        }
        return acc;
      },
      {},
    );
    message.numServices = object.numServices ?? 0;
    message.numMessages = object.numMessages ?? 0;
    message.numPackages = object.numPackages ?? 0;
    message.project = (object.project !== undefined && object.project !== null)
      ? SylkProject.fromPartial(object.project)
      : undefined;
    return message;
  },
};

function createBaseSylkProjectDisplay_MembersEntry(): SylkProjectDisplay_MembersEntry {
  return { key: "", value: 0 };
}

export const SylkProjectDisplay_MembersEntry = {
  encode(message: SylkProjectDisplay_MembersEntry, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.key !== "") {
      writer.uint32(10).string(message.key);
    }
    if (message.value !== 0) {
      writer.uint32(16).int32(message.value);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkProjectDisplay_MembersEntry {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkProjectDisplay_MembersEntry();
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
          if (tag !== 16) {
            break;
          }

          message.value = reader.int32() as any;
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkProjectDisplay_MembersEntry {
    return {
      key: isSet(object.key) ? String(object.key) : "",
      value: isSet(object.value) ? sylkUserRolesFromJSON(object.value) : 0,
    };
  },

  toJSON(message: SylkProjectDisplay_MembersEntry): unknown {
    const obj: any = {};
    message.key !== undefined && (obj.key = message.key);
    message.value !== undefined && (obj.value = sylkUserRolesToJSON(message.value));
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkProjectDisplay_MembersEntry>, I>>(base?: I): SylkProjectDisplay_MembersEntry {
    return SylkProjectDisplay_MembersEntry.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkProjectDisplay_MembersEntry>, I>>(
    object: I,
  ): SylkProjectDisplay_MembersEntry {
    const message = createBaseSylkProjectDisplay_MembersEntry();
    message.key = object.key ?? "";
    message.value = object.value ?? 0;
    return message;
  },
};

function createBaseSylkProject(): SylkProject {
  return {
    description: "",
    javaPackage: "",
    goPackage: "",
    name: "",
    uri: "",
    clients: [],
    server: undefined,
    packageName: "",
    extensions: [],
  };
}

export const SylkProject = {
  encode(message: SylkProject, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.description !== "") {
      writer.uint32(66).string(message.description);
    }
    if (message.javaPackage !== "") {
      writer.uint32(50).string(message.javaPackage);
    }
    if (message.goPackage !== "") {
      writer.uint32(42).string(message.goPackage);
    }
    if (message.name !== "") {
      writer.uint32(18).string(message.name);
    }
    if (message.uri !== "") {
      writer.uint32(10).string(message.uri);
    }
    for (const v of message.clients) {
      SylkClient.encode(v!, writer.uint32(34).fork()).ldelim();
    }
    if (message.server !== undefined) {
      SylkServer.encode(message.server, writer.uint32(58).fork()).ldelim();
    }
    if (message.packageName !== "") {
      writer.uint32(26).string(message.packageName);
    }
    for (const v of message.extensions) {
      Any.encode(v!, writer.uint32(74).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkProject {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkProject();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 8:
          if (tag !== 66) {
            break;
          }

          message.description = reader.string();
          continue;
        case 6:
          if (tag !== 50) {
            break;
          }

          message.javaPackage = reader.string();
          continue;
        case 5:
          if (tag !== 42) {
            break;
          }

          message.goPackage = reader.string();
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
        case 4:
          if (tag !== 34) {
            break;
          }

          message.clients.push(SylkClient.decode(reader, reader.uint32()));
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.server = SylkServer.decode(reader, reader.uint32());
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.packageName = reader.string();
          continue;
        case 9:
          if (tag !== 74) {
            break;
          }

          message.extensions.push(Any.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkProject {
    return {
      description: isSet(object.description) ? String(object.description) : "",
      javaPackage: isSet(object.javaPackage) ? String(object.javaPackage) : "",
      goPackage: isSet(object.goPackage) ? String(object.goPackage) : "",
      name: isSet(object.name) ? String(object.name) : "",
      uri: isSet(object.uri) ? String(object.uri) : "",
      clients: Array.isArray(object?.clients) ? object.clients.map((e: any) => SylkClient.fromJSON(e)) : [],
      server: isSet(object.server) ? SylkServer.fromJSON(object.server) : undefined,
      packageName: isSet(object.packageName) ? String(object.packageName) : "",
      extensions: Array.isArray(object?.extensions) ? object.extensions.map((e: any) => Any.fromJSON(e)) : [],
    };
  },

  toJSON(message: SylkProject): unknown {
    const obj: any = {};
    message.description !== undefined && (obj.description = message.description);
    message.javaPackage !== undefined && (obj.javaPackage = message.javaPackage);
    message.goPackage !== undefined && (obj.goPackage = message.goPackage);
    message.name !== undefined && (obj.name = message.name);
    message.uri !== undefined && (obj.uri = message.uri);
    if (message.clients) {
      obj.clients = message.clients.map((e) => e ? SylkClient.toJSON(e) : undefined);
    } else {
      obj.clients = [];
    }
    message.server !== undefined && (obj.server = message.server ? SylkServer.toJSON(message.server) : undefined);
    message.packageName !== undefined && (obj.packageName = message.packageName);
    if (message.extensions) {
      obj.extensions = message.extensions.map((e) => e ? Any.toJSON(e) : undefined);
    } else {
      obj.extensions = [];
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkProject>, I>>(base?: I): SylkProject {
    return SylkProject.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkProject>, I>>(object: I): SylkProject {
    const message = createBaseSylkProject();
    message.description = object.description ?? "";
    message.javaPackage = object.javaPackage ?? "";
    message.goPackage = object.goPackage ?? "";
    message.name = object.name ?? "";
    message.uri = object.uri ?? "";
    message.clients = object.clients?.map((e) => SylkClient.fromPartial(e)) || [];
    message.server = (object.server !== undefined && object.server !== null)
      ? SylkServer.fromPartial(object.server)
      : undefined;
    message.packageName = object.packageName ?? "";
    message.extensions = object.extensions?.map((e) => Any.fromPartial(e)) || [];
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
