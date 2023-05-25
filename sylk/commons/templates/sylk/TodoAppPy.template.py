
"""Init script for sylk.build template TodoAppPy
Generated thanks to -

                _   _    
               | | | |   
  ___   _   _  | | | | __
 / __| | | | | | | | |/ /
 \__ \ | |_| | | | |   < 
 |___/  \__, | |_| |_|\_\
         __/ |           
        |___/            

Sample template for quick-start guide of sylk.build

Author: Amit Shmulevitch
"""
# Main sylk.build class to create gRPC services programmatically
# (Same inteface that sylk.build cli is built as wrapper for
# SylkArchitect whenever you generate new resource / create new project)
from sylk import SylkArchitect

# Some common utils modules to help us build the services faster
# and adds an validations to object before they created
from sylk.commons import helpers, file_system

# Sylk.build proto modules also helps us here to construct our services
# gRPC used to create another gRPC ! :)
from sylk.commons.protos import SylkServer_pb2, SylkClient_pb2, SylkCommons_pb2

# Default system imports
import os
import sys
import argparse
import zlib

    
"""Initialize constants and SylkArchitect class"""
parser = argparse.ArgumentParser(
                    prog = 'TodoAppPy',
                    description = 'What the program does',
                    epilog = 'Text at the bottom of help')
parser.add_argument('--domain',default='sylk')           # optional argument
parser.add_argument('--project-name',default='TodoAppPy')           # optional argument

args = parser.parse_args()

# Constants
_PATH = file_system.join_path(os.getcwd(), 'sylk.json') 
_DOMAIN = args.domain
_PROJECT_NAME = args.project_name
_SERVER_LANGUAGE = SylkServer_pb2.SylkServerLanguages.Name(SylkServer_pb2.SylkServerLanguages.python)
_HOST = 'localhost'
_PORT = 44880

# Initializing SylkArchitect class which we going to interact with
# It is used to create all of our 'sylk' resources
_architect = SylkArchitect(path=_PATH,
                             domain=_DOMAIN,
                             project_name=_PROJECT_NAME)
_architect.SetConfig({'host': _HOST, 'port': _PORT})
_architect.SetDomain(_DOMAIN)
    
"""Project specific configurations"""
    
# Init all the client to be used with your services
# Here we configured a python + nodejs clients to be created with our services    
_clients = [{'language': 'python', 'out_dir': file_system.join_path(_PATH, 'clients', SylkClient_pb2.SylkClientLanguages.Name(SylkClient_pb2.SylkClientLanguages.python))}, {'language': 'nodejs', 'out_dir': file_system.join_path(_PATH, 'clients', SylkClient_pb2.SylkClientLanguages.Name(SylkClient_pb2.SylkClientLanguages.nodejs))}]
    
# Adding the base project data
_project = _architect.AddProject(server_language=_SERVER_LANGUAGE,
                                 clients=_clients)

# NOTE - that every call to SylkArchitect executions
# it will return the proto generated class of that object
# which can be used to enrich the sylk base structure
# or debug easly whats going on beneath the surface
# print(type(_project))
# <class 'sylk.SylkProject'>

    
# Creating enums values

# Instantiating all enum values for [public_Todo_v1_Statuses]
_enum_values_public_Todo_v1_Statuses = [helpers.SylkEnumValue('UNKNOWN',0,description='The default value for enums must be the first enum value'),
	helpers.SylkEnumValue('DONE',1,description='When the todo is in DONE state'),
	helpers.SylkEnumValue('PENDING',2,description='When the todo is in PENDING state'),
	helpers.SylkEnumValue('OVER_DUE',3,description='When the todo is in OVER_DUE state')]
        
# Creating enums   

# Constructing enum [public_Todo_v1_Statuses]
_enum_public_Todo_v1_Statuses = helpers.SylkEnum('Statuses',enum_values=_enum_values_public_Todo_v1_Statuses) 
        
"""Packages and thier resources"""
# Construct fields    

# Constructing a field for [public_API_v1_GetTodoRequest_todo_id]
_field_public_API_v1_GetTodoRequest_todo_id = helpers.SylkField(name='todo_id',
                              description='The todo ID to be fetched',
                              label='LABEL_OPTIONAL',
                              type='TYPE_STRING',
                              message_type=None,
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_API_v1_DeleteTodoRequest_id]
_field_public_API_v1_DeleteTodoRequest_id = helpers.SylkField(name='id',
                              description='The id of the todo to be removed',
                              label='LABEL_OPTIONAL',
                              type='TYPE_STRING',
                              message_type=None,
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_API_v1_CreateTodoResponse_id]
_field_public_API_v1_CreateTodoResponse_id = helpers.SylkField(name='id',
                              description='The new todo id',
                              label='LABEL_OPTIONAL',
                              type='TYPE_STRING',
                              message_type=None,
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_API_v1_CreateTodoRequest_todo]
_field_public_API_v1_CreateTodoRequest_todo = helpers.SylkField(name='todo',
                              description='Create new todo data',
                              label='LABEL_OPTIONAL',
                              type='TYPE_MESSAGE',
                              message_type=_DOMAIN + '.Todo.v1.Todo',
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_API_v1_GetTodoResponse_data]
_field_public_API_v1_GetTodoResponse_data = helpers.SylkField(name='data',
                              description='The todo data',
                              label='LABEL_OPTIONAL',
                              type='TYPE_MESSAGE',
                              message_type=_DOMAIN + '.Todo.v1.Todo',
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_API_v1_DeleteTodoResponse_status]
_field_public_API_v1_DeleteTodoResponse_status = helpers.SylkField(name='status',
                              description='Should indicate "OK" if the todo is deleted properly',
                              label='LABEL_OPTIONAL',
                              type='TYPE_STRING',
                              message_type=None,
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_API_v1_UpdateTodoRequest_update]
_field_public_API_v1_UpdateTodoRequest_update = helpers.SylkField(name='update',
                              description='The update properties of the todo',
                              label='LABEL_OPTIONAL',
                              type='TYPE_MESSAGE',
                              message_type='google.protobuf.Struct',
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_API_v1_UpdateTodoResponse_status]
_field_public_API_v1_UpdateTodoResponse_status = helpers.SylkField(name='status',
                              description='Should indicate "OK" if the todo is updated properly',
                              label='LABEL_OPTIONAL',
                              type='TYPE_STRING',
                              message_type=None,
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_Todo_v1_Todo_created_at]
_field_public_Todo_v1_Todo_created_at = helpers.SylkField(name='created_at',
                              description='The todo created_at timestamp',
                              label='LABEL_OPTIONAL',
                              type='TYPE_MESSAGE',
                              message_type='google.protobuf.Timestamp',
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_Todo_v1_Todo_title]
_field_public_Todo_v1_Todo_title = helpers.SylkField(name='title',
                              description='The todo title',
                              label='LABEL_OPTIONAL',
                              type='TYPE_STRING',
                              message_type=None,
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_Todo_v1_Todo_due_date]
_field_public_Todo_v1_Todo_due_date = helpers.SylkField(name='due_date',
                              description='The todo due_date timestamp',
                              label='LABEL_OPTIONAL',
                              type='TYPE_MESSAGE',
                              message_type='google.protobuf.Timestamp',
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_Todo_v1_Todo_status]
_field_public_Todo_v1_Todo_status = helpers.SylkField(name='status',
                              description='The todo status',
                              label='LABEL_OPTIONAL',
                              type='TYPE_ENUM',
                              message_type=None,
                              enum_type=_DOMAIN+'.Todo.v1.Statuses',
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_Todo_v1_Todo_id]
_field_public_Todo_v1_Todo_id = helpers.SylkField(name='id',
                              description='The todo ID',
                              label='LABEL_OPTIONAL',
                              type='TYPE_STRING',
                              message_type=None,
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Constructing a field for [public_Todo_v1_Todo_description]
_field_public_Todo_v1_Todo_description = helpers.SylkField(name='description',
                              description='The todo description',
                              label='LABEL_OPTIONAL',
                              type='TYPE_STRING',
                              message_type=None,
                              enum_type=None,
                              key_type=None,
                              value_type=None,
                              oneof_fields=None, # Not supporting templating with oneof_fields !
                              extensions=None)

# Packing all fields for [public_API_v1_GetTodoRequest]
_msg_fields_public_API_v1_GetTodoRequest = [_field_public_API_v1_GetTodoRequest_todo_id]
# Packing all fields for [public_API_v1_DeleteTodoRequest]
_msg_fields_public_API_v1_DeleteTodoRequest = [_field_public_API_v1_DeleteTodoRequest_id]
# Packing all fields for [public_API_v1_CreateTodoResponse]
_msg_fields_public_API_v1_CreateTodoResponse = [_field_public_API_v1_CreateTodoResponse_id]
# Packing all fields for [public_API_v1_CreateTodoRequest]
_msg_fields_public_API_v1_CreateTodoRequest = [_field_public_API_v1_CreateTodoRequest_todo]
# Packing all fields for [public_API_v1_GetTodoResponse]
_msg_fields_public_API_v1_GetTodoResponse = [_field_public_API_v1_GetTodoResponse_data]
# Packing all fields for [public_API_v1_DeleteTodoResponse]
_msg_fields_public_API_v1_DeleteTodoResponse = [_field_public_API_v1_DeleteTodoResponse_status]
# Packing all fields for [public_API_v1_UpdateTodoRequest]
_msg_fields_public_API_v1_UpdateTodoRequest = [_field_public_API_v1_UpdateTodoRequest_update]
# Packing all fields for [public_API_v1_UpdateTodoResponse]
_msg_fields_public_API_v1_UpdateTodoResponse = [_field_public_API_v1_UpdateTodoResponse_status]
# Packing all fields for [public_Todo_v1_Todo]
_msg_fields_public_Todo_v1_Todo = [_field_public_Todo_v1_Todo_created_at,_field_public_Todo_v1_Todo_title,_field_public_Todo_v1_Todo_due_date,_field_public_Todo_v1_Todo_status,_field_public_Todo_v1_Todo_id,_field_public_Todo_v1_Todo_description]
    
# Construct messages

# Constructing message [public_API_v1_GetTodoRequest]
_msg_public_API_v1_GetTodoRequest = helpers.SylkMessage(name='GetTodoRequest',
                                 description='The passed query for methods',
                                 fields=_msg_fields_public_API_v1_GetTodoRequest,
                                 extension_type=None,
                                 extensions=None)

# Constructing message [public_API_v1_DeleteTodoRequest]
_msg_public_API_v1_DeleteTodoRequest = helpers.SylkMessage(name='DeleteTodoRequest',
                                 description='Remove todo data by id',
                                 fields=_msg_fields_public_API_v1_DeleteTodoRequest,
                                 extension_type=None,
                                 extensions=None)

# Constructing message [public_API_v1_CreateTodoResponse]
_msg_public_API_v1_CreateTodoResponse = helpers.SylkMessage(name='CreateTodoResponse',
                                 description='Create new todo object response',
                                 fields=_msg_fields_public_API_v1_CreateTodoResponse,
                                 extension_type=None,
                                 extensions=None)

# Constructing message [public_API_v1_CreateTodoRequest]
_msg_public_API_v1_CreateTodoRequest = helpers.SylkMessage(name='CreateTodoRequest',
                                 description='Create new todo object request',
                                 fields=_msg_fields_public_API_v1_CreateTodoRequest,
                                 extension_type=None,
                                 extensions=None)

# Constructing message [public_API_v1_GetTodoResponse]
_msg_public_API_v1_GetTodoResponse = helpers.SylkMessage(name='GetTodoResponse',
                                 description='The response object from service with the todo data',
                                 fields=_msg_fields_public_API_v1_GetTodoResponse,
                                 extension_type=None,
                                 extensions=None)

# Constructing message [public_API_v1_DeleteTodoResponse]
_msg_public_API_v1_DeleteTodoResponse = helpers.SylkMessage(name='DeleteTodoResponse',
                                 description='Delete todo object response',
                                 fields=_msg_fields_public_API_v1_DeleteTodoResponse,
                                 extension_type=None,
                                 extensions=None)

# Constructing message [public_API_v1_UpdateTodoRequest]
_msg_public_API_v1_UpdateTodoRequest = helpers.SylkMessage(name='UpdateTodoRequest',
                                 description='Remove todo data by id',
                                 fields=_msg_fields_public_API_v1_UpdateTodoRequest,
                                 extension_type=None,
                                 extensions=None)

# Constructing message [public_API_v1_UpdateTodoResponse]
_msg_public_API_v1_UpdateTodoResponse = helpers.SylkMessage(name='UpdateTodoResponse',
                                 description='Update todo object response',
                                 fields=_msg_fields_public_API_v1_UpdateTodoResponse,
                                 extension_type=None,
                                 extensions=None)

# Constructing message [public_Todo_v1_Todo]
_msg_public_Todo_v1_Todo = helpers.SylkMessage(name='Todo',
                                 description='The main entity of the todo application',
                                 fields=_msg_fields_public_Todo_v1_Todo,
                                 extension_type=None,
                                 extensions=None)

    
# Construct packages

_pkg_public_API_v1 = helpers.SylkPackage(name='API',
                                                messages=[_msg_public_API_v1_GetTodoRequest,_msg_public_API_v1_DeleteTodoRequest,_msg_public_API_v1_CreateTodoResponse,_msg_public_API_v1_CreateTodoRequest,_msg_public_API_v1_GetTodoResponse,_msg_public_API_v1_DeleteTodoResponse,_msg_public_API_v1_UpdateTodoRequest,_msg_public_API_v1_UpdateTodoResponse],
                                                enums=[],
                                                extensions=None)

# Unpacking package [public_API_v1]
_pkg_public_API_v1_name, _pkg_public_API_v1_messages, _pkg_public_API_v1_enums, _pkg_public_API_v1_ext, _pkg_public_API_v1_domain = _pkg_public_API_v1.to_tuple()
_pkg_public_Todo_v1 = helpers.SylkPackage(name='Todo',
                                                messages=[_msg_public_Todo_v1_Todo],
                                                enums=[_enum_public_Todo_v1_Statuses],
                                                extensions=None)

# Unpacking package [public_Todo_v1]
_pkg_public_Todo_v1_name, _pkg_public_Todo_v1_messages, _pkg_public_Todo_v1_enums, _pkg_public_Todo_v1_ext, _pkg_public_Todo_v1_domain = _pkg_public_Todo_v1.to_tuple()
    
# Add packages

# Adding package [public_API_v1]
_pkg_public_API_v1 = _architect.AddPackage(_pkg_public_API_v1_name,
                                                    dependencies=[],
                                                    description='The main entities of our application which represnets the schema of our buisness logic',
                                                    domain=_pkg_public_API_v1_domain,
                                                    extensions=_pkg_public_API_v1_ext)
# Adding package [public_Todo_v1]
_pkg_public_Todo_v1 = _architect.AddPackage(_pkg_public_Todo_v1_name,
                                                    dependencies=[],
                                                    description='The main entities of our application which represnets the schema of our buisness logic',
                                                    domain=_pkg_public_Todo_v1_domain,
                                                    extensions=_pkg_public_Todo_v1_ext)
    
msgs_map = {}

# Add packages messages

for m in _pkg_public_API_v1_messages:
	msg_name, msg_fields, msg_desc, msg_opt, msg_ext, msg_domain = m
	temp_msg = _architect.AddMessage(package=_pkg_public_API_v1, name=msg_name, fields=msg_fields, description=msg_desc, options=msg_opt, extensions=msg_ext, domain=msg_domain)
	msgs_map[temp_msg.full_name] = temp_msg
for m in _pkg_public_Todo_v1_messages:
	msg_name, msg_fields, msg_desc, msg_opt, msg_ext, msg_domain = m
	temp_msg = _architect.AddMessage(package=_pkg_public_Todo_v1, name=msg_name, fields=msg_fields, description=msg_desc, options=msg_opt, extensions=msg_ext, domain=msg_domain)
	msgs_map[temp_msg.full_name] = temp_msg
    
# Add packages enums

for e in _pkg_public_API_v1_enums:
	enum_name, enum_values, enum_desc, enum_domain = e
	_architect.AddEnum(package=_pkg_public_API_v1, name=enum_name, enum_values=enum_values, description=enum_desc, domain=enum_domain)
for e in _pkg_public_Todo_v1_enums:
	enum_name, enum_values, enum_desc, enum_domain = e
	_architect.AddEnum(package=_pkg_public_Todo_v1, name=enum_name, enum_values=enum_values, description=enum_desc, domain=enum_domain)
    
"""Services and thier resources"""
# Construct rpc's

_rpc_public_Todos_v1_GetTodo = helpers.SylkRPC(name='GetTodo',client_stream=None,server_stream=None,in_type=msgs_map[_DOMAIN+'.API.v1.GetTodoRequest'].full_name, out_type=msgs_map[_DOMAIN+'.API.v1.GetTodoResponse'].full_name, description='Get a todo')
_rpc_public_Todos_v1_CreateTodo = helpers.SylkRPC(name='CreateTodo',client_stream=None,server_stream=None,in_type=msgs_map[_DOMAIN+'.API.v1.CreateTodoRequest'].full_name, out_type=msgs_map[_DOMAIN+'.API.v1.CreateTodoResponse'].full_name, description='Creates a new todo')
_rpc_public_Todos_v1_UpdateTodo = helpers.SylkRPC(name='UpdateTodo',client_stream=None,server_stream=None,in_type=msgs_map[_DOMAIN+'.API.v1.UpdateTodoRequest'].full_name, out_type=msgs_map[_DOMAIN+'.API.v1.UpdateTodoResponse'].full_name, description='Update a todo')
_rpc_public_Todos_v1_DeleteTodo = helpers.SylkRPC(name='DeleteTodo',client_stream=None,server_stream=None,in_type=msgs_map[_DOMAIN+'.API.v1.DeleteTodoRequest'].full_name, out_type=msgs_map[_DOMAIN+'.API.v1.DeleteTodoResponse'].full_name, description='Remove a todo')
        
# Construct services

_svc_Todos = helpers.SylkService('Todos',
                                                methods=[_rpc_public_Todos_v1_GetTodo,_rpc_public_Todos_v1_CreateTodo,_rpc_public_Todos_v1_UpdateTodo,_rpc_public_Todos_v1_DeleteTodo],
                                                dependencies=[_pkg_public_API_v1.package],
                                                description='The todos service which will interact with todo tasks list',
                                                extensions=None)

_svc_Todos_name, _svc_Todos_methods, _svc_Todos_dependencies, _svc_Todos_desc, _svc_Todos_ext = _svc_Todos.to_tuple()
        
# Add services

_svc_Todos = _architect.AddService(_svc_Todos_name,_svc_Todos_dependencies,_svc_Todos_desc,[],extensions=_svc_Todos_ext)
        

for rpc in _svc_Todos_methods:
	rpc_name, rpc_in_out, rpc_desc = rpc
	_architect.AddRPC(_svc_Todos, rpc_name, rpc_in_out, rpc_desc)
    
# Initalize all code files 
_context = SylkCommons_pb2.SylkContext(files=[SylkCommons_pb2.SylkFileContext(file='services/Todos.py',code=b'x\x9c\xb5TQo\xd30\x10~N~\xc5){\x98#:K\xf0X)hc-h\x02V\xb4v\x084M\x91\xdb\\\x8a\xb5\xc4\x0e\xb63\xadB\xfcwl\xa7\xa1^\xbb\x95\n\xc4S\xe4\xf3w\xbe\xef\xbe\xefrI\x92\xe8UuG\xe7-\xaf\n\xd0\xa8\xee\xf9\x02\x81\xd7M\x855\x13\x86\x19.\x05\x94R\xc1\xc9k\x98\xc9B\xea$Ib{-\x95\x81\xa5j\x16q\xa9d\rK)\x97\x15\xd2FI#\xe7mI\r\xafQ\x1bV7y3\x7f\x05k\xf8\xac\x0fv9f\xd5p\xb1\xec//\x0c*f\xa4\x1a\xc0\x07\xaeM_\xc1Wto\xe4\xbeV\x10u\xc1\xfe|\xf6\xe9\xc2\x1f\xe3E\xc5\xb4\xee\x92\xc8\xe3T\xea\x8f\xd3\xae=\x95\x0e\xe38*\xb0\x84<\xe7\x82\x9b<\'q\x14i\xac\xca\x81\xfd\x1a\xa6\xef\xf4\xd0\xb1\xb8\xe9\x0b\xf9\xec\xdb\xec\xe66\x8eR\'\xc4\xa5\x148\\\xa7\xd0\xdc\'@\x06\xfek\x1f\x8e\x8e`$a%[\x05\xa37\xb0\x90B\xe0\xc2\xc9\xa8\xe1\x1b*\xa4\x94Z\xcc\x11\x9cZVpz\xea\xc4\x87\x13\x18M\xe0r2\x83\xab\xf1\xc7\xc9\xe7q\xc7\xed\x1d\x1aW\x96x^\xa0\xf0{k\xd5\x1b\xf6\xcd\xd2\xf5\xf5U\x17\x1f\xb8:\x06\x1f\x8c\xe7\xb7\x83\xd1\x8d-\xef)7\x8a\x0bC\xd6`\xca\xc5\xbd\\x\x8f\xf3\x1a\r+\x98a$M\xd7"\xd8\x96\x84\x05\x11b\xfc\x00\x18\xe0\x02\xc2\x8ey\t\xf6\x85\x02\xb2\xacgG\x8d\x13\x8c\x17\xe9\xc0)\xe4\xdeq\x18\xf7\x14\xd7 \xa4\xf9-\\\xa4\xd6\x94l\x8dg\xc8\x12G&s\xc9i\x97`Z%\xa0\xcf\xb3!\xac\xba\x8e\xa2\xbe\x196\xb7\xc3@\xbc\xdbS;\xb8\xad>\x97\x05R+k\xfevr}9\x1a\x94\xc73Ge\xbe\x02^\x0c!\xf9\xb1E\xfag\xe2)\x96\xb2\x15\x05=N\xe3\xc3\\:W\xc8\x0c\xee3j\x83\xd8\xebU\x08\xdb\xd8u\xb0\x0f\x86\x9b\n\xb7\xad\xe8\xa2O\xba\x118\x11\xe0\x9d\x9b\xa0\x8d"5{ 7nR\x9c\xc3\xe9\x93uo\xd3\x17/\xbd5A\x8c\xb2\xa6AQ\x90\xf0\xd1\xf4\x19\xbfw\x1b&\xbc\xc8\xb6\xe8\xfc\x9b\xf7g\x1f\xae\xc6g\xa3\xaf\xf9\xf8\xcb\xc5t6\r\x06\xc0\xeb\xb2=\x03\x9dZv\x0cXe\xa9\x15+\xc0\x07\xbb\x04\xf4\xe1\xb3p\xdd\x14\x7f\x98\x85\rb\xef,\x84\xb0\xcd,\x1c\xc1\x13*\xeeB\x89\xf6\x02d\xbd\xe9.\xed\xb1~ns\xb5\r*\x92\x06\xe9\xbdg\x1bF\x875=\xc2\n\xf77\xbdA\xecm:\x84\xfd\xc5\x0f\xf0x\x11\x1d\xb2\x83\xc2\xb9UX\xcb{$\xc1\xba\xd9Qz\x97_\xaft2y\x9f\xfc\xef%\xb5\xb3\x9f~\x01F\x86\x8f\xb9'),
SylkCommons_pb2.SylkFileContext(file='server/server.py',code=b'x\x9c\x85Tak\xdb0\x10\xfd\x1c\xff\x8aCPf\x97\xd4\xa4]\x19%\xe0A\x96\x84\x126\xd2\xb2t\x1b\xa5\x14\xa1X\x97D\xd4\xb2\x8cN^\xea\x7f?YN\xda\xb4k)\x81\xa0{\xd2\x9d\xde\xbd{2c\x8c\x9a\xe2!]\xd6\xaa\x90p\x89%Z\xe1P\xc2\x02\xed_\xb406\x12\x19c\x11\xbf\x9aO\xf9dt\xcbgs\xbe\x98\x8e\xaf\xe6\x93\x05d\xf0e\x00\xc7\xdd\xdf\xd9y\xb4\xb2FCn\xca\xbc\xb6\x16K\x07JW\xc6:X\xd5\xae\xb6H\xd1.tJ\xe3~\xbd\xb6U\xbe_\xdf\x18ix\xb5<;\x8c\xa9\x05\xf8\xebS\xd4\xdd\x14X\xe7FkSR\xaaJ\x876\xc7\xca\x19K\xfb\x8b\x17\xfe\xc0\xa8v\x9b\xd9\xf3^\xbf\xc5~\x98\xf5Z\x95\xeb\x038\x8a$\xae\x80\xda\x8e\xe3\x8d!\x97\xb1A\x1a~\xc3\xf3\xf3\x8b\x8b\x01K\x86Q\xd4s-A\'\xe8\x81|\xe3wQ\xaf\xb7g\x9c\xb6\x8b\xd8\x03=%3v\xca\xfa\xed\xd2)W`\xc6\xc6\x16\xbd\x9a0\xda"\x19\x8dAT\x95#\xc1\x1f\xe56\x81`\xa7{\x97CN\xb8\x9a\xb2\xa7\xba\x8b\x10#\xa5\x13/~8!\x91r\xab*\xa7L\x99\xb1oabZ\x94b\x8d J\t\x12\xab\xc24\xa0Un\xcd\t\xed\xaf\xda\xb6W\x1d\x8cx\xfcc\xc6|\xad\xa4\xffn\x0bg/ZX\xe4\xa2@\xb85\xb5}\xa2\xff\x01\xdd\xeb\xe9|2\x9b_\xfe\xcf\xb8+\xd5\xb4\xa5DU\x15*\x17-N\x80\x82T\xd1|\xc0\xea\xf3\x0bV3\xf7\x89`T\x140Z\x9a\xda\xcf\xday\xa1\xf5G\xc4\xae~O\x7f\xf2\xc9\xaf7\xb4\xec\xf2\x01W+\x95+o\xde\xa2\x01)\x9cx-^\xa0\x18\xf5\xee\xbd\x1d\xa8{\x1fY0q\xdaE\xf1\xce\xeb\xe9\xcd\xc6\x97\x93\xd7\xc6\x14\xd3G\xccko\xb1X\x8bG\xbe5\xf6\x01-e\xa7\x83\xa4\x7f\xe8\xd8,~\xc3\xabq\xf2\x8e[\xfdF\xe2I\xbc| \xa9\x90\x92\x07h7$\xcb\x9d\xe1;Z\x01\x0fjR\xfcl\xe3\xa4\xdfm\'\xfbfB\rU\x92gl\x91\xb7o(\xbc\x86\xe7}/\xac\xc7|\\YO?fw\xc7\xf7^y\x8f\xf9\xef\xc5\x81\xc3v\xd2\x08\x07\'_\xe1\x88\x18\x1cAW\xc8g:\xdb\x0c\xbd\x88\xdb\x8d\xf2N\xb8\xb15\x0e\xbb\xa1jL\xa9@\xac\xe27>4>\r\x1f\xdb\xde\xe1;6K#\xac\x0cj\xd8\xbarm\xf6\x139S\xc5\x83$\x8a\xd4\n8/\x85F\xce!\xcb\x80q\xae\x85*9g\xc3]#q\xf2\x0f\xb4\xd3\xa3\xcc'),
SylkCommons_pb2.SylkFileContext(file='server/interceptors.py',code=b'x\x9c\xb5V\xd1j\xe38\x14}\xf7W\\X\x06\xdb\xe0\x98a\xd9\xa7\xb0^\xc8\xa6aZf(K\xdb<\x0c\xcb"T[vDl)+\xc9aC\xe9\xbf\xef\xb5\xe44r\xe2\x84\xd0\x99\xfa\xc1\xb1\x9c\xab\xa3{\xcf9\xbar\xa9d\x03T\xefD\xceeZ\xcb\nx\xb3\x91\xca\x00>VL\x05\xfd\xa8\xa0\x86\x19\xde\xb0\xfd\xb8R\x9b<\xf0"\xb9\xa8\x82\x80<\xde}\xb9\x9f=-\x1f\x16\xe4v1\xbbY<\x90\xaf\x8b\xefY\xa8w\xf5zb\xe4\x9a\x890\x08\xf2\x9aj\r\xf3V\x1b\xd9\xdc\t\xc3T\xce6F\xaa\xa8\x03L\x1f\x99\xda2\xe5\xbd\x8e\xa7A\x00x\x15\xac\x04B\xb8\xe0\x86\x90H\xb3\xbaL\xaaZ>\xd3\x9a\xd0<gZ\x13\x8b\x9e\xddK\xc1p\x06\xf4W\x17\x97\x0e" \x83\x91y\xc1\xdb\x8cn\x19\xfa\x8c5E\xbc\x12R\xb1\x82(\xf6o\xcb\xb4I \x97\x98\xd5\x7f\xc6\x83\xef\xae\xfem\xea&\xb9\x1a\x0c5\xad\x9e\xcb\x82\xa5\xcb\xfb\xd9\xf2\xe9vq\xfft7\x9f=-n\x12\x08\xef\xc4\x96\xd6\xbc\x00\x8d\xf8\x18\xa6X\x18\x07\xc7\xf9vP\\\xda\\;\xbcVP\xb5#\xee\x8ec\xd20\xb3\x92\x05YQQ\xd4LE6<>\xb0\x84\xfc\xf1rGV\x8c\x16L\x915\xdb9\xba\xf0!\xc1\x99\x14u\xa4^\r\x8aa\x12\x02\xa8\xd8E\x18\x01\\\x00\x87R*\xbc\xe3\xe3[\xfc\t:m\xcd\x8a`%-s\xe8#\xc8\x1d\xca:\xd9\xfa8C\xeax\tk\xc82\x185\xcd0\xd4\xcbt\xdbM9\x15\xf6\x90!\xdf\x9b\x87h4\x13\xcf\xfb\x0c\xadR\\\xb4\xb4\xa36\x81\x9e=\x92\xd3\xba&\x05\xe6\xc7k\xed%\x8f\xb9\x8d\x98\x87k\x10\xd2@\xe7\xb2a~M\x81b\x8dA\xa6\\len\xd7${\x16\x8eI\x88NJ\xb5K\x9f\xea\xd8\x14\xf1I(\xae9\x08\xf7\x849\x0e\x8f\xcfr\xeaS\x13\x8d23\x98\xc9j\xcd\xceb\r=\x1c\x9c\x9f\xb3\xa7\xf8\xb4\xceQC$\xd7\xd2\xfb\xc1e^Yw\xdf\xe6\x1e\xb1\xf3}s\xdd\xf1\xaa^\xd7\x01\x9e\xb6:\xdcJ\r5SmT\x16\xfe\xfd)\xaa\xd9\x96\xd5\x826,\xd6\xff\xc0\xa7\x88\xea\xbck\xcc\xb1\x9e\xe2\xc0\xbd\x86\t>6h\\Z\xe1(\x8ca\xf2\xc7\x91k\xfb\x96\x9d>S\xcd\xf3\xb9\x14%\xaf"\xb7L\xe6~\x12\xbbJ\xb6\x8f\xbbY\xfc\xb9\xfc\x12\xff\xe4]\xd6R\xdc6\x05\xcf\xcd\xa8\x1a\xa3\xe2\xa6\x153Q\xd8\xe2\xa2\x13\xacM\x98\xf0\xa0Yw\xca\x10dT\xbb\xde\xf9\x1e\\{P\xf5\x10~c\xde\xb3\xc0E)\xa3\xf0\xe1\xaf\xf9\xf4\xc5u\xe1)\xfc\xfe\xeb\xe7WX\xce\xa6/-\xed\x06\xbf\xbd\xc2\x8bF\x84\xd70u<\x0ew\xb7\x9b\x95\x8d\xa6\xe5\xfeK\x06\xf1-\xcdZ:|\xd5\xa1ge\xf8\xf8\xfd\xdb\xd7\xe9\x8b_\xf3kh\xf7\x94\xcf\x82\xd7\xb0\xac\x9d!\x0c\xe3\xf8\xb8\xf7_\xb1-|;?0\xa38\xd3\xce\xc3\xcb\xeeT\xb2\xb7y\xcdQ\x0e\xcf\xcd\t\xf4\xa7\xa1b\xb4\xb9\x18b\xfftq\x97Q\xce\xc4\x9c\xdb7\x9e\xd36\x98\xfd\x98y\xbd\xb3u\xd4\xc0\xb9]k\xc0F\x02\xfd\'\x81\x0f\xaf\x102\nm!\x9e#\x7f\x81[K\'\x98\x15\x03\xbb\xc8\xc4\xde\x01\x1d\xd4[\xc1\x13Co\xa4\xd0\x8c\x94m\xf7Y\x80\x06\x1e\xe8r1\x91cE\x8f\xb0Fw\xad\xa5\xf2\x9d\x95\x13\x8e0\xf4\xc0\xfcI\xad\x0e\xfdC\x8a=\xac\xfd\x8e\xaa\x9d\xdc.\xbb\x1f\xd1{DX\x07z\xb1\xd8}\xe6?G\xdb=\xda\x05u\xdfY\xe8\xb5\xf2~P\xc9W(\xfcV\xfb\xff\xd6\xdf-\xfa'),
SylkCommons_pb2.SylkFileContext(file='test.py',code=b'x\x9c}\x92KO\xc4 \x14\x85\xf7\xfc\nv\x94\x84!\xa9\xcb&,\xcc\x8c\x1a7j\xd4\xc4\x851\r\x96;)\xe9\x0b\xcb\x9dE\xff\xbd\xf41m\xb5\x8e\xec\x0e\xe7p\xefw\x81c\xdbT4+-\xd4\xe8\xa5\xeb0ojj+\xd7\xb4H\xb11\x8dv\xceuT\xfbA\x90\xe36,\xaf\x9f\xeeS\xf7yu>\xb4oA#\xbc\x86\xf43|\x9d\xc0\xa3\xa0\x07(\xe1\xd7\xd6\x1d\xe0J\xffY\xb7\xf7\xd7\x85{-^P\xe3\xc9\x83\'$\xcd\xa8\x1a\xa0"\x1eDe\x82\x8a"\xe6\xbb\xb2\xd8aS@\xcd\x04[P\xd8{\x92\xec\xe2\x0f.8i\xc1\x87h\x9a\xc9\xc5\x8d\xda\x11Cm\xd8#B\xc3\xea\xbb\xa8!8\xc8~\xf9\x81C\x9dq\xe4\xe1\xf1\xe1F\xcc.Z,A1\x0c\x15\xd8\xb0\xc9\t\x17\x15\xa06\x1a\xb5\n\xb0\x9c\xb8\xd6\xd6\x18M\x88\x86\xa2\xf6\x05\x13\x81\xed\xe20\xd3\x8d\xad&\xc1x\x1cdr\xe6)~\xde\xed2Bj\x8d\n\x1d\xa45\x97hn\x01\xb3|\xa2I\x98\xc0\xf8"\xcd\xf2\xa4+ \x83\xb1\xa0\x99.\xcb\x91k\xc9\xa4o\x16\xf3}0f\xc6\xcd\x97\x181\x03!\xc6\xb2\xe7\xfa\x87r<;S\x86\xae\xfc\x1bo\xdb\xeag')]) 

# Creating all code files on target project
for f in _context.files:
	file_system.wFile(file_system.get_current_location()+'/'+f.file,zlib.decompress(f.code).decode(),force=True)

    
_architect.Save()
    