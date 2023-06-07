/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { SylkProjectConfigs } from "../../SylkConfigs/v1/SylkConfigs";
import { SylkOrganization } from "../../SylkOrganization/v1/SylkOrganization";
import { SylkPackage } from "../../SylkPackage/v1/SylkPackage";
import { SylkProject } from "../../SylkProject/v1/SylkProject";
import { SylkService } from "../../SylkService/v1/SylkService";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.Sylk.v1.SylkJson] - None */
export interface SylkJson {
  /** [sylk.Sylk.v1.SylkJson.sylk_version] - The sylk cli version used to generate project resources */
  sylkVersion: string;
  /** [sylk.Sylk.v1.SylkJson.project] - Sylk project metadata */
  project?: SylkProject;
  /** [sylk.Sylk.v1.SylkJson.organization] - The project assigned organization, the details under this field are used to authenticate to sylk.build api's when trying to publish and pull resources from remote project */
  organization?: SylkOrganization;
  services: { [key: string]: SylkService };
  /** [sylk.Sylk.v1.SylkJson.packages] - Sylk project packages map for the project, the map key should be as follows: "protos/<version>/<package>.proto" and the value should be a valid `SylkPackage` */
  packages: { [key: string]: SylkPackage };
  /** [sylk.Sylk.v1.SylkJson.configs] - Sylk project configurations */
  configs?: SylkProjectConfigs;
}

export interface SylkJson_ServicesEntry {
  key: string;
  value?: SylkService;
}

export interface SylkJson_PackagesEntry {
  key: string;
  value?: SylkPackage;
}

function createBaseSylkJson(): SylkJson {
  return {
    sylkVersion: "",
    project: undefined,
    organization: undefined,
    services: {},
    packages: {},
    configs: undefined,
  };
}

export const SylkJson = {
  encode(message: SylkJson, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.sylkVersion !== "") {
      writer.uint32(42).string(message.sylkVersion);
    }
    if (message.project !== undefined) {
      SylkProject.encode(message.project, writer.uint32(50).fork()).ldelim();
    }
    if (message.organization !== undefined) {
      SylkOrganization.encode(message.organization, writer.uint32(10).fork()).ldelim();
    }
    Object.entries(message.services).forEach(([key, value]) => {
      SylkJson_ServicesEntry.encode({ key: key as any, value }, writer.uint32(26).fork()).ldelim();
    });
    Object.entries(message.packages).forEach(([key, value]) => {
      SylkJson_PackagesEntry.encode({ key: key as any, value }, writer.uint32(18).fork()).ldelim();
    });
    if (message.configs !== undefined) {
      SylkProjectConfigs.encode(message.configs, writer.uint32(34).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkJson {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkJson();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 5:
          if (tag !== 42) {
            break;
          }

          message.sylkVersion = reader.string();
          continue;
        case 6:
          if (tag !== 50) {
            break;
          }

          message.project = SylkProject.decode(reader, reader.uint32());
          continue;
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

          const entry3 = SylkJson_ServicesEntry.decode(reader, reader.uint32());
          if (entry3.value !== undefined) {
            message.services[entry3.key] = entry3.value;
          }
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          const entry2 = SylkJson_PackagesEntry.decode(reader, reader.uint32());
          if (entry2.value !== undefined) {
            message.packages[entry2.key] = entry2.value;
          }
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.configs = SylkProjectConfigs.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkJson {
    return {
      sylkVersion: isSet(object.sylkVersion) ? String(object.sylkVersion) : "",
      project: isSet(object.project) ? SylkProject.fromJSON(object.project) : undefined,
      organization: isSet(object.organization) ? SylkOrganization.fromJSON(object.organization) : undefined,
      services: isObject(object.services)
        ? Object.entries(object.services).reduce<{ [key: string]: SylkService }>((acc, [key, value]) => {
          acc[key] = SylkService.fromJSON(value);
          return acc;
        }, {})
        : {},
      packages: isObject(object.packages)
        ? Object.entries(object.packages).reduce<{ [key: string]: SylkPackage }>((acc, [key, value]) => {
          acc[key] = SylkPackage.fromJSON(value);
          return acc;
        }, {})
        : {},
      configs: isSet(object.configs) ? SylkProjectConfigs.fromJSON(object.configs) : undefined,
    };
  },

  toJSON(message: SylkJson): unknown {
    const obj: any = {};
    message.sylkVersion !== undefined && (obj.sylkVersion = message.sylkVersion);
    message.project !== undefined && (obj.project = message.project ? SylkProject.toJSON(message.project) : undefined);
    message.organization !== undefined &&
      (obj.organization = message.organization ? SylkOrganization.toJSON(message.organization) : undefined);
    obj.services = {};
    if (message.services) {
      Object.entries(message.services).forEach(([k, v]) => {
        obj.services[k] = SylkService.toJSON(v);
      });
    }
    obj.packages = {};
    if (message.packages) {
      Object.entries(message.packages).forEach(([k, v]) => {
        obj.packages[k] = SylkPackage.toJSON(v);
      });
    }
    message.configs !== undefined &&
      (obj.configs = message.configs ? SylkProjectConfigs.toJSON(message.configs) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkJson>, I>>(base?: I): SylkJson {
    return SylkJson.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkJson>, I>>(object: I): SylkJson {
    const message = createBaseSylkJson();
    message.sylkVersion = object.sylkVersion ?? "";
    message.project = (object.project !== undefined && object.project !== null)
      ? SylkProject.fromPartial(object.project)
      : undefined;
    message.organization = (object.organization !== undefined && object.organization !== null)
      ? SylkOrganization.fromPartial(object.organization)
      : undefined;
    message.services = Object.entries(object.services ?? {}).reduce<{ [key: string]: SylkService }>(
      (acc, [key, value]) => {
        if (value !== undefined) {
          acc[key] = SylkService.fromPartial(value);
        }
        return acc;
      },
      {},
    );
    message.packages = Object.entries(object.packages ?? {}).reduce<{ [key: string]: SylkPackage }>(
      (acc, [key, value]) => {
        if (value !== undefined) {
          acc[key] = SylkPackage.fromPartial(value);
        }
        return acc;
      },
      {},
    );
    message.configs = (object.configs !== undefined && object.configs !== null)
      ? SylkProjectConfigs.fromPartial(object.configs)
      : undefined;
    return message;
  },
};

function createBaseSylkJson_ServicesEntry(): SylkJson_ServicesEntry {
  return { key: "", value: undefined };
}

export const SylkJson_ServicesEntry = {
  encode(message: SylkJson_ServicesEntry, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.key !== "") {
      writer.uint32(10).string(message.key);
    }
    if (message.value !== undefined) {
      SylkService.encode(message.value, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkJson_ServicesEntry {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkJson_ServicesEntry();
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

          message.value = SylkService.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkJson_ServicesEntry {
    return {
      key: isSet(object.key) ? String(object.key) : "",
      value: isSet(object.value) ? SylkService.fromJSON(object.value) : undefined,
    };
  },

  toJSON(message: SylkJson_ServicesEntry): unknown {
    const obj: any = {};
    message.key !== undefined && (obj.key = message.key);
    message.value !== undefined && (obj.value = message.value ? SylkService.toJSON(message.value) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkJson_ServicesEntry>, I>>(base?: I): SylkJson_ServicesEntry {
    return SylkJson_ServicesEntry.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkJson_ServicesEntry>, I>>(object: I): SylkJson_ServicesEntry {
    const message = createBaseSylkJson_ServicesEntry();
    message.key = object.key ?? "";
    message.value = (object.value !== undefined && object.value !== null)
      ? SylkService.fromPartial(object.value)
      : undefined;
    return message;
  },
};

function createBaseSylkJson_PackagesEntry(): SylkJson_PackagesEntry {
  return { key: "", value: undefined };
}

export const SylkJson_PackagesEntry = {
  encode(message: SylkJson_PackagesEntry, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.key !== "") {
      writer.uint32(10).string(message.key);
    }
    if (message.value !== undefined) {
      SylkPackage.encode(message.value, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): SylkJson_PackagesEntry {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseSylkJson_PackagesEntry();
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

          message.value = SylkPackage.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): SylkJson_PackagesEntry {
    return {
      key: isSet(object.key) ? String(object.key) : "",
      value: isSet(object.value) ? SylkPackage.fromJSON(object.value) : undefined,
    };
  },

  toJSON(message: SylkJson_PackagesEntry): unknown {
    const obj: any = {};
    message.key !== undefined && (obj.key = message.key);
    message.value !== undefined && (obj.value = message.value ? SylkPackage.toJSON(message.value) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<SylkJson_PackagesEntry>, I>>(base?: I): SylkJson_PackagesEntry {
    return SylkJson_PackagesEntry.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<SylkJson_PackagesEntry>, I>>(object: I): SylkJson_PackagesEntry {
    const message = createBaseSylkJson_PackagesEntry();
    message.key = object.key ?? "";
    message.value = (object.value !== undefined && object.value !== null)
      ? SylkPackage.fromPartial(object.value)
      : undefined;
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

function isObject(value: any): boolean {
  return typeof value === "object" && value !== null;
}

function isSet(value: any): boolean {
  return value !== null && value !== undefined;
}
