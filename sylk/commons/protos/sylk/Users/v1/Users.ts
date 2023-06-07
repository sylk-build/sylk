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
  CreateAccessTokenRequest,
  CreateAccessTokenResponse,
  CreateUserRequest,
  CreateUserResponse,
  GetAccessTokenRequest,
  GetAccessTokenResponse,
  GetUserRequest,
  GetUserResponse,
  ListAccessTokensRequest,
  RevokeAccessTokenRequest,
  RevokeAccessTokenResponse,
  UpdateUserRequest,
  UpdateUserResponse,
} from "../../SylkApi/v1/SylkApi";

/** sylk.build Generated proto DO NOT EDIT */

export type UsersService = typeof UsersService;
export const UsersService = {
  /** [sylk] - None */
  createUser: {
    path: "/Users/CreateUser",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: CreateUserRequest) => Buffer.from(CreateUserRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => CreateUserRequest.decode(value),
    responseSerialize: (value: CreateUserResponse) => Buffer.from(CreateUserResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => CreateUserResponse.decode(value),
  },
  /** [sylk] - None */
  getAccessToken: {
    path: "/Users/GetAccessToken",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetAccessTokenRequest) => Buffer.from(GetAccessTokenRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetAccessTokenRequest.decode(value),
    responseSerialize: (value: GetAccessTokenResponse) => Buffer.from(GetAccessTokenResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetAccessTokenResponse.decode(value),
  },
  /** [sylk] - None */
  createAccessToken: {
    path: "/Users/CreateAccessToken",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: CreateAccessTokenRequest) => Buffer.from(CreateAccessTokenRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => CreateAccessTokenRequest.decode(value),
    responseSerialize: (value: CreateAccessTokenResponse) =>
      Buffer.from(CreateAccessTokenResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => CreateAccessTokenResponse.decode(value),
  },
  /** [sylk] - None */
  getUser: {
    path: "/Users/GetUser",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetUserRequest) => Buffer.from(GetUserRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetUserRequest.decode(value),
    responseSerialize: (value: GetUserResponse) => Buffer.from(GetUserResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetUserResponse.decode(value),
  },
  /** [sylk] - None */
  listAccessTokens: {
    path: "/Users/ListAccessTokens",
    requestStream: false,
    responseStream: true,
    requestSerialize: (value: ListAccessTokensRequest) => Buffer.from(ListAccessTokensRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => ListAccessTokensRequest.decode(value),
    responseSerialize: (value: GetAccessTokenResponse) => Buffer.from(GetAccessTokenResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetAccessTokenResponse.decode(value),
  },
  /** [sylk] - None */
  revokeAccessToken: {
    path: "/Users/RevokeAccessToken",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: RevokeAccessTokenRequest) => Buffer.from(RevokeAccessTokenRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => RevokeAccessTokenRequest.decode(value),
    responseSerialize: (value: RevokeAccessTokenResponse) =>
      Buffer.from(RevokeAccessTokenResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => RevokeAccessTokenResponse.decode(value),
  },
  /** [sylk] - None */
  updateUser: {
    path: "/Users/UpdateUser",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateUserRequest) => Buffer.from(UpdateUserRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateUserRequest.decode(value),
    responseSerialize: (value: UpdateUserResponse) => Buffer.from(UpdateUserResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateUserResponse.decode(value),
  },
} as const;

export interface UsersServer extends UntypedServiceImplementation {
  /** [sylk] - None */
  createUser: handleUnaryCall<CreateUserRequest, CreateUserResponse>;
  /** [sylk] - None */
  getAccessToken: handleUnaryCall<GetAccessTokenRequest, GetAccessTokenResponse>;
  /** [sylk] - None */
  createAccessToken: handleUnaryCall<CreateAccessTokenRequest, CreateAccessTokenResponse>;
  /** [sylk] - None */
  getUser: handleUnaryCall<GetUserRequest, GetUserResponse>;
  /** [sylk] - None */
  listAccessTokens: handleServerStreamingCall<ListAccessTokensRequest, GetAccessTokenResponse>;
  /** [sylk] - None */
  revokeAccessToken: handleUnaryCall<RevokeAccessTokenRequest, RevokeAccessTokenResponse>;
  /** [sylk] - None */
  updateUser: handleUnaryCall<UpdateUserRequest, UpdateUserResponse>;
}

export interface UsersClient extends Client {
  /** [sylk] - None */
  createUser(
    request: CreateUserRequest,
    callback: (error: ServiceError | null, response: CreateUserResponse) => void,
  ): ClientUnaryCall;
  createUser(
    request: CreateUserRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: CreateUserResponse) => void,
  ): ClientUnaryCall;
  createUser(
    request: CreateUserRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: CreateUserResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  getAccessToken(
    request: GetAccessTokenRequest,
    callback: (error: ServiceError | null, response: GetAccessTokenResponse) => void,
  ): ClientUnaryCall;
  getAccessToken(
    request: GetAccessTokenRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetAccessTokenResponse) => void,
  ): ClientUnaryCall;
  getAccessToken(
    request: GetAccessTokenRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetAccessTokenResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  createAccessToken(
    request: CreateAccessTokenRequest,
    callback: (error: ServiceError | null, response: CreateAccessTokenResponse) => void,
  ): ClientUnaryCall;
  createAccessToken(
    request: CreateAccessTokenRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: CreateAccessTokenResponse) => void,
  ): ClientUnaryCall;
  createAccessToken(
    request: CreateAccessTokenRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: CreateAccessTokenResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  getUser(
    request: GetUserRequest,
    callback: (error: ServiceError | null, response: GetUserResponse) => void,
  ): ClientUnaryCall;
  getUser(
    request: GetUserRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetUserResponse) => void,
  ): ClientUnaryCall;
  getUser(
    request: GetUserRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetUserResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  listAccessTokens(
    request: ListAccessTokensRequest,
    options?: Partial<CallOptions>,
  ): ClientReadableStream<GetAccessTokenResponse>;
  listAccessTokens(
    request: ListAccessTokensRequest,
    metadata?: Metadata,
    options?: Partial<CallOptions>,
  ): ClientReadableStream<GetAccessTokenResponse>;
  /** [sylk] - None */
  revokeAccessToken(
    request: RevokeAccessTokenRequest,
    callback: (error: ServiceError | null, response: RevokeAccessTokenResponse) => void,
  ): ClientUnaryCall;
  revokeAccessToken(
    request: RevokeAccessTokenRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: RevokeAccessTokenResponse) => void,
  ): ClientUnaryCall;
  revokeAccessToken(
    request: RevokeAccessTokenRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: RevokeAccessTokenResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateUser(
    request: UpdateUserRequest,
    callback: (error: ServiceError | null, response: UpdateUserResponse) => void,
  ): ClientUnaryCall;
  updateUser(
    request: UpdateUserRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateUserResponse) => void,
  ): ClientUnaryCall;
  updateUser(
    request: UpdateUserRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateUserResponse) => void,
  ): ClientUnaryCall;
}

export const UsersClient = makeGenericClientConstructor(UsersService, "Users") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ClientOptions>): UsersClient;
  service: typeof UsersService;
};
