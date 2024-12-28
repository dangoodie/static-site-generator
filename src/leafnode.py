from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value is None:
            raise ValueError("LeafNode value cannot be empty")
        super().__init__(value=value, tag=tag, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode value cannot be empty")
        if self.tag == None or self.tag == "":
            return f"{self.value}"
        else:
            props_html = self.props_to_html() if self.props else ""
            return f"<{self.tag}{props_html}>{self.value}</{self.tag}>"
