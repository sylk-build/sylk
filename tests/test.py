from sylk.commons.sylk import SylkTree

# Create a new SylkTree
tree = SylkTree("google")

# Add nodes to the tree with validated properties
tree.add_node_with_validated_properties("google.protobuf", "package")
tree.add_node_with_validated_properties("google.protobuf.Timestamp", "message", {"tag": "timestamp"})
tree.add_node_with_validated_properties("google.protobuf.Empty", "message")
tree.add_node_with_validated_properties("google.analytics.admin.v1beta", "package")
tree.add_node_with_validated_properties("google.analytics.admin.v1beta.AnalyticsAdminService", "service")
tree.add_node_with_validated_properties("google.analytics.data.v1beta", "package")
tree.add_node_with_validated_properties("google.analytics.data.v1beta.Metrics", "message")
tree.add_node_with_validated_properties("google.analytics.data.v1beta.MessageType", "message")
tree.add_node_with_validated_properties("google.analytics.data.v1beta.EnumType", "enum")
tree.add_node_with_validated_properties("google.analytics.data.v1beta.Metrics.Field1", "field")
tree.add_node_with_validated_properties("google.analytics.data.v1beta.Metrics.Field2", "field")

# Add field references to message nodes
tree.add_field_reference("google.analytics.data.v1beta.Metrics", "Field1", "google.analytics.data.v1beta.MessageType")
# tree.add_field_reference("google.analytics.data.v1beta.Metrics", "Field2", "google.analytics.data.v1beta.EnumType")

# Print the tree structure
tree.dfs_traversal()
# Get references of a node
node_name = "google.analytics.admin.v1beta"
# tree.get_references(node_name)
parent = tree.get_references('google.analytics.data.v1beta.Metrics')
print(parent)
tree.save_to_json('sylk_test.json')