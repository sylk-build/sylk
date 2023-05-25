# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import SylkApi_pb2 as SylkApi__pb2


class ProjectsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateUserRoleProject = channel.unary_unary(
                '/Projects/UpdateUserRoleProject',
                request_serializer=SylkApi__pb2.UpdateUserRoleRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.UpdateUserRoleResponse.FromString,
                )
        self.RemoveUserProject = channel.unary_unary(
                '/Projects/RemoveUserProject',
                request_serializer=SylkApi__pb2.RemoveUserRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.RemoveUserResponse.FromString,
                )
        self.AddUserProject = channel.unary_unary(
                '/Projects/AddUserProject',
                request_serializer=SylkApi__pb2.AddUserRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.AddUserResponse.FromString,
                )
        self.GetProject = channel.unary_unary(
                '/Projects/GetProject',
                request_serializer=SylkApi__pb2.GetProjectRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.GetProjectResponse.FromString,
                )
        self.UpdateProject = channel.unary_unary(
                '/Projects/UpdateProject',
                request_serializer=SylkApi__pb2.UpdateProjectRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.UpdateProjectResponse.FromString,
                )
        self.CreateProject = channel.unary_unary(
                '/Projects/CreateProject',
                request_serializer=SylkApi__pb2.CreateProjectRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.CreateProjectResponse.FromString,
                )
        self.DeleteProject = channel.unary_unary(
                '/Projects/DeleteProject',
                request_serializer=SylkApi__pb2.DeleteProjectRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.DeleteProjectResponse.FromString,
                )
        self.ListProjects = channel.unary_stream(
                '/Projects/ListProjects',
                request_serializer=SylkApi__pb2.ListProjectsRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.GetProjectResponse.FromString,
                )
        self.UpdateUserStatusProject = channel.unary_unary(
                '/Projects/UpdateUserStatusProject',
                request_serializer=SylkApi__pb2.UpdateUserStatusRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.UpdateUserStatusResponse.FromString,
                )


class ProjectsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UpdateUserRoleProject(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveUserProject(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddUserProject(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProject(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProject(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateProject(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteProject(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListProjects(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUserStatusProject(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateUserRoleProject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUserRoleProject,
                    request_deserializer=SylkApi__pb2.UpdateUserRoleRequest.FromString,
                    response_serializer=SylkApi__pb2.UpdateUserRoleResponse.SerializeToString,
            ),
            'RemoveUserProject': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveUserProject,
                    request_deserializer=SylkApi__pb2.RemoveUserRequest.FromString,
                    response_serializer=SylkApi__pb2.RemoveUserResponse.SerializeToString,
            ),
            'AddUserProject': grpc.unary_unary_rpc_method_handler(
                    servicer.AddUserProject,
                    request_deserializer=SylkApi__pb2.AddUserRequest.FromString,
                    response_serializer=SylkApi__pb2.AddUserResponse.SerializeToString,
            ),
            'GetProject': grpc.unary_unary_rpc_method_handler(
                    servicer.GetProject,
                    request_deserializer=SylkApi__pb2.GetProjectRequest.FromString,
                    response_serializer=SylkApi__pb2.GetProjectResponse.SerializeToString,
            ),
            'UpdateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateProject,
                    request_deserializer=SylkApi__pb2.UpdateProjectRequest.FromString,
                    response_serializer=SylkApi__pb2.UpdateProjectResponse.SerializeToString,
            ),
            'CreateProject': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateProject,
                    request_deserializer=SylkApi__pb2.CreateProjectRequest.FromString,
                    response_serializer=SylkApi__pb2.CreateProjectResponse.SerializeToString,
            ),
            'DeleteProject': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteProject,
                    request_deserializer=SylkApi__pb2.DeleteProjectRequest.FromString,
                    response_serializer=SylkApi__pb2.DeleteProjectResponse.SerializeToString,
            ),
            'ListProjects': grpc.unary_stream_rpc_method_handler(
                    servicer.ListProjects,
                    request_deserializer=SylkApi__pb2.ListProjectsRequest.FromString,
                    response_serializer=SylkApi__pb2.GetProjectResponse.SerializeToString,
            ),
            'UpdateUserStatusProject': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUserStatusProject,
                    request_deserializer=SylkApi__pb2.UpdateUserStatusRequest.FromString,
                    response_serializer=SylkApi__pb2.UpdateUserStatusResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Projects', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Projects(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UpdateUserRoleProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Projects/UpdateUserRoleProject',
            SylkApi__pb2.UpdateUserRoleRequest.SerializeToString,
            SylkApi__pb2.UpdateUserRoleResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveUserProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Projects/RemoveUserProject',
            SylkApi__pb2.RemoveUserRequest.SerializeToString,
            SylkApi__pb2.RemoveUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddUserProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Projects/AddUserProject',
            SylkApi__pb2.AddUserRequest.SerializeToString,
            SylkApi__pb2.AddUserResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Projects/GetProject',
            SylkApi__pb2.GetProjectRequest.SerializeToString,
            SylkApi__pb2.GetProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Projects/UpdateProject',
            SylkApi__pb2.UpdateProjectRequest.SerializeToString,
            SylkApi__pb2.UpdateProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Projects/CreateProject',
            SylkApi__pb2.CreateProjectRequest.SerializeToString,
            SylkApi__pb2.CreateProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Projects/DeleteProject',
            SylkApi__pb2.DeleteProjectRequest.SerializeToString,
            SylkApi__pb2.DeleteProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListProjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Projects/ListProjects',
            SylkApi__pb2.ListProjectsRequest.SerializeToString,
            SylkApi__pb2.GetProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUserStatusProject(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Projects/UpdateUserStatusProject',
            SylkApi__pb2.UpdateUserStatusRequest.SerializeToString,
            SylkApi__pb2.UpdateUserStatusResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
