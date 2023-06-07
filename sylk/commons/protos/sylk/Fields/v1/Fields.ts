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
  CreateFieldRequest,
  CreateFieldResponse,
  DeleteFieldRequest,
  DeleteFieldResponse,
  GetFieldRequest,
  GetFieldResponse,
  UpdateFieldRequest,
  UpdateFieldResponse,
} from "../../SylkApi/v1/SylkApi";

/** sylk.build Generated proto DO NOT EDIT */

export type FieldsService = typeof FieldsService;
export const FieldsService = {
  /** [sylk] - None */
  createField: {
    path: "/Fields/CreateField",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: CreateFieldRequest) => Buffer.from(CreateFieldRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => CreateFieldRequest.decode(value),
    responseSerialize: (value: CreateFieldResponse) => Buffer.from(CreateFieldResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => CreateFieldResponse.decode(value),
  },
  /** [sylk] - None */
  getField: {
    path: "/Fields/GetField",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetFieldRequest) => Buffer.from(GetFieldRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetFieldRequest.decode(value),
    responseSerialize: (value: GetFieldResponse) => Buffer.from(GetFieldResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetFieldResponse.decode(value),
  },
  /** [sylk] - None */
  deleteField: {
    path: "/Fields/DeleteField",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: DeleteFieldRequest) => Buffer.from(DeleteFieldRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => DeleteFieldRequest.decode(value),
    responseSerialize: (value: DeleteFieldResponse) => Buffer.from(DeleteFieldResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => DeleteFieldResponse.decode(value),
  },
  /** [sylk] - None */
  updateField: {
    path: "/Fields/UpdateField",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateFieldRequest) => Buffer.from(UpdateFieldRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateFieldRequest.decode(value),
    responseSerialize: (value: UpdateFieldResponse) => Buffer.from(UpdateFieldResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateFieldResponse.decode(value),
  },
} as const;

export interface FieldsServer extends UntypedServiceImplementation {
  /** [sylk] - None */
  createField: handleUnaryCall<CreateFieldRequest, CreateFieldResponse>;
  /** [sylk] - None */
  getField: handleUnaryCall<GetFieldRequest, GetFieldResponse>;
  /** [sylk] - None */
  deleteField: handleUnaryCall<DeleteFieldRequest, DeleteFieldResponse>;
  /** [sylk] - None */
  updateField: handleUnaryCall<UpdateFieldRequest, UpdateFieldResponse>;
}

export interface FieldsClient extends Client {
  /** [sylk] - None */
  createField(
    request: CreateFieldRequest,
    callback: (error: ServiceError | null, response: CreateFieldResponse) => void,
  ): ClientUnaryCall;
  createField(
    request: CreateFieldRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: CreateFieldResponse) => void,
  ): ClientUnaryCall;
  createField(
    request: CreateFieldRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: CreateFieldResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  getField(
    request: GetFieldRequest,
    callback: (error: ServiceError | null, response: GetFieldResponse) => void,
  ): ClientUnaryCall;
  getField(
    request: GetFieldRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetFieldResponse) => void,
  ): ClientUnaryCall;
  getField(
    request: GetFieldRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetFieldResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  deleteField(
    request: DeleteFieldRequest,
    callback: (error: ServiceError | null, response: DeleteFieldResponse) => void,
  ): ClientUnaryCall;
  deleteField(
    request: DeleteFieldRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: DeleteFieldResponse) => void,
  ): ClientUnaryCall;
  deleteField(
    request: DeleteFieldRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: DeleteFieldResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateField(
    request: UpdateFieldRequest,
    callback: (error: ServiceError | null, response: UpdateFieldResponse) => void,
  ): ClientUnaryCall;
  updateField(
    request: UpdateFieldRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateFieldResponse) => void,
  ): ClientUnaryCall;
  updateField(
    request: UpdateFieldRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateFieldResponse) => void,
  ): ClientUnaryCall;
}

export const FieldsClient = makeGenericClientConstructor(FieldsService, "Fields") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ClientOptions>): FieldsClient;
  service: typeof FieldsService;
};
