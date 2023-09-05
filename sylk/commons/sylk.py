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
from collections import deque
import json
import logging
import re
from typing import Dict, List
from sylk.commons.protos.sylk.SylkClient.v1 import SylkClient_pb2
from sylk.commons.protos.sylk.SylkEnumValue.v1 import SylkEnumValue_pb2
from sylk.commons.protos.sylk.SylkField.v1 import SylkField_pb2
from sylk import __version__
from sylk.commons.protos.sylk.SylkMessage.v2 import SylkMessage_pb2
from sylk.commons.protos.sylk.SylkEnum.v2 import SylkEnum_pb2
from sylk.commons.protos.sylk.SylkMethod.v1 import SylkMethod_pb2
from sylk.commons.protos.sylk.SylkPackage.v2 import SylkPackage_pb2
from sylk.commons.protos.sylk.SylkServer.v1 import SylkServer_pb2
from sylk.commons.protos.sylk.SylkService.v2 import SylkService_pb2
from sylk.commons.protos.sylk.SylkProject.v1 import SylkProject_pb2

from google.protobuf.json_format import MessageToDict, ParseDict
from google.protobuf.any_pb2 import Any

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="[{plugin_name}] - %(message)s".format(plugin_name="sylk-tree"),
)


class SylkBuilder:
    def __init__(self) -> None:
        self._parse_configs()
        self._parse_current_project()

    def _parse_configs(self):
        pass

    def _parse_current_project(self):
        pass

    def get_project(self):
        pass

    def get_services(self):
        pass

    def get_packages(self):
        pass

    def get_messages(self):
        pass

    def get_enums(self):
        pass

    def get_fields(self):
        pass

    def get_enum_values(self):
        pass

    def get_ext(self):
        pass


class Node:
    def __init__(self, name, type=None, properties=None, parent=None):
        self.name = name
        self.children = []
        self.type = type
        self.properties = properties if properties else {}
        self.references = []
        self.parent = parent
        self.full_path = self._calculate_full_path()

    def add_child(self, child):
        self.children.append(child)

    def _calculate_full_path(self):
        if self.parent:
            return f"{self.parent.full_path}.{self.name}"
        return self.name


class SylkTree:
    VALID_PROPERTIES = [
        "root",
        "message",
        "enum",
        "service",
        "field",
        "value",
        "method",
        "package",
        "oneof"
    ]

    TYPE_RULES = {
        "enum": ["value"],
        "service": ["method"],
        "message": ["field", "enum", "message"],
        "package": ["package", "service", "message", "enum"],
        "root": ["package"],
        "field": ["oneof"],
    }

    def __init__(self, root_name, project_name=None):
        self.root = Node(root_name, "root")
        self.project_name = project_name
        self.proto_modules: Dict[str, SylkTree] = {}

    def load_module(self, module):
        self.proto_modules[module.root.name] = module

    def resolve_dependency_order(self,messages: List[Dict]):
        def topological_sort(nodes):
            sorted_nodes = []
            visited = set()
            def dfs(node):
                if node["node"] in visited:
                    return
                visited.add(node["node"])
                for ref_node in node["refs"]:
                    ref = next((n for n in nodes if n["node"] == ref_node), None)
                    if ref:
                        dfs(ref)
                sorted_nodes.append(node["node"])

            for node in nodes:
                dfs(node)

            sorted_nodes
            return sorted_nodes
        # Create a dictionary to store the mapping of message name to message object
        message_map = {message.get('fullName'): message for message in messages}

        # Create a list of nodes where each node is a message name with its references being the field types
        nodes = []
        for message in messages:
            refs = [
                field.get('messageType')
                for field in message.get('fields', [])
                if field.get('fieldType') is not None
                and (field.get('fieldType') == SylkField_pb2.SylkFieldTypes.Name(SylkField_pb2.TYPE_MESSAGE)
                or field.get('valueType') == SylkField_pb2.SylkFieldTypes.Name(SylkField_pb2.TYPE_ENUM))
            ] + [
                field.get('enumType')
                for field in message.get('fields', [])
                if field.get('fieldType') is not None
                and (field.get('fieldType') == SylkField_pb2.SylkFieldTypes.Name(SylkField_pb2.TYPE_ENUM)
                or field.get('valueType') == SylkField_pb2.SylkFieldTypes.Name(SylkField_pb2.TYPE_ENUM))
            ]
            nodes.append({"node": message.get('fullName'), "refs": refs})

        # Perform topological sorting
        sorted_message_names = topological_sort(nodes)

        # Reorder the messages based on the sorted names
        sorted_messages = [message_map[name] for name in sorted_message_names]

        return sorted_messages

    def add_node(self, path, type=None, properties=None):
        current_node = self.root

        # Split the path into individual node names
        node_names = path.split(".")

        # Check if the first node name matches the root node name
        if node_names[0] != current_node.name:
            raise ValueError(
                f"Invalid path. The root node '{current_node.name}' does not match the path '{path}'"
            )

        for i, name in enumerate(node_names[1:]):
            # Check if the current node already has a child with the same name
            child_node = self._find_child_node(name, current_node)
            if child_node:
                current_node = child_node
            else:
                # Create a new node and add it as a child of the current node
                new_node = Node(name, type, properties, current_node)

                current_node.add_child(new_node)
                current_node = new_node
                # Validate the parent hierarchy based on node types
                if current_node != self.root and i > 0:
                    if (
                        name not in self.VALID_PROPERTIES
                        and current_node.name != self.root.name
                    ):
                        parent_type = current_node.parent.type
                        type = current_node.type
                        if type not in self.TYPE_RULES.get(parent_type, []):
                            raise ValueError(
                                f"Invalid parent hierarchy for node '{current_node.name}' of type '{type}' under '{parent_type}'"
                            )

    def dfs_traversal(self):
        return self._dfs(self.root)

    def bfs_traversal(self):
        self._bfs(self.root)

    def get_parent(self, node_name) -> Node:
        if node_name.split(".")[0] != self.root.name:
            n = self.proto_modules[node_name.split(".")[0]].root
        else:
            n = self.root
        return self._find_parent(node_name, n)

    def get_parents_refs(self, refs) -> List[str]:
        packages_paths = []
        for ref in refs:
            if ref.split('.')[0] != self.root.name:
                p = self._find_parent(ref, self.proto_modules[ref.split('.')[0]].root)
            else:
                p = self._find_parent(ref, self.root)
            if p is not None:
                if p.full_path not in packages_paths:
                    packages_paths.append(p.full_path)
            else: 
                raise ValueError(
                    f"Failed to find parent for '{ref}' is not a message node."
                )
        return packages_paths

    def get_references(self, node_name):
        node = self._find_node(node_name, self.root)
        if node:
            return self._get_references_helper(node)
        else:
            logger.error("Node not found.")

    def resolve_dependencies(self):
        sorted_nodes = self._topological_sort()
        if sorted_nodes:
            # logger.debug("Dependency resolution order:")
            # for node in sorted_nodes:
            #     logger.debug(node.name)
            return sorted_nodes
        else:
            logger.error("Dependency cycle detected. Unable to resolve dependencies.")
        return None

    def _dfs(self, node):
        yield self._process_node(node)

        for child in node.children:
            self._dfs(child)

    def _bfs(self, node):
        queue = deque()
        queue.append(node)

        while queue:
            current_node = queue.popleft()
            yield self._process_node(current_node)

            for child in current_node.children:
                queue.append(child)

    def _process_node(self, node):
        return node
        # logger.debug(f"Node: {node.name}")
        # logger.debug(f"Properties: {node.properties}")
        # logger.debug(f"References: {node.references}")

    def _find_parent(self, node_path, current_node, recursive=False):
        path_parts = node_path.split(".")
        if len(path_parts) > 1:
            parent_path = ".".join(path_parts[:-1])
            parent_node = self._find_node(parent_path, current_node)
            if recursive:
                if parent_node.type != 'package':
                    parent_node = self._find_parent(parent_node.full_path,current_node,recursive)
            return parent_node
        else:
            return self._find_node(node_path.split('.')[0], current_node)
        return None

    def _find_node(self, node_path, current_node) -> Node:
        if current_node.full_path == node_path:
            return current_node

        for child in current_node.children:
            found_node = self._find_node(node_path, child)
            if found_node:
                return found_node

        return None
        # if current_node.name == node_name:
        #     return current_node

        # for child in current_node.children:
        #     found_node = self._find_node(node_name, child)
        #     if found_node:
        #         return found_node

        # return None

    def _find_child_node(self, name, current_node):
        for child in current_node.children:
            if child.name == name:
                return child

        return None

    def _parse_version_component(self, full_name: str) -> dict or None:
        full_name = full_name.replace("/", ".")
        if full_name:
            segments = full_name.split(".")

            pattern = r"^v(\d+)(alpha|beta)?(\d+)?$"

            for segment in segments:
                regex = re.compile("[@!#$%^&*()<>?/\|}{~:]")
                # Pass the string in search
                # method of regex object.
                if regex.search(segment) is not None:
                    raise Exception("package name cannot hold any special characters")

                match = re.match(pattern, segment)

                if match:
                    version = int(match.group(1))
                    channel = match.group(2)
                    release = int(match.group(3)) if match.group(3) else None
                    return {"version": version, "channel": channel, "release": release}

        return None

    def _find_package_node(self, node: Node):
        if node.type == "package":
            return node

        for child in node.children:
            package_node = self._find_package_node(child)
            if package_node:
                return package_node

        return None

    def validate_properties(self, type):
        return type in self.VALID_PROPERTIES

    def add_node_with_validated_properties(self, path, type=None, properties=None):
        if properties and not self.validate_properties(type):
            raise ValueError("Invalid properties")
        self.add_node(path, type, properties)

    def get_all_file_paths(self):
        files = []
        for node in self._bfs(self.root):
            if node.type == "package":
                if len([c for c in node.children if c.type != "package"]) > 0:
                    tags = set(
                        [
                            c.properties.get("tag")
                            for c in node.children
                            if c.properties.get("tag") is not None
                        ]
                    )
                    if len(tags) > 0:
                        for t in tags:
                            files.append(
                                node.full_path.replace(".", "/") + "/" + f"{t}.proto"
                            )

                    if len(
                        [
                            c.properties.get("tag")
                            for c in node.children
                            if c.properties.get("tag") is not None
                        ]
                    ) != len([c for c in node.children if c.type != "package"]):
                        ver = self._parse_version_component(node.full_path)
                        if ver is not None:
                            pkg_name = node.full_path.split(".")[-2]
                        else:
                            pkg_name = node.full_path.split(".")[-1]
                        files.append(
                            node.full_path.replace(".", "/") + "/" + f"{pkg_name}.proto"
                        )
            elif node.type == "root":
                if len([c for c in node.children if c.type != "package"]) > 0:
                    tags = set(
                        [
                            c.properties.get("tag")
                            for c in node.children
                            if c.properties.get("tag") is not None
                        ]
                    )
                    if len(tags) > 0:
                        for t in tags:
                            files.append(
                                node.full_path.replace(".", "/") + "/" + f"{t}.proto"
                            )

                    if len(
                        [
                            c.properties.get("tag")
                            for c in node.children
                            if c.properties.get("tag") is not None
                        ]
                    ) != len([c for c in node.children if c.type != "package"]):
                        ver = self._parse_version_component(node.full_path)
                        if ver is not None:
                            pkg_name = node.full_path.split(".")[-2]
                        else:
                            pkg_name = node.full_path.split(".")[-1]
                        files.append(
                            node.full_path.replace(".", "/") + "/" + f"{pkg_name}.proto"
                        )

        for mod in self.proto_modules:
            module = self.proto_modules[mod].root
            for node in self._bfs(module):
                if node.type == "package":
                    if len([c for c in node.children if c.type != "package"]) > 0:
                        tags = set(
                            [
                                c.properties.get("tag")
                                for c in node.children
                                if c.properties.get("tag") is not None
                            ]
                        )
                        if len(tags) > 0:
                            for t in tags:
                                files.append(
                                    node.full_path.replace(".", "/")
                                    + "/"
                                    + f"{t}.proto"
                                )
                        if len(
                            [
                                c.properties.get("tag")
                                for c in node.children
                                if c.properties.get("tag") is not None
                            ]
                        ) < len(
                            [
                                c
                                for c in node.children
                                if c.type != "package"
                                and c.properties.get("tag") is None
                            ]
                        ):
                            ver = self._parse_version_component(node.full_path)
                            if ver is not None:
                                pkg_name = node.full_path.split(".")[-2]
                            else:
                                pkg_name = node.full_path.split(".")[-1]
                            files.append(
                                node.full_path.replace(".", "/")
                                + "/"
                                + f"{pkg_name}.proto"
                            )
        return files
    
    def update_node_prop(self, node_path, props):
        node = self._find_node(node_path,self.root)
        if node is not None:
            node.properties = { **node.properties, **props}


    def _get_file_paths(self, references: List[str]):
        files = []
        for ref in references:
            if ref.split(".")[0] != self.root.name:
                n = self._find_node(ref, self.proto_modules[ref.split(".")[0]].root)
                p = self._find_parent(
                    n.full_path, self.proto_modules[ref.split(".")[0]].root
                )
            else:
                n = self._find_node(ref, self.root)
                p = self._find_parent(n.full_path, self.root, True)
            tag = None
            if n.properties is not None:
                tag = n.properties.get("tag")
            if tag is not None:
                file = p.full_path.replace(".", "/") + f"/{tag}.proto"
                if file not in files:
                    files.append(file)
            else:
                ver = self._parse_version_component(p.full_path)
                if ver is not None:
                    pkg_name = p.full_path.split(".")[-2]
                else:
                    pkg_name = p.full_path.split(".")[-1]

                file = p.full_path.replace(".", "/") + f"/{pkg_name}.proto"
                if file not in files:
                    files.append(file)
        return files

    def _get_references_helper(self, node: Node):
        if node.type == "message":
            for child in node.children:
                node.references.extend(self._get_references_helper(child))
        elif node.type == "service":
            for child in node.children:
                node.references.extend(self._get_references_helper(child))
        elif node.type == "enum":
            for child in node.children:
                node.references.extend(self._get_references_helper(child))
        elif node.type == "package":
            for child in node.children:
                node.references.extend(self._get_references_helper(child))
        elif node.type == "field":
            for child in node.children:
                node.references.extend(self._get_references_helper(child))
        elif node.type == "root":
            for child in node.children:
                node.references.extend(self._get_references_helper(child))
        return node.references

    def _resolve_dependencies_refs(self, node):
        for dep in node.references:
            refs = self.get_references(dep)
            for ref in refs:
                if dep in ref:
                    return f'"{node.full_path}" found in "{dep}" dependencies'
        return None

    def nested_topological_sort(self,children):
        in_degree = {}
        sorted_nodes = []
        visited = set()

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            if node in in_degree:
                for ref_node in in_degree[node]:
                    dfs(ref_node)
            sorted_nodes.append(node)

        # Calculate the in-degree for each node
        for child in children:
            refs = child.references
            for ref_node in refs:
                if ref_node not in in_degree:
                    in_degree[ref_node] = set()
                in_degree[ref_node].add(child.full_path)

        # Perform topological sorting using DFS
        for child in children:
            dfs(child.full_path)
        sorted_nodes.reverse()
        return sorted_nodes

    def topological_sort(self):
        in_degree = {}
        sorted_nodes = []
        queue = deque()
        nodes = []
        for n in [
            pkg
            for pkg in self._bfs(self.root)
            
        ]:  
            if n.type == "package" and len([c for c in n.children if c.type != "package"]) > 0:
                refs = [
                    self.get_parent(c) for c in self.get_references(n.full_path)
                ]
                nodes.append({"node": n.full_path, "refs": [r.full_path for r in refs if r is not None]})
            else:
                nodes.append({"node": n.full_path, "refs": []})
        # Calculate the in-degree for each node
        sorted_nodes = []
        visited = set()

        def dfs(node):
            if node["node"] in visited:
                return
            visited.add(node["node"])
            for ref_node in node["refs"]:
                ref = next((n for n in nodes if n["node"] == ref_node), None)
                if ref:
                    dfs(ref)
            sorted_nodes.append(node["node"])

        for node in nodes:
            dfs(node)
        sorted_nodes.reverse()
        return sorted_nodes

    def _topological_sort(self):
        in_degree = {}
        sorted_nodes = []
        queue = deque()

        # Calculate the in-degree for each node
        self._calculate_in_degree(self.root, in_degree)

        # Enqueue nodes with no incoming edges (in-degree = 0)
        for node in in_degree:
            if in_degree[node] == 0:
                queue.append(node)

        # Perform topological sorting using Kahn's algorithm
        while queue:
            current_node = queue.popleft()
            sorted_nodes.append(current_node)

            for child in current_node.children:
                if (
                    child.type != "type"
                    and len([c for c in child.children if c.type != "package"]) > 0
                ):
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        queue.append(child)

            # Resolve dependencies based on references
            for ref_node_name in current_node.references:
                ref_node = self._find_parent(ref_node_name, self.root)
                if ref_node:
                    in_degree[ref_node] -= 1
                    if in_degree[ref_node] == 0:
                        queue.append(ref_node)

        # Check for a dependency cycle
        # print(len(sorted_nodes), len(in_degree))
        # if len(sorted_nodes) != len(in_degree):
        #     return None

        return sorted_nodes

    def _calculate_in_degree(self, node, in_degree):
        if node not in in_degree:
            in_degree[node] = 0

        for child in node.children:
            if child in in_degree:
                in_degree[child] += 1
            else:
                in_degree[child] = 1

            self._calculate_in_degree(child, in_degree)

    def add_field_reference(self, message_path, field_name, ref_path):
        root_module = self.root
        message_node = self._find_node(message_path, self.root)
        if ref_path.split(".")[0] != self.root.name:
            root_module = self.proto_modules[ref_path.split(".")[0]].root
        ref_node = self._find_node(ref_path, root_module)
        if message_node and ref_node:
            field = [field for field in message_node.children if field.name == field_name]
            if message_node.type == "message":
                ref_node_name = ref_node.full_path
                if len(field) == 1:
                    field[0].references.append(ref_node_name)
                if ref_node_name not in message_node.references:
                    message_node.references.append(ref_node_name)
            elif message_node.type == "field":
                ref_node_name = ref_node.full_path
                message_node = self._find_parent(message_node.full_path, self.root)
                if len(field) == 1:
                    field[0].references.append(ref_node_name)
                if ref_node_name not in message_node.references:
                    message_node.references.append(ref_node_name)
            else:
                raise ValueError(
                    f"The node '{message_node.name}' is not a message node."
                )
        else:
            logger.info(f"parent: {message_path}, ref: {ref_path}")
            raise ValueError("One or both nodes not found in the tree.")

    def add_method_reference(self, method_path, ref_path):
        method_node = self._find_node(method_path, self.root)
        if ref_path.split(".")[0] != self.root.name:
            ref_node = self._find_node(
                ref_path, self.proto_modules[ref_path.split(".")[0]].root
            )
        else:
            ref_node = self._find_node(ref_path, self.root)
        if method_node and ref_node:
            if method_node.type == "method":
                ref_node_name = ref_node.full_path
                if ref_node_name not in method_node.references:
                    method_node.references.append(ref_node_name)
            else:
                raise ValueError(f"The node '{method_node.name}' is not a method node.")
        else:
            raise ValueError("One or both nodes not found in the tree.")

    def _get_full_path(self, node):
        if node is not None:
            if node.parent == self.root:
                return node.parent.name + "." + node.name
            else:
                return f"{self._get_full_path(node.parent)}.{node.name}"
        else:
            return ""

    # def _flatten_packages(self, node, packages_dict):
    #     if "package" in node.properties and not self._contains_only_packages(node):
    #         package_path = self._get_full_path(node)
    #         packages_dict[package_path] = self._node_to_dict(node)

    #     for child in node.children:
    #         self._flatten_packages(child, packages_dict)

    def _flatten_packages(self, node: Node, packages_dict):

        if node.type == "package":
            if self._has_messages_services_enums(node) or self._is_empty(node):
                package_path = self._get_full_path(node)
                packages_dict[package_path.replace(".", "/")] = self._node_to_dict(node)
            else:
                for child in node.children:
                    self._flatten_packages(child, packages_dict)
        else:
            for child in node.children:
                self._flatten_packages(child, packages_dict)

    def to_dict(self, base_path: str):
        tree_dict = {
            "organization": {"domain": self.root.name},
            "packages": {},
            "configs": {
                "host": "localhost",
                "port": 44880,
                "protoBasePath": ""
            },
            "sylk_version": __version__.__version__,
            "project": MessageToDict(
                SylkProject_pb2.SylkProject(
                    name=self.project_name,
                    package_name=self.project_name.replace("-", "")
                    .replace(" ", "_")
                    .lower(),
                    uri=base_path,
                    server=SylkServer_pb2.SylkServer(
                        language=SylkServer_pb2.SylkServerLanguages.python
                    ),
                    clients= [
                        SylkClient_pb2.SylkClient(
                            language=SylkClient_pb2.SylkClientLanguages.python
                        )
                    ]
                )
            ),
        }

        # if self.root.type == "root":
        #     tree_dict["project"] = self._node_to_dict(self.root)
        self._flatten_packages(self.root, tree_dict["packages"])

        return tree_dict

    def _has_messages_services_enums(self, node):
        for child in node.children:
            if (
                "message" == child.type
                or "service" == child.type
                or "enum" == child.type
            ):
                return True
        return False

    def _is_empty(self, node):
        return len(node.children) == 0

    def _node_to_dict(self, node: Node):
        childrens = []
        if self.root != node:
            msgs = self.nested_topological_sort(node.children)
            for m in msgs:
                child_dict = self._node_to_dict(self._find_node(m,self.root))
                childrens.append(child_dict)

            for child in node.children:
                if child.full_path not in msgs:
                    child_dict = self._node_to_dict(child)
                    childrens.append(child_dict)
        node_dict = None
        message_type_url = 'types.googleapis.com/sylk.SylkMessage.v2.SylkMessage'
        enum_type_url = 'types.googleapis.com/sylk.SylkEnum.v2.SylkEnum'
        if node.type == "message":
            node_dict = MessageToDict(
                SylkMessage_pb2.SylkMessage(
                    full_name=node.full_path,
                    name=node.name,
                    type=node.type,
                    inlines=list(
                        map(
                            lambda c: ParseDict(
                                {
                                    "@type": enum_type_url if c.get('type') == 'enum' else message_type_url,
                                    **c,
                                },
                                Any(),
                            ),
                            [
                                c
                                for c in childrens
                                if c.get("type") == "message" or c.get("type") == "enum"
                            ],
                        )
                    ),
                    fields=[
                        ParseDict(c, SylkField_pb2.SylkField())
                        for c in childrens
                        if c.get("type") == "field"
                    ],
                    **node.properties,
                )
            )
        elif node.type == "enum":
            node_dict = MessageToDict(
                SylkEnum_pb2.SylkEnum(
                    full_name=node.full_path,
                    name=node.name,
                    type=node.type,
                    values=[
                        ParseDict(c, SylkEnumValue_pb2.SylkEnumValue())
                        for c in childrens
                        if c.get("type") == "value"
                    ],
                    **node.properties,
                )
            )
        elif node.type == "service":
            node_dict = MessageToDict(
                SylkService_pb2.SylkService(
                    full_name=node.full_path,
                    name=node.name,
                    type=node.type,
                    methods=[
                        ParseDict(c, SylkMethod_pb2.SylkMethod())
                        for c in childrens
                        if c.get("type") == "method"
                    ],
                    **node.properties,
                )
            )

        elif node.type == "package":
            refs = self.get_references(node.full_path)
            deps = self.get_parents_refs(refs)
            # files = self._get_file_paths(refs)
            node_dict = MessageToDict(
                SylkPackage_pb2.SylkPackage(
                    package=node.full_path,
                    type=node.type,
                    dependencies=deps,
                    services=[
                        ParseDict(c, SylkService_pb2.SylkService())
                        for c in childrens
                        if c.get("type") == "service"
                    ],
                    messages=[
                        ParseDict(c, SylkMessage_pb2.SylkMessage())
                        for c in childrens
                        if c.get("type") == "message"
                    ],
                    enums=[
                        ParseDict(c, SylkEnum_pb2.SylkEnum())
                        for c in childrens
                        if c.get("type") == "enum"
                    ],
                    **node.properties,
                )
            )

        elif node.type == "field":
            node_dict = MessageToDict(
                SylkField_pb2.SylkField(
                    full_name=node.full_path,
                    name=node.name,
                    type=node.type,
                    oneof_fields=list(
                        map(
                            lambda c: ParseDict(c.properties, SylkField_pb2.SylkOneOfField()),
                            [c for c in node.children if c.type == 'oneof']
                        ),
                    ),
                    **node.properties,
                )
            )
        elif node.type == "value":
            node_dict = MessageToDict(
                SylkEnumValue_pb2.SylkEnumValue(
                    full_name=node.full_path,
                    name=node.name,
                    type=node.type,
                    **node.properties,
                )
            )
        elif node.type == "method":
            node_dict = MessageToDict(
                SylkMethod_pb2.SylkMethod(
                    full_name=node.full_path,
                    name=node.name,
                    type=node.type,
                    **node.properties,
                )
            )
        else:
            pass
        return node_dict

    def save_to_json(self, filename):
        # Save the tree state to a JSON file
        tree_dict = self.to_dict()
        with open(filename, "w") as file:
            json.dump(tree_dict, file, indent=4)

    def to_json(self, base_path):
        # Save the tree state to a JSON file
        tree_dict = self.to_dict(base_path)
        return json.dumps(tree_dict, indent=4)
