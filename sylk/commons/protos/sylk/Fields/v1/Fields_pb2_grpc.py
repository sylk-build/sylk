# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from sylk.commons.protos.sylk.SylkApi.v1 import SylkApi_pb2 as sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2


class FieldsStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateField = channel.unary_unary(
                '/sylk.Fields.v1.Fields/CreateField',
                request_serializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.CreateFieldRequest.SerializeToString,
                response_deserializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.CreateFieldResponse.FromString,
                )
        self.GetField = channel.unary_unary(
                '/sylk.Fields.v1.Fields/GetField',
                request_serializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.GetFieldRequest.SerializeToString,
                response_deserializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.GetFieldResponse.FromString,
                )
        self.DeleteField = channel.unary_unary(
                '/sylk.Fields.v1.Fields/DeleteField',
                request_serializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.DeleteFieldRequest.SerializeToString,
                response_deserializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.DeleteFieldResponse.FromString,
                )
        self.UpdateField = channel.unary_unary(
                '/sylk.Fields.v1.Fields/UpdateField',
                request_serializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.UpdateFieldRequest.SerializeToString,
                response_deserializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.UpdateFieldResponse.FromString,
                )


class FieldsServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateField(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetField(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteField(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateField(self, request, context):
        """[sylk] - None
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FieldsServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateField': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateField,
                    request_deserializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.CreateFieldRequest.FromString,
                    response_serializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.CreateFieldResponse.SerializeToString,
            ),
            'GetField': grpc.unary_unary_rpc_method_handler(
                    servicer.GetField,
                    request_deserializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.GetFieldRequest.FromString,
                    response_serializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.GetFieldResponse.SerializeToString,
            ),
            'DeleteField': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteField,
                    request_deserializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.DeleteFieldRequest.FromString,
                    response_serializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.DeleteFieldResponse.SerializeToString,
            ),
            'UpdateField': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateField,
                    request_deserializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.UpdateFieldRequest.FromString,
                    response_serializer=sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.UpdateFieldResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'sylk.Fields.v1.Fields', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Fields(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sylk.Fields.v1.Fields/CreateField',
            sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.CreateFieldRequest.SerializeToString,
            sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.CreateFieldResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sylk.Fields.v1.Fields/GetField',
            sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.GetFieldRequest.SerializeToString,
            sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.GetFieldResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sylk.Fields.v1.Fields/DeleteField',
            sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.DeleteFieldRequest.SerializeToString,
            sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.DeleteFieldResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sylk.Fields.v1.Fields/UpdateField',
            sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.UpdateFieldRequest.SerializeToString,
            sylk_dot_SylkApi_dot_v1_dot_SylkApi__pb2.UpdateFieldResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
