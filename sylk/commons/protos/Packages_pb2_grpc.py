# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import SylkApi_pb2 as SylkApi__pb2


class PackagesStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPackage = channel.unary_unary(
                '/Packages/GetPackage',
                request_serializer=SylkApi__pb2.GetPackageRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.GetPackageResponse.FromString,
                )
        self.CreatePackage = channel.unary_unary(
                '/Packages/CreatePackage',
                request_serializer=SylkApi__pb2.CreatePackageRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.CreatePackageResponse.FromString,
                )
        self.DeletePackage = channel.unary_unary(
                '/Packages/DeletePackage',
                request_serializer=SylkApi__pb2.DeletePackageRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.DeletePackageResponse.FromString,
                )
        self.UpdatePackage = channel.unary_unary(
                '/Packages/UpdatePackage',
                request_serializer=SylkApi__pb2.UpdatePackageRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.UpdatePackageResponse.FromString,
                )
        self.ListPackages = channel.unary_stream(
                '/Packages/ListPackages',
                request_serializer=SylkApi__pb2.ListPackagesRequest.SerializeToString,
                response_deserializer=SylkApi__pb2.GetPackageResponse.FromString,
                )


class PackagesServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetPackage(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreatePackage(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePackage(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePackage(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPackages(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PackagesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPackage': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPackage,
                    request_deserializer=SylkApi__pb2.GetPackageRequest.FromString,
                    response_serializer=SylkApi__pb2.GetPackageResponse.SerializeToString,
            ),
            'CreatePackage': grpc.unary_unary_rpc_method_handler(
                    servicer.CreatePackage,
                    request_deserializer=SylkApi__pb2.CreatePackageRequest.FromString,
                    response_serializer=SylkApi__pb2.CreatePackageResponse.SerializeToString,
            ),
            'DeletePackage': grpc.unary_unary_rpc_method_handler(
                    servicer.DeletePackage,
                    request_deserializer=SylkApi__pb2.DeletePackageRequest.FromString,
                    response_serializer=SylkApi__pb2.DeletePackageResponse.SerializeToString,
            ),
            'UpdatePackage': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdatePackage,
                    request_deserializer=SylkApi__pb2.UpdatePackageRequest.FromString,
                    response_serializer=SylkApi__pb2.UpdatePackageResponse.SerializeToString,
            ),
            'ListPackages': grpc.unary_stream_rpc_method_handler(
                    servicer.ListPackages,
                    request_deserializer=SylkApi__pb2.ListPackagesRequest.FromString,
                    response_serializer=SylkApi__pb2.GetPackageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Packages', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Packages(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetPackage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Packages/GetPackage',
            SylkApi__pb2.GetPackageRequest.SerializeToString,
            SylkApi__pb2.GetPackageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreatePackage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Packages/CreatePackage',
            SylkApi__pb2.CreatePackageRequest.SerializeToString,
            SylkApi__pb2.CreatePackageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeletePackage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Packages/DeletePackage',
            SylkApi__pb2.DeletePackageRequest.SerializeToString,
            SylkApi__pb2.DeletePackageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdatePackage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Packages/UpdatePackage',
            SylkApi__pb2.UpdatePackageRequest.SerializeToString,
            SylkApi__pb2.UpdatePackageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListPackages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Packages/ListPackages',
            SylkApi__pb2.ListPackagesRequest.SerializeToString,
            SylkApi__pb2.GetPackageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
