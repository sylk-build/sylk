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
  CreateEnumValueRequest,
  CreateEnumValueResponse,
  DeleteEnumValueRequest,
  DeleteEnumValueResponse,
  GetEnumValueRequest,
  GetEnumValueResponse,
  UpdateEnumValueRequest,
  UpdateEnumValueResponse,
} from "../../SylkApi/v1/SylkApi";

/** sylk.build Generated proto DO NOT EDIT */

export type EnumValuesService = typeof EnumValuesService;
export const EnumValuesService = {
  /** [sylk] - None */
  getEnumValue: {
    path: "/EnumValues/GetEnumValue",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetEnumValueRequest) => Buffer.from(GetEnumValueRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetEnumValueRequest.decode(value),
    responseSerialize: (value: GetEnumValueResponse) => Buffer.from(GetEnumValueResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetEnumValueResponse.decode(value),
  },
  /** [sylk] - None */
  createEnumValue: {
    path: "/EnumValues/CreateEnumValue",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: CreateEnumValueRequest) => Buffer.from(CreateEnumValueRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => CreateEnumValueRequest.decode(value),
    responseSerialize: (value: CreateEnumValueResponse) => Buffer.from(CreateEnumValueResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => CreateEnumValueResponse.decode(value),
  },
  /** [sylk] - None */
  deleteEnumValue: {
    path: "/EnumValues/DeleteEnumValue",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: DeleteEnumValueRequest) => Buffer.from(DeleteEnumValueRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => DeleteEnumValueRequest.decode(value),
    responseSerialize: (value: DeleteEnumValueResponse) => Buffer.from(DeleteEnumValueResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => DeleteEnumValueResponse.decode(value),
  },
  /** [sylk] - None */
  updateEnumValue: {
    path: "/EnumValues/UpdateEnumValue",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateEnumValueRequest) => Buffer.from(UpdateEnumValueRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateEnumValueRequest.decode(value),
    responseSerialize: (value: UpdateEnumValueResponse) => Buffer.from(UpdateEnumValueResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateEnumValueResponse.decode(value),
  },
} as const;

export interface EnumValuesServer extends UntypedServiceImplementation {
  /** [sylk] - None */
  getEnumValue: handleUnaryCall<GetEnumValueRequest, GetEnumValueResponse>;
  /** [sylk] - None */
  createEnumValue: handleUnaryCall<CreateEnumValueRequest, CreateEnumValueResponse>;
  /** [sylk] - None */
  deleteEnumValue: handleUnaryCall<DeleteEnumValueRequest, DeleteEnumValueResponse>;
  /** [sylk] - None */
  updateEnumValue: handleUnaryCall<UpdateEnumValueRequest, UpdateEnumValueResponse>;
}

export interface EnumValuesClient extends Client {
  /** [sylk] - None */
  getEnumValue(
    request: GetEnumValueRequest,
    callback: (error: ServiceError | null, response: GetEnumValueResponse) => void,
  ): ClientUnaryCall;
  getEnumValue(
    request: GetEnumValueRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetEnumValueResponse) => void,
  ): ClientUnaryCall;
  getEnumValue(
    request: GetEnumValueRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetEnumValueResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  createEnumValue(
    request: CreateEnumValueRequest,
    callback: (error: ServiceError | null, response: CreateEnumValueResponse) => void,
  ): ClientUnaryCall;
  createEnumValue(
    request: CreateEnumValueRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: CreateEnumValueResponse) => void,
  ): ClientUnaryCall;
  createEnumValue(
    request: CreateEnumValueRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: CreateEnumValueResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  deleteEnumValue(
    request: DeleteEnumValueRequest,
    callback: (error: ServiceError | null, response: DeleteEnumValueResponse) => void,
  ): ClientUnaryCall;
  deleteEnumValue(
    request: DeleteEnumValueRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: DeleteEnumValueResponse) => void,
  ): ClientUnaryCall;
  deleteEnumValue(
    request: DeleteEnumValueRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: DeleteEnumValueResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateEnumValue(
    request: UpdateEnumValueRequest,
    callback: (error: ServiceError | null, response: UpdateEnumValueResponse) => void,
  ): ClientUnaryCall;
  updateEnumValue(
    request: UpdateEnumValueRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateEnumValueResponse) => void,
  ): ClientUnaryCall;
  updateEnumValue(
    request: UpdateEnumValueRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateEnumValueResponse) => void,
  ): ClientUnaryCall;
}

export const EnumValuesClient = makeGenericClientConstructor(EnumValuesService, "EnumValues") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ClientOptions>): EnumValuesClient;
  service: typeof EnumValuesService;
};
