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
  CreateMessageRequest,
  CreateMessageResponse,
  DeleteMessageRequest,
  DeleteMessageResponse,
  GetMessageRequest,
  GetMessageResponse,
  UpdateMessageRequest,
  UpdateMessageResponse,
} from "../../SylkApi/v1/SylkApi";

/** sylk.build Generated proto DO NOT EDIT */

export type MessagesService = typeof MessagesService;
export const MessagesService = {
  /** [sylk] - None */
  getMessage: {
    path: "/Messages/GetMessage",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetMessageRequest) => Buffer.from(GetMessageRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetMessageRequest.decode(value),
    responseSerialize: (value: GetMessageResponse) => Buffer.from(GetMessageResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetMessageResponse.decode(value),
  },
  /** [sylk] - None */
  updateMessage: {
    path: "/Messages/UpdateMessage",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateMessageRequest) => Buffer.from(UpdateMessageRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateMessageRequest.decode(value),
    responseSerialize: (value: UpdateMessageResponse) => Buffer.from(UpdateMessageResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateMessageResponse.decode(value),
  },
  /** [sylk] - None */
  createMessage: {
    path: "/Messages/CreateMessage",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: CreateMessageRequest) => Buffer.from(CreateMessageRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => CreateMessageRequest.decode(value),
    responseSerialize: (value: CreateMessageResponse) => Buffer.from(CreateMessageResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => CreateMessageResponse.decode(value),
  },
  /** [sylk] - None */
  deleteMessage: {
    path: "/Messages/DeleteMessage",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: DeleteMessageRequest) => Buffer.from(DeleteMessageRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => DeleteMessageRequest.decode(value),
    responseSerialize: (value: DeleteMessageResponse) => Buffer.from(DeleteMessageResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => DeleteMessageResponse.decode(value),
  },
} as const;

export interface MessagesServer extends UntypedServiceImplementation {
  /** [sylk] - None */
  getMessage: handleUnaryCall<GetMessageRequest, GetMessageResponse>;
  /** [sylk] - None */
  updateMessage: handleUnaryCall<UpdateMessageRequest, UpdateMessageResponse>;
  /** [sylk] - None */
  createMessage: handleUnaryCall<CreateMessageRequest, CreateMessageResponse>;
  /** [sylk] - None */
  deleteMessage: handleUnaryCall<DeleteMessageRequest, DeleteMessageResponse>;
}

export interface MessagesClient extends Client {
  /** [sylk] - None */
  getMessage(
    request: GetMessageRequest,
    callback: (error: ServiceError | null, response: GetMessageResponse) => void,
  ): ClientUnaryCall;
  getMessage(
    request: GetMessageRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetMessageResponse) => void,
  ): ClientUnaryCall;
  getMessage(
    request: GetMessageRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetMessageResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateMessage(
    request: UpdateMessageRequest,
    callback: (error: ServiceError | null, response: UpdateMessageResponse) => void,
  ): ClientUnaryCall;
  updateMessage(
    request: UpdateMessageRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateMessageResponse) => void,
  ): ClientUnaryCall;
  updateMessage(
    request: UpdateMessageRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateMessageResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  createMessage(
    request: CreateMessageRequest,
    callback: (error: ServiceError | null, response: CreateMessageResponse) => void,
  ): ClientUnaryCall;
  createMessage(
    request: CreateMessageRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: CreateMessageResponse) => void,
  ): ClientUnaryCall;
  createMessage(
    request: CreateMessageRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: CreateMessageResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  deleteMessage(
    request: DeleteMessageRequest,
    callback: (error: ServiceError | null, response: DeleteMessageResponse) => void,
  ): ClientUnaryCall;
  deleteMessage(
    request: DeleteMessageRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: DeleteMessageResponse) => void,
  ): ClientUnaryCall;
  deleteMessage(
    request: DeleteMessageRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: DeleteMessageResponse) => void,
  ): ClientUnaryCall;
}

export const MessagesClient = makeGenericClientConstructor(MessagesService, "Messages") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ClientOptions>): MessagesClient;
  service: typeof MessagesService;
};
