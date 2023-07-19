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
    return tree
