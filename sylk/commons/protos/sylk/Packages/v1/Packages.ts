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
  CreatePackageRequest,
  CreatePackageResponse,
  DeletePackageRequest,
  DeletePackageResponse,
  GetPackageRequest,
  GetPackageResponse,
  ListPackagesRequest,
  UpdatePackageRequest,
  UpdatePackageResponse,
} from "../../SylkApi/v1/SylkApi";

/** sylk.build Generated proto DO NOT EDIT */

export type PackagesService = typeof PackagesService;
export const PackagesService = {
  /** [sylk] - None */
  getPackage: {
    path: "/Packages/GetPackage",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetPackageRequest) => Buffer.from(GetPackageRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetPackageRequest.decode(value),
    responseSerialize: (value: GetPackageResponse) => Buffer.from(GetPackageResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetPackageResponse.decode(value),
  },
  /** [sylk] - None */
  createPackage: {
    path: "/Packages/CreatePackage",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: CreatePackageRequest) => Buffer.from(CreatePackageRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => CreatePackageRequest.decode(value),
    responseSerialize: (value: CreatePackageResponse) => Buffer.from(CreatePackageResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => CreatePackageResponse.decode(value),
  },
  /** [sylk] - None */
  deletePackage: {
    path: "/Packages/DeletePackage",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: DeletePackageRequest) => Buffer.from(DeletePackageRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => DeletePackageRequest.decode(value),
    responseSerialize: (value: DeletePackageResponse) => Buffer.from(DeletePackageResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => DeletePackageResponse.decode(value),
  },
  /** [sylk] - None */
  updatePackage: {
    path: "/Packages/UpdatePackage",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdatePackageRequest) => Buffer.from(UpdatePackageRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdatePackageRequest.decode(value),
    responseSerialize: (value: UpdatePackageResponse) => Buffer.from(UpdatePackageResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdatePackageResponse.decode(value),
  },
  /** [sylk] - None */
  listPackages: {
    path: "/Packages/ListPackages",
    requestStream: false,
    responseStream: true,
    requestSerialize: (value: ListPackagesRequest) => Buffer.from(ListPackagesRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => ListPackagesRequest.decode(value),
    responseSerialize: (value: GetPackageResponse) => Buffer.from(GetPackageResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetPackageResponse.decode(value),
  },
} as const;

export interface PackagesServer extends UntypedServiceImplementation {
  /** [sylk] - None */
  getPackage: handleUnaryCall<GetPackageRequest, GetPackageResponse>;
  /** [sylk] - None */
  createPackage: handleUnaryCall<CreatePackageRequest, CreatePackageResponse>;
  /** [sylk] - None */
  deletePackage: handleUnaryCall<DeletePackageRequest, DeletePackageResponse>;
  /** [sylk] - None */
  updatePackage: handleUnaryCall<UpdatePackageRequest, UpdatePackageResponse>;
  /** [sylk] - None */
  listPackages: handleServerStreamingCall<ListPackagesRequest, GetPackageResponse>;
}

export interface PackagesClient extends Client {
  /** [sylk] - None */
  getPackage(
    request: GetPackageRequest,
    callback: (error: ServiceError | null, response: GetPackageResponse) => void,
  ): ClientUnaryCall;
  getPackage(
    request: GetPackageRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetPackageResponse) => void,
  ): ClientUnaryCall;
  getPackage(
    request: GetPackageRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetPackageResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  createPackage(
    request: CreatePackageRequest,
    callback: (error: ServiceError | null, response: CreatePackageResponse) => void,
  ): ClientUnaryCall;
  createPackage(
    request: CreatePackageRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: CreatePackageResponse) => void,
  ): ClientUnaryCall;
  createPackage(
    request: CreatePackageRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: CreatePackageResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  deletePackage(
    request: DeletePackageRequest,
    callback: (error: ServiceError | null, response: DeletePackageResponse) => void,
  ): ClientUnaryCall;
  deletePackage(
    request: DeletePackageRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: DeletePackageResponse) => void,
  ): ClientUnaryCall;
  deletePackage(
    request: DeletePackageRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: DeletePackageResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updatePackage(
    request: UpdatePackageRequest,
    callback: (error: ServiceError | null, response: UpdatePackageResponse) => void,
  ): ClientUnaryCall;
  updatePackage(
    request: UpdatePackageRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdatePackageResponse) => void,
  ): ClientUnaryCall;
  updatePackage(
    request: UpdatePackageRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdatePackageResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  listPackages(request: ListPackagesRequest, options?: Partial<CallOptions>): ClientReadableStream<GetPackageResponse>;
  listPackages(
    request: ListPackagesRequest,
    metadata?: Metadata,
    options?: Partial<CallOptions>,
  ): ClientReadableStream<GetPackageResponse>;
}

export const PackagesClient = makeGenericClientConstructor(PackagesService, "Packages") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ClientOptions>): PackagesClient;
  service: typeof PackagesService;
};
