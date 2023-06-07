/* eslint-disable */
import _m0 from "protobufjs/minimal";
import { Struct } from "../../../google/protobuf/struct";
import { Timestamp } from "../../../google/protobuf/timestamp";
import { SylkEnum, SylkEnumDisplay } from "../../SylkEnum/v1/SylkEnum";
import { SylkEnumValue, SylkEnumValueDisplay } from "../../SylkEnumValue/v1/SylkEnumValue";
import { SylkField, SylkFieldDisplay } from "../../SylkField/v1/SylkField";
import { SylkMessage, SylkMessageDisplay } from "../../SylkMessage/v1/SylkMessage";
import { SylkMethod, SylkMethodDisplay } from "../../SylkMethod/v1/SylkMethod";
import { SylkOrganization, SylkOrganizationDisplay } from "../../SylkOrganization/v1/SylkOrganization";
import { SylkPackage, SylkPackageDisplay } from "../../SylkPackage/v1/SylkPackage";
import { SylkProject, SylkProjectDisplay } from "../../SylkProject/v1/SylkProject";
import { SylkService, SylkServiceDisplay } from "../../SylkService/v1/SylkService";
import {
  PersonalAccessToken,
  SylkUser,
  SylkUserDisplay,
  SylkUserRoles,
  sylkUserRolesFromJSON,
  sylkUserRolesToJSON,
  SylkUserStatuses,
  sylkUserStatusesFromJSON,
  sylkUserStatusesToJSON,
} from "../../SylkUser/v1/SylkUser";

/** sylk.build Generated proto DO NOT EDIT */

/** [sylk.SylkApi.v1.RemoveUserResponse] - None */
export interface RemoveUserResponse {
  status: string;
}

/** [sylk.SylkApi.v1.RemoveUserRequest] - None */
export interface RemoveUserRequest {
  projectId: string;
  userEmail: string;
  orgId: string;
}

/** [sylk.SylkApi.v1.UpdateOrganizationRequest] - None */
export interface UpdateOrganizationRequest {
  orgId: string;
  update?: SylkOrganization;
}

/** [sylk.SylkApi.v1.GetOrganizationResponse] - None */
export interface GetOrganizationResponse {
  result?: SylkOrganizationDisplay;
}

/** [sylk.SylkApi.v1.GetOrganizationRequest] - None */
export interface GetOrganizationRequest {
  orgId: string;
}

/** [sylk.SylkApi.v1.UpdateUserStatusResponse] - None */
export interface UpdateUserStatusResponse {
  status: string;
}

/** [sylk.SylkApi.v1.UpdateUserStatusRequest] - None */
export interface UpdateUserStatusRequest {
  userEmailOrId: string;
  orgId: string;
  status: SylkUserStatuses;
}

/** [sylk.SylkApi.v1.UpdateUserRoleResponse] - None */
export interface UpdateUserRoleResponse {
  status: string;
}

/** [sylk.SylkApi.v1.UpdateUserRoleRequest] - None */
export interface UpdateUserRoleRequest {
  role: SylkUserRoles;
  userId: string;
  orgId: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.DeleteProjectResponse] - None */
export interface DeleteProjectResponse {
  status: string;
}

/** [sylk.SylkApi.v1.DeleteProjectRequest] - None */
export interface DeleteProjectRequest {
  project: string;
}

/** [sylk.SylkApi.v1.UpdateProjectResponse] - None */
export interface UpdateProjectResponse {
  updated?: SylkProjectDisplay;
  projectId: string;
}

/** [sylk.SylkApi.v1.UpdateProjectRequest] - None */
export interface UpdateProjectRequest {
  projectId: string;
  update?: SylkProject;
}

/** [sylk.SylkApi.v1.GetProjectResponse] - None */
export interface GetProjectResponse {
  result?: SylkProjectDisplay;
}

/** [sylk.SylkApi.v1.GetProjectRequest] - None */
export interface GetProjectRequest {
  project: string;
}

/** [sylk.SylkApi.v1.GetUserResponse] - None */
export interface GetUserResponse {
  result?: SylkUserDisplay;
}

/** [sylk.SylkApi.v1.GetUserRequest] - None */
export interface GetUserRequest {
  userId: string;
}

/** [sylk.SylkApi.v1.AddUserResponse] - None */
export interface AddUserResponse {
  status: string;
}

/** [sylk.SylkApi.v1.AddUserRequest] - None */
export interface AddUserRequest {
  role: SylkUserRoles;
  orgId: string;
  project: string;
  userEmail: string;
}

/** [sylk.SylkApi.v1.AcceptUserInviteResponse] - None */
export interface AcceptUserInviteResponse {
  status: string;
}

/** [sylk.SylkApi.v1.AcceptUserInviteRequest] - None */
export interface AcceptUserInviteRequest {
  email: string;
  orgId: string;
}

/** [sylk.SylkApi.v1.UpdateUserResponse] - None */
export interface UpdateUserResponse {
  updated?: SylkUser;
  userId: string;
}

/** [sylk.SylkApi.v1.UpdateUserRequest] - None */
export interface UpdateUserRequest {
  update?: SylkUser;
  userId: string;
}

/** [sylk.SylkApi.v1.CreateUserResponse] - None */
export interface CreateUserResponse {
  user?: SylkUser;
  organization?: SylkOrganization;
}

/** [sylk.SylkApi.v1.CreateUserRequest] - None */
export interface CreateUserRequest {
  orgId: string;
  user?: SylkUser;
}

/** [sylk.SylkApi.v1.ListOrganizationsRequest] - None */
export interface ListOrganizationsRequest {
  userId: string;
}

/** [sylk.SylkApi.v1.UpdateOrganizationResponse] - None */
export interface UpdateOrganizationResponse {
  updated?: SylkOrganization;
  orgId: string;
}

/** [sylk.SylkApi.v1.GetPackageRequest] - None */
export interface GetPackageRequest {
  projectId: string;
  package: string;
}

/** [sylk.SylkApi.v1.GetPackageResponse] - None */
export interface GetPackageResponse {
  result?: SylkPackageDisplay;
}

/** [sylk.SylkApi.v1.CreatePackageRequest] - None */
export interface CreatePackageRequest {
  package?: SylkPackage;
  projectId: string;
}

/** [sylk.SylkApi.v1.CreatePackageResponse] - None */
export interface CreatePackageResponse {
  projectId: string;
  result?: SylkPackageDisplay;
}

/** [sylk.SylkApi.v1.UpdatePackageRequest] - None */
export interface UpdatePackageRequest {
  projectId: string;
  package: string;
  update?: SylkPackage;
}

/** [sylk.SylkApi.v1.UpdatePackageResponse] - None */
export interface UpdatePackageResponse {
  updated?: SylkPackageDisplay;
  package: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.DeletePackageRequest] - None */
export interface DeletePackageRequest {
  projectId: string;
  package: string;
}

/** [sylk.SylkApi.v1.DeletePackageResponse] - None */
export interface DeletePackageResponse {
  package: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.GetServiceRequest] - None */
export interface GetServiceRequest {
  service: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.GetServiceResponse] - None */
export interface GetServiceResponse {
  result?: SylkServiceDisplay;
}

/** [sylk.SylkApi.v1.CreateServiceRequest] - None */
export interface CreateServiceRequest {
  projectId: string;
  service?: SylkService;
}

/** [sylk.SylkApi.v1.CreateServiceResponse] - None */
export interface CreateServiceResponse {
  result?: SylkServiceDisplay;
  projectId: string;
}

/** [sylk.SylkApi.v1.UpdateServiceRequest] - None */
export interface UpdateServiceRequest {
  service: string;
  projectId: string;
  update?: SylkService;
}

/** [sylk.SylkApi.v1.UpdateServiceResponse] - None */
export interface UpdateServiceResponse {
  updated?: SylkServiceDisplay;
  service: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.DeleteServiceRequest] - None */
export interface DeleteServiceRequest {
  projectId: string;
  service: string;
}

/** [sylk.SylkApi.v1.DeleteServiceResponse] - None */
export interface DeleteServiceResponse {
  projectId: string;
  service: string;
}

/** [sylk.SylkApi.v1.ListServicesRequest] - None */
export interface ListServicesRequest {
  projectId: string;
}

/** [sylk.SylkApi.v1.ListPackagesRequest] - None */
export interface ListPackagesRequest {
  projectId: string;
}

/** [sylk.SylkApi.v1.GetMessageRequest] - None */
export interface GetMessageRequest {
  projectId: string;
  message: string;
}

/** [sylk.SylkApi.v1.GetMessageResponse] - None */
export interface GetMessageResponse {
  result?: SylkMessageDisplay;
}

/** [sylk.SylkApi.v1.CreateMessageRequest] - None */
export interface CreateMessageRequest {
  projectId: string;
  package: string;
  message?: SylkMessage;
}

/** [sylk.SylkApi.v1.CreateMessageResponse] - None */
export interface CreateMessageResponse {
  result?: SylkMessageDisplay;
  message: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.UpdateMessageRequest] - None */
export interface UpdateMessageRequest {
  projectId: string;
  message: string;
  update?: SylkMessage;
}

/** [sylk.SylkApi.v1.UpdateMessageResponse] - None */
export interface UpdateMessageResponse {
  message: string;
  updated?: SylkMessageDisplay;
  projectId: string;
}

/** [sylk.SylkApi.v1.DeleteMessageRequest] - None */
export interface DeleteMessageRequest {
  message: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.DeleteMessageResponse] - None */
export interface DeleteMessageResponse {
  projectId: string;
  message: string;
}

/** [sylk.SylkApi.v1.GetMethodRequest] - None */
export interface GetMethodRequest {
  projectId: string;
  method: string;
}

/** [sylk.SylkApi.v1.GetMethodResponse] - None */
export interface GetMethodResponse {
  result?: SylkMethodDisplay;
}

/** [sylk.SylkApi.v1.CreateMethodRequest] - None */
export interface CreateMethodRequest {
  service: string;
  projectId: string;
  method?: SylkMethod;
}

/** [sylk.SylkApi.v1.CreateMethodResponse] - None */
export interface CreateMethodResponse {
  result?: SylkMethodDisplay;
  projectId: string;
  service: string;
}

/** [sylk.SylkApi.v1.UpdateMethodRequest] - None */
export interface UpdateMethodRequest {
  method: string;
  projectId: string;
  update?: SylkMethod;
}

/** [sylk.SylkApi.v1.UpdateMethodResponse] - None */
export interface UpdateMethodResponse {
  method: string;
  projectId: string;
  updated?: SylkMethodDisplay;
}

/** [sylk.SylkApi.v1.DeleteMethodRequest] - None */
export interface DeleteMethodRequest {
  method: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.DeleteMethodResponse] - None */
export interface DeleteMethodResponse {
  method: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.GetFieldRequest] - None */
export interface GetFieldRequest {
  projectId: string;
  field: string;
}

/** [sylk.SylkApi.v1.GetFieldResponse] - None */
export interface GetFieldResponse {
  result?: SylkFieldDisplay;
}

/** [sylk.SylkApi.v1.UpdateFieldRequest] - None */
export interface UpdateFieldRequest {
  field: string;
  projectId: string;
  update?: SylkField;
}

/** [sylk.SylkApi.v1.UpdateFieldResponse] - None */
export interface UpdateFieldResponse {
  projectId: string;
  field: string;
  updated?: SylkFieldDisplay;
}

/** [sylk.SylkApi.v1.DeleteFieldRequest] - None */
export interface DeleteFieldRequest {
  field: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.DeleteFieldResponse] - None */
export interface DeleteFieldResponse {
  field: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.CreateFieldRequest] - None */
export interface CreateFieldRequest {
  projectId: string;
  message: string;
  field?: SylkField;
}

/** [sylk.SylkApi.v1.CreateFieldResponse] - None */
export interface CreateFieldResponse {
  result?: SylkFieldDisplay;
}

/** [sylk.SylkApi.v1.GetEnumRequest] - None */
export interface GetEnumRequest {
  projectId: string;
  enum: string;
}

/** [sylk.SylkApi.v1.GetEnumResponse] - None */
export interface GetEnumResponse {
  result?: SylkEnumDisplay;
}

/** [sylk.SylkApi.v1.CreateEnumRequest] - None */
export interface CreateEnumRequest {
  package: string;
  enum?: SylkEnum;
  projectId: string;
}

/** [sylk.SylkApi.v1.CreateEnumResponse] - None */
export interface CreateEnumResponse {
  result?: SylkEnumDisplay;
  projectId: string;
}

/** [sylk.SylkApi.v1.UpdateEnumRequest] - None */
export interface UpdateEnumRequest {
  update?: SylkEnum;
  enum: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.UpdateEnumResponse] - None */
export interface UpdateEnumResponse {
  enum: string;
  projectId: string;
  updated?: SylkEnumDisplay;
}

/** [sylk.SylkApi.v1.DeleteEnumRequest] - None */
export interface DeleteEnumRequest {
  enum: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.DeleteEnumResponse] - None */
export interface DeleteEnumResponse {
  enum: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.GetEnumValueRequest] - None */
export interface GetEnumValueRequest {
  projectId: string;
  enumValue: string;
}

/** [sylk.SylkApi.v1.GetEnumValueResponse] - None */
export interface GetEnumValueResponse {
  result?: SylkEnumValueDisplay;
}

/** [sylk.SylkApi.v1.CreateEnumValueRequest] - None */
export interface CreateEnumValueRequest {
  enum: string;
  projectId: string;
  enumValue?: SylkEnumValue;
}

/** [sylk.SylkApi.v1.CreateEnumValueResponse] - None */
export interface CreateEnumValueResponse {
  result?: SylkEnumValueDisplay;
}

/** [sylk.SylkApi.v1.UpdateEnumValueRequest] - None */
export interface UpdateEnumValueRequest {
  update?: SylkEnumValue;
  projectId: string;
  enumValue: string;
}

/** [sylk.SylkApi.v1.UpdateEnumValueResponse] - None */
export interface UpdateEnumValueResponse {
  projectId: string;
  updated?: SylkEnumValueDisplay;
  enumValue: string;
}

/** [sylk.SylkApi.v1.DeleteEnumValueRequest] - None */
export interface DeleteEnumValueRequest {
  enumValue: string;
  projectId: string;
}

/** [sylk.SylkApi.v1.DeleteEnumValueResponse] - None */
export interface DeleteEnumValueResponse {
  projectId: string;
  enumValue: string;
}

/** [sylk.SylkApi.v1.ListOrganizationsResponseCache] - None */
export interface ListOrganizationsResponseCache {
  organizations: GetOrganizationResponse[];
}

/** [sylk.SylkApi.v1.ListProjectsRequest] - None */
export interface ListProjectsRequest {
  orgId: string;
}

/** [sylk.SylkApi.v1.CreateProjectRequest] - None */
export interface CreateProjectRequest {
  project?: SylkProject;
  orgId: string;
}

/** [sylk.SylkApi.v1.CreateProjectResponse] - None */
export interface CreateProjectResponse {
  orgId: string;
  result?: SylkProjectDisplay;
}

/** [sylk.SylkApi.v1.ListProjectsResponseCache] - None */
export interface ListProjectsResponseCache {
  projects: GetProjectResponse[];
}

/** [sylk.SylkApi.v1.CachedSession] - None */
export interface CachedSession {
  session?: { [key: string]: any };
}

/** [sylk.SylkApi.v1.CreateAccessTokenRequest] - None */
export interface CreateAccessTokenRequest {
  description: string;
  orgId: string;
  expiresAt?: Date;
}

/** [sylk.SylkApi.v1.CreateAccessTokenResponse] - None */
export interface CreateAccessTokenResponse {
  status: string;
}

/** [sylk.SylkApi.v1.ListAccessTokensRequest] - None */
export interface ListAccessTokensRequest {
  orgId: string;
}

/** [sylk.SylkApi.v1.GetAccessTokenResponse] - None */
export interface GetAccessTokenResponse {
  result?: PersonalAccessToken;
}

/** [sylk.SylkApi.v1.GetAccessTokenRequest] - None */
export interface GetAccessTokenRequest {
  token: string;
}

/** [sylk.SylkApi.v1.RevokeAccessTokenRequest] - None */
export interface RevokeAccessTokenRequest {
  token: string;
  orgId: string;
}

/** [sylk.SylkApi.v1.RevokeAccessTokenResponse] - None */
export interface RevokeAccessTokenResponse {
  status: string;
}

function createBaseRemoveUserResponse(): RemoveUserResponse {
  return { status: "" };
}

export const RemoveUserResponse = {
  encode(message: RemoveUserResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.status !== "") {
      writer.uint32(10).string(message.status);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): RemoveUserResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseRemoveUserResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.status = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): RemoveUserResponse {
    return { status: isSet(object.status) ? String(object.status) : "" };
  },

  toJSON(message: RemoveUserResponse): unknown {
    const obj: any = {};
    message.status !== undefined && (obj.status = message.status);
    return obj;
  },

  create<I extends Exact<DeepPartial<RemoveUserResponse>, I>>(base?: I): RemoveUserResponse {
    return RemoveUserResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<RemoveUserResponse>, I>>(object: I): RemoveUserResponse {
    const message = createBaseRemoveUserResponse();
    message.status = object.status ?? "";
    return message;
  },
};

function createBaseRemoveUserRequest(): RemoveUserRequest {
  return { projectId: "", userEmail: "", orgId: "" };
}

export const RemoveUserRequest = {
  encode(message: RemoveUserRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(26).string(message.projectId);
    }
    if (message.userEmail !== "") {
      writer.uint32(10).string(message.userEmail);
    }
    if (message.orgId !== "") {
      writer.uint32(18).string(message.orgId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): RemoveUserRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseRemoveUserRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 26) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.userEmail = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.orgId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): RemoveUserRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      userEmail: isSet(object.userEmail) ? String(object.userEmail) : "",
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
    };
  },

  toJSON(message: RemoveUserRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.userEmail !== undefined && (obj.userEmail = message.userEmail);
    message.orgId !== undefined && (obj.orgId = message.orgId);
    return obj;
  },

  create<I extends Exact<DeepPartial<RemoveUserRequest>, I>>(base?: I): RemoveUserRequest {
    return RemoveUserRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<RemoveUserRequest>, I>>(object: I): RemoveUserRequest {
    const message = createBaseRemoveUserRequest();
    message.projectId = object.projectId ?? "";
    message.userEmail = object.userEmail ?? "";
    message.orgId = object.orgId ?? "";
    return message;
  },
};

function createBaseUpdateOrganizationRequest(): UpdateOrganizationRequest {
  return { orgId: "", update: undefined };
}

export const UpdateOrganizationRequest = {
  encode(message: UpdateOrganizationRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.orgId !== "") {
      writer.uint32(10).string(message.orgId);
    }
    if (message.update !== undefined) {
      SylkOrganization.encode(message.update, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateOrganizationRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateOrganizationRequest();
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

          message.update = SylkOrganization.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateOrganizationRequest {
    return {
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
      update: isSet(object.update) ? SylkOrganization.fromJSON(object.update) : undefined,
    };
  },

  toJSON(message: UpdateOrganizationRequest): unknown {
    const obj: any = {};
    message.orgId !== undefined && (obj.orgId = message.orgId);
    message.update !== undefined && (obj.update = message.update ? SylkOrganization.toJSON(message.update) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateOrganizationRequest>, I>>(base?: I): UpdateOrganizationRequest {
    return UpdateOrganizationRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateOrganizationRequest>, I>>(object: I): UpdateOrganizationRequest {
    const message = createBaseUpdateOrganizationRequest();
    message.orgId = object.orgId ?? "";
    message.update = (object.update !== undefined && object.update !== null)
      ? SylkOrganization.fromPartial(object.update)
      : undefined;
    return message;
  },
};

function createBaseGetOrganizationResponse(): GetOrganizationResponse {
  return { result: undefined };
}

export const GetOrganizationResponse = {
  encode(message: GetOrganizationResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkOrganizationDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetOrganizationResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetOrganizationResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkOrganizationDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetOrganizationResponse {
    return { result: isSet(object.result) ? SylkOrganizationDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetOrganizationResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkOrganizationDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetOrganizationResponse>, I>>(base?: I): GetOrganizationResponse {
    return GetOrganizationResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetOrganizationResponse>, I>>(object: I): GetOrganizationResponse {
    const message = createBaseGetOrganizationResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkOrganizationDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseGetOrganizationRequest(): GetOrganizationRequest {
  return { orgId: "" };
}

export const GetOrganizationRequest = {
  encode(message: GetOrganizationRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.orgId !== "") {
      writer.uint32(10).string(message.orgId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetOrganizationRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetOrganizationRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.orgId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetOrganizationRequest {
    return { orgId: isSet(object.orgId) ? String(object.orgId) : "" };
  },

  toJSON(message: GetOrganizationRequest): unknown {
    const obj: any = {};
    message.orgId !== undefined && (obj.orgId = message.orgId);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetOrganizationRequest>, I>>(base?: I): GetOrganizationRequest {
    return GetOrganizationRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetOrganizationRequest>, I>>(object: I): GetOrganizationRequest {
    const message = createBaseGetOrganizationRequest();
    message.orgId = object.orgId ?? "";
    return message;
  },
};

function createBaseUpdateUserStatusResponse(): UpdateUserStatusResponse {
  return { status: "" };
}

export const UpdateUserStatusResponse = {
  encode(message: UpdateUserStatusResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.status !== "") {
      writer.uint32(10).string(message.status);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateUserStatusResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateUserStatusResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.status = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateUserStatusResponse {
    return { status: isSet(object.status) ? String(object.status) : "" };
  },

  toJSON(message: UpdateUserStatusResponse): unknown {
    const obj: any = {};
    message.status !== undefined && (obj.status = message.status);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateUserStatusResponse>, I>>(base?: I): UpdateUserStatusResponse {
    return UpdateUserStatusResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateUserStatusResponse>, I>>(object: I): UpdateUserStatusResponse {
    const message = createBaseUpdateUserStatusResponse();
    message.status = object.status ?? "";
    return message;
  },
};

function createBaseUpdateUserStatusRequest(): UpdateUserStatusRequest {
  return { userEmailOrId: "", orgId: "", status: 0 };
}

export const UpdateUserStatusRequest = {
  encode(message: UpdateUserStatusRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.userEmailOrId !== "") {
      writer.uint32(10).string(message.userEmailOrId);
    }
    if (message.orgId !== "") {
      writer.uint32(26).string(message.orgId);
    }
    if (message.status !== 0) {
      writer.uint32(16).int32(message.status);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateUserStatusRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateUserStatusRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.userEmailOrId = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.orgId = reader.string();
          continue;
        case 2:
          if (tag !== 16) {
            break;
          }

          message.status = reader.int32() as any;
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateUserStatusRequest {
    return {
      userEmailOrId: isSet(object.userEmailOrId) ? String(object.userEmailOrId) : "",
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
      status: isSet(object.status) ? sylkUserStatusesFromJSON(object.status) : 0,
    };
  },

  toJSON(message: UpdateUserStatusRequest): unknown {
    const obj: any = {};
    message.userEmailOrId !== undefined && (obj.userEmailOrId = message.userEmailOrId);
    message.orgId !== undefined && (obj.orgId = message.orgId);
    message.status !== undefined && (obj.status = sylkUserStatusesToJSON(message.status));
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateUserStatusRequest>, I>>(base?: I): UpdateUserStatusRequest {
    return UpdateUserStatusRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateUserStatusRequest>, I>>(object: I): UpdateUserStatusRequest {
    const message = createBaseUpdateUserStatusRequest();
    message.userEmailOrId = object.userEmailOrId ?? "";
    message.orgId = object.orgId ?? "";
    message.status = object.status ?? 0;
    return message;
  },
};

function createBaseUpdateUserRoleResponse(): UpdateUserRoleResponse {
  return { status: "" };
}

export const UpdateUserRoleResponse = {
  encode(message: UpdateUserRoleResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.status !== "") {
      writer.uint32(10).string(message.status);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateUserRoleResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateUserRoleResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.status = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateUserRoleResponse {
    return { status: isSet(object.status) ? String(object.status) : "" };
  },

  toJSON(message: UpdateUserRoleResponse): unknown {
    const obj: any = {};
    message.status !== undefined && (obj.status = message.status);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateUserRoleResponse>, I>>(base?: I): UpdateUserRoleResponse {
    return UpdateUserRoleResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateUserRoleResponse>, I>>(object: I): UpdateUserRoleResponse {
    const message = createBaseUpdateUserRoleResponse();
    message.status = object.status ?? "";
    return message;
  },
};

function createBaseUpdateUserRoleRequest(): UpdateUserRoleRequest {
  return { role: 0, userId: "", orgId: "", projectId: "" };
}

export const UpdateUserRoleRequest = {
  encode(message: UpdateUserRoleRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.role !== 0) {
      writer.uint32(24).int32(message.role);
    }
    if (message.userId !== "") {
      writer.uint32(10).string(message.userId);
    }
    if (message.orgId !== "") {
      writer.uint32(18).string(message.orgId);
    }
    if (message.projectId !== "") {
      writer.uint32(34).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateUserRoleRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateUserRoleRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 24) {
            break;
          }

          message.role = reader.int32() as any;
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.userId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.orgId = reader.string();
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateUserRoleRequest {
    return {
      role: isSet(object.role) ? sylkUserRolesFromJSON(object.role) : 0,
      userId: isSet(object.userId) ? String(object.userId) : "",
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: UpdateUserRoleRequest): unknown {
    const obj: any = {};
    message.role !== undefined && (obj.role = sylkUserRolesToJSON(message.role));
    message.userId !== undefined && (obj.userId = message.userId);
    message.orgId !== undefined && (obj.orgId = message.orgId);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateUserRoleRequest>, I>>(base?: I): UpdateUserRoleRequest {
    return UpdateUserRoleRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateUserRoleRequest>, I>>(object: I): UpdateUserRoleRequest {
    const message = createBaseUpdateUserRoleRequest();
    message.role = object.role ?? 0;
    message.userId = object.userId ?? "";
    message.orgId = object.orgId ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseDeleteProjectResponse(): DeleteProjectResponse {
  return { status: "" };
}

export const DeleteProjectResponse = {
  encode(message: DeleteProjectResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.status !== "") {
      writer.uint32(10).string(message.status);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteProjectResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteProjectResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.status = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteProjectResponse {
    return { status: isSet(object.status) ? String(object.status) : "" };
  },

  toJSON(message: DeleteProjectResponse): unknown {
    const obj: any = {};
    message.status !== undefined && (obj.status = message.status);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteProjectResponse>, I>>(base?: I): DeleteProjectResponse {
    return DeleteProjectResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteProjectResponse>, I>>(object: I): DeleteProjectResponse {
    const message = createBaseDeleteProjectResponse();
    message.status = object.status ?? "";
    return message;
  },
};

function createBaseDeleteProjectRequest(): DeleteProjectRequest {
  return { project: "" };
}

export const DeleteProjectRequest = {
  encode(message: DeleteProjectRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.project !== "") {
      writer.uint32(10).string(message.project);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteProjectRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteProjectRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.project = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteProjectRequest {
    return { project: isSet(object.project) ? String(object.project) : "" };
  },

  toJSON(message: DeleteProjectRequest): unknown {
    const obj: any = {};
    message.project !== undefined && (obj.project = message.project);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteProjectRequest>, I>>(base?: I): DeleteProjectRequest {
    return DeleteProjectRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteProjectRequest>, I>>(object: I): DeleteProjectRequest {
    const message = createBaseDeleteProjectRequest();
    message.project = object.project ?? "";
    return message;
  },
};

function createBaseUpdateProjectResponse(): UpdateProjectResponse {
  return { updated: undefined, projectId: "" };
}

export const UpdateProjectResponse = {
  encode(message: UpdateProjectResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.updated !== undefined) {
      SylkProjectDisplay.encode(message.updated, writer.uint32(18).fork()).ldelim();
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateProjectResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateProjectResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.updated = SylkProjectDisplay.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateProjectResponse {
    return {
      updated: isSet(object.updated) ? SylkProjectDisplay.fromJSON(object.updated) : undefined,
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: UpdateProjectResponse): unknown {
    const obj: any = {};
    message.updated !== undefined &&
      (obj.updated = message.updated ? SylkProjectDisplay.toJSON(message.updated) : undefined);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateProjectResponse>, I>>(base?: I): UpdateProjectResponse {
    return UpdateProjectResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateProjectResponse>, I>>(object: I): UpdateProjectResponse {
    const message = createBaseUpdateProjectResponse();
    message.updated = (object.updated !== undefined && object.updated !== null)
      ? SylkProjectDisplay.fromPartial(object.updated)
      : undefined;
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseUpdateProjectRequest(): UpdateProjectRequest {
  return { projectId: "", update: undefined };
}

export const UpdateProjectRequest = {
  encode(message: UpdateProjectRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.update !== undefined) {
      SylkProject.encode(message.update, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateProjectRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateProjectRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.update = SylkProject.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateProjectRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      update: isSet(object.update) ? SylkProject.fromJSON(object.update) : undefined,
    };
  },

  toJSON(message: UpdateProjectRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.update !== undefined && (obj.update = message.update ? SylkProject.toJSON(message.update) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateProjectRequest>, I>>(base?: I): UpdateProjectRequest {
    return UpdateProjectRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateProjectRequest>, I>>(object: I): UpdateProjectRequest {
    const message = createBaseUpdateProjectRequest();
    message.projectId = object.projectId ?? "";
    message.update = (object.update !== undefined && object.update !== null)
      ? SylkProject.fromPartial(object.update)
      : undefined;
    return message;
  },
};

function createBaseGetProjectResponse(): GetProjectResponse {
  return { result: undefined };
}

export const GetProjectResponse = {
  encode(message: GetProjectResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkProjectDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetProjectResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetProjectResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkProjectDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetProjectResponse {
    return { result: isSet(object.result) ? SylkProjectDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetProjectResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkProjectDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetProjectResponse>, I>>(base?: I): GetProjectResponse {
    return GetProjectResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetProjectResponse>, I>>(object: I): GetProjectResponse {
    const message = createBaseGetProjectResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkProjectDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseGetProjectRequest(): GetProjectRequest {
  return { project: "" };
}

export const GetProjectRequest = {
  encode(message: GetProjectRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.project !== "") {
      writer.uint32(10).string(message.project);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetProjectRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetProjectRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.project = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetProjectRequest {
    return { project: isSet(object.project) ? String(object.project) : "" };
  },

  toJSON(message: GetProjectRequest): unknown {
    const obj: any = {};
    message.project !== undefined && (obj.project = message.project);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetProjectRequest>, I>>(base?: I): GetProjectRequest {
    return GetProjectRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetProjectRequest>, I>>(object: I): GetProjectRequest {
    const message = createBaseGetProjectRequest();
    message.project = object.project ?? "";
    return message;
  },
};

function createBaseGetUserResponse(): GetUserResponse {
  return { result: undefined };
}

export const GetUserResponse = {
  encode(message: GetUserResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkUserDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetUserResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetUserResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkUserDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetUserResponse {
    return { result: isSet(object.result) ? SylkUserDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetUserResponse): unknown {
    const obj: any = {};
    message.result !== undefined && (obj.result = message.result ? SylkUserDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetUserResponse>, I>>(base?: I): GetUserResponse {
    return GetUserResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetUserResponse>, I>>(object: I): GetUserResponse {
    const message = createBaseGetUserResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkUserDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseGetUserRequest(): GetUserRequest {
  return { userId: "" };
}

export const GetUserRequest = {
  encode(message: GetUserRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.userId !== "") {
      writer.uint32(10).string(message.userId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetUserRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetUserRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
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

  fromJSON(object: any): GetUserRequest {
    return { userId: isSet(object.userId) ? String(object.userId) : "" };
  },

  toJSON(message: GetUserRequest): unknown {
    const obj: any = {};
    message.userId !== undefined && (obj.userId = message.userId);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetUserRequest>, I>>(base?: I): GetUserRequest {
    return GetUserRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetUserRequest>, I>>(object: I): GetUserRequest {
    const message = createBaseGetUserRequest();
    message.userId = object.userId ?? "";
    return message;
  },
};

function createBaseAddUserResponse(): AddUserResponse {
  return { status: "" };
}

export const AddUserResponse = {
  encode(message: AddUserResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.status !== "") {
      writer.uint32(10).string(message.status);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): AddUserResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseAddUserResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.status = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): AddUserResponse {
    return { status: isSet(object.status) ? String(object.status) : "" };
  },

  toJSON(message: AddUserResponse): unknown {
    const obj: any = {};
    message.status !== undefined && (obj.status = message.status);
    return obj;
  },

  create<I extends Exact<DeepPartial<AddUserResponse>, I>>(base?: I): AddUserResponse {
    return AddUserResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<AddUserResponse>, I>>(object: I): AddUserResponse {
    const message = createBaseAddUserResponse();
    message.status = object.status ?? "";
    return message;
  },
};

function createBaseAddUserRequest(): AddUserRequest {
  return { role: 0, orgId: "", project: "", userEmail: "" };
}

export const AddUserRequest = {
  encode(message: AddUserRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.role !== 0) {
      writer.uint32(16).int32(message.role);
    }
    if (message.orgId !== "") {
      writer.uint32(26).string(message.orgId);
    }
    if (message.project !== "") {
      writer.uint32(34).string(message.project);
    }
    if (message.userEmail !== "") {
      writer.uint32(10).string(message.userEmail);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): AddUserRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseAddUserRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 16) {
            break;
          }

          message.role = reader.int32() as any;
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.orgId = reader.string();
          continue;
        case 4:
          if (tag !== 34) {
            break;
          }

          message.project = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.userEmail = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): AddUserRequest {
    return {
      role: isSet(object.role) ? sylkUserRolesFromJSON(object.role) : 0,
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
      project: isSet(object.project) ? String(object.project) : "",
      userEmail: isSet(object.userEmail) ? String(object.userEmail) : "",
    };
  },

  toJSON(message: AddUserRequest): unknown {
    const obj: any = {};
    message.role !== undefined && (obj.role = sylkUserRolesToJSON(message.role));
    message.orgId !== undefined && (obj.orgId = message.orgId);
    message.project !== undefined && (obj.project = message.project);
    message.userEmail !== undefined && (obj.userEmail = message.userEmail);
    return obj;
  },

  create<I extends Exact<DeepPartial<AddUserRequest>, I>>(base?: I): AddUserRequest {
    return AddUserRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<AddUserRequest>, I>>(object: I): AddUserRequest {
    const message = createBaseAddUserRequest();
    message.role = object.role ?? 0;
    message.orgId = object.orgId ?? "";
    message.project = object.project ?? "";
    message.userEmail = object.userEmail ?? "";
    return message;
  },
};

function createBaseAcceptUserInviteResponse(): AcceptUserInviteResponse {
  return { status: "" };
}

export const AcceptUserInviteResponse = {
  encode(message: AcceptUserInviteResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.status !== "") {
      writer.uint32(10).string(message.status);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): AcceptUserInviteResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseAcceptUserInviteResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.status = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): AcceptUserInviteResponse {
    return { status: isSet(object.status) ? String(object.status) : "" };
  },

  toJSON(message: AcceptUserInviteResponse): unknown {
    const obj: any = {};
    message.status !== undefined && (obj.status = message.status);
    return obj;
  },

  create<I extends Exact<DeepPartial<AcceptUserInviteResponse>, I>>(base?: I): AcceptUserInviteResponse {
    return AcceptUserInviteResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<AcceptUserInviteResponse>, I>>(object: I): AcceptUserInviteResponse {
    const message = createBaseAcceptUserInviteResponse();
    message.status = object.status ?? "";
    return message;
  },
};

function createBaseAcceptUserInviteRequest(): AcceptUserInviteRequest {
  return { email: "", orgId: "" };
}

export const AcceptUserInviteRequest = {
  encode(message: AcceptUserInviteRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.email !== "") {
      writer.uint32(10).string(message.email);
    }
    if (message.orgId !== "") {
      writer.uint32(18).string(message.orgId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): AcceptUserInviteRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseAcceptUserInviteRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.email = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.orgId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): AcceptUserInviteRequest {
    return {
      email: isSet(object.email) ? String(object.email) : "",
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
    };
  },

  toJSON(message: AcceptUserInviteRequest): unknown {
    const obj: any = {};
    message.email !== undefined && (obj.email = message.email);
    message.orgId !== undefined && (obj.orgId = message.orgId);
    return obj;
  },

  create<I extends Exact<DeepPartial<AcceptUserInviteRequest>, I>>(base?: I): AcceptUserInviteRequest {
    return AcceptUserInviteRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<AcceptUserInviteRequest>, I>>(object: I): AcceptUserInviteRequest {
    const message = createBaseAcceptUserInviteRequest();
    message.email = object.email ?? "";
    message.orgId = object.orgId ?? "";
    return message;
  },
};

function createBaseUpdateUserResponse(): UpdateUserResponse {
  return { updated: undefined, userId: "" };
}

export const UpdateUserResponse = {
  encode(message: UpdateUserResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.updated !== undefined) {
      SylkUser.encode(message.updated, writer.uint32(18).fork()).ldelim();
    }
    if (message.userId !== "") {
      writer.uint32(10).string(message.userId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateUserResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateUserResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.updated = SylkUser.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
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

  fromJSON(object: any): UpdateUserResponse {
    return {
      updated: isSet(object.updated) ? SylkUser.fromJSON(object.updated) : undefined,
      userId: isSet(object.userId) ? String(object.userId) : "",
    };
  },

  toJSON(message: UpdateUserResponse): unknown {
    const obj: any = {};
    message.updated !== undefined && (obj.updated = message.updated ? SylkUser.toJSON(message.updated) : undefined);
    message.userId !== undefined && (obj.userId = message.userId);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateUserResponse>, I>>(base?: I): UpdateUserResponse {
    return UpdateUserResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateUserResponse>, I>>(object: I): UpdateUserResponse {
    const message = createBaseUpdateUserResponse();
    message.updated = (object.updated !== undefined && object.updated !== null)
      ? SylkUser.fromPartial(object.updated)
      : undefined;
    message.userId = object.userId ?? "";
    return message;
  },
};

function createBaseUpdateUserRequest(): UpdateUserRequest {
  return { update: undefined, userId: "" };
}

export const UpdateUserRequest = {
  encode(message: UpdateUserRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.update !== undefined) {
      SylkUser.encode(message.update, writer.uint32(18).fork()).ldelim();
    }
    if (message.userId !== "") {
      writer.uint32(10).string(message.userId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateUserRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateUserRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.update = SylkUser.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
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

  fromJSON(object: any): UpdateUserRequest {
    return {
      update: isSet(object.update) ? SylkUser.fromJSON(object.update) : undefined,
      userId: isSet(object.userId) ? String(object.userId) : "",
    };
  },

  toJSON(message: UpdateUserRequest): unknown {
    const obj: any = {};
    message.update !== undefined && (obj.update = message.update ? SylkUser.toJSON(message.update) : undefined);
    message.userId !== undefined && (obj.userId = message.userId);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateUserRequest>, I>>(base?: I): UpdateUserRequest {
    return UpdateUserRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateUserRequest>, I>>(object: I): UpdateUserRequest {
    const message = createBaseUpdateUserRequest();
    message.update = (object.update !== undefined && object.update !== null)
      ? SylkUser.fromPartial(object.update)
      : undefined;
    message.userId = object.userId ?? "";
    return message;
  },
};

function createBaseCreateUserResponse(): CreateUserResponse {
  return { user: undefined, organization: undefined };
}

export const CreateUserResponse = {
  encode(message: CreateUserResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.user !== undefined) {
      SylkUser.encode(message.user, writer.uint32(10).fork()).ldelim();
    }
    if (message.organization !== undefined) {
      SylkOrganization.encode(message.organization, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateUserResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateUserResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.user = SylkUser.decode(reader, reader.uint32());
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.organization = SylkOrganization.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateUserResponse {
    return {
      user: isSet(object.user) ? SylkUser.fromJSON(object.user) : undefined,
      organization: isSet(object.organization) ? SylkOrganization.fromJSON(object.organization) : undefined,
    };
  },

  toJSON(message: CreateUserResponse): unknown {
    const obj: any = {};
    message.user !== undefined && (obj.user = message.user ? SylkUser.toJSON(message.user) : undefined);
    message.organization !== undefined &&
      (obj.organization = message.organization ? SylkOrganization.toJSON(message.organization) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateUserResponse>, I>>(base?: I): CreateUserResponse {
    return CreateUserResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateUserResponse>, I>>(object: I): CreateUserResponse {
    const message = createBaseCreateUserResponse();
    message.user = (object.user !== undefined && object.user !== null) ? SylkUser.fromPartial(object.user) : undefined;
    message.organization = (object.organization !== undefined && object.organization !== null)
      ? SylkOrganization.fromPartial(object.organization)
      : undefined;
    return message;
  },
};

function createBaseCreateUserRequest(): CreateUserRequest {
  return { orgId: "", user: undefined };
}

export const CreateUserRequest = {
  encode(message: CreateUserRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.orgId !== "") {
      writer.uint32(10).string(message.orgId);
    }
    if (message.user !== undefined) {
      SylkUser.encode(message.user, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateUserRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateUserRequest();
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

          message.user = SylkUser.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateUserRequest {
    return {
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
      user: isSet(object.user) ? SylkUser.fromJSON(object.user) : undefined,
    };
  },

  toJSON(message: CreateUserRequest): unknown {
    const obj: any = {};
    message.orgId !== undefined && (obj.orgId = message.orgId);
    message.user !== undefined && (obj.user = message.user ? SylkUser.toJSON(message.user) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateUserRequest>, I>>(base?: I): CreateUserRequest {
    return CreateUserRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateUserRequest>, I>>(object: I): CreateUserRequest {
    const message = createBaseCreateUserRequest();
    message.orgId = object.orgId ?? "";
    message.user = (object.user !== undefined && object.user !== null) ? SylkUser.fromPartial(object.user) : undefined;
    return message;
  },
};

function createBaseListOrganizationsRequest(): ListOrganizationsRequest {
  return { userId: "" };
}

export const ListOrganizationsRequest = {
  encode(message: ListOrganizationsRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.userId !== "") {
      writer.uint32(10).string(message.userId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListOrganizationsRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseListOrganizationsRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
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

  fromJSON(object: any): ListOrganizationsRequest {
    return { userId: isSet(object.userId) ? String(object.userId) : "" };
  },

  toJSON(message: ListOrganizationsRequest): unknown {
    const obj: any = {};
    message.userId !== undefined && (obj.userId = message.userId);
    return obj;
  },

  create<I extends Exact<DeepPartial<ListOrganizationsRequest>, I>>(base?: I): ListOrganizationsRequest {
    return ListOrganizationsRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<ListOrganizationsRequest>, I>>(object: I): ListOrganizationsRequest {
    const message = createBaseListOrganizationsRequest();
    message.userId = object.userId ?? "";
    return message;
  },
};

function createBaseUpdateOrganizationResponse(): UpdateOrganizationResponse {
  return { updated: undefined, orgId: "" };
}

export const UpdateOrganizationResponse = {
  encode(message: UpdateOrganizationResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.updated !== undefined) {
      SylkOrganization.encode(message.updated, writer.uint32(18).fork()).ldelim();
    }
    if (message.orgId !== "") {
      writer.uint32(10).string(message.orgId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateOrganizationResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateOrganizationResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.updated = SylkOrganization.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.orgId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateOrganizationResponse {
    return {
      updated: isSet(object.updated) ? SylkOrganization.fromJSON(object.updated) : undefined,
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
    };
  },

  toJSON(message: UpdateOrganizationResponse): unknown {
    const obj: any = {};
    message.updated !== undefined &&
      (obj.updated = message.updated ? SylkOrganization.toJSON(message.updated) : undefined);
    message.orgId !== undefined && (obj.orgId = message.orgId);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateOrganizationResponse>, I>>(base?: I): UpdateOrganizationResponse {
    return UpdateOrganizationResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateOrganizationResponse>, I>>(object: I): UpdateOrganizationResponse {
    const message = createBaseUpdateOrganizationResponse();
    message.updated = (object.updated !== undefined && object.updated !== null)
      ? SylkOrganization.fromPartial(object.updated)
      : undefined;
    message.orgId = object.orgId ?? "";
    return message;
  },
};

function createBaseGetPackageRequest(): GetPackageRequest {
  return { projectId: "", package: "" };
}

export const GetPackageRequest = {
  encode(message: GetPackageRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.package !== "") {
      writer.uint32(18).string(message.package);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetPackageRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetPackageRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.package = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetPackageRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      package: isSet(object.package) ? String(object.package) : "",
    };
  },

  toJSON(message: GetPackageRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.package !== undefined && (obj.package = message.package);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetPackageRequest>, I>>(base?: I): GetPackageRequest {
    return GetPackageRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetPackageRequest>, I>>(object: I): GetPackageRequest {
    const message = createBaseGetPackageRequest();
    message.projectId = object.projectId ?? "";
    message.package = object.package ?? "";
    return message;
  },
};

function createBaseGetPackageResponse(): GetPackageResponse {
  return { result: undefined };
}

export const GetPackageResponse = {
  encode(message: GetPackageResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkPackageDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetPackageResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetPackageResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkPackageDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetPackageResponse {
    return { result: isSet(object.result) ? SylkPackageDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetPackageResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkPackageDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetPackageResponse>, I>>(base?: I): GetPackageResponse {
    return GetPackageResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetPackageResponse>, I>>(object: I): GetPackageResponse {
    const message = createBaseGetPackageResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkPackageDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseCreatePackageRequest(): CreatePackageRequest {
  return { package: undefined, projectId: "" };
}

export const CreatePackageRequest = {
  encode(message: CreatePackageRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.package !== undefined) {
      SylkPackage.encode(message.package, writer.uint32(18).fork()).ldelim();
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreatePackageRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreatePackageRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.package = SylkPackage.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreatePackageRequest {
    return {
      package: isSet(object.package) ? SylkPackage.fromJSON(object.package) : undefined,
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: CreatePackageRequest): unknown {
    const obj: any = {};
    message.package !== undefined && (obj.package = message.package ? SylkPackage.toJSON(message.package) : undefined);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreatePackageRequest>, I>>(base?: I): CreatePackageRequest {
    return CreatePackageRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreatePackageRequest>, I>>(object: I): CreatePackageRequest {
    const message = createBaseCreatePackageRequest();
    message.package = (object.package !== undefined && object.package !== null)
      ? SylkPackage.fromPartial(object.package)
      : undefined;
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseCreatePackageResponse(): CreatePackageResponse {
  return { projectId: "", result: undefined };
}

export const CreatePackageResponse = {
  encode(message: CreatePackageResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.result !== undefined) {
      SylkPackageDisplay.encode(message.result, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreatePackageResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreatePackageResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.result = SylkPackageDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreatePackageResponse {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      result: isSet(object.result) ? SylkPackageDisplay.fromJSON(object.result) : undefined,
    };
  },

  toJSON(message: CreatePackageResponse): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.result !== undefined &&
      (obj.result = message.result ? SylkPackageDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreatePackageResponse>, I>>(base?: I): CreatePackageResponse {
    return CreatePackageResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreatePackageResponse>, I>>(object: I): CreatePackageResponse {
    const message = createBaseCreatePackageResponse();
    message.projectId = object.projectId ?? "";
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkPackageDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseUpdatePackageRequest(): UpdatePackageRequest {
  return { projectId: "", package: "", update: undefined };
}

export const UpdatePackageRequest = {
  encode(message: UpdatePackageRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(18).string(message.projectId);
    }
    if (message.package !== "") {
      writer.uint32(10).string(message.package);
    }
    if (message.update !== undefined) {
      SylkPackage.encode(message.update, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdatePackageRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdatePackageRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.package = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.update = SylkPackage.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdatePackageRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      package: isSet(object.package) ? String(object.package) : "",
      update: isSet(object.update) ? SylkPackage.fromJSON(object.update) : undefined,
    };
  },

  toJSON(message: UpdatePackageRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.package !== undefined && (obj.package = message.package);
    message.update !== undefined && (obj.update = message.update ? SylkPackage.toJSON(message.update) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdatePackageRequest>, I>>(base?: I): UpdatePackageRequest {
    return UpdatePackageRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdatePackageRequest>, I>>(object: I): UpdatePackageRequest {
    const message = createBaseUpdatePackageRequest();
    message.projectId = object.projectId ?? "";
    message.package = object.package ?? "";
    message.update = (object.update !== undefined && object.update !== null)
      ? SylkPackage.fromPartial(object.update)
      : undefined;
    return message;
  },
};

function createBaseUpdatePackageResponse(): UpdatePackageResponse {
  return { updated: undefined, package: "", projectId: "" };
}

export const UpdatePackageResponse = {
  encode(message: UpdatePackageResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.updated !== undefined) {
      SylkPackageDisplay.encode(message.updated, writer.uint32(26).fork()).ldelim();
    }
    if (message.package !== "") {
      writer.uint32(18).string(message.package);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdatePackageResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdatePackageResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updated = SylkPackageDisplay.decode(reader, reader.uint32());
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.package = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdatePackageResponse {
    return {
      updated: isSet(object.updated) ? SylkPackageDisplay.fromJSON(object.updated) : undefined,
      package: isSet(object.package) ? String(object.package) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: UpdatePackageResponse): unknown {
    const obj: any = {};
    message.updated !== undefined &&
      (obj.updated = message.updated ? SylkPackageDisplay.toJSON(message.updated) : undefined);
    message.package !== undefined && (obj.package = message.package);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdatePackageResponse>, I>>(base?: I): UpdatePackageResponse {
    return UpdatePackageResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdatePackageResponse>, I>>(object: I): UpdatePackageResponse {
    const message = createBaseUpdatePackageResponse();
    message.updated = (object.updated !== undefined && object.updated !== null)
      ? SylkPackageDisplay.fromPartial(object.updated)
      : undefined;
    message.package = object.package ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseDeletePackageRequest(): DeletePackageRequest {
  return { projectId: "", package: "" };
}

export const DeletePackageRequest = {
  encode(message: DeletePackageRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(18).string(message.projectId);
    }
    if (message.package !== "") {
      writer.uint32(10).string(message.package);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeletePackageRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeletePackageRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.package = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeletePackageRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      package: isSet(object.package) ? String(object.package) : "",
    };
  },

  toJSON(message: DeletePackageRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.package !== undefined && (obj.package = message.package);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeletePackageRequest>, I>>(base?: I): DeletePackageRequest {
    return DeletePackageRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeletePackageRequest>, I>>(object: I): DeletePackageRequest {
    const message = createBaseDeletePackageRequest();
    message.projectId = object.projectId ?? "";
    message.package = object.package ?? "";
    return message;
  },
};

function createBaseDeletePackageResponse(): DeletePackageResponse {
  return { package: "", projectId: "" };
}

export const DeletePackageResponse = {
  encode(message: DeletePackageResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.package !== "") {
      writer.uint32(18).string(message.package);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeletePackageResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeletePackageResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.package = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeletePackageResponse {
    return {
      package: isSet(object.package) ? String(object.package) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: DeletePackageResponse): unknown {
    const obj: any = {};
    message.package !== undefined && (obj.package = message.package);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeletePackageResponse>, I>>(base?: I): DeletePackageResponse {
    return DeletePackageResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeletePackageResponse>, I>>(object: I): DeletePackageResponse {
    const message = createBaseDeletePackageResponse();
    message.package = object.package ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseGetServiceRequest(): GetServiceRequest {
  return { service: "", projectId: "" };
}

export const GetServiceRequest = {
  encode(message: GetServiceRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.service !== "") {
      writer.uint32(18).string(message.service);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetServiceRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetServiceRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.service = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetServiceRequest {
    return {
      service: isSet(object.service) ? String(object.service) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: GetServiceRequest): unknown {
    const obj: any = {};
    message.service !== undefined && (obj.service = message.service);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetServiceRequest>, I>>(base?: I): GetServiceRequest {
    return GetServiceRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetServiceRequest>, I>>(object: I): GetServiceRequest {
    const message = createBaseGetServiceRequest();
    message.service = object.service ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseGetServiceResponse(): GetServiceResponse {
  return { result: undefined };
}

export const GetServiceResponse = {
  encode(message: GetServiceResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkServiceDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetServiceResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetServiceResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkServiceDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetServiceResponse {
    return { result: isSet(object.result) ? SylkServiceDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetServiceResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkServiceDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetServiceResponse>, I>>(base?: I): GetServiceResponse {
    return GetServiceResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetServiceResponse>, I>>(object: I): GetServiceResponse {
    const message = createBaseGetServiceResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkServiceDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseCreateServiceRequest(): CreateServiceRequest {
  return { projectId: "", service: undefined };
}

export const CreateServiceRequest = {
  encode(message: CreateServiceRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.service !== undefined) {
      SylkService.encode(message.service, writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateServiceRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateServiceRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.service = SylkService.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateServiceRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      service: isSet(object.service) ? SylkService.fromJSON(object.service) : undefined,
    };
  },

  toJSON(message: CreateServiceRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.service !== undefined && (obj.service = message.service ? SylkService.toJSON(message.service) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateServiceRequest>, I>>(base?: I): CreateServiceRequest {
    return CreateServiceRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateServiceRequest>, I>>(object: I): CreateServiceRequest {
    const message = createBaseCreateServiceRequest();
    message.projectId = object.projectId ?? "";
    message.service = (object.service !== undefined && object.service !== null)
      ? SylkService.fromPartial(object.service)
      : undefined;
    return message;
  },
};

function createBaseCreateServiceResponse(): CreateServiceResponse {
  return { result: undefined, projectId: "" };
}

export const CreateServiceResponse = {
  encode(message: CreateServiceResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkServiceDisplay.encode(message.result, writer.uint32(18).fork()).ldelim();
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateServiceResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateServiceResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.result = SylkServiceDisplay.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateServiceResponse {
    return {
      result: isSet(object.result) ? SylkServiceDisplay.fromJSON(object.result) : undefined,
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: CreateServiceResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkServiceDisplay.toJSON(message.result) : undefined);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateServiceResponse>, I>>(base?: I): CreateServiceResponse {
    return CreateServiceResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateServiceResponse>, I>>(object: I): CreateServiceResponse {
    const message = createBaseCreateServiceResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkServiceDisplay.fromPartial(object.result)
      : undefined;
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseUpdateServiceRequest(): UpdateServiceRequest {
  return { service: "", projectId: "", update: undefined };
}

export const UpdateServiceRequest = {
  encode(message: UpdateServiceRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.service !== "") {
      writer.uint32(18).string(message.service);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.update !== undefined) {
      SylkService.encode(message.update, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateServiceRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateServiceRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.service = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.update = SylkService.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateServiceRequest {
    return {
      service: isSet(object.service) ? String(object.service) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      update: isSet(object.update) ? SylkService.fromJSON(object.update) : undefined,
    };
  },

  toJSON(message: UpdateServiceRequest): unknown {
    const obj: any = {};
    message.service !== undefined && (obj.service = message.service);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.update !== undefined && (obj.update = message.update ? SylkService.toJSON(message.update) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateServiceRequest>, I>>(base?: I): UpdateServiceRequest {
    return UpdateServiceRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateServiceRequest>, I>>(object: I): UpdateServiceRequest {
    const message = createBaseUpdateServiceRequest();
    message.service = object.service ?? "";
    message.projectId = object.projectId ?? "";
    message.update = (object.update !== undefined && object.update !== null)
      ? SylkService.fromPartial(object.update)
      : undefined;
    return message;
  },
};

function createBaseUpdateServiceResponse(): UpdateServiceResponse {
  return { updated: undefined, service: "", projectId: "" };
}

export const UpdateServiceResponse = {
  encode(message: UpdateServiceResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.updated !== undefined) {
      SylkServiceDisplay.encode(message.updated, writer.uint32(26).fork()).ldelim();
    }
    if (message.service !== "") {
      writer.uint32(18).string(message.service);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateServiceResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateServiceResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updated = SylkServiceDisplay.decode(reader, reader.uint32());
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.service = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateServiceResponse {
    return {
      updated: isSet(object.updated) ? SylkServiceDisplay.fromJSON(object.updated) : undefined,
      service: isSet(object.service) ? String(object.service) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: UpdateServiceResponse): unknown {
    const obj: any = {};
    message.updated !== undefined &&
      (obj.updated = message.updated ? SylkServiceDisplay.toJSON(message.updated) : undefined);
    message.service !== undefined && (obj.service = message.service);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateServiceResponse>, I>>(base?: I): UpdateServiceResponse {
    return UpdateServiceResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateServiceResponse>, I>>(object: I): UpdateServiceResponse {
    const message = createBaseUpdateServiceResponse();
    message.updated = (object.updated !== undefined && object.updated !== null)
      ? SylkServiceDisplay.fromPartial(object.updated)
      : undefined;
    message.service = object.service ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseDeleteServiceRequest(): DeleteServiceRequest {
  return { projectId: "", service: "" };
}

export const DeleteServiceRequest = {
  encode(message: DeleteServiceRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.service !== "") {
      writer.uint32(18).string(message.service);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteServiceRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteServiceRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.service = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteServiceRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      service: isSet(object.service) ? String(object.service) : "",
    };
  },

  toJSON(message: DeleteServiceRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.service !== undefined && (obj.service = message.service);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteServiceRequest>, I>>(base?: I): DeleteServiceRequest {
    return DeleteServiceRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteServiceRequest>, I>>(object: I): DeleteServiceRequest {
    const message = createBaseDeleteServiceRequest();
    message.projectId = object.projectId ?? "";
    message.service = object.service ?? "";
    return message;
  },
};

function createBaseDeleteServiceResponse(): DeleteServiceResponse {
  return { projectId: "", service: "" };
}

export const DeleteServiceResponse = {
  encode(message: DeleteServiceResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.service !== "") {
      writer.uint32(18).string(message.service);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteServiceResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteServiceResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.service = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteServiceResponse {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      service: isSet(object.service) ? String(object.service) : "",
    };
  },

  toJSON(message: DeleteServiceResponse): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.service !== undefined && (obj.service = message.service);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteServiceResponse>, I>>(base?: I): DeleteServiceResponse {
    return DeleteServiceResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteServiceResponse>, I>>(object: I): DeleteServiceResponse {
    const message = createBaseDeleteServiceResponse();
    message.projectId = object.projectId ?? "";
    message.service = object.service ?? "";
    return message;
  },
};

function createBaseListServicesRequest(): ListServicesRequest {
  return { projectId: "" };
}

export const ListServicesRequest = {
  encode(message: ListServicesRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListServicesRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseListServicesRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): ListServicesRequest {
    return { projectId: isSet(object.projectId) ? String(object.projectId) : "" };
  },

  toJSON(message: ListServicesRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<ListServicesRequest>, I>>(base?: I): ListServicesRequest {
    return ListServicesRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<ListServicesRequest>, I>>(object: I): ListServicesRequest {
    const message = createBaseListServicesRequest();
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseListPackagesRequest(): ListPackagesRequest {
  return { projectId: "" };
}

export const ListPackagesRequest = {
  encode(message: ListPackagesRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListPackagesRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseListPackagesRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): ListPackagesRequest {
    return { projectId: isSet(object.projectId) ? String(object.projectId) : "" };
  },

  toJSON(message: ListPackagesRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<ListPackagesRequest>, I>>(base?: I): ListPackagesRequest {
    return ListPackagesRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<ListPackagesRequest>, I>>(object: I): ListPackagesRequest {
    const message = createBaseListPackagesRequest();
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseGetMessageRequest(): GetMessageRequest {
  return { projectId: "", message: "" };
}

export const GetMessageRequest = {
  encode(message: GetMessageRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.message !== "") {
      writer.uint32(18).string(message.message);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetMessageRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetMessageRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.message = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetMessageRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      message: isSet(object.message) ? String(object.message) : "",
    };
  },

  toJSON(message: GetMessageRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.message !== undefined && (obj.message = message.message);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetMessageRequest>, I>>(base?: I): GetMessageRequest {
    return GetMessageRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetMessageRequest>, I>>(object: I): GetMessageRequest {
    const message = createBaseGetMessageRequest();
    message.projectId = object.projectId ?? "";
    message.message = object.message ?? "";
    return message;
  },
};

function createBaseGetMessageResponse(): GetMessageResponse {
  return { result: undefined };
}

export const GetMessageResponse = {
  encode(message: GetMessageResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkMessageDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetMessageResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetMessageResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkMessageDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetMessageResponse {
    return { result: isSet(object.result) ? SylkMessageDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetMessageResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkMessageDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetMessageResponse>, I>>(base?: I): GetMessageResponse {
    return GetMessageResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetMessageResponse>, I>>(object: I): GetMessageResponse {
    const message = createBaseGetMessageResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkMessageDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseCreateMessageRequest(): CreateMessageRequest {
  return { projectId: "", package: "", message: undefined };
}

export const CreateMessageRequest = {
  encode(message: CreateMessageRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.package !== "") {
      writer.uint32(18).string(message.package);
    }
    if (message.message !== undefined) {
      SylkMessage.encode(message.message, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateMessageRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateMessageRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.package = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.message = SylkMessage.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateMessageRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      package: isSet(object.package) ? String(object.package) : "",
      message: isSet(object.message) ? SylkMessage.fromJSON(object.message) : undefined,
    };
  },

  toJSON(message: CreateMessageRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.package !== undefined && (obj.package = message.package);
    message.message !== undefined && (obj.message = message.message ? SylkMessage.toJSON(message.message) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateMessageRequest>, I>>(base?: I): CreateMessageRequest {
    return CreateMessageRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateMessageRequest>, I>>(object: I): CreateMessageRequest {
    const message = createBaseCreateMessageRequest();
    message.projectId = object.projectId ?? "";
    message.package = object.package ?? "";
    message.message = (object.message !== undefined && object.message !== null)
      ? SylkMessage.fromPartial(object.message)
      : undefined;
    return message;
  },
};

function createBaseCreateMessageResponse(): CreateMessageResponse {
  return { result: undefined, message: "", projectId: "" };
}

export const CreateMessageResponse = {
  encode(message: CreateMessageResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkMessageDisplay.encode(message.result, writer.uint32(26).fork()).ldelim();
    }
    if (message.message !== "") {
      writer.uint32(18).string(message.message);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateMessageResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateMessageResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 26) {
            break;
          }

          message.result = SylkMessageDisplay.decode(reader, reader.uint32());
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.message = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateMessageResponse {
    return {
      result: isSet(object.result) ? SylkMessageDisplay.fromJSON(object.result) : undefined,
      message: isSet(object.message) ? String(object.message) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: CreateMessageResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkMessageDisplay.toJSON(message.result) : undefined);
    message.message !== undefined && (obj.message = message.message);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateMessageResponse>, I>>(base?: I): CreateMessageResponse {
    return CreateMessageResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateMessageResponse>, I>>(object: I): CreateMessageResponse {
    const message = createBaseCreateMessageResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkMessageDisplay.fromPartial(object.result)
      : undefined;
    message.message = object.message ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseUpdateMessageRequest(): UpdateMessageRequest {
  return { projectId: "", message: "", update: undefined };
}

export const UpdateMessageRequest = {
  encode(message: UpdateMessageRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.message !== "") {
      writer.uint32(18).string(message.message);
    }
    if (message.update !== undefined) {
      SylkMessage.encode(message.update, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateMessageRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateMessageRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.message = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.update = SylkMessage.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateMessageRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      message: isSet(object.message) ? String(object.message) : "",
      update: isSet(object.update) ? SylkMessage.fromJSON(object.update) : undefined,
    };
  },

  toJSON(message: UpdateMessageRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.message !== undefined && (obj.message = message.message);
    message.update !== undefined && (obj.update = message.update ? SylkMessage.toJSON(message.update) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateMessageRequest>, I>>(base?: I): UpdateMessageRequest {
    return UpdateMessageRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateMessageRequest>, I>>(object: I): UpdateMessageRequest {
    const message = createBaseUpdateMessageRequest();
    message.projectId = object.projectId ?? "";
    message.message = object.message ?? "";
    message.update = (object.update !== undefined && object.update !== null)
      ? SylkMessage.fromPartial(object.update)
      : undefined;
    return message;
  },
};

function createBaseUpdateMessageResponse(): UpdateMessageResponse {
  return { message: "", updated: undefined, projectId: "" };
}

export const UpdateMessageResponse = {
  encode(message: UpdateMessageResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.message !== "") {
      writer.uint32(18).string(message.message);
    }
    if (message.updated !== undefined) {
      SylkMessageDisplay.encode(message.updated, writer.uint32(26).fork()).ldelim();
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateMessageResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateMessageResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.message = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updated = SylkMessageDisplay.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateMessageResponse {
    return {
      message: isSet(object.message) ? String(object.message) : "",
      updated: isSet(object.updated) ? SylkMessageDisplay.fromJSON(object.updated) : undefined,
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: UpdateMessageResponse): unknown {
    const obj: any = {};
    message.message !== undefined && (obj.message = message.message);
    message.updated !== undefined &&
      (obj.updated = message.updated ? SylkMessageDisplay.toJSON(message.updated) : undefined);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateMessageResponse>, I>>(base?: I): UpdateMessageResponse {
    return UpdateMessageResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateMessageResponse>, I>>(object: I): UpdateMessageResponse {
    const message = createBaseUpdateMessageResponse();
    message.message = object.message ?? "";
    message.updated = (object.updated !== undefined && object.updated !== null)
      ? SylkMessageDisplay.fromPartial(object.updated)
      : undefined;
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseDeleteMessageRequest(): DeleteMessageRequest {
  return { message: "", projectId: "" };
}

export const DeleteMessageRequest = {
  encode(message: DeleteMessageRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.message !== "") {
      writer.uint32(18).string(message.message);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteMessageRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteMessageRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.message = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteMessageRequest {
    return {
      message: isSet(object.message) ? String(object.message) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: DeleteMessageRequest): unknown {
    const obj: any = {};
    message.message !== undefined && (obj.message = message.message);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteMessageRequest>, I>>(base?: I): DeleteMessageRequest {
    return DeleteMessageRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteMessageRequest>, I>>(object: I): DeleteMessageRequest {
    const message = createBaseDeleteMessageRequest();
    message.message = object.message ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseDeleteMessageResponse(): DeleteMessageResponse {
  return { projectId: "", message: "" };
}

export const DeleteMessageResponse = {
  encode(message: DeleteMessageResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.message !== "") {
      writer.uint32(18).string(message.message);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteMessageResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteMessageResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.message = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteMessageResponse {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      message: isSet(object.message) ? String(object.message) : "",
    };
  },

  toJSON(message: DeleteMessageResponse): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.message !== undefined && (obj.message = message.message);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteMessageResponse>, I>>(base?: I): DeleteMessageResponse {
    return DeleteMessageResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteMessageResponse>, I>>(object: I): DeleteMessageResponse {
    const message = createBaseDeleteMessageResponse();
    message.projectId = object.projectId ?? "";
    message.message = object.message ?? "";
    return message;
  },
};

function createBaseGetMethodRequest(): GetMethodRequest {
  return { projectId: "", method: "" };
}

export const GetMethodRequest = {
  encode(message: GetMethodRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.method !== "") {
      writer.uint32(18).string(message.method);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetMethodRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetMethodRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.method = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetMethodRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      method: isSet(object.method) ? String(object.method) : "",
    };
  },

  toJSON(message: GetMethodRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.method !== undefined && (obj.method = message.method);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetMethodRequest>, I>>(base?: I): GetMethodRequest {
    return GetMethodRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetMethodRequest>, I>>(object: I): GetMethodRequest {
    const message = createBaseGetMethodRequest();
    message.projectId = object.projectId ?? "";
    message.method = object.method ?? "";
    return message;
  },
};

function createBaseGetMethodResponse(): GetMethodResponse {
  return { result: undefined };
}

export const GetMethodResponse = {
  encode(message: GetMethodResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkMethodDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetMethodResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetMethodResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkMethodDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetMethodResponse {
    return { result: isSet(object.result) ? SylkMethodDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetMethodResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkMethodDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetMethodResponse>, I>>(base?: I): GetMethodResponse {
    return GetMethodResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetMethodResponse>, I>>(object: I): GetMethodResponse {
    const message = createBaseGetMethodResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkMethodDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseCreateMethodRequest(): CreateMethodRequest {
  return { service: "", projectId: "", method: undefined };
}

export const CreateMethodRequest = {
  encode(message: CreateMethodRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.service !== "") {
      writer.uint32(18).string(message.service);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.method !== undefined) {
      SylkMethod.encode(message.method, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateMethodRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateMethodRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.service = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.method = SylkMethod.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateMethodRequest {
    return {
      service: isSet(object.service) ? String(object.service) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      method: isSet(object.method) ? SylkMethod.fromJSON(object.method) : undefined,
    };
  },

  toJSON(message: CreateMethodRequest): unknown {
    const obj: any = {};
    message.service !== undefined && (obj.service = message.service);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.method !== undefined && (obj.method = message.method ? SylkMethod.toJSON(message.method) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateMethodRequest>, I>>(base?: I): CreateMethodRequest {
    return CreateMethodRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateMethodRequest>, I>>(object: I): CreateMethodRequest {
    const message = createBaseCreateMethodRequest();
    message.service = object.service ?? "";
    message.projectId = object.projectId ?? "";
    message.method = (object.method !== undefined && object.method !== null)
      ? SylkMethod.fromPartial(object.method)
      : undefined;
    return message;
  },
};

function createBaseCreateMethodResponse(): CreateMethodResponse {
  return { result: undefined, projectId: "", service: "" };
}

export const CreateMethodResponse = {
  encode(message: CreateMethodResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkMethodDisplay.encode(message.result, writer.uint32(26).fork()).ldelim();
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.service !== "") {
      writer.uint32(18).string(message.service);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateMethodResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateMethodResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 26) {
            break;
          }

          message.result = SylkMethodDisplay.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.service = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateMethodResponse {
    return {
      result: isSet(object.result) ? SylkMethodDisplay.fromJSON(object.result) : undefined,
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      service: isSet(object.service) ? String(object.service) : "",
    };
  },

  toJSON(message: CreateMethodResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkMethodDisplay.toJSON(message.result) : undefined);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.service !== undefined && (obj.service = message.service);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateMethodResponse>, I>>(base?: I): CreateMethodResponse {
    return CreateMethodResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateMethodResponse>, I>>(object: I): CreateMethodResponse {
    const message = createBaseCreateMethodResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkMethodDisplay.fromPartial(object.result)
      : undefined;
    message.projectId = object.projectId ?? "";
    message.service = object.service ?? "";
    return message;
  },
};

function createBaseUpdateMethodRequest(): UpdateMethodRequest {
  return { method: "", projectId: "", update: undefined };
}

export const UpdateMethodRequest = {
  encode(message: UpdateMethodRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.method !== "") {
      writer.uint32(18).string(message.method);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.update !== undefined) {
      SylkMethod.encode(message.update, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateMethodRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateMethodRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.method = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.update = SylkMethod.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateMethodRequest {
    return {
      method: isSet(object.method) ? String(object.method) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      update: isSet(object.update) ? SylkMethod.fromJSON(object.update) : undefined,
    };
  },

  toJSON(message: UpdateMethodRequest): unknown {
    const obj: any = {};
    message.method !== undefined && (obj.method = message.method);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.update !== undefined && (obj.update = message.update ? SylkMethod.toJSON(message.update) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateMethodRequest>, I>>(base?: I): UpdateMethodRequest {
    return UpdateMethodRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateMethodRequest>, I>>(object: I): UpdateMethodRequest {
    const message = createBaseUpdateMethodRequest();
    message.method = object.method ?? "";
    message.projectId = object.projectId ?? "";
    message.update = (object.update !== undefined && object.update !== null)
      ? SylkMethod.fromPartial(object.update)
      : undefined;
    return message;
  },
};

function createBaseUpdateMethodResponse(): UpdateMethodResponse {
  return { method: "", projectId: "", updated: undefined };
}

export const UpdateMethodResponse = {
  encode(message: UpdateMethodResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.method !== "") {
      writer.uint32(18).string(message.method);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.updated !== undefined) {
      SylkMethodDisplay.encode(message.updated, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateMethodResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateMethodResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.method = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updated = SylkMethodDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateMethodResponse {
    return {
      method: isSet(object.method) ? String(object.method) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      updated: isSet(object.updated) ? SylkMethodDisplay.fromJSON(object.updated) : undefined,
    };
  },

  toJSON(message: UpdateMethodResponse): unknown {
    const obj: any = {};
    message.method !== undefined && (obj.method = message.method);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.updated !== undefined &&
      (obj.updated = message.updated ? SylkMethodDisplay.toJSON(message.updated) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateMethodResponse>, I>>(base?: I): UpdateMethodResponse {
    return UpdateMethodResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateMethodResponse>, I>>(object: I): UpdateMethodResponse {
    const message = createBaseUpdateMethodResponse();
    message.method = object.method ?? "";
    message.projectId = object.projectId ?? "";
    message.updated = (object.updated !== undefined && object.updated !== null)
      ? SylkMethodDisplay.fromPartial(object.updated)
      : undefined;
    return message;
  },
};

function createBaseDeleteMethodRequest(): DeleteMethodRequest {
  return { method: "", projectId: "" };
}

export const DeleteMethodRequest = {
  encode(message: DeleteMethodRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.method !== "") {
      writer.uint32(18).string(message.method);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteMethodRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteMethodRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.method = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteMethodRequest {
    return {
      method: isSet(object.method) ? String(object.method) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: DeleteMethodRequest): unknown {
    const obj: any = {};
    message.method !== undefined && (obj.method = message.method);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteMethodRequest>, I>>(base?: I): DeleteMethodRequest {
    return DeleteMethodRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteMethodRequest>, I>>(object: I): DeleteMethodRequest {
    const message = createBaseDeleteMethodRequest();
    message.method = object.method ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseDeleteMethodResponse(): DeleteMethodResponse {
  return { method: "", projectId: "" };
}

export const DeleteMethodResponse = {
  encode(message: DeleteMethodResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.method !== "") {
      writer.uint32(18).string(message.method);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteMethodResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteMethodResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.method = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteMethodResponse {
    return {
      method: isSet(object.method) ? String(object.method) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: DeleteMethodResponse): unknown {
    const obj: any = {};
    message.method !== undefined && (obj.method = message.method);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteMethodResponse>, I>>(base?: I): DeleteMethodResponse {
    return DeleteMethodResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteMethodResponse>, I>>(object: I): DeleteMethodResponse {
    const message = createBaseDeleteMethodResponse();
    message.method = object.method ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseGetFieldRequest(): GetFieldRequest {
  return { projectId: "", field: "" };
}

export const GetFieldRequest = {
  encode(message: GetFieldRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.field !== "") {
      writer.uint32(18).string(message.field);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetFieldRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetFieldRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.field = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetFieldRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      field: isSet(object.field) ? String(object.field) : "",
    };
  },

  toJSON(message: GetFieldRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.field !== undefined && (obj.field = message.field);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetFieldRequest>, I>>(base?: I): GetFieldRequest {
    return GetFieldRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetFieldRequest>, I>>(object: I): GetFieldRequest {
    const message = createBaseGetFieldRequest();
    message.projectId = object.projectId ?? "";
    message.field = object.field ?? "";
    return message;
  },
};

function createBaseGetFieldResponse(): GetFieldResponse {
  return { result: undefined };
}

export const GetFieldResponse = {
  encode(message: GetFieldResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkFieldDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetFieldResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetFieldResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkFieldDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetFieldResponse {
    return { result: isSet(object.result) ? SylkFieldDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetFieldResponse): unknown {
    const obj: any = {};
    message.result !== undefined && (obj.result = message.result ? SylkFieldDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetFieldResponse>, I>>(base?: I): GetFieldResponse {
    return GetFieldResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetFieldResponse>, I>>(object: I): GetFieldResponse {
    const message = createBaseGetFieldResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkFieldDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseUpdateFieldRequest(): UpdateFieldRequest {
  return { field: "", projectId: "", update: undefined };
}

export const UpdateFieldRequest = {
  encode(message: UpdateFieldRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.field !== "") {
      writer.uint32(18).string(message.field);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.update !== undefined) {
      SylkField.encode(message.update, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateFieldRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateFieldRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.field = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.update = SylkField.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateFieldRequest {
    return {
      field: isSet(object.field) ? String(object.field) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      update: isSet(object.update) ? SylkField.fromJSON(object.update) : undefined,
    };
  },

  toJSON(message: UpdateFieldRequest): unknown {
    const obj: any = {};
    message.field !== undefined && (obj.field = message.field);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.update !== undefined && (obj.update = message.update ? SylkField.toJSON(message.update) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateFieldRequest>, I>>(base?: I): UpdateFieldRequest {
    return UpdateFieldRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateFieldRequest>, I>>(object: I): UpdateFieldRequest {
    const message = createBaseUpdateFieldRequest();
    message.field = object.field ?? "";
    message.projectId = object.projectId ?? "";
    message.update = (object.update !== undefined && object.update !== null)
      ? SylkField.fromPartial(object.update)
      : undefined;
    return message;
  },
};

function createBaseUpdateFieldResponse(): UpdateFieldResponse {
  return { projectId: "", field: "", updated: undefined };
}

export const UpdateFieldResponse = {
  encode(message: UpdateFieldResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.field !== "") {
      writer.uint32(18).string(message.field);
    }
    if (message.updated !== undefined) {
      SylkFieldDisplay.encode(message.updated, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateFieldResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateFieldResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.field = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updated = SylkFieldDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateFieldResponse {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      field: isSet(object.field) ? String(object.field) : "",
      updated: isSet(object.updated) ? SylkFieldDisplay.fromJSON(object.updated) : undefined,
    };
  },

  toJSON(message: UpdateFieldResponse): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.field !== undefined && (obj.field = message.field);
    message.updated !== undefined &&
      (obj.updated = message.updated ? SylkFieldDisplay.toJSON(message.updated) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateFieldResponse>, I>>(base?: I): UpdateFieldResponse {
    return UpdateFieldResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateFieldResponse>, I>>(object: I): UpdateFieldResponse {
    const message = createBaseUpdateFieldResponse();
    message.projectId = object.projectId ?? "";
    message.field = object.field ?? "";
    message.updated = (object.updated !== undefined && object.updated !== null)
      ? SylkFieldDisplay.fromPartial(object.updated)
      : undefined;
    return message;
  },
};

function createBaseDeleteFieldRequest(): DeleteFieldRequest {
  return { field: "", projectId: "" };
}

export const DeleteFieldRequest = {
  encode(message: DeleteFieldRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.field !== "") {
      writer.uint32(18).string(message.field);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteFieldRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteFieldRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.field = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteFieldRequest {
    return {
      field: isSet(object.field) ? String(object.field) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: DeleteFieldRequest): unknown {
    const obj: any = {};
    message.field !== undefined && (obj.field = message.field);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteFieldRequest>, I>>(base?: I): DeleteFieldRequest {
    return DeleteFieldRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteFieldRequest>, I>>(object: I): DeleteFieldRequest {
    const message = createBaseDeleteFieldRequest();
    message.field = object.field ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseDeleteFieldResponse(): DeleteFieldResponse {
  return { field: "", projectId: "" };
}

export const DeleteFieldResponse = {
  encode(message: DeleteFieldResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.field !== "") {
      writer.uint32(18).string(message.field);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteFieldResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteFieldResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.field = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteFieldResponse {
    return {
      field: isSet(object.field) ? String(object.field) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: DeleteFieldResponse): unknown {
    const obj: any = {};
    message.field !== undefined && (obj.field = message.field);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteFieldResponse>, I>>(base?: I): DeleteFieldResponse {
    return DeleteFieldResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteFieldResponse>, I>>(object: I): DeleteFieldResponse {
    const message = createBaseDeleteFieldResponse();
    message.field = object.field ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseCreateFieldRequest(): CreateFieldRequest {
  return { projectId: "", message: "", field: undefined };
}

export const CreateFieldRequest = {
  encode(message: CreateFieldRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.message !== "") {
      writer.uint32(18).string(message.message);
    }
    if (message.field !== undefined) {
      SylkField.encode(message.field, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateFieldRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateFieldRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.message = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.field = SylkField.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateFieldRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      message: isSet(object.message) ? String(object.message) : "",
      field: isSet(object.field) ? SylkField.fromJSON(object.field) : undefined,
    };
  },

  toJSON(message: CreateFieldRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.message !== undefined && (obj.message = message.message);
    message.field !== undefined && (obj.field = message.field ? SylkField.toJSON(message.field) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateFieldRequest>, I>>(base?: I): CreateFieldRequest {
    return CreateFieldRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateFieldRequest>, I>>(object: I): CreateFieldRequest {
    const message = createBaseCreateFieldRequest();
    message.projectId = object.projectId ?? "";
    message.message = object.message ?? "";
    message.field = (object.field !== undefined && object.field !== null)
      ? SylkField.fromPartial(object.field)
      : undefined;
    return message;
  },
};

function createBaseCreateFieldResponse(): CreateFieldResponse {
  return { result: undefined };
}

export const CreateFieldResponse = {
  encode(message: CreateFieldResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkFieldDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateFieldResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateFieldResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkFieldDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateFieldResponse {
    return { result: isSet(object.result) ? SylkFieldDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: CreateFieldResponse): unknown {
    const obj: any = {};
    message.result !== undefined && (obj.result = message.result ? SylkFieldDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateFieldResponse>, I>>(base?: I): CreateFieldResponse {
    return CreateFieldResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateFieldResponse>, I>>(object: I): CreateFieldResponse {
    const message = createBaseCreateFieldResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkFieldDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseGetEnumRequest(): GetEnumRequest {
  return { projectId: "", enum: "" };
}

export const GetEnumRequest = {
  encode(message: GetEnumRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.enum !== "") {
      writer.uint32(18).string(message.enum);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetEnumRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetEnumRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enum = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetEnumRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      enum: isSet(object.enum) ? String(object.enum) : "",
    };
  },

  toJSON(message: GetEnumRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.enum !== undefined && (obj.enum = message.enum);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetEnumRequest>, I>>(base?: I): GetEnumRequest {
    return GetEnumRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetEnumRequest>, I>>(object: I): GetEnumRequest {
    const message = createBaseGetEnumRequest();
    message.projectId = object.projectId ?? "";
    message.enum = object.enum ?? "";
    return message;
  },
};

function createBaseGetEnumResponse(): GetEnumResponse {
  return { result: undefined };
}

export const GetEnumResponse = {
  encode(message: GetEnumResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkEnumDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetEnumResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetEnumResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkEnumDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetEnumResponse {
    return { result: isSet(object.result) ? SylkEnumDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetEnumResponse): unknown {
    const obj: any = {};
    message.result !== undefined && (obj.result = message.result ? SylkEnumDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetEnumResponse>, I>>(base?: I): GetEnumResponse {
    return GetEnumResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetEnumResponse>, I>>(object: I): GetEnumResponse {
    const message = createBaseGetEnumResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkEnumDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseCreateEnumRequest(): CreateEnumRequest {
  return { package: "", enum: undefined, projectId: "" };
}

export const CreateEnumRequest = {
  encode(message: CreateEnumRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.package !== "") {
      writer.uint32(18).string(message.package);
    }
    if (message.enum !== undefined) {
      SylkEnum.encode(message.enum, writer.uint32(26).fork()).ldelim();
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateEnumRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateEnumRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.package = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.enum = SylkEnum.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateEnumRequest {
    return {
      package: isSet(object.package) ? String(object.package) : "",
      enum: isSet(object.enum) ? SylkEnum.fromJSON(object.enum) : undefined,
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: CreateEnumRequest): unknown {
    const obj: any = {};
    message.package !== undefined && (obj.package = message.package);
    message.enum !== undefined && (obj.enum = message.enum ? SylkEnum.toJSON(message.enum) : undefined);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateEnumRequest>, I>>(base?: I): CreateEnumRequest {
    return CreateEnumRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateEnumRequest>, I>>(object: I): CreateEnumRequest {
    const message = createBaseCreateEnumRequest();
    message.package = object.package ?? "";
    message.enum = (object.enum !== undefined && object.enum !== null) ? SylkEnum.fromPartial(object.enum) : undefined;
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseCreateEnumResponse(): CreateEnumResponse {
  return { result: undefined, projectId: "" };
}

export const CreateEnumResponse = {
  encode(message: CreateEnumResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkEnumDisplay.encode(message.result, writer.uint32(18).fork()).ldelim();
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateEnumResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateEnumResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.result = SylkEnumDisplay.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateEnumResponse {
    return {
      result: isSet(object.result) ? SylkEnumDisplay.fromJSON(object.result) : undefined,
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: CreateEnumResponse): unknown {
    const obj: any = {};
    message.result !== undefined && (obj.result = message.result ? SylkEnumDisplay.toJSON(message.result) : undefined);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateEnumResponse>, I>>(base?: I): CreateEnumResponse {
    return CreateEnumResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateEnumResponse>, I>>(object: I): CreateEnumResponse {
    const message = createBaseCreateEnumResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkEnumDisplay.fromPartial(object.result)
      : undefined;
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseUpdateEnumRequest(): UpdateEnumRequest {
  return { update: undefined, enum: "", projectId: "" };
}

export const UpdateEnumRequest = {
  encode(message: UpdateEnumRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.update !== undefined) {
      SylkEnum.encode(message.update, writer.uint32(26).fork()).ldelim();
    }
    if (message.enum !== "") {
      writer.uint32(18).string(message.enum);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateEnumRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateEnumRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 26) {
            break;
          }

          message.update = SylkEnum.decode(reader, reader.uint32());
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enum = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateEnumRequest {
    return {
      update: isSet(object.update) ? SylkEnum.fromJSON(object.update) : undefined,
      enum: isSet(object.enum) ? String(object.enum) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: UpdateEnumRequest): unknown {
    const obj: any = {};
    message.update !== undefined && (obj.update = message.update ? SylkEnum.toJSON(message.update) : undefined);
    message.enum !== undefined && (obj.enum = message.enum);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateEnumRequest>, I>>(base?: I): UpdateEnumRequest {
    return UpdateEnumRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateEnumRequest>, I>>(object: I): UpdateEnumRequest {
    const message = createBaseUpdateEnumRequest();
    message.update = (object.update !== undefined && object.update !== null)
      ? SylkEnum.fromPartial(object.update)
      : undefined;
    message.enum = object.enum ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseUpdateEnumResponse(): UpdateEnumResponse {
  return { enum: "", projectId: "", updated: undefined };
}

export const UpdateEnumResponse = {
  encode(message: UpdateEnumResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.enum !== "") {
      writer.uint32(18).string(message.enum);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.updated !== undefined) {
      SylkEnumDisplay.encode(message.updated, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateEnumResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateEnumResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enum = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updated = SylkEnumDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateEnumResponse {
    return {
      enum: isSet(object.enum) ? String(object.enum) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      updated: isSet(object.updated) ? SylkEnumDisplay.fromJSON(object.updated) : undefined,
    };
  },

  toJSON(message: UpdateEnumResponse): unknown {
    const obj: any = {};
    message.enum !== undefined && (obj.enum = message.enum);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.updated !== undefined &&
      (obj.updated = message.updated ? SylkEnumDisplay.toJSON(message.updated) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateEnumResponse>, I>>(base?: I): UpdateEnumResponse {
    return UpdateEnumResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateEnumResponse>, I>>(object: I): UpdateEnumResponse {
    const message = createBaseUpdateEnumResponse();
    message.enum = object.enum ?? "";
    message.projectId = object.projectId ?? "";
    message.updated = (object.updated !== undefined && object.updated !== null)
      ? SylkEnumDisplay.fromPartial(object.updated)
      : undefined;
    return message;
  },
};

function createBaseDeleteEnumRequest(): DeleteEnumRequest {
  return { enum: "", projectId: "" };
}

export const DeleteEnumRequest = {
  encode(message: DeleteEnumRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.enum !== "") {
      writer.uint32(18).string(message.enum);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteEnumRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteEnumRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enum = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteEnumRequest {
    return {
      enum: isSet(object.enum) ? String(object.enum) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: DeleteEnumRequest): unknown {
    const obj: any = {};
    message.enum !== undefined && (obj.enum = message.enum);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteEnumRequest>, I>>(base?: I): DeleteEnumRequest {
    return DeleteEnumRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteEnumRequest>, I>>(object: I): DeleteEnumRequest {
    const message = createBaseDeleteEnumRequest();
    message.enum = object.enum ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseDeleteEnumResponse(): DeleteEnumResponse {
  return { enum: "", projectId: "" };
}

export const DeleteEnumResponse = {
  encode(message: DeleteEnumResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.enum !== "") {
      writer.uint32(18).string(message.enum);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteEnumResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteEnumResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enum = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteEnumResponse {
    return {
      enum: isSet(object.enum) ? String(object.enum) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: DeleteEnumResponse): unknown {
    const obj: any = {};
    message.enum !== undefined && (obj.enum = message.enum);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteEnumResponse>, I>>(base?: I): DeleteEnumResponse {
    return DeleteEnumResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteEnumResponse>, I>>(object: I): DeleteEnumResponse {
    const message = createBaseDeleteEnumResponse();
    message.enum = object.enum ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseGetEnumValueRequest(): GetEnumValueRequest {
  return { projectId: "", enumValue: "" };
}

export const GetEnumValueRequest = {
  encode(message: GetEnumValueRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.enumValue !== "") {
      writer.uint32(18).string(message.enumValue);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetEnumValueRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetEnumValueRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enumValue = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetEnumValueRequest {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      enumValue: isSet(object.enumValue) ? String(object.enumValue) : "",
    };
  },

  toJSON(message: GetEnumValueRequest): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.enumValue !== undefined && (obj.enumValue = message.enumValue);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetEnumValueRequest>, I>>(base?: I): GetEnumValueRequest {
    return GetEnumValueRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetEnumValueRequest>, I>>(object: I): GetEnumValueRequest {
    const message = createBaseGetEnumValueRequest();
    message.projectId = object.projectId ?? "";
    message.enumValue = object.enumValue ?? "";
    return message;
  },
};

function createBaseGetEnumValueResponse(): GetEnumValueResponse {
  return { result: undefined };
}

export const GetEnumValueResponse = {
  encode(message: GetEnumValueResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkEnumValueDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetEnumValueResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetEnumValueResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkEnumValueDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetEnumValueResponse {
    return { result: isSet(object.result) ? SylkEnumValueDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetEnumValueResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkEnumValueDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetEnumValueResponse>, I>>(base?: I): GetEnumValueResponse {
    return GetEnumValueResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetEnumValueResponse>, I>>(object: I): GetEnumValueResponse {
    const message = createBaseGetEnumValueResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkEnumValueDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseCreateEnumValueRequest(): CreateEnumValueRequest {
  return { enum: "", projectId: "", enumValue: undefined };
}

export const CreateEnumValueRequest = {
  encode(message: CreateEnumValueRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.enum !== "") {
      writer.uint32(18).string(message.enum);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.enumValue !== undefined) {
      SylkEnumValue.encode(message.enumValue, writer.uint32(26).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateEnumValueRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateEnumValueRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enum = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.enumValue = SylkEnumValue.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateEnumValueRequest {
    return {
      enum: isSet(object.enum) ? String(object.enum) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      enumValue: isSet(object.enumValue) ? SylkEnumValue.fromJSON(object.enumValue) : undefined,
    };
  },

  toJSON(message: CreateEnumValueRequest): unknown {
    const obj: any = {};
    message.enum !== undefined && (obj.enum = message.enum);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.enumValue !== undefined &&
      (obj.enumValue = message.enumValue ? SylkEnumValue.toJSON(message.enumValue) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateEnumValueRequest>, I>>(base?: I): CreateEnumValueRequest {
    return CreateEnumValueRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateEnumValueRequest>, I>>(object: I): CreateEnumValueRequest {
    const message = createBaseCreateEnumValueRequest();
    message.enum = object.enum ?? "";
    message.projectId = object.projectId ?? "";
    message.enumValue = (object.enumValue !== undefined && object.enumValue !== null)
      ? SylkEnumValue.fromPartial(object.enumValue)
      : undefined;
    return message;
  },
};

function createBaseCreateEnumValueResponse(): CreateEnumValueResponse {
  return { result: undefined };
}

export const CreateEnumValueResponse = {
  encode(message: CreateEnumValueResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      SylkEnumValueDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateEnumValueResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateEnumValueResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkEnumValueDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateEnumValueResponse {
    return { result: isSet(object.result) ? SylkEnumValueDisplay.fromJSON(object.result) : undefined };
  },

  toJSON(message: CreateEnumValueResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? SylkEnumValueDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateEnumValueResponse>, I>>(base?: I): CreateEnumValueResponse {
    return CreateEnumValueResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateEnumValueResponse>, I>>(object: I): CreateEnumValueResponse {
    const message = createBaseCreateEnumValueResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkEnumValueDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseUpdateEnumValueRequest(): UpdateEnumValueRequest {
  return { update: undefined, projectId: "", enumValue: "" };
}

export const UpdateEnumValueRequest = {
  encode(message: UpdateEnumValueRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.update !== undefined) {
      SylkEnumValue.encode(message.update, writer.uint32(26).fork()).ldelim();
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.enumValue !== "") {
      writer.uint32(18).string(message.enumValue);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateEnumValueRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateEnumValueRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 3:
          if (tag !== 26) {
            break;
          }

          message.update = SylkEnumValue.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enumValue = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateEnumValueRequest {
    return {
      update: isSet(object.update) ? SylkEnumValue.fromJSON(object.update) : undefined,
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      enumValue: isSet(object.enumValue) ? String(object.enumValue) : "",
    };
  },

  toJSON(message: UpdateEnumValueRequest): unknown {
    const obj: any = {};
    message.update !== undefined && (obj.update = message.update ? SylkEnumValue.toJSON(message.update) : undefined);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.enumValue !== undefined && (obj.enumValue = message.enumValue);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateEnumValueRequest>, I>>(base?: I): UpdateEnumValueRequest {
    return UpdateEnumValueRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateEnumValueRequest>, I>>(object: I): UpdateEnumValueRequest {
    const message = createBaseUpdateEnumValueRequest();
    message.update = (object.update !== undefined && object.update !== null)
      ? SylkEnumValue.fromPartial(object.update)
      : undefined;
    message.projectId = object.projectId ?? "";
    message.enumValue = object.enumValue ?? "";
    return message;
  },
};

function createBaseUpdateEnumValueResponse(): UpdateEnumValueResponse {
  return { projectId: "", updated: undefined, enumValue: "" };
}

export const UpdateEnumValueResponse = {
  encode(message: UpdateEnumValueResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.updated !== undefined) {
      SylkEnumValueDisplay.encode(message.updated, writer.uint32(26).fork()).ldelim();
    }
    if (message.enumValue !== "") {
      writer.uint32(18).string(message.enumValue);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): UpdateEnumValueResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseUpdateEnumValueResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 3:
          if (tag !== 26) {
            break;
          }

          message.updated = SylkEnumValueDisplay.decode(reader, reader.uint32());
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enumValue = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): UpdateEnumValueResponse {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      updated: isSet(object.updated) ? SylkEnumValueDisplay.fromJSON(object.updated) : undefined,
      enumValue: isSet(object.enumValue) ? String(object.enumValue) : "",
    };
  },

  toJSON(message: UpdateEnumValueResponse): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.updated !== undefined &&
      (obj.updated = message.updated ? SylkEnumValueDisplay.toJSON(message.updated) : undefined);
    message.enumValue !== undefined && (obj.enumValue = message.enumValue);
    return obj;
  },

  create<I extends Exact<DeepPartial<UpdateEnumValueResponse>, I>>(base?: I): UpdateEnumValueResponse {
    return UpdateEnumValueResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<UpdateEnumValueResponse>, I>>(object: I): UpdateEnumValueResponse {
    const message = createBaseUpdateEnumValueResponse();
    message.projectId = object.projectId ?? "";
    message.updated = (object.updated !== undefined && object.updated !== null)
      ? SylkEnumValueDisplay.fromPartial(object.updated)
      : undefined;
    message.enumValue = object.enumValue ?? "";
    return message;
  },
};

function createBaseDeleteEnumValueRequest(): DeleteEnumValueRequest {
  return { enumValue: "", projectId: "" };
}

export const DeleteEnumValueRequest = {
  encode(message: DeleteEnumValueRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.enumValue !== "") {
      writer.uint32(18).string(message.enumValue);
    }
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteEnumValueRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteEnumValueRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enumValue = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteEnumValueRequest {
    return {
      enumValue: isSet(object.enumValue) ? String(object.enumValue) : "",
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
    };
  },

  toJSON(message: DeleteEnumValueRequest): unknown {
    const obj: any = {};
    message.enumValue !== undefined && (obj.enumValue = message.enumValue);
    message.projectId !== undefined && (obj.projectId = message.projectId);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteEnumValueRequest>, I>>(base?: I): DeleteEnumValueRequest {
    return DeleteEnumValueRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteEnumValueRequest>, I>>(object: I): DeleteEnumValueRequest {
    const message = createBaseDeleteEnumValueRequest();
    message.enumValue = object.enumValue ?? "";
    message.projectId = object.projectId ?? "";
    return message;
  },
};

function createBaseDeleteEnumValueResponse(): DeleteEnumValueResponse {
  return { projectId: "", enumValue: "" };
}

export const DeleteEnumValueResponse = {
  encode(message: DeleteEnumValueResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.projectId !== "") {
      writer.uint32(10).string(message.projectId);
    }
    if (message.enumValue !== "") {
      writer.uint32(18).string(message.enumValue);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): DeleteEnumValueResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseDeleteEnumValueResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projectId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.enumValue = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): DeleteEnumValueResponse {
    return {
      projectId: isSet(object.projectId) ? String(object.projectId) : "",
      enumValue: isSet(object.enumValue) ? String(object.enumValue) : "",
    };
  },

  toJSON(message: DeleteEnumValueResponse): unknown {
    const obj: any = {};
    message.projectId !== undefined && (obj.projectId = message.projectId);
    message.enumValue !== undefined && (obj.enumValue = message.enumValue);
    return obj;
  },

  create<I extends Exact<DeepPartial<DeleteEnumValueResponse>, I>>(base?: I): DeleteEnumValueResponse {
    return DeleteEnumValueResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<DeleteEnumValueResponse>, I>>(object: I): DeleteEnumValueResponse {
    const message = createBaseDeleteEnumValueResponse();
    message.projectId = object.projectId ?? "";
    message.enumValue = object.enumValue ?? "";
    return message;
  },
};

function createBaseListOrganizationsResponseCache(): ListOrganizationsResponseCache {
  return { organizations: [] };
}

export const ListOrganizationsResponseCache = {
  encode(message: ListOrganizationsResponseCache, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    for (const v of message.organizations) {
      GetOrganizationResponse.encode(v!, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListOrganizationsResponseCache {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseListOrganizationsResponseCache();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.organizations.push(GetOrganizationResponse.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): ListOrganizationsResponseCache {
    return {
      organizations: Array.isArray(object?.organizations)
        ? object.organizations.map((e: any) => GetOrganizationResponse.fromJSON(e))
        : [],
    };
  },

  toJSON(message: ListOrganizationsResponseCache): unknown {
    const obj: any = {};
    if (message.organizations) {
      obj.organizations = message.organizations.map((e) => e ? GetOrganizationResponse.toJSON(e) : undefined);
    } else {
      obj.organizations = [];
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<ListOrganizationsResponseCache>, I>>(base?: I): ListOrganizationsResponseCache {
    return ListOrganizationsResponseCache.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<ListOrganizationsResponseCache>, I>>(
    object: I,
  ): ListOrganizationsResponseCache {
    const message = createBaseListOrganizationsResponseCache();
    message.organizations = object.organizations?.map((e) => GetOrganizationResponse.fromPartial(e)) || [];
    return message;
  },
};

function createBaseListProjectsRequest(): ListProjectsRequest {
  return { orgId: "" };
}

export const ListProjectsRequest = {
  encode(message: ListProjectsRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.orgId !== "") {
      writer.uint32(10).string(message.orgId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListProjectsRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseListProjectsRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.orgId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): ListProjectsRequest {
    return { orgId: isSet(object.orgId) ? String(object.orgId) : "" };
  },

  toJSON(message: ListProjectsRequest): unknown {
    const obj: any = {};
    message.orgId !== undefined && (obj.orgId = message.orgId);
    return obj;
  },

  create<I extends Exact<DeepPartial<ListProjectsRequest>, I>>(base?: I): ListProjectsRequest {
    return ListProjectsRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<ListProjectsRequest>, I>>(object: I): ListProjectsRequest {
    const message = createBaseListProjectsRequest();
    message.orgId = object.orgId ?? "";
    return message;
  },
};

function createBaseCreateProjectRequest(): CreateProjectRequest {
  return { project: undefined, orgId: "" };
}

export const CreateProjectRequest = {
  encode(message: CreateProjectRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.project !== undefined) {
      SylkProject.encode(message.project, writer.uint32(18).fork()).ldelim();
    }
    if (message.orgId !== "") {
      writer.uint32(10).string(message.orgId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateProjectRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateProjectRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.project = SylkProject.decode(reader, reader.uint32());
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.orgId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateProjectRequest {
    return {
      project: isSet(object.project) ? SylkProject.fromJSON(object.project) : undefined,
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
    };
  },

  toJSON(message: CreateProjectRequest): unknown {
    const obj: any = {};
    message.project !== undefined && (obj.project = message.project ? SylkProject.toJSON(message.project) : undefined);
    message.orgId !== undefined && (obj.orgId = message.orgId);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateProjectRequest>, I>>(base?: I): CreateProjectRequest {
    return CreateProjectRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateProjectRequest>, I>>(object: I): CreateProjectRequest {
    const message = createBaseCreateProjectRequest();
    message.project = (object.project !== undefined && object.project !== null)
      ? SylkProject.fromPartial(object.project)
      : undefined;
    message.orgId = object.orgId ?? "";
    return message;
  },
};

function createBaseCreateProjectResponse(): CreateProjectResponse {
  return { orgId: "", result: undefined };
}

export const CreateProjectResponse = {
  encode(message: CreateProjectResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.orgId !== "") {
      writer.uint32(18).string(message.orgId);
    }
    if (message.result !== undefined) {
      SylkProjectDisplay.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateProjectResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateProjectResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 2:
          if (tag !== 18) {
            break;
          }

          message.orgId = reader.string();
          continue;
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = SylkProjectDisplay.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateProjectResponse {
    return {
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
      result: isSet(object.result) ? SylkProjectDisplay.fromJSON(object.result) : undefined,
    };
  },

  toJSON(message: CreateProjectResponse): unknown {
    const obj: any = {};
    message.orgId !== undefined && (obj.orgId = message.orgId);
    message.result !== undefined &&
      (obj.result = message.result ? SylkProjectDisplay.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateProjectResponse>, I>>(base?: I): CreateProjectResponse {
    return CreateProjectResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateProjectResponse>, I>>(object: I): CreateProjectResponse {
    const message = createBaseCreateProjectResponse();
    message.orgId = object.orgId ?? "";
    message.result = (object.result !== undefined && object.result !== null)
      ? SylkProjectDisplay.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseListProjectsResponseCache(): ListProjectsResponseCache {
  return { projects: [] };
}

export const ListProjectsResponseCache = {
  encode(message: ListProjectsResponseCache, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    for (const v of message.projects) {
      GetProjectResponse.encode(v!, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListProjectsResponseCache {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseListProjectsResponseCache();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.projects.push(GetProjectResponse.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): ListProjectsResponseCache {
    return {
      projects: Array.isArray(object?.projects) ? object.projects.map((e: any) => GetProjectResponse.fromJSON(e)) : [],
    };
  },

  toJSON(message: ListProjectsResponseCache): unknown {
    const obj: any = {};
    if (message.projects) {
      obj.projects = message.projects.map((e) => e ? GetProjectResponse.toJSON(e) : undefined);
    } else {
      obj.projects = [];
    }
    return obj;
  },

  create<I extends Exact<DeepPartial<ListProjectsResponseCache>, I>>(base?: I): ListProjectsResponseCache {
    return ListProjectsResponseCache.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<ListProjectsResponseCache>, I>>(object: I): ListProjectsResponseCache {
    const message = createBaseListProjectsResponseCache();
    message.projects = object.projects?.map((e) => GetProjectResponse.fromPartial(e)) || [];
    return message;
  },
};

function createBaseCachedSession(): CachedSession {
  return { session: undefined };
}

export const CachedSession = {
  encode(message: CachedSession, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.session !== undefined) {
      Struct.encode(Struct.wrap(message.session), writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CachedSession {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCachedSession();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.session = Struct.unwrap(Struct.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CachedSession {
    return { session: isObject(object.session) ? object.session : undefined };
  },

  toJSON(message: CachedSession): unknown {
    const obj: any = {};
    message.session !== undefined && (obj.session = message.session);
    return obj;
  },

  create<I extends Exact<DeepPartial<CachedSession>, I>>(base?: I): CachedSession {
    return CachedSession.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CachedSession>, I>>(object: I): CachedSession {
    const message = createBaseCachedSession();
    message.session = object.session ?? undefined;
    return message;
  },
};

function createBaseCreateAccessTokenRequest(): CreateAccessTokenRequest {
  return { description: "", orgId: "", expiresAt: undefined };
}

export const CreateAccessTokenRequest = {
  encode(message: CreateAccessTokenRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.description !== "") {
      writer.uint32(26).string(message.description);
    }
    if (message.orgId !== "") {
      writer.uint32(10).string(message.orgId);
    }
    if (message.expiresAt !== undefined) {
      Timestamp.encode(toTimestamp(message.expiresAt), writer.uint32(18).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateAccessTokenRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateAccessTokenRequest();
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

          message.orgId = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.expiresAt = fromTimestamp(Timestamp.decode(reader, reader.uint32()));
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateAccessTokenRequest {
    return {
      description: isSet(object.description) ? String(object.description) : "",
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
      expiresAt: isSet(object.expiresAt) ? fromJsonTimestamp(object.expiresAt) : undefined,
    };
  },

  toJSON(message: CreateAccessTokenRequest): unknown {
    const obj: any = {};
    message.description !== undefined && (obj.description = message.description);
    message.orgId !== undefined && (obj.orgId = message.orgId);
    message.expiresAt !== undefined && (obj.expiresAt = message.expiresAt.toISOString());
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateAccessTokenRequest>, I>>(base?: I): CreateAccessTokenRequest {
    return CreateAccessTokenRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateAccessTokenRequest>, I>>(object: I): CreateAccessTokenRequest {
    const message = createBaseCreateAccessTokenRequest();
    message.description = object.description ?? "";
    message.orgId = object.orgId ?? "";
    message.expiresAt = object.expiresAt ?? undefined;
    return message;
  },
};

function createBaseCreateAccessTokenResponse(): CreateAccessTokenResponse {
  return { status: "" };
}

export const CreateAccessTokenResponse = {
  encode(message: CreateAccessTokenResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.status !== "") {
      writer.uint32(10).string(message.status);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): CreateAccessTokenResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseCreateAccessTokenResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.status = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): CreateAccessTokenResponse {
    return { status: isSet(object.status) ? String(object.status) : "" };
  },

  toJSON(message: CreateAccessTokenResponse): unknown {
    const obj: any = {};
    message.status !== undefined && (obj.status = message.status);
    return obj;
  },

  create<I extends Exact<DeepPartial<CreateAccessTokenResponse>, I>>(base?: I): CreateAccessTokenResponse {
    return CreateAccessTokenResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<CreateAccessTokenResponse>, I>>(object: I): CreateAccessTokenResponse {
    const message = createBaseCreateAccessTokenResponse();
    message.status = object.status ?? "";
    return message;
  },
};

function createBaseListAccessTokensRequest(): ListAccessTokensRequest {
  return { orgId: "" };
}

export const ListAccessTokensRequest = {
  encode(message: ListAccessTokensRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.orgId !== "") {
      writer.uint32(10).string(message.orgId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): ListAccessTokensRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseListAccessTokensRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.orgId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): ListAccessTokensRequest {
    return { orgId: isSet(object.orgId) ? String(object.orgId) : "" };
  },

  toJSON(message: ListAccessTokensRequest): unknown {
    const obj: any = {};
    message.orgId !== undefined && (obj.orgId = message.orgId);
    return obj;
  },

  create<I extends Exact<DeepPartial<ListAccessTokensRequest>, I>>(base?: I): ListAccessTokensRequest {
    return ListAccessTokensRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<ListAccessTokensRequest>, I>>(object: I): ListAccessTokensRequest {
    const message = createBaseListAccessTokensRequest();
    message.orgId = object.orgId ?? "";
    return message;
  },
};

function createBaseGetAccessTokenResponse(): GetAccessTokenResponse {
  return { result: undefined };
}

export const GetAccessTokenResponse = {
  encode(message: GetAccessTokenResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.result !== undefined) {
      PersonalAccessToken.encode(message.result, writer.uint32(10).fork()).ldelim();
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetAccessTokenResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetAccessTokenResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.result = PersonalAccessToken.decode(reader, reader.uint32());
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetAccessTokenResponse {
    return { result: isSet(object.result) ? PersonalAccessToken.fromJSON(object.result) : undefined };
  },

  toJSON(message: GetAccessTokenResponse): unknown {
    const obj: any = {};
    message.result !== undefined &&
      (obj.result = message.result ? PersonalAccessToken.toJSON(message.result) : undefined);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetAccessTokenResponse>, I>>(base?: I): GetAccessTokenResponse {
    return GetAccessTokenResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetAccessTokenResponse>, I>>(object: I): GetAccessTokenResponse {
    const message = createBaseGetAccessTokenResponse();
    message.result = (object.result !== undefined && object.result !== null)
      ? PersonalAccessToken.fromPartial(object.result)
      : undefined;
    return message;
  },
};

function createBaseGetAccessTokenRequest(): GetAccessTokenRequest {
  return { token: "" };
}

export const GetAccessTokenRequest = {
  encode(message: GetAccessTokenRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.token !== "") {
      writer.uint32(10).string(message.token);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): GetAccessTokenRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseGetAccessTokenRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.token = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): GetAccessTokenRequest {
    return { token: isSet(object.token) ? String(object.token) : "" };
  },

  toJSON(message: GetAccessTokenRequest): unknown {
    const obj: any = {};
    message.token !== undefined && (obj.token = message.token);
    return obj;
  },

  create<I extends Exact<DeepPartial<GetAccessTokenRequest>, I>>(base?: I): GetAccessTokenRequest {
    return GetAccessTokenRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<GetAccessTokenRequest>, I>>(object: I): GetAccessTokenRequest {
    const message = createBaseGetAccessTokenRequest();
    message.token = object.token ?? "";
    return message;
  },
};

function createBaseRevokeAccessTokenRequest(): RevokeAccessTokenRequest {
  return { token: "", orgId: "" };
}

export const RevokeAccessTokenRequest = {
  encode(message: RevokeAccessTokenRequest, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.token !== "") {
      writer.uint32(10).string(message.token);
    }
    if (message.orgId !== "") {
      writer.uint32(18).string(message.orgId);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): RevokeAccessTokenRequest {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseRevokeAccessTokenRequest();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.token = reader.string();
          continue;
        case 2:
          if (tag !== 18) {
            break;
          }

          message.orgId = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): RevokeAccessTokenRequest {
    return {
      token: isSet(object.token) ? String(object.token) : "",
      orgId: isSet(object.orgId) ? String(object.orgId) : "",
    };
  },

  toJSON(message: RevokeAccessTokenRequest): unknown {
    const obj: any = {};
    message.token !== undefined && (obj.token = message.token);
    message.orgId !== undefined && (obj.orgId = message.orgId);
    return obj;
  },

  create<I extends Exact<DeepPartial<RevokeAccessTokenRequest>, I>>(base?: I): RevokeAccessTokenRequest {
    return RevokeAccessTokenRequest.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<RevokeAccessTokenRequest>, I>>(object: I): RevokeAccessTokenRequest {
    const message = createBaseRevokeAccessTokenRequest();
    message.token = object.token ?? "";
    message.orgId = object.orgId ?? "";
    return message;
  },
};

function createBaseRevokeAccessTokenResponse(): RevokeAccessTokenResponse {
  return { status: "" };
}

export const RevokeAccessTokenResponse = {
  encode(message: RevokeAccessTokenResponse, writer: _m0.Writer = _m0.Writer.create()): _m0.Writer {
    if (message.status !== "") {
      writer.uint32(10).string(message.status);
    }
    return writer;
  },

  decode(input: _m0.Reader | Uint8Array, length?: number): RevokeAccessTokenResponse {
    const reader = input instanceof _m0.Reader ? input : _m0.Reader.create(input);
    let end = length === undefined ? reader.len : reader.pos + length;
    const message = createBaseRevokeAccessTokenResponse();
    while (reader.pos < end) {
      const tag = reader.uint32();
      switch (tag >>> 3) {
        case 1:
          if (tag !== 10) {
            break;
          }

          message.status = reader.string();
          continue;
      }
      if ((tag & 7) === 4 || tag === 0) {
        break;
      }
      reader.skipType(tag & 7);
    }
    return message;
  },

  fromJSON(object: any): RevokeAccessTokenResponse {
    return { status: isSet(object.status) ? String(object.status) : "" };
  },

  toJSON(message: RevokeAccessTokenResponse): unknown {
    const obj: any = {};
    message.status !== undefined && (obj.status = message.status);
    return obj;
  },

  create<I extends Exact<DeepPartial<RevokeAccessTokenResponse>, I>>(base?: I): RevokeAccessTokenResponse {
    return RevokeAccessTokenResponse.fromPartial(base ?? {});
  },

  fromPartial<I extends Exact<DeepPartial<RevokeAccessTokenResponse>, I>>(object: I): RevokeAccessTokenResponse {
    const message = createBaseRevokeAccessTokenResponse();
    message.status = object.status ?? "";
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
