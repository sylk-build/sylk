/* eslint-disable */
import {
  CallOptions,
  ChannelCredentials,
  Client,
  ClientOptions,
  ClientReadableStream,
  ClientUnaryCall,
  handleServerStreamingCall,
  handleUnaryCall,
  makeGenericClientConstructor,
  Metadata,
  ServiceError,
  UntypedServiceImplementation,
} from "@grpc/grpc-js";
import {
  AcceptUserInviteRequest,
  AcceptUserInviteResponse,
  AddUserRequest,
  AddUserResponse,
  GetOrganizationRequest,
  GetOrganizationResponse,
  ListOrganizationsRequest,
  RemoveUserRequest,
  RemoveUserResponse,
  UpdateOrganizationRequest,
  UpdateOrganizationResponse,
  UpdateUserRoleRequest,
  UpdateUserRoleResponse,
  UpdateUserStatusRequest,
  UpdateUserStatusResponse,
} from "../../SylkApi/v1/SylkApi";

/** sylk.build Generated proto DO NOT EDIT */

export type OrganizationsService = typeof OrganizationsService;
export const OrganizationsService = {
  /** [sylk] - None */
  acceprUserInvite: {
    path: "/Organizations/AcceprUserInvite",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: AcceptUserInviteRequest) => Buffer.from(AcceptUserInviteRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => AcceptUserInviteRequest.decode(value),
    responseSerialize: (value: AcceptUserInviteResponse) =>
      Buffer.from(AcceptUserInviteResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => AcceptUserInviteResponse.decode(value),
  },
  /** [sylk] - None */
  getOrganization: {
    path: "/Organizations/GetOrganization",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetOrganizationRequest) => Buffer.from(GetOrganizationRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetOrganizationRequest.decode(value),
    responseSerialize: (value: GetOrganizationResponse) => Buffer.from(GetOrganizationResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetOrganizationResponse.decode(value),
  },
  /** [sylk] - None */
  updateOrganization: {
    path: "/Organizations/UpdateOrganization",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateOrganizationRequest) =>
      Buffer.from(UpdateOrganizationRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateOrganizationRequest.decode(value),
    responseSerialize: (value: UpdateOrganizationResponse) =>
      Buffer.from(UpdateOrganizationResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateOrganizationResponse.decode(value),
  },
  /** [sylk] - None */
  listOrganizations: {
    path: "/Organizations/ListOrganizations",
    requestStream: false,
    responseStream: true,
    requestSerialize: (value: ListOrganizationsRequest) => Buffer.from(ListOrganizationsRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => ListOrganizationsRequest.decode(value),
    responseSerialize: (value: GetOrganizationResponse) => Buffer.from(GetOrganizationResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetOrganizationResponse.decode(value),
  },
  /** [sylk] - None */
  addUser: {
    path: "/Organizations/AddUser",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: AddUserRequest) => Buffer.from(AddUserRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => AddUserRequest.decode(value),
    responseSerialize: (value: AddUserResponse) => Buffer.from(AddUserResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => AddUserResponse.decode(value),
  },
  /** [sylk] - None */
  updateUserStatus: {
    path: "/Organizations/UpdateUserStatus",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateUserStatusRequest) => Buffer.from(UpdateUserStatusRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateUserStatusRequest.decode(value),
    responseSerialize: (value: UpdateUserStatusResponse) =>
      Buffer.from(UpdateUserStatusResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateUserStatusResponse.decode(value),
  },
  /** [sylk] - None */
  removeUser: {
    path: "/Organizations/RemoveUser",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: RemoveUserRequest) => Buffer.from(RemoveUserRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => RemoveUserRequest.decode(value),
    responseSerialize: (value: RemoveUserResponse) => Buffer.from(RemoveUserResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => RemoveUserResponse.decode(value),
  },
  /** [sylk] - None */
  updateUserRole: {
    path: "/Organizations/UpdateUserRole",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateUserRoleRequest) => Buffer.from(UpdateUserRoleRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateUserRoleRequest.decode(value),
    responseSerialize: (value: UpdateUserRoleResponse) => Buffer.from(UpdateUserRoleResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateUserRoleResponse.decode(value),
  },
} as const;

export interface OrganizationsServer extends UntypedServiceImplementation {
  /** [sylk] - None */
  acceprUserInvite: handleUnaryCall<AcceptUserInviteRequest, AcceptUserInviteResponse>;
  /** [sylk] - None */
  getOrganization: handleUnaryCall<GetOrganizationRequest, GetOrganizationResponse>;
  /** [sylk] - None */
  updateOrganization: handleUnaryCall<UpdateOrganizationRequest, UpdateOrganizationResponse>;
  /** [sylk] - None */
  listOrganizations: handleServerStreamingCall<ListOrganizationsRequest, GetOrganizationResponse>;
  /** [sylk] - None */
  addUser: handleUnaryCall<AddUserRequest, AddUserResponse>;
  /** [sylk] - None */
  updateUserStatus: handleUnaryCall<UpdateUserStatusRequest, UpdateUserStatusResponse>;
  /** [sylk] - None */
  removeUser: handleUnaryCall<RemoveUserRequest, RemoveUserResponse>;
  /** [sylk] - None */
  updateUserRole: handleUnaryCall<UpdateUserRoleRequest, UpdateUserRoleResponse>;
}

export interface OrganizationsClient extends Client {
  /** [sylk] - None */
  acceprUserInvite(
    request: AcceptUserInviteRequest,
    callback: (error: ServiceError | null, response: AcceptUserInviteResponse) => void,
  ): ClientUnaryCall;
  acceprUserInvite(
    request: AcceptUserInviteRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: AcceptUserInviteResponse) => void,
  ): ClientUnaryCall;
  acceprUserInvite(
    request: AcceptUserInviteRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: AcceptUserInviteResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  getOrganization(
    request: GetOrganizationRequest,
    callback: (error: ServiceError | null, response: GetOrganizationResponse) => void,
  ): ClientUnaryCall;
  getOrganization(
    request: GetOrganizationRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetOrganizationResponse) => void,
  ): ClientUnaryCall;
  getOrganization(
    request: GetOrganizationRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetOrganizationResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateOrganization(
    request: UpdateOrganizationRequest,
    callback: (error: ServiceError | null, response: UpdateOrganizationResponse) => void,
  ): ClientUnaryCall;
  updateOrganization(
    request: UpdateOrganizationRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateOrganizationResponse) => void,
  ): ClientUnaryCall;
  updateOrganization(
    request: UpdateOrganizationRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateOrganizationResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  listOrganizations(
    request: ListOrganizationsRequest,
    options?: Partial<CallOptions>,
  ): ClientReadableStream<GetOrganizationResponse>;
  listOrganizations(
    request: ListOrganizationsRequest,
    metadata?: Metadata,
    options?: Partial<CallOptions>,
  ): ClientReadableStream<GetOrganizationResponse>;
  /** [sylk] - None */
  addUser(
    request: AddUserRequest,
    callback: (error: ServiceError | null, response: AddUserResponse) => void,
  ): ClientUnaryCall;
  addUser(
    request: AddUserRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: AddUserResponse) => void,
  ): ClientUnaryCall;
  addUser(
    request: AddUserRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: AddUserResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateUserStatus(
    request: UpdateUserStatusRequest,
    callback: (error: ServiceError | null, response: UpdateUserStatusResponse) => void,
  ): ClientUnaryCall;
  updateUserStatus(
    request: UpdateUserStatusRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateUserStatusResponse) => void,
  ): ClientUnaryCall;
  updateUserStatus(
    request: UpdateUserStatusRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateUserStatusResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  removeUser(
    request: RemoveUserRequest,
    callback: (error: ServiceError | null, response: RemoveUserResponse) => void,
  ): ClientUnaryCall;
  removeUser(
    request: RemoveUserRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: RemoveUserResponse) => void,
  ): ClientUnaryCall;
  removeUser(
    request: RemoveUserRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: RemoveUserResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateUserRole(
    request: UpdateUserRoleRequest,
    callback: (error: ServiceError | null, response: UpdateUserRoleResponse) => void,
  ): ClientUnaryCall;
  updateUserRole(
    request: UpdateUserRoleRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateUserRoleResponse) => void,
  ): ClientUnaryCall;
  updateUserRole(
    request: UpdateUserRoleRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateUserRoleResponse) => void,
  ): ClientUnaryCall;
}

export const OrganizationsClient = makeGenericClientConstructor(OrganizationsService, "Organizations") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ClientOptions>): OrganizationsClient;
  service: typeof OrganizationsService;
};
