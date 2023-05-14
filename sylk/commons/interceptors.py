import datetime
import grpc
import logging
from functools import wraps
from sylk import __version__

import os
import logging

LOGLEVEL = os.environ.get('SYLK_LOG_LEVEL', 'DEBUG').upper()
logging.basicConfig(level=LOGLEVEL)

# Server side interceptors

class SylkAuthInterceptor(grpc.ServerInterceptor):
    """Sylk Auth Interceptor - Used with server interceptors"""

    def __init__(self,global_access_token=None,auth_header_key='sylk-token'):
        self._signature_header_key = auth_header_key
        self._access_token = global_access_token
        def abort(ignored_request, context):
            context.abort(grpc.StatusCode.UNAUTHENTICATED, '[SylkAuthInterceptorError]: Invalid auth header key')

        self._abortion = grpc.unary_unary_rpc_method_handler(abort)

    def _verify_header_key(self,metadata):
        return any(self._signature_header_key in i for i in metadata)

    def _verify_auth_value(self,metadata):
        for k,v in metadata:
            if k == self._signature_header_key:
                return v == self._access_token

    def intercept_service(self, continuation, handler_call_details):
        if self._access_token is not None:
            md = handler_call_details.invocation_metadata
            if (
                self._verify_header_key(md)
                and self._verify_auth_value(md)
            ):
                return continuation(handler_call_details)
            else:
                return self._abortion
        else:
            print(handler_call_details)
            if self._verify_header_key(handler_call_details.invocation_metadata):
                return continuation(handler_call_details)
            else:
                
                return self._abortion

class SylkLoggingInterceptor(grpc.ServerInterceptor):
    def __init__(self,format:str='[%(levelname)s] %(asctime)s: %(name)s - %(message)s') -> None:
        logging.basicConfig(format=format,level=logging.DEBUG)

    def intercept_service(self, continuation, handler_call_details):
        ua = dict(handler_call_details.invocation_metadata).get('user-agent')
        sylk_version = dict(handler_call_details.invocation_metadata).get('sylk-version')

        logging.info('RPC:{method: <20} UA:{ua: <24} {sver}'.format(
            method=handler_call_details.method,
            ua=ua,
            sver=f'SYLK:{sylk_version}' if sylk_version is not None else ''))
        return continuation(handler_call_details)

# Client side interceptors and decorators


class SylkRetries(grpc.UnaryUnaryClientInterceptor, grpc.StreamUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor, grpc.StreamStreamClientInterceptor):
    def __init__(self):
        pass

    def intercept_unary_unary(self, continuation, client_call_details, request):
        print('Unary')
        # Handle the unary-unary RPC method
        response_future = continuation(client_call_details, request)
        print(dir(response_future))
        print(response_future.code())

        return response_future

    def intercept_stream_unary(self, continuation, client_call_details, request_iterator):
        # Handle the stream-unary RPC method
        response_future = continuation(client_call_details, request_iterator)
        return response_future

    def intercept_unary_stream(self, continuation, client_call_details, request):
        # Handle the unary-stream RPC method
        response_iterator = continuation(client_call_details, request)
        return response_iterator

    def intercept_stream_stream(self, continuation, client_call_details, request_iterator):
        # Handle the stream-stream RPC method
        response_iterator = continuation(client_call_details, request_iterator)
        return response_iterator


def sylk_client_pre_rpc(*decorators):
    def wrap(func):
        func = _sylk_client_defaults(func)
        for decorator in reversed(decorators):
            func = decorator(func)
        return func
    return wrap

def sylk_enforce_version(*args):
    md_keys = len(dict(*args))
    sylk_ver = dict(*args).get('sylk-version')
    if md_keys > 0 and sylk_ver is None:
        return ((*args[0] + (('sylk-version',__version__.__version__),),),)

def sylk_log_client(func,context,*args):
    logging.debug(f'RPC: {func}')
    logging.debug(f'Request: {context}')
    logging.debug(f'Metadata: {dict(*args)}')

def _sylk_client_defaults(func):
    @wraps(func)
    def sylk_client_defaults(client, context, *args, **kwargs):
        # Do something with the request and metadata objects here
        # For example, you could print the metadata object
        args = sylk_enforce_version(*args)
        sylk_log_client(func,context,*args)

        # Call the RPC method
        return func(client, context, *args, **kwargs)
    return sylk_client_defaults

def sylk_client_auth(func):
    @wraps(func)
    def sylk_client_auth(client, context, *args, **kwargs):
        # Do something with the request and metadata objects here
        # For example, you could print the metadata object
        if hasattr(client,'_sylk_global_auth_key') and getattr(client,'_sylk_global_auth_key') is not None:
           logging.debug(f'Sylk Auth')
        else:
            logging.debug(f'Passed sylk auth: no global key for sylk client.')

        # Call the RPC method
        return func(client, context, *args, **kwargs)
    return sylk_client_auth