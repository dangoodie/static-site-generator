from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Split nodes by a delimiter"""
    new_nodes = list()
    for node in old_nodes:
        parts = node.text.split(delimiter)

        toggle = node.text.startswith(delimiter)

        for part in parts:
            if part:
                new_node = TextNode(part, text_type if toggle else node.text_type)
                new_nodes.append(new_node)
            toggle = not toggle

    return new_nodes
