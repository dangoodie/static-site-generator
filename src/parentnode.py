from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        if tag == None or tag == "":
            raise ValueError("Parent Node requires a tag")
        if children == None or not children:
            raise ValueError("Parent Node requires children")
    
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None or self.tag == "":
            raise ValueError("Parent Node requires a tag")
        if self.children == None or not self.children:
            raise ValueError("Parent Node requires children")
        
        inner_html = list()
        for child in self.children:
            inner_html.append(child.to_html())
        
        props_html = self.props_to_html() if self.props else ""
        return f"<{self.tag}{props_html}>{"".join(inner_html)}</{self.tag}>"

