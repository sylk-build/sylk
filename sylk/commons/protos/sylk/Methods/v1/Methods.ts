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
  CreateMethodRequest,
  CreateMethodResponse,
  DeleteMethodRequest,
  DeleteMethodResponse,
  GetMethodRequest,
  GetMethodResponse,
  UpdateMethodRequest,
  UpdateMethodResponse,
} from "../../SylkApi/v1/SylkApi";

/** sylk.build Generated proto DO NOT EDIT */

export type MethodsService = typeof MethodsService;
export const MethodsService = {
  /** [sylk] - None */
  createMethod: {
    path: "/Methods/CreateMethod",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: CreateMethodRequest) => Buffer.from(CreateMethodRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => CreateMethodRequest.decode(value),
    responseSerialize: (value: CreateMethodResponse) => Buffer.from(CreateMethodResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => CreateMethodResponse.decode(value),
  },
  /** [sylk] - None */
  getMethod: {
    path: "/Methods/GetMethod",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetMethodRequest) => Buffer.from(GetMethodRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetMethodRequest.decode(value),
    responseSerialize: (value: GetMethodResponse) => Buffer.from(GetMethodResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetMethodResponse.decode(value),
  },
  /** [sylk] - None */
  deleteMethod: {
    path: "/Methods/DeleteMethod",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: DeleteMethodRequest) => Buffer.from(DeleteMethodRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => DeleteMethodRequest.decode(value),
    responseSerialize: (value: DeleteMethodResponse) => Buffer.from(DeleteMethodResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => DeleteMethodResponse.decode(value),
  },
  /** [sylk] - None */
  updateMethod: {
    path: "/Methods/UpdateMethod",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateMethodRequest) => Buffer.from(UpdateMethodRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateMethodRequest.decode(value),
    responseSerialize: (value: UpdateMethodResponse) => Buffer.from(UpdateMethodResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateMethodResponse.decode(value),
  },
} as const;

export interface MethodsServer extends UntypedServiceImplementation {
  /** [sylk] - None */
  createMethod: handleUnaryCall<CreateMethodRequest, CreateMethodResponse>;
  /** [sylk] - None */
  getMethod: handleUnaryCall<GetMethodRequest, GetMethodResponse>;
  /** [sylk] - None */
  deleteMethod: handleUnaryCall<DeleteMethodRequest, DeleteMethodResponse>;
  /** [sylk] - None */
  updateMethod: handleUnaryCall<UpdateMethodRequest, UpdateMethodResponse>;
}

export interface MethodsClient extends Client {
  /** [sylk] - None */
  createMethod(
    request: CreateMethodRequest,
    callback: (error: ServiceError | null, response: CreateMethodResponse) => void,
  ): ClientUnaryCall;
  createMethod(
    request: CreateMethodRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: CreateMethodResponse) => void,
  ): ClientUnaryCall;
  createMethod(
    request: CreateMethodRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: CreateMethodResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  getMethod(
    request: GetMethodRequest,
    callback: (error: ServiceError | null, response: GetMethodResponse) => void,
  ): ClientUnaryCall;
  getMethod(
    request: GetMethodRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetMethodResponse) => void,
  ): ClientUnaryCall;
  getMethod(
    request: GetMethodRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetMethodResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  deleteMethod(
    request: DeleteMethodRequest,
    callback: (error: ServiceError | null, response: DeleteMethodResponse) => void,
  ): ClientUnaryCall;
  deleteMethod(
    request: DeleteMethodRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: DeleteMethodResponse) => void,
  ): ClientUnaryCall;
  deleteMethod(
    request: DeleteMethodRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: DeleteMethodResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateMethod(
    request: UpdateMethodRequest,
    callback: (error: ServiceError | null, response: UpdateMethodResponse) => void,
  ): ClientUnaryCall;
  updateMethod(
    request: UpdateMethodRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateMethodResponse) => void,
  ): ClientUnaryCall;
  updateMethod(
    request: UpdateMethodRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateMethodResponse) => void,
  ): ClientUnaryCall;
}

export const MethodsClient = makeGenericClientConstructor(MethodsService, "Methods") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ClientOptions>): MethodsClient;
  service: typeof MethodsService;
};
