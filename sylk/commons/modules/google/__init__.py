from sylk.commons.sylk import SylkTree
def google():
    tree = SylkTree("google", "google")
    tree.add_node("google.protobuf", "package")
    tree.add_node(
        "google.protobuf.Timestamp", "message", {"tag": "timestamp"}
    )
    tree.add_node(
        "google.protobuf.Duration", "message", {"tag": "duration"}
    )
    tree.add_node(
        "google.protobuf.Empty", "message", {"tag": "empty"}
    )
    tree.add_node(
        "google.protobuf.Any", "message", {"tag": "any"}
    )
    tree.add_node(
        "google.protobuf.Struct", "message", {"tag": "struct"}
    )
    tree.add_node(
        "google.protobuf.Value", "message", {"tag": "struct"}
    )
    tree.add_node(
        "google.protobuf.ListValue", "message", {"tag": "struct"}
    )
    tree.add_node(
        "google.protobuf.NullValue", "message", {"tag": "struct"}
    )
    tree.add_node(
        "google.protobuf.BoolValue", "message", {"tag": "wrappers"}
    )
    tree.add_node(
        "google.protobuf.StringValue", "message", {"tag": "wrappers"}
    )
    tree.add_node(
        "google.protobuf.BytesValue", "message", {"tag": "wrappers"}
    )
    tree.add_node(
        "google.protobuf.DoubleValue", "message", {"tag": "wrappers"}
    )
    tree.add_node(
        "google.protobuf.FloatValue", "message", {"tag": "wrappers"}
    )
    tree.add_node(
        "google.protobuf.Int64Value", "message", {"tag": "wrappers"}
    )
    tree.add_node(
        "google.protobuf.UInt64Value", "message", {"tag": "wrappers"}
    )
    tree.add_node(
        "google.protobuf.Int32Value", "message", {"tag": "wrappers"}
    )
    tree.add_node(
        "google.protobuf.UInt32Value", "message", {"tag": "wrappers"}
    )
    tree.add_node(
        "google.protobuf.UInt64Value", "message", {"tag": "wrappers"}
    )
    tree.add_node(
        "google.protobuf.FieldMask", "message", {"tag": "field_mask"}
    )
    return tree
