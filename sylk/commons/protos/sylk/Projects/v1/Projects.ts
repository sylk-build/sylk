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
  AddUserRequest,
  AddUserResponse,
  CreateProjectRequest,
  CreateProjectResponse,
  DeleteProjectRequest,
  DeleteProjectResponse,
  GetProjectRequest,
  GetProjectResponse,
  ListProjectsRequest,
  RemoveUserRequest,
  RemoveUserResponse,
  UpdateProjectRequest,
  UpdateProjectResponse,
  UpdateUserRoleRequest,
  UpdateUserRoleResponse,
  UpdateUserStatusRequest,
  UpdateUserStatusResponse,
} from "../../SylkApi/v1/SylkApi";

/** sylk.build Generated proto DO NOT EDIT */

export type ProjectsService = typeof ProjectsService;
export const ProjectsService = {
  /** [sylk] - None */
  updateUserRoleProject: {
    path: "/Projects/UpdateUserRoleProject",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateUserRoleRequest) => Buffer.from(UpdateUserRoleRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateUserRoleRequest.decode(value),
    responseSerialize: (value: UpdateUserRoleResponse) => Buffer.from(UpdateUserRoleResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateUserRoleResponse.decode(value),
  },
  /** [sylk] - None */
  removeUserProject: {
    path: "/Projects/RemoveUserProject",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: RemoveUserRequest) => Buffer.from(RemoveUserRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => RemoveUserRequest.decode(value),
    responseSerialize: (value: RemoveUserResponse) => Buffer.from(RemoveUserResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => RemoveUserResponse.decode(value),
  },
  /** [sylk] - None */
  addUserProject: {
    path: "/Projects/AddUserProject",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: AddUserRequest) => Buffer.from(AddUserRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => AddUserRequest.decode(value),
    responseSerialize: (value: AddUserResponse) => Buffer.from(AddUserResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => AddUserResponse.decode(value),
  },
  /** [sylk] - None */
  getProject: {
    path: "/Projects/GetProject",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: GetProjectRequest) => Buffer.from(GetProjectRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => GetProjectRequest.decode(value),
    responseSerialize: (value: GetProjectResponse) => Buffer.from(GetProjectResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetProjectResponse.decode(value),
  },
  /** [sylk] - None */
  updateProject: {
    path: "/Projects/UpdateProject",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateProjectRequest) => Buffer.from(UpdateProjectRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateProjectRequest.decode(value),
    responseSerialize: (value: UpdateProjectResponse) => Buffer.from(UpdateProjectResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateProjectResponse.decode(value),
  },
  /** [sylk] - None */
  createProject: {
    path: "/Projects/CreateProject",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: CreateProjectRequest) => Buffer.from(CreateProjectRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => CreateProjectRequest.decode(value),
    responseSerialize: (value: CreateProjectResponse) => Buffer.from(CreateProjectResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => CreateProjectResponse.decode(value),
  },
  /** [sylk] - None */
  deleteProject: {
    path: "/Projects/DeleteProject",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: DeleteProjectRequest) => Buffer.from(DeleteProjectRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => DeleteProjectRequest.decode(value),
    responseSerialize: (value: DeleteProjectResponse) => Buffer.from(DeleteProjectResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => DeleteProjectResponse.decode(value),
  },
  /** [sylk] - None */
  listProjects: {
    path: "/Projects/ListProjects",
    requestStream: false,
    responseStream: true,
    requestSerialize: (value: ListProjectsRequest) => Buffer.from(ListProjectsRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => ListProjectsRequest.decode(value),
    responseSerialize: (value: GetProjectResponse) => Buffer.from(GetProjectResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => GetProjectResponse.decode(value),
  },
  /** [sylk] - None */
  updateUserStatusProject: {
    path: "/Projects/UpdateUserStatusProject",
    requestStream: false,
    responseStream: false,
    requestSerialize: (value: UpdateUserStatusRequest) => Buffer.from(UpdateUserStatusRequest.encode(value).finish()),
    requestDeserialize: (value: Buffer) => UpdateUserStatusRequest.decode(value),
    responseSerialize: (value: UpdateUserStatusResponse) =>
      Buffer.from(UpdateUserStatusResponse.encode(value).finish()),
    responseDeserialize: (value: Buffer) => UpdateUserStatusResponse.decode(value),
  },
} as const;

export interface ProjectsServer extends UntypedServiceImplementation {
  /** [sylk] - None */
  updateUserRoleProject: handleUnaryCall<UpdateUserRoleRequest, UpdateUserRoleResponse>;
  /** [sylk] - None */
  removeUserProject: handleUnaryCall<RemoveUserRequest, RemoveUserResponse>;
  /** [sylk] - None */
  addUserProject: handleUnaryCall<AddUserRequest, AddUserResponse>;
  /** [sylk] - None */
  getProject: handleUnaryCall<GetProjectRequest, GetProjectResponse>;
  /** [sylk] - None */
  updateProject: handleUnaryCall<UpdateProjectRequest, UpdateProjectResponse>;
  /** [sylk] - None */
  createProject: handleUnaryCall<CreateProjectRequest, CreateProjectResponse>;
  /** [sylk] - None */
  deleteProject: handleUnaryCall<DeleteProjectRequest, DeleteProjectResponse>;
  /** [sylk] - None */
  listProjects: handleServerStreamingCall<ListProjectsRequest, GetProjectResponse>;
  /** [sylk] - None */
  updateUserStatusProject: handleUnaryCall<UpdateUserStatusRequest, UpdateUserStatusResponse>;
}

export interface ProjectsClient extends Client {
  /** [sylk] - None */
  updateUserRoleProject(
    request: UpdateUserRoleRequest,
    callback: (error: ServiceError | null, response: UpdateUserRoleResponse) => void,
  ): ClientUnaryCall;
  updateUserRoleProject(
    request: UpdateUserRoleRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateUserRoleResponse) => void,
  ): ClientUnaryCall;
  updateUserRoleProject(
    request: UpdateUserRoleRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateUserRoleResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  removeUserProject(
    request: RemoveUserRequest,
    callback: (error: ServiceError | null, response: RemoveUserResponse) => void,
  ): ClientUnaryCall;
  removeUserProject(
    request: RemoveUserRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: RemoveUserResponse) => void,
  ): ClientUnaryCall;
  removeUserProject(
    request: RemoveUserRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: RemoveUserResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  addUserProject(
    request: AddUserRequest,
    callback: (error: ServiceError | null, response: AddUserResponse) => void,
  ): ClientUnaryCall;
  addUserProject(
    request: AddUserRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: AddUserResponse) => void,
  ): ClientUnaryCall;
  addUserProject(
    request: AddUserRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: AddUserResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  getProject(
    request: GetProjectRequest,
    callback: (error: ServiceError | null, response: GetProjectResponse) => void,
  ): ClientUnaryCall;
  getProject(
    request: GetProjectRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: GetProjectResponse) => void,
  ): ClientUnaryCall;
  getProject(
    request: GetProjectRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: GetProjectResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  updateProject(
    request: UpdateProjectRequest,
    callback: (error: ServiceError | null, response: UpdateProjectResponse) => void,
  ): ClientUnaryCall;
  updateProject(
    request: UpdateProjectRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateProjectResponse) => void,
  ): ClientUnaryCall;
  updateProject(
    request: UpdateProjectRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateProjectResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  createProject(
    request: CreateProjectRequest,
    callback: (error: ServiceError | null, response: CreateProjectResponse) => void,
  ): ClientUnaryCall;
  createProject(
    request: CreateProjectRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: CreateProjectResponse) => void,
  ): ClientUnaryCall;
  createProject(
    request: CreateProjectRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: CreateProjectResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  deleteProject(
    request: DeleteProjectRequest,
    callback: (error: ServiceError | null, response: DeleteProjectResponse) => void,
  ): ClientUnaryCall;
  deleteProject(
    request: DeleteProjectRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: DeleteProjectResponse) => void,
  ): ClientUnaryCall;
  deleteProject(
    request: DeleteProjectRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: DeleteProjectResponse) => void,
  ): ClientUnaryCall;
  /** [sylk] - None */
  listProjects(request: ListProjectsRequest, options?: Partial<CallOptions>): ClientReadableStream<GetProjectResponse>;
  listProjects(
    request: ListProjectsRequest,
    metadata?: Metadata,
    options?: Partial<CallOptions>,
  ): ClientReadableStream<GetProjectResponse>;
  /** [sylk] - None */
  updateUserStatusProject(
    request: UpdateUserStatusRequest,
    callback: (error: ServiceError | null, response: UpdateUserStatusResponse) => void,
  ): ClientUnaryCall;
  updateUserStatusProject(
    request: UpdateUserStatusRequest,
    metadata: Metadata,
    callback: (error: ServiceError | null, response: UpdateUserStatusResponse) => void,
  ): ClientUnaryCall;
  updateUserStatusProject(
    request: UpdateUserStatusRequest,
    metadata: Metadata,
    options: Partial<CallOptions>,
    callback: (error: ServiceError | null, response: UpdateUserStatusResponse) => void,
  ): ClientUnaryCall;
}

export const ProjectsClient = makeGenericClientConstructor(ProjectsService, "Projects") as unknown as {
  new (address: string, credentials: ChannelCredentials, options?: Partial<ClientOptions>): ProjectsClient;
  service: typeof ProjectsService;
};
