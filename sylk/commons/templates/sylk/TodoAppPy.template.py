
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
parser.add_argument('--domain',default='public')           # optional argument
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
_context = SylkCommons_pb2.SylkContext(files=[SylkCommons_pb2.SylkFileContext(file='services/Todos.py',code=b'x\x9c\xc5T\xc1j\xdb@\x10=[_1(\x87\xac\xa8\xb3\xd0\x1e\r*Ic\xb7\x84\xa6q\x89\x9d\xd2\x12\x82\x90\xbd#w\x89\xa4UwG\xc1\xa6\xf4\xdf\xbb\xbb\xb2j\xc5N\\\xd3\x1cz\x12;z3\xf3\xe6\xcdc\xc204\xab\xfc\x9e\xcfj\x99\x0b0\xa8\x1f\xe4\x1cA\x16U\x8eEZRJR\x95\x90)\r\'oa\xaa\x842a\x18\x06\xf6\xb7\xd2\x04\x0b]\xcd\x83L\xab\x02\x16J-r\xe4\x95V\xa4fu\xc6I\x16h(-\xaa\xa4\x9a\xbd\x815|\xda\x06\x9b\x1cZU\xb2\\\xb4?/\x08uJJ\xf7\xe1R\x1aj;\xf8\x8e\xaeF\xe2{u\xa2.\xd8\xbe\xcf>_\xf8g0\xcfSc\x9a$\xf68\x95\xfb\xe7\xa4\x19OG\x83 \xe8\t\xcc Id))IX\xd0\xeb\x19\xcc\xb3\xbe\xfdRj\xee\xcd\xc0\xb1\xb8m\x1b\xf9\xec\xbb\xf8\xf6.\xe8EN\x88+U\xe2`\x9d\xc2\x13\x9f\x001\xf8\xaf-\xdc;\x82\xa1\x82\x95\xaa5\x0c\xdf\xc1\\\x95%\xce\x9d\x8c\x06\xbe\xa3F\xce\xb9\xc5\x1c\xc1\xa9e\x05\xa7\xa7N|8\x81\xe1\x18\xae\xc6S\xb8\x1e}\x1a\x7f\x195\xdc> \xb9\xb6\xcc\xf3\x02\x8d?j\xab\xde\xa0\x1d\x96\xaf\x7f_7\xf1\xbe\xebC\xb8$\xcfo\x07c*\xdb\xdeSv$-\xd7\xd2B\x19#\xbfY\x02YBw\x14\x99\x01q) \x8e\xdb\xb6\x9c\x9c\x12RD}7zd\xeb8\x8c+%\r\x94\x8a\xfe(\xd2\xd3\xeb^\xb6\xc73,\x98H)\x8d]r\xd4$P\xadKh\xf3l\x08\xf3\x86jo=\x127H\xc9\\\td~\x93\x13k\xca\xda\x9c\xdb7\xb7\x92%\xef\xc77W\xc3h\x1b.\x90R\x99\x1b\x96\x1dO\x1d\xcb\xd9\n\xa4\x18@\xf8sk\x9e_\xa1g\x9f\xa9\xba\x14\xfc\xb8\xcbg]\xec\xb0U\x9dkL\t\xf7mk\x83\xd8\xbb\xb0.\xec\x1fvF\x92r\xdc^[\x13}rs\x9d\xadu\xf0n\xf3`H\xb3"]\xb2[Y\x12sn\x88\x9e\xec{\x17\xbdz\xede\xeb\xc4xZUX\n\xd6-\x1a=\xe3\x8d\xdd\x81\x99\x14\xf1\x16\x9d\x17\xfb\xe4\xec\xf2zt6\xfc\x96\x8c\xbe^L\xa6\x93\x03\xcc\xe2%\xdb\xf6K#\xa4\xb5L\x9a[\xd6b\x05\xb8\xb4G\xc2\xbc\xc077\x95\xf8\x8bo6\x88\xbd\xbe\xe9\xc26\xbe9\x82\'\x14\xdf\x852\xe3\x95\x8a[\x83\xb8\xb4\xc7Z\xbbSWW\xa8Y\xd4Io\xf7\xbbat\xd8\xd0C\xccq\xff\xd0\x1b\xc4\xde\xa1\xbb\xb0\x17\x1f\xb8Cn[\xd7\xe3\x1a\x0b\xf5\x80\xacs\xc6v\x94\xde\xe5\xd7*\x1d\x8e?\x86\xff\xf1\xf8\x1dp\xf7~\x03\xd63\xaf\x1f'),
SylkCommons_pb2.SylkFileContext(file='server/server.py',code=b"x\x9c\x85T\x7fk\xdb0\x10\xfd;\xfe\x14\x87\xa0\xcc.\xa9I\xbb2J\xc0\x83,\t%l\xa4e\xce6J)B\xb1.\x8d\xa8m\x19\x9d\xbc\xd4\xdf~\xb2\x9c\xa4\xe9\x8f\x11\x0c\xe6\xee\xe4\xbb{\xf7\xee\xc9\x8c1j\xf2\xa7xY\xab\\\xc25\x96h\x84E\t)\x9a\xbfh`\xac%2\xc6\x02~3\x9f\xf2\xc9\xe8\x8e\xcf\xe6<\x9d\x8eo\xe6\x93\x14\x12\xf82\x80\xd3\xeeuq\x19\xac\x8c. \xd3eV\x1b\x83\xa5\x05UT\xdaXX\xd5\xb66H\xc1\xd6\xb5\xaa\xc0\x9d\xfdh\xaalg/\xb4\xd4\xbcZ^\x1c\xfa\xd4\x06\xf8\xdb\xaf\xa8\xeb\xa4J\x8b&\xc3\xcajC\xbb^\xe3\x9a\xac.f/'A q\x05\xd4\xce\x12\xae5\xd9\x84\rb\xff\x0c//\xaf\xae\x06,\x1a\x06A\xcf\xb6\xad\xad\xa0'r#\xdd\x07\xbd\xde\x0eK\xdc\x1a\xa1\x0b\xf4\x94L\xd89\xeb\xb7\xa6U6\xc7\x84\x8d\r:\x9e`\xb4A\xd2\x05z\xbaT\x86\x04\x7f\x94]C\xbag\xb4\xcb!+lM\xc9\xben\xea}\xa4x\xe2h\xf5_H\xa4\xcc\xa8\xca*]&\xec\x9b\xdfE!J\xf1\x88 J\t\x12\xab\\7P\xa8\xcc\xe83\xda\xb5\xda\xb4\xad\x0e\x967\xfe1c\xaeV\xd4\xff\xef\x08\x17\xafFH3\x91#\xdc\xe9\xda\xec\xe1\x1f\x81{;\x9dOf\xf3\xeb\xf7\x88\xbbRM[JTU\xae2\xd1\xc6\tP\x90\xca\x9b#\xa8>\xbfB5\xb3\x9f\x08Fy\x0e\xa3\xa5\xae-\xa4\xd6\x11]\x1c\x03v\xf3{\xfa\x93O~}\xc0e\x97\x0f\xb8Z\xa9L9Y\xe6\rHa\xc5[\xf2<\xc4\xa0\xf7\xe0\xe4@\x9d\xf2\x13/\xcf\xb8\xf3\xc2\xad\x8a\xe3\xc5\xda\x95\x93\xb7Z\xe7\xd3g\xccj'\xb1\xb0\x10\xcf|\xa3\xcd\x13\x1aJ\xce\x07Q\xffP\x98I\xf8N\x92a\xd4\x8f\\\xa7\xd7\xfa\x8e\x85\x94\xdc\x87\xb6\x9b0\xdcj\xbe\xed\xed\xe3\x9e2\n_\xb4\x1a\xf5\xbb\xe3h\x87\xd8\xd7P%9X\x06y{\x1f\xbc\xe4_\xce\x1d{.\xe6\xfc\xca8\x8c!\xbb?}p\xf4\xba\x98\xbb\xee\x072\xda\xce/,\x9c}\x85\x13bp\x02]!\x97iM3tLm\xd6\xca\xad{aj\x1cv\x9b+0\xa6\x1c\xb1\n?\xf8O\xb84|ng\x87\xef\xd8,\xb50\xd2\xb3a\xea\xca\xb6\xd9{p\xba\n\x07Q\x10\xa8\x15p^\x8a\x029\x87$\x01\xc6y!T\xc99\x1bn\x07\t\xa3\x7fX\xbd\x8a\xa2"),
SylkCommons_pb2.SylkFileContext(file='server/interceptors.py',code=b'x\x9cmR\xc1\x8e\x820\x10\xbd\xf3\x15M\xf6\x00$X\xb3W\x13\x0eF\x89\x9aM<(\x1e6f\xd3T:j\xd7\xd2\xb2mq\xf5\xef\xb7\x80(\xae\xcc\x81\x84\xe9\x9b7\xef\xcd\x0c\xcf\x0b\xa5-:\xe8"\xf3<\xb2^\xcc\x96\xe3t\xb3J\xc8<\x19O\x93\x15\xf9H>c\xdf\\\xc5i`\xd5\t\xa4\xefy\x99\xa0\xc6\xa0Ii\xac\xca\x17\xd2\x82\xce\xa0\xb0J\x07\x15\x03^\x83>\x83\xee\xa4\xc3\x91\xe7!\x17\x0c\xf6\x88\x10.\xb9%$0 \xf6\xedC\xfbHwNF\xc0\x0fRi`D\xc3O\t\xc6F(S\x8e\xebb\x1d\x1au\xe2\x96\xc5MQ\xd3\xd9R[\x9a\x89b\x807\xcb\xf1&\x9d\'\xcbt1\x19\xa7\xc94B\xfeB\x9e\xa9\xe0\x0c\x19\xc7\xef`\x1a\xfc\xf0\xd1\xbdR\x83IM\xc5\x95Dq=\x0b\\J\xaa\xaf\xa4\xf9\xba\x7f\x92\x83=*F\x8eT2\x01:\xa8\xe1\xe1\xc3\x1bo-\x13\xe3F\xc03\xa8M6\xfa\xb9,iE\x1d\xa1[5\xc9\xa8\x10\x84\x81\xa5\\\x98\x8e\xb57\x94\\h^\x08@\xf3\x068q\xb8i\x03Cj\xf7\r\x99\xed\x82\xab \xaf\xc8\xe0\x1f\x04\xa1F{\\\xfa\xc3#\x08\xa1~\x95\x16\x0c\xcf4\x80\xd3<\\\xd3\xeb\xbc\xca\xfa\xd1K\x1d\x97g\x95\xd5\xd2+\xfb\x94QKc\x8cqx\x07\xde\x86"i\x0enn}\xeep\x03\xc1\xa6\x10\xdc\x06\xfe\xd0\x0f\xb7\x83\xf7\xaf;\x01\\\ng\xca-\xbc\xe5w4A\xef\x15F\xddf\xdb\xd1\xc8\xb1<t\xf0}\x0f\x13\x97\xfd\x8az\\=_\x97\x06w"\xf2iuA\xef\xe6\x1e6\x84\x81^\x8e\xe7\xdb\xfa\x03\x86\\\x18G')]) 

# Creating all code files on target project
for f in _context.files:
	file_system.wFile(file_system.get_current_location()+'/'+f.file,zlib.decompress(f.code).decode(),force=True)

    
_architect.Save()
    