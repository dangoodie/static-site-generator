from enum import Enum
from leafnode import LeafNode


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    """A node that represents text"""
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return NotImplemented
        return (self.text, self.text_type, self.url) == (
            other.text,
            other.text_type,
            other.url,
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    """Convert a TextNode to an HTMLNode"""
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(tag="", value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag="b", value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag="i", value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag="code", value=text_node.text)
        case TextType.LINK:
            return LeafNode(
                tag="a", value=text_node.text, props={"href": text_node.url}
            )
        case TextType.IMAGE:
            return LeafNode(
                tag="img", value="", props={"src": text_node.url, "alt": text_node.text}
            )
        case _:
            raise Exception("Not a valid type")


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
