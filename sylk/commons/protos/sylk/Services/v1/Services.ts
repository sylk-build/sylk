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
  CreateServiceRequest,
  CreateServiceResponse,
  DeleteServiceRequest,
  DeleteServiceResponse,
  GetServiceRequest,
  GetServiceResponse,
  ListServicesRequest,
  UpdateServiceRequest,
  UpdateServiceResponse,
} from "../../SylkApi/v1/SylkApi";

/** sylk.build Generated proto DO NOT EDIT */

export type ServicesService = typeof ServicesService;
export const ServicesService = {
  /** [sylk] - None */
  createService: {
    path: "/Services/CreateService",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: CreateServiceRequest) => Buffer.from(CreateServiceRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => CreateServiceRequest.decode(value),
    responseSerialize: (value: CreateServiceResponse) => Buffer.from(CreateServiceResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => CreateServiceResponse.decode(value),
  },
  /** [sylk] - None */
  getService: {
    path: "/Services/GetService",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetServiceRequest) => Buffer.from(GetServiceRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetServiceRequest.decode(value),
    responseSerialize: (value: GetServiceResponse) => Buffer.from(GetServiceResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetServiceResponse.decode(value),
  },
  /** [sylk] - None */
  updateService: {
    path: "/Services/UpdateService",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateServiceRequest) => Buffer.from(UpdateServiceRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateServiceRequest.decode(value),
    responseSerialize: (value: UpdateServiceResponse) => Buffer.from(UpdateServiceResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateServiceResponse.decode(value),
  },
  /** [sylk] - None */
  listServices: {
    path: "/Services/ListServices",
    requestStream: false,
    responseStream: true,
    requestSerialize: (value: ListServicesRequest) => Buffer.from(ListServicesRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => ListServicesRequest.decode(value),
    responseSerialize: (value: GetServiceResponse) => Buffer.from(GetServiceResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetServiceResponse.decode(value),
  },
  /** [sylk] - None */
  deleteService: {
    path: "/Services/DeleteService",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: DeleteServiceRequest) => Buffer.from(DeleteServiceRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => DeleteServiceRequest.decode(value),
    responseSerialize: (value: DeleteServiceResponse) => Buffer.from(DeleteServiceResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => DeleteServiceResponse.decode(value),
  },
} as const;

export interface ServicesServer extends UntypedServiceImplementation {
  /** [sylk] - None */
  createService: handleUnaryCall<CreateServiceRequest, CreateServiceResponse>;
  /** [sylk] - None */
  getService: handleUnaryCall<GetServiceRequest, GetServiceResponse>;
  /** [sylk] - None */
  updateService: handleUnaryCall<UpdateServiceRequest, UpdateServiceResponse>;
  /** [sylk] - None */
  listServices: handleServerStreamingCall<ListServicesRequest, GetServiceResponse>;
  /** [sylk] - None */
  deleteService: handleUnaryCall<DeleteServiceRequest, DeleteServiceResponse>;
}

export interface ServicesClient extends Client {
  /** [sylk] - None */
  createService(
    request: CreateServiceRequest,
    callback: (error: ServiceError | null, response: CreateServiceResponse) => void,
  ): ClientUnaryCall;
  createService(
    request: CreateServiceRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: CreateServiceResponse) => void,
  ): ClientUnaryCall;
  createService(
    request: CreateServiceRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: CreateServiceResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  getService(
    request: GetServiceRequest,
    callback: (error: ServiceError | null, response: GetServiceResponse) => void,
  ): ClientUnaryCall;
  getService(
    request: GetServiceRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetServiceResponse) => void,
  ): ClientUnaryCall;
  getService(
    request: GetServiceRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetServiceResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateService(
    request: UpdateServiceRequest,
    callback: (error: ServiceError | null, response: UpdateServiceResponse) => void,
  ): ClientUnaryCall;
  updateService(
    request: UpdateServiceRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateServiceResponse) => void,
  ): ClientUnaryCall;
  updateService(
    request: UpdateServiceRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateServiceResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  listServices(request: ListServicesRequest, options?: Partial<CallOptions>): ClientReadableStream<GetServiceResponse>;
  listServices(
    request: ListServicesRequest,
    metadata?: Metadata,
    options?: Partial<CallOptions>,
  ): ClientReadableStream<GetServiceResponse>;
  /** [sylk] - None */
  deleteService(
    request: DeleteServiceRequest,
    callback: (error: ServiceError | null, response: DeleteServiceResponse) => void,
  ): ClientUnaryCall;
  deleteService(
    request: DeleteServiceRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: DeleteServiceResponse) => void,
  ): ClientUnaryCall;
  deleteService(
    request: DeleteServiceRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: DeleteServiceResponse) => void,
  ): ClientUnaryCall;
}

export const ServicesClient = makeGenericClientConstructor(ServicesService, "Services") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ClientOptions>): ServicesClient;
  service: typeof ServicesService;
};
