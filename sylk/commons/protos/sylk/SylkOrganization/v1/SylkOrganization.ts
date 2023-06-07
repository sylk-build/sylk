/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { SylkProjectDisplay } from "../../SylkProject/v1/SylkProject";
import { SylkUserDisplay } from "../../SylkUser/v1/SylkUser";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkOrganization.v1.SylkOrganizationDisplay] - None */
export interface SylkOrganizationDisplay {
  organization?: SylkOrganization;
  projects: SylkProjectDisplay[];
  users: SylkUserDisplay[];
}

/** [sylk.SylkOrganization.v1.SylkOrganization] - None */
export interface SylkOrganization {
  orgId: string;
  name: string;
  owner: string;
  domain: string;
}

function createBaseSylkOrganizationDisplay(): SylkOrganizationDisplay {
  return { organization: undefined, projects: [], users: [] };
}

export const SylkOrganizationDisplay = {
  encode(message: SylkOrganizationDisplay, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.organization !== undefined) {
      SylkOrganization.encode(message.organization, writer.uint32(10).fork()).ldelim();
    }
    for (const v of message.projects) {
      SylkProjectDisplay.encode(v!, writer.uint32(26).fork()).ldelim();
    }
    for (const v of message.users) {
      SylkUserDisplay.encode(v!, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkOrganizationDisplay {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkOrganizationDisplay();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.organization = SylkOrganization.decode(reader, reader.uint32());
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.projects.push(SylkProjectDisplay.decode(reader, reader.uint32()));
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.users.push(SylkUserDisplay.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkOrganizationDisplay {
    return {
      organization: isSet(object.organization) ? SylkOrganization.fromJSON(object.organization) : undefined,
      projects: Array.isArray(object?.projects) ? object.projects.map((e: any) => SylkProjectDisplay.fromJSON(e)) : [],
      users: Array.isArray(object?.users) ? object.users.map((e: any) => SylkUserDisplay.fromJSON(e)) : [],
    };
  },

  toJSON(message: SylkOrganizationDisplay): unknown {
    const obj: any = {};
    message.organization !== undefined &&
      (obj.organization = message.organization ? SylkOrganization.toJSON(message.organization) : undefined);
    if (message.projects) {
      obj.projects = message.projects.map((e) => e ? SylkProjectDisplay.toJSON(e) : undefined);
    } else {
      obj.projects = [];
    }
    if (message.users) {
      obj.users = message.users.map((e) => e ? SylkUserDisplay.toJSON(e) : undefined);
    } else {
      obj.users = [];
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkOrganizationDisplay>, I>>(base?: I): SylkOrganizationDisplay {
    return SylkOrganizationDisplay.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkOrganizationDisplay>, I>>(object: I): SylkOrganizationDisplay {
    const message = createBaseSylkOrganizationDisplay();
    message.organization = (object.organization !== undefined && object.organization !== null)
      ? SylkOrganization.fromPartial(object.organization)
      : undefined;
    message.projects = object.projects?.map((e) => SylkProjectDisplay.fromPartial(e)) || [];
    message.users = object.users?.map((e) => SylkUserDisplay.fromPartial(e)) || [];
    return message;
  },
};

function createBaseSylkOrganization(): SylkOrganization {
  return { orgId: "", name: "", owner: "", domain: "" };
}

export const SylkOrganization = {
  encode(message: SylkOrganization, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.orgId !== "") {
      writer.uint32(10).string(message.orgId);
    }
    if (message.name !== "") {
      writer.uint32(18).string(message.name);
    }
    if (message.owner !== "") {
      writer.uint32(34).string(message.owner);
    }
    if (message.domain !== "") {
      writer.uint32(26).string(message.domain);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkOrganization {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkOrganization();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.orgId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.name = reader.string();
          continue;
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

          message.domain = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkOrganization {
    return {
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
      name: isSet(object.name) ? String(object.name) : "",
      owner: isSet(object.owner) ? String(object.owner) : "",
      domain: isSet(object.domain) ? String(object.domain) : "",
    };
  },

  toJSON(message: SylkOrganization): unknown {
    const obj: any = {};
    message.orgId !== undefined && (obj.orgId = message.orgId);
    message.name !== undefined && (obj.name = message.name);
    message.owner !== undefined && (obj.owner = message.owner);
    message.domain !== undefined && (obj.domain = message.domain);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkOrganization>, I>>(base?: I): SylkOrganization {
    return SylkOrganization.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkOrganization>, I>>(object: I): SylkOrganization {
    const message = createBaseSylkOrganization();
    message.orgId = object.orgId ?? "";
    message.name = object.name ?? "";
    message.owner = object.owner ?? "";
    message.domain = object.domain ?? "";
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
