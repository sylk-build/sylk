# Copyright (c) 2023 sylk.build

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import logging
from typing import List
from prettytable import PrettyTable
from sylk.commons.pretty import print_info,print_warning,print_error,print_note,print_success
from sylk.commons.helpers import Graph, SylkJson
from sylk.commons.protos.sylk.SylkApi.v1.SylkApi_pb2 import GetProjectResponse
from sylk.commons.protos.sylk.SylkClient.v1.SylkClient_pb2 import SylkClientLanguages
from sylk.commons.protos.sylk.SylkProject.v1.SylkProject_pb2 import SylkProject, SylkProjectDisplay
from sylk.commons.protos.sylk.SylkServer.v1.SylkServer_pb2 import SylkServerLanguages
# from sylk.commons.protos import SylkCommons_pb2

def display_resource(resource_name,sylk_json:SylkJson,count,level=None,nested=False):
    tabs = '\t'
    pipe = f'{(tabs*level)}|' if level is not None else ''
    empty = ''
    level_temp =  f'{pipe if nested == True else empty}{tabs*(level - 1 if nested == True else level)}|-- ' if level is not None else tabs*count
    is_level =level_temp if level is not None else tabs*count
    spacer = is_level
    if len(resource_name.split('.')) == 1:
        print_success('|| Service: {}'.format(resource_name))
        if 'google.protobuf.' not in resource_name:
            for d in sylk_json.services[resource_name].get('dependencies'):
                count += 1
                display_resource(d,sylk_json,count,level=count)
        else:
            display_resource(d,sylk_json,count,level=count)
    else:
        count += 1
        print_success(spacer+'Package: {}'.format(resource_name))
        if 'google.protobuf.' not in resource_name:
            domain = pkg_name = resource_name.split('.')[0]
            pkg_name = resource_name.split('.')[1]
            pkg_ver = resource_name.split('.')[2]
            count_pkgs_dep = 0
            pkg_path = f'protos/{domain}/{pkg_name}/{pkg_ver}/{pkg_name}.proto'
            for d in sylk_json.packages[pkg_path].get('dependencies'):
                count_pkgs_dep +=1
                display_resource(d,sylk_json,count,level=count,nested=nested if nested ==True else len(sylk_json.packages[pkg_path].get('dependencies'))>count_pkgs_dep )


def list_templates(configs,sylk_json:SylkJson):
    print_note("Sylk templates:")
    for tmp in configs.sylk_templates:
        print_info(tmp)
    print()
    print_note("In order to create a new project based on template run the following\n\t-> $ sylk new MyTodo --template @sylk/TodoAppPy")

def list_dependencies(resource,sylk_json:SylkJson):
    resources = []
    print(sylk_json._proto_tree.topological_sort())
    if resource is None or resource in ['service','package']:
        for p in sylk_json.packages:
            pkg = sylk_json.packages[p]
            resources.append(pkg)
        for s in sylk_json.services:
            resources.append(s)

        resourcesSorted = Graph(resources,True).topologicalSort()
    elif resource == 'message':
        for p in sylk_json.packages:
            pkg = sylk_json.packages[p]
            for m in pkg.get('messages'):
                resources.append(m)
        resourcesSorted = dict(Graph(resources).graph)
        del resourcesSorted[None]
    else:
        print_error("not supporting listing dependencies for: rpc / fields / enums / enum values")
        exit(1)

    print_info('Listing Dependencies {}'.format(resource if resource is not None else 'All'),True)
    
    for dep in resourcesSorted:
        try:
            pkg = sylk_json.get_package(dep)
            if resource is None or resource == 'package':
                print()
                print_note('|| Package: {}'.format(dep))
                pkg_name = '{0}/{1}'.format(sylk_json._root_protos,dep.replace('.','/'))
                if sylk_json.packages[pkg_name].get('dependencies'):
                    for d in sylk_json.packages[pkg_name].get('dependencies'):
                        print('    ||\t     |\n    ||\t      -- {}'.format(d))
        except:
            svc = sylk_json.get_service(dep)
            if resource is None or resource == 'service':
                print()
                # display_resource(dep,sylk_json,1)
                print_success('|| Service: {}'.format(dep))

                if svc.get('dependencies'):
                    for d in svc.get('dependencies'):
                        print('    ||\t     |\n    ||\t     Package -- {}'.format(d))
                        if 'google.protobuf.' not in d:
                            pkg_proto_path = '.'.join(d.split('.')[:-1])
                            if sylk_json.packages[pkg_proto_path].get('dependencies'):
                                for deep_dep in sylk_json.packages[pkg_proto_path].get('dependencies'):
                                    if 'google.protobuf.' not in deep_dep:
                                        print('    ||\t\t     |\n    ||\t             Package -- {}'.format(deep_dep))
                                    else: 
                                        print('    ||\t\t     |\n    ||\t             Package -- {}'.format(deep_dep))

                            # for deep_dep in sylk_json.packages[f'protos/{deep_pkg_version}/{deep_pkg}.proto'].get('dependencies'):
                        else:
                            print('    ||\t     |\n    ||\t      Package -- {}'.format(d))
        
        
        if resource == 'message':
            msg = resourcesSorted[dep]
            print()
            print_note('|| Message: {}'.format(dep))
            for m in msg:
                if m is not None:
                    print('    ||\t     |\n    |\t      - * {}'.format(m))

            print()


def list_by_name(full_name,sylk_json:SylkJson):
    """Will print in pretty table the resource description and child descriptions from full name of the resource 
    e.g listing package description and messages + enums child descriptions the 'full_name' param will need to be <domain>.<package>.<version>
    """
    args_split = len(full_name.split('.'))
    if args_split == 1:
        print_info(full_name)
    # Services list
    elif args_split > 1 and args_split <=2:
        try:
            header = ['Service','RPC\'s','Dependencies']
            svc = sylk_json.get_service(full_name.split('.')[1],sylk_json=sylk_json._sylk_json)
            tab = PrettyTable(header)
            add_service_desc(tab,svc)
            # tab.add_row([svc['name'],len(svc.get('methods') if svc.get('methods') is not None else []),svc.get('dependencies')])
            print_info(tab,True,'Listing service resource')
        except Exception:
            print_warning(f'Resource {full_name} wasnt found services')
    # Packages list
    elif args_split == 3:
        try:
            pkg = sylk_json.get_package(full_name.split('.')[1])
            header = ['Package','Messages','Enums','Dependencies']
            tab = PrettyTable(header)
            tab.add_row([pkg['name']+ ' [{}]'.format(pkg['package'].split('.')[-1]),len(pkg.get('messages') if pkg.get('messages') is not None else []),len(pkg.get('enums')) if pkg.get('enums') is not None else 0,pkg.get('dependencies')])
            print_info(tab,True,'Listing package resource')
        except Exception as e:
            logging.error(e)
            print_warning(f'Resource {full_name} wasnt found on packages')
    # Enums list
    elif args_split > 3 and args_split <= 4:
        try:
            enum = sylk_json.get_enum(full_name)
            if enum is not None:
                header = ['Name', 'Value']
                tab = PrettyTable(header)
                for v in enum.get('values'):
                    tab.add_row([v['name'],v.get('number')])
                print_info(tab,True,'Listing enum [{0}] values'.format(enum.get('fullName')))
            else:
                msg = sylk_json.get_message(full_name)
                header = ['Field', 'Field type', 'Enum type', 'Message type']
                oneof_exist = next((f for f in msg.get('fields') if f.get('fieldType') == 'TYPE_ONEOF'),False)
                map_exist = next((f for f in msg.get('fields') if f.get('fieldType') == 'TYPE_MAP'),False)
                
                if oneof_exist:
                    header.append('Oneof')
                if map_exist:
                    header.append('Key type')
                    header.append('Value type')
                tab = PrettyTable(header)

                for f in msg.get('fields'):
                    
                    temp_row = [f['name'],f.get('fieldType','-'),f.get('enumType','-'),f.get('messageType','-')]

                    if oneof_exist:
                        temp_row.append(list(map(lambda x: x.get('name'),f.get('oneofFields'))))
                    if map_exist:
                        temp_row.append(f.get('keyType','-'))
                        temp_row.append(f.get('valueType','-'))

                    tab.add_row(temp_row)
                print_info(tab,True,'Listing message [{0}] fields'.format(msg.get('fullName')))
        except Exception as e:
            print_error(e)
            print_warning(f'Resource {full_name} wasnt found on enums or messages')
    # Fields list ?
    else:
        try:
            msg = sylk_json.get_message('.'.join(full_name.split('.')[:-1]))
            field = next((f for f in msg['fields'] if f['name'] == full_name.split('.')[-1]),None)
            print_info(field,True)
        except Exception:
            print_warning(f'Field {full_name} wasnt found on message')

def list_projects(org,project:List[GetProjectResponse]):
    header = ['ID','Name','Server','Clients','# Services','# Packages','# Methods','# Messages']
    tab = PrettyTable(header)
    for p in project:
        add_project_desc(tab,p.result,org)
    print_info(tab,True,'Listing projects')


def list_by_resource(type,sylk_json:SylkJson):
    """Will print in pretty table the resource description and child descriptions from a resource type
    e.g to list all services description and all methods (RPC's) under the services, the 'type' param will need to be passed with 'service' string
    """
    # Services list
    if type == 'service':
        header = ['Service','RPC\'s','Dependencies','Extensions']
        tab = PrettyTable(header)
        header = ['RPC','Type','Input','Output']
        tab_rpcs = PrettyTable(header)
        if sylk_json.services is not None:
            for svc in sylk_json.services:
                service=sylk_json.services[svc]
                ext = []
                if service.get('extensions') is not None:
                    ext = list(map(lambda k: k,service.get('extensions')))
                ext = ext if len(ext) >0 else '-'
                if service.get('methods') is not None:
                    for rpc in service.get('methods'):
                        add_rpc_desc(tab_rpcs,rpc)
                add_service_desc(tab,service,ext)
            print_info(tab,True,'Listing services resources')
        else:
            print_warning("No services under {}".format(sylk_json.project.get('packageName')))
    
    # Packages list
    elif type == 'package':
        header = ['Package','Messages','Enums','Dependencies','Extensions']
        tab = PrettyTable(header)
        if sylk_json.packages is not None:

            for pkg in sylk_json.packages:
                pkg = sylk_json.packages[pkg]
                ext = []
                if pkg.get('extensions') is not None:
                    ext = list(map(lambda k: k,pkg.get('extensions')))
                ext = ext if len(ext) >0 else '-'
                tab.add_row([pkg['name']+ ' [{}]'.format(pkg['package'].split('.')[-1]),len(pkg.get('messages') if pkg.get('messages') is not None else []),len(pkg.get('enums') if pkg.get('enums') is not None else []),pkg.get('dependencies'),ext ])
            print_info(tab,True,'Listing packages resources')
        else:
            print_warning("No packages under {}".format(sylk_json.project.get('packageName')))

    # Messages List
    elif type == 'message':
        header = ['Message','Fields','Package','Extensions','Extending']
        tab = PrettyTable(header)
        if sylk_json.packages is not None:
            for pkg in sylk_json.packages:
                package = sylk_json.packages[pkg]
                if package.get('messages'):
                    for m in package['messages']:
                        ext = []
                        if m.get('extensions') is not None:
                            ext = list(map(lambda k: k,m.get('extensions')))
                        ext_type = m.get('extensionType') if m.get('extensionType') is not None else '-'
                        ext = ext if len(ext) >0 else '-'
                        tab.add_row([m['name'],len(m.get('fields') if m.get('fields') is not None else []), package.get('package'), ext,ext_type ])
            print_info(tab,True,'Listing packages resources')
        else:
            print_warning("No packages under {}".format(sylk_json.project.get('packageName')))

    # RPC's List
    elif type == 'rpc':
        header = ['RPC','Type','Input','Output']
        tab_rpcs = PrettyTable(header)
        if sylk_json.services is not None:
            for svc in sylk_json.services:
                service = sylk_json.services[svc]
                for rpc in service.get('methods'):
                    add_rpc_desc(tab_rpcs,rpc)
            print_info(tab_rpcs,True,'Listing RPC\'s')
        else:
            print_warning("No services under {}".format(sylk_json.project.get('packageName')))
    
    # Extensions List
    elif type == 'extension':
        header = ['Name','Package','Extending']
        tab_exts = PrettyTable(header)
        
        options = sylk_json.get_extensions()
        # Extensions fields options
        if len(options) > 0:
            for opt in options:
                add_ext_desc(tab_exts,opt)
            print_info(tab_exts,True,'Listing Extensions')
        else:
            print_warning("No services under {}".format(sylk_json.project.get('packageName')))
    

    # Not supported listing ALL resources
    else:
        if type is not None:
            print_warning("Listing '{0}' not supported yet".format(type))
        list_all(sylk_json)

def list_all(sylk_json:SylkJson):
    """Will print all sylk.build project resource that are declared on sylk.json file"""

    prj_name = sylk_json.project.get('name')
    sylk_ver = sylk_json.sylk_version
    print_info(f'Listing project \'{prj_name}\' resources (sylk version: {sylk_ver})')
    inline_enums = []
    # Services list
    header = ['Service','RPC\'s','Dependencies','Extensions']
    tab = PrettyTable(header)
    
    if sylk_json.services:
        # RPC's list
        header = ['RPC','Type','Input','Output']
        tab_rpcs = PrettyTable(header)
        
        for svc in sylk_json.services:
            ext = []
            if svc.get('extensions') is not None:
                ext = list(map(lambda k: k,svc.get('extensions')))
            ext = ext if len(ext) >0 else '-'
            add_service_desc(tab,svc,ext)
            if svc.get('methods') is not None:
                for rpc in svc.get('methods'):
                    add_rpc_desc(tab_rpcs,rpc,)
    
        print_info(tab,True,'📡 Listing services resources')
        print_info(tab_rpcs,True,'Listing RPC\'s')
    
    # Packages list
    header = ['Package','Messages','Enums','Dependencies','Extensions']
    tab = PrettyTable(header)
    if sylk_json.packages is not None:
        for pkg in sylk_json.packages:
            pkg = sylk_json.packages[pkg]
            ext = []
            if pkg.get('extensions') is not None:
                ext = list(map(lambda k: k,pkg.get('extensions')))
            ext = ext if len(ext) >0 else '-'
            add_package_desc(tab,pkg,ext)
    else:
        print_warning("No packages on project")

    print_info(tab,True,'📁 Listing packages resources')

    # Messages List
    header = ['Message','Fields','Package','Extensions','Extending']
    tab = PrettyTable(header)

    if sylk_json.packages is not None:
        for pkg in sylk_json.packages:
            package = sylk_json.packages[pkg]
            if package.get('messages'):
                for m in package['messages']:
                    ext = []
                    if m.get('extensions') is not None:
                        ext = list(map(lambda k: k,m.get('extensions')))
                    ext_type = m.get('extensionType') if m.get('extensionType') is not None else '-'
                    ext = ext if len(ext) >0 else '-'
                    add_message_desc(tab,m,package,ext,ext_type)
                    for im in m.get('inlines', []):
                        if 'SylkMessage' in im.get('@type'):
                            ext = []
                            if im.get('extensions') is not None:
                                ext = list(map(lambda k: k,im.get('extensions')))
                            ext_type = im.get('extensionType') if im.get('extensionType') is not None else '-'
                            ext = ext if len(ext) >0 else '-'
                            add_message_desc(tab,im,package,ext,ext_type)
                        else:
                            inline_enums.append((im,package))

    else:
        print_warning("No packages on project")
    
    print_info(tab,True,'📝 Listing packages messages')
    
    # Enums list
    header = ['Enum','Values','Package']
    tab = PrettyTable(header)
    for inline_enum in inline_enums:
        add_enum_desc(tab,*inline_enum)
    if sylk_json.packages is not None:
        for pkg in sylk_json.packages:
            package = sylk_json.packages[pkg]
            if package.get('enums'):

                for e in package['enums']:
                    add_enum_desc(tab,e,package)
    else:
        print_warning("No packages on project")
    print_info(tab,True,'📝 Listing packages enums')


def add_project_desc(tab,prj,org):
    
    tab.add_row([f'{org}.{prj.project.package_name}',prj.project.name, SylkServerLanguages.Name(prj.project.server.language),[SylkClientLanguages.Name(c.language) for c in prj.project.clients],prj.numServices,prj.numPackages,prj.numMethods,prj.numMessages])

def add_service_desc(tab,svc_description,extensions=None):
    tab.add_row([svc_description.get('name') + ' [{}]'.format(svc_description.get('fullName')),len(svc_description.get('methods') if svc_description.get('methods') is not None else []),svc_description.get('dependencies'),extensions])

def add_package_desc(tab,package_desc,ext):
    tab.add_row([package_desc.get('name') + ' [{}]'.format(package_desc.get('package')),len(package_desc.get('messages') if package_desc.get('messages') is not None else []),len(package_desc.get('enums') if package_desc.get('enums') is not None else []),package_desc.get('dependencies') if package_desc.get('dependencies') is not None and len(package_desc.get('dependencies')) < 3 else f"{len(package_desc.get('dependencies'))} deps" if package_desc.get('dependencies') is not None else None,ext ])

def add_message_desc(tab,msg_desc,package_desc, ext,ext_type ):
    tab.add_row([msg_desc.get('name') + ' [{}]'.format(msg_desc.get('fullName')),len(msg_desc.get('fields') if msg_desc.get('fields') is not None else []),package_desc.get('package'), ext,ext_type ])

def add_enum_desc(tab,enum_desc,package_desc):
    tab.add_row([enum_desc.get('name') + ' [{}]'.format(enum_desc.get('fullName')),len(enum_desc.get('values') if enum_desc.get('values') is not None else []),package_desc.get('package')])

def add_rpc_desc(tab,rpc_desc):
    rpc_type_server = rpc_desc.get('serverStreaming')
    rpc_type_client = rpc_desc.get('clientStreaming')
    rpc_type = 'Unary' if (rpc_type_client == False or rpc_type_client is None ) and (rpc_type_server == False or rpc_type_server is None) else 'Client stream' if rpc_type_client == True and (rpc_type_server == False or rpc_type_server is None) else 'Server Stream' if rpc_type_server == True and (rpc_type_client == False or rpc_type_client is None ) else 'Bidi' if rpc_type_client == True and rpc_type_server == True else ''
    tab.add_row([rpc_desc.get('name'),rpc_type,rpc_desc.get('inputType'),rpc_desc.get('outputType')])

def add_ext_desc(tab,ext_desc):
    ext_package = '.'.join(ext_desc.get('fullName').split('.')[:-1])
    tab.add_row([ext_desc.get('name'),ext_package,ext_desc.get('extensionType')])
