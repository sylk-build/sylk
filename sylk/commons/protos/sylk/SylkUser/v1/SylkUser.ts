/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { Timestamp } from "../../../google/protobuf/timestamp";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkUser.v1.SylkUserStatuses] - None */
export enum SylkUserStatuses {
  /** DEFAULT_SYLKUSERSTATUSES - [sylk.SylkUser.v1.SylkUserStatuses] - Default enum value for "sylk.SylkUser.v1.SylkUserStatuses" */
  DEFAULT_SYLKUSERSTATUSES = 0,
  /** ACTIVE - [sylk.SylkUser.v1.SylkUserStatuses] - None */
  ACTIVE = 1,
  /** INACTIVE - [sylk.SylkUser.v1.SylkUserStatuses] - None */
  INACTIVE = 2,
  /** PENDING - [sylk.SylkUser.v1.SylkUserStatuses] - None */
  PENDING = 3,
  UNRECOGNIZED = -1,
}

export function sylkUserStatusesFromJSON(object: any): SylkUserStatuses {
  switch (object) {
    case 0:
    case "DEFAULT_SYLKUSERSTATUSES":
      return SylkUserStatuses.DEFAULT_SYLKUSERSTATUSES;
    case 1:
    case "ACTIVE":
      return SylkUserStatuses.ACTIVE;
    case 2:
    case "INACTIVE":
      return SylkUserStatuses.INACTIVE;
    case 3:
    case "PENDING":
      return SylkUserStatuses.PENDING;
    case -1:
    case "UNRECOGNIZED":
    default:
      return SylkUserStatuses.UNRECOGNIZED;
  }
}

export function sylkUserStatusesToJSON(object: SylkUserStatuses): string {
  switch (object) {
    case SylkUserStatuses.DEFAULT_SYLKUSERSTATUSES:
      return "DEFAULT_SYLKUSERSTATUSES";
    case SylkUserStatuses.ACTIVE:
      return "ACTIVE";
    case SylkUserStatuses.INACTIVE:
      return "INACTIVE";
    case SylkUserStatuses.PENDING:
      return "PENDING";
    case SylkUserStatuses.UNRECOGNIZED:
    default:
      return "UNRECOGNIZED";
  }
}

/** [sylk.SylkUser.v1.SylkUserRoles] - None */
export enum SylkUserRoles {
  /** DEFAULT_SYLKUSERROLES - [sylk.SylkUser.v1.SylkUserRoles] - Default enum value for "sylk.SylkUser.v1.SylkUserRoles" */
  DEFAULT_SYLKUSERROLES = 0,
  /** ADMIN - [sylk.SylkUser.v1.SylkUserRoles] - None */
  ADMIN = 1,
  /** CONTRIBUTER - [sylk.SylkUser.v1.SylkUserRoles] - None */
  CONTRIBUTER = 2,
  /** READER - [sylk.SylkUser.v1.SylkUserRoles] - None */
  READER = 3,
  UNRECOGNIZED = -1,
}

export function sylkUserRolesFromJSON(object: any): SylkUserRoles {
  switch (object) {
    case 0:
    case "DEFAULT_SYLKUSERROLES":
      return SylkUserRoles.DEFAULT_SYLKUSERROLES;
    case 1:
    case "ADMIN":
      return SylkUserRoles.ADMIN;
    case 2:
    case "CONTRIBUTER":
      return SylkUserRoles.CONTRIBUTER;
    case 3:
    case "READER":
      return SylkUserRoles.READER;
    case -1:
    case "UNRECOGNIZED":
    default:
      return SylkUserRoles.UNRECOGNIZED;
  }
}

export function sylkUserRolesToJSON(object: SylkUserRoles): string {
  switch (object) {
    case SylkUserRoles.DEFAULT_SYLKUSERROLES:
      return "DEFAULT_SYLKUSERROLES";
    case SylkUserRoles.ADMIN:
      return "ADMIN";
    case SylkUserRoles.CONTRIBUTER:
      return "CONTRIBUTER";
    case SylkUserRoles.READER:
      return "READER";
    case SylkUserRoles.UNRECOGNIZED:
    default:
      return "UNRECOGNIZED";
  }
}

/** [sylk.SylkUser.v1.PersonalAccessToken] - None */
export interface PersonalAccessToken {
  token: string;
  orgId: string;
  description: string;
  expiresAt?: Date;
  createdAt?: Date;
  revoked: boolean;
  userId: string;
}

/** [sylk.SylkUser.v1.SylkUserDisplay] - None */
export interface SylkUserDisplay {
  user?: SylkUser;
  lastActive?: Date;
  createdAt?: Date;
  updatedAt?: Date;
}

/** [sylk.SylkUser.v1.SylkUser] - None */
export interface SylkUser {
  email: string;
  orgsIds: { [key: string]: SylkUserRoles };
  locale: string;
  givenName: string;
  nickname: string;
  status: SylkUserStatuses;
  picture: string;
  connection: string;
  userId: string;
  emailVerified: boolean;
  familyName: string;
}

export interface SylkUser_OrgsIdsEntry {
  key: string;
  value: SylkUserRoles;
}

function createBasePersonalAccessToken(): PersonalAccessToken {
  return {
    token: "",
    orgId: "",
    description: "",
    expiresAt: undefined,
    createdAt: undefined,
    revoked: false,
    userId: "",
  };
}

export const PersonalAccessToken = {
  encode(message: PersonalAccessToken, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.token !== "") {
      writer.uint32(10).string(message.token);
    }
    if (message.orgId !== "") {
      writer.uint32(50).string(message.orgId);
    }
    if (message.description !== "") {
      writer.uint32(42).string(message.description);
    }
    if (message.expiresAt !== undefined) {
      Timestamp.encode(toTimestamp(message.expiresAt), writer.uint32(26).fork()).ldelim();
    }
    if (message.createdAt !== undefined) {
      Timestamp.encode(toTimestamp(message.createdAt), writer.uint32(18).fork()).ldelim();
    }
    if (message.revoked === true) {
      writer.uint32(32).bool(message.revoked);
    }
    if (message.userId !== "") {
      writer.uint32(58).string(message.userId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): PersonalAccessToken {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBasePersonalAccessToken();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.token = reader.string();
          continue;
        case 6:
          if (tag !== 50) {
            break;
          }

          message.orgId = reader.string();
          continue;
        case 5:
          if (tag !== 42) {
            break;
          }

          message.description = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.expiresAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.createdAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
          continue;
        case 4:
          if (tag !== 32) {
            break;
          }

          message.revoked = reader.bool();
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.userId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): PersonalAccessToken {
    return {
      token: isSet(object.token) ? String(object.token) : "",
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
      description: isSet(object.description) ? String(object.description) : "",
      expiresAt: isSet(object.expiresAt) ? fromJsonTimestamp(object.expiresAt) : undefined,
      createdAt: isSet(object.createdAt) ? fromJsonTimestamp(object.createdAt) : undefined,
      revoked: isSet(object.revoked) ? Boolean(object.revoked) : false,
      userId: isSet(object.userId) ? String(object.userId) : "",
    };
  },

  toJSON(message: PersonalAccessToken): unknown {
    const obj: any = {};
    message.token !== undefined && (obj.token = message.token);
    message.orgId !== undefined && (obj.orgId = message.orgId);
    message.description !== undefined && (obj.description = message.description);
    message.expiresAt !== undefined && (obj.expiresAt = message.expiresAt.toISOString());
    message.createdAt !== undefined && (obj.createdAt = message.createdAt.toISOString());
    message.revoked !== undefined && (obj.revoked = message.revoked);
    message.userId !== undefined && (obj.userId = message.userId);
    return obj;
  },

  create<I extends Exact<DeepPartial<PersonalAccessToken>, I>>(base?: I): PersonalAccessToken {
    return PersonalAccessToken.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<PersonalAccessToken>, I>>(object: I): PersonalAccessToken {
    const message = createBasePersonalAccessToken();
    message.token = object.token ?? "";
    message.orgId = object.orgId ?? "";
    message.description = object.description ?? "";
    message.expiresAt = object.expiresAt ?? undefined;
    message.createdAt = object.createdAt ?? undefined;
    message.revoked = object.revoked ?? false;
    message.userId = object.userId ?? "";
    return message;
  },
};

function createBaseSylkUserDisplay(): SylkUserDisplay {
  return { user: undefined, lastActive: undefined, createdAt: undefined, updatedAt: undefined };
}

export const SylkUserDisplay = {
  encode(message: SylkUserDisplay, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.user !== undefined) {
      SylkUser.encode(message.user, writer.uint32(10).fork()).ldelim();
    }
    if (message.lastActive !== undefined) {
      Timestamp.encode(toTimestamp(message.lastActive), writer.uint32(34).fork()).ldelim();
    }
    if (message.createdAt !== undefined) {
      Timestamp.encode(toTimestamp(message.createdAt), writer.uint32(18).fork()).ldelim();
    }
    if (message.updatedAt !== undefined) {
      Timestamp.encode(toTimestamp(message.updatedAt), writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkUserDisplay {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkUserDisplay();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.user = SylkUser.decode(reader, reader.uint32());
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.lastActive = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
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

  fromJSON(object: any): SylkUserDisplay {
    return {
      user: isSet(object.user) ? SylkUser.fromJSON(object.user) : undefined,
      lastActive: isSet(object.lastActive) ? fromJsonTimestamp(object.lastActive) : undefined,
      createdAt: isSet(object.createdAt) ? fromJsonTimestamp(object.createdAt) : undefined,
      updatedAt: isSet(object.updatedAt) ? fromJsonTimestamp(object.updatedAt) : undefined,
    };
  },

  toJSON(message: SylkUserDisplay): unknown {
    const obj: any = {};
    message.user !== undefined && (obj.user = message.user ? SylkUser.toJSON(message.user) : undefined);
    message.lastActive !== undefined && (obj.lastActive = message.lastActive.toISOString());
    message.createdAt !== undefined && (obj.createdAt = message.createdAt.toISOString());
    message.updatedAt !== undefined && (obj.updatedAt = message.updatedAt.toISOString());
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkUserDisplay>, I>>(base?: I): SylkUserDisplay {
    return SylkUserDisplay.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkUserDisplay>, I>>(object: I): SylkUserDisplay {
    const message = createBaseSylkUserDisplay();
    message.user = (object.user !== undefined && object.user !== null) ? SylkUser.fromPartial(object.user) : undefined;
    message.lastActive = object.lastActive ?? undefined;
    message.createdAt = object.createdAt ?? undefined;
    message.updatedAt = object.updatedAt ?? undefined;
    return message;
  },
};

function createBaseSylkUser(): SylkUser {
  return {
    email: "",
    orgsIds: {},
    locale: "",
    givenName: "",
    nickname: "",
    status: 0,
    picture: "",
    connection: "",
    userId: "",
    emailVerified: false,
    familyName: "",
  };
}

export const SylkUser = {
  encode(message: SylkUser, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.email !== "") {
      writer.uint32(18).string(message.email);
    }
    Object.entries(message.orgsIds).forEach(([key, value]) => {
      SylkUser_OrgsIdsEntry.encode({ key: key as any, value }, writer.uint32(90).fork()).ldelim();
    });
    if (message.locale !== "") {
      writer.uint32(50).string(message.locale);
    }
    if (message.givenName !== "") {
      writer.uint32(42).string(message.givenName);
    }
    if (message.nickname !== "") {
      writer.uint32(58).string(message.nickname);
    }
    if (message.status !== 0) {
      writer.uint32(80).int32(message.status);
    }
    if (message.picture !== "") {
      writer.uint32(66).string(message.picture);
    }
    if (message.connection !== "") {
      writer.uint32(74).string(message.connection);
    }
    if (message.userId !== "") {
      writer.uint32(10).string(message.userId);
    }
    if (message.emailVerified === true) {
      writer.uint32(24).bool(message.emailVerified);
    }
    if (message.familyName !== "") {
      writer.uint32(34).string(message.familyName);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkUser {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkUser();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.email = reader.string();
          continue;
        case 11:
          if (tag !== 90) {
            break;
          }

          const entry11 = SylkUser_OrgsIdsEntry.decode(reader, reader.uint32());
          if (entry11.value !== undefined) {
            message.orgsIds[entry11.key] = entry11.value;
          }
          continue;
        case 6:
          if (tag !== 50) {
            break;
          }

          message.locale = reader.string();
          continue;
        case 5:
          if (tag !== 42) {
            break;
          }

          message.givenName = reader.string();
          continue;
        case 7:
          if (tag !== 58) {
            break;
          }

          message.nickname = reader.string();
          continue;
        case 10:
          if (tag !== 80) {
            break;
          }

          message.status = reader.int32() as any;
          continue;
        case 8:
          if (tag !== 66) {
            break;
          }

          message.picture = reader.string();
          continue;
        case 9:
          if (tag !== 74) {
            break;
          }

          message.connection = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.userId = reader.string();
          continue;
        case 3:
          if (tag !== 24) {
            break;
          }

          message.emailVerified = reader.bool();
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.familyName = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkUser {
    return {
      email: isSet(object.email) ? String(object.email) : "",
      orgsIds: isObject(object.orgsIds)
        ? Object.entries(object.orgsIds).reduce<{ [key: string]: SylkUserRoles }>((acc, [key, value]) => {
          acc[key] = sylkUserRolesFromJSON(value);
          return acc;
        }, {})
        : {},
      locale: isSet(object.locale) ? String(object.locale) : "",
      givenName: isSet(object.givenName) ? String(object.givenName) : "",
      nickname: isSet(object.nickname) ? String(object.nickname) : "",
      status: isSet(object.status) ? sylkUserStatusesFromJSON(object.status) : 0,
      picture: isSet(object.picture) ? String(object.picture) : "",
      connection: isSet(object.connection) ? String(object.connection) : "",
      userId: isSet(object.userId) ? String(object.userId) : "",
      emailVerified: isSet(object.emailVerified) ? Boolean(object.emailVerified) : false,
      familyName: isSet(object.familyName) ? String(object.familyName) : "",
    };
  },

  toJSON(message: SylkUser): unknown {
    const obj: any = {};
    message.email !== undefined && (obj.email = message.email);
    obj.orgsIds = {};
    if (message.orgsIds) {
      Object.entries(message.orgsIds).forEach(([k, v]) => {
        obj.orgsIds[k] = sylkUserRolesToJSON(v);
      });
    }
    message.locale !== undefined && (obj.locale = message.locale);
    message.givenName !== undefined && (obj.givenName = message.givenName);
    message.nickname !== undefined && (obj.nickname = message.nickname);
    message.status !== undefined && (obj.status = sylkUserStatusesToJSON(message.status));
    message.picture !== undefined && (obj.picture = message.picture);
    message.connection !== undefined && (obj.connection = message.connection);
    message.userId !== undefined && (obj.userId = message.userId);
    message.emailVerified !== undefined && (obj.emailVerified = message.emailVerified);
    message.familyName !== undefined && (obj.familyName = message.familyName);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkUser>, I>>(base?: I): SylkUser {
    return SylkUser.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkUser>, I>>(object: I): SylkUser {
    const message = createBaseSylkUser();
    message.email = object.email ?? "";
    message.orgsIds = Object.entries(object.orgsIds ?? {}).reduce<{ [key: string]: SylkUserRoles }>(
      (acc, [key, value]) => {
        if (value !== undefined) {
          acc[key] = value as SylkUserRoles;
        }
        return acc;
      },
      {},
    );
    message.locale = object.locale ?? "";
    message.givenName = object.givenName ?? "";
    message.nickname = object.nickname ?? "";
    message.status = object.status ?? 0;
    message.picture = object.picture ?? "";
    message.connection = object.connection ?? "";
    message.userId = object.userId ?? "";
    message.emailVerified = object.emailVerified ?? false;
    message.familyName = object.familyName ?? "";
    return message;
  },
};

function createBaseSylkUser_OrgsIdsEntry(): SylkUser_OrgsIdsEntry {
  return { key: "", value: 0 };
}

export const SylkUser_OrgsIdsEntry = {
  encode(message: SylkUser_OrgsIdsEntry, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.key !== "") {
      writer.uint32(10).string(message.key);
    }
    if (message.value !== 0) {
      writer.uint32(16).int32(message.value);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkUser_OrgsIdsEntry {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkUser_OrgsIdsEntry();
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

  fromJSON(object: any): SylkUser_OrgsIdsEntry {
    return {
      key: isSet(object.key) ? String(object.key) : "",
      value: isSet(object.value) ? sylkUserRolesFromJSON(object.value) : 0,
    };
  },

  toJSON(message: SylkUser_OrgsIdsEntry): unknown {
    const obj: any = {};
    message.key !== undefined && (obj.key = message.key);
    message.value !== undefined && (obj.value = sylkUserRolesToJSON(message.value));
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkUser_OrgsIdsEntry>, I>>(base?: I): SylkUser_OrgsIdsEntry {
    return SylkUser_OrgsIdsEntry.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkUser_OrgsIdsEntry>, I>>(object: I): SylkUser_OrgsIdsEntry {
    const message = createBaseSylkUser_OrgsIdsEntry();
    message.key = object.key ?? "";
    message.value = object.value ?? 0;
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
