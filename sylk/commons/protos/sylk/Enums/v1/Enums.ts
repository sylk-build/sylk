/* eslint-disable */
import {
  CallOptions,
  ChannelCredentials,
  Client,
  ClientOptions,
  ClientUnaryCall,
  handleUnaryCall,
  makeGenericClientConstructor,
  Metadata,
  ServiceError,
  UntypedServiceImplementation,
} from "@grpc/grpc-js";
import {
  CreateEnumRequest,
  CreateEnumResponse,
  DeleteEnumRequest,
  DeleteEnumResponse,
  GetEnumRequest,
  GetEnumResponse,
  UpdateEnumRequest,
  UpdateEnumResponse,
} from "../../SylkApi/v1/SylkApi";

/** sylk.build Generated proto DO NOT EDIT */

export type EnumsService = typeof EnumsService;
export const EnumsService = {
  /** [sylk] - None */
  getEnum: {
    path: "/Enums/GetEnum",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetEnumRequest) => Buffer.from(GetEnumRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetEnumRequest.decode(value),
    responseSerialize: (value: GetEnumResponse) => Buffer.from(GetEnumResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetEnumResponse.decode(value),
  },
  /** [sylk] - None */
  updateEnum: {
    path: "/Enums/UpdateEnum",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateEnumRequest) => Buffer.from(UpdateEnumRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateEnumRequest.decode(value),
    responseSerialize: (value: UpdateEnumResponse) => Buffer.from(UpdateEnumResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateEnumResponse.decode(value),
  },
  /** [sylk] - None */
  deleteEnum: {
    path: "/Enums/DeleteEnum",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: DeleteEnumRequest) => Buffer.from(DeleteEnumRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => DeleteEnumRequest.decode(value),
    responseSerialize: (value: DeleteEnumResponse) => Buffer.from(DeleteEnumResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => DeleteEnumResponse.decode(value),
  },
  /** [sylk] - None */
  createEnum: {
    path: "/Enums/CreateEnum",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: CreateEnumRequest) => Buffer.from(CreateEnumRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => CreateEnumRequest.decode(value),
    responseSerialize: (value: CreateEnumResponse) => Buffer.from(CreateEnumResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => CreateEnumResponse.decode(value),
  },
} as const;

export interface EnumsServer extends UntypedServiceImplementation {
  /** [sylk] - None */
  getEnum: handleUnaryCall<GetEnumRequest, GetEnumResponse>;
  /** [sylk] - None */
  updateEnum: handleUnaryCall<UpdateEnumRequest, UpdateEnumResponse>;
  /** [sylk] - None */
  deleteEnum: handleUnaryCall<DeleteEnumRequest, DeleteEnumResponse>;
  /** [sylk] - None */
  createEnum: handleUnaryCall<CreateEnumRequest, CreateEnumResponse>;
}

export interface EnumsClient extends Client {
  /** [sylk] - None */
  getEnum(
    request: GetEnumRequest,
    callback: (error: ServiceError | null, response: GetEnumResponse) => void,
  ): ClientUnaryCall;
  getEnum(
    request: GetEnumRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetEnumResponse) => void,
  ): ClientUnaryCall;
  getEnum(
    request: GetEnumRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetEnumResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateEnum(
    request: UpdateEnumRequest,
    callback: (error: ServiceError | null, response: UpdateEnumResponse) => void,
  ): ClientUnaryCall;
  updateEnum(
    request: UpdateEnumRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateEnumResponse) => void,
  ): ClientUnaryCall;
  updateEnum(
    request: UpdateEnumRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateEnumResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  deleteEnum(
    request: DeleteEnumRequest,
    callback: (error: ServiceError | null, response: DeleteEnumResponse) => void,
  ): ClientUnaryCall;
  deleteEnum(
    request: DeleteEnumRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: DeleteEnumResponse) => void,
  ): ClientUnaryCall;
  deleteEnum(
    request: DeleteEnumRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: DeleteEnumResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  createEnum(
    request: CreateEnumRequest,
    callback: (error: ServiceError | null, response: CreateEnumResponse) => void,
  ): ClientUnaryCall;
  createEnum(
    request: CreateEnumRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: CreateEnumResponse) => void,
  ): ClientUnaryCall;
  createEnum(
    request: CreateEnumRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: CreateEnumResponse) => void,
  ): ClientUnaryCall;
}

export const EnumsClient = makeGenericClientConstructor(EnumsService, "Enums") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ClientOptions>): EnumsClient;
  service: typeof EnumsService;
};
