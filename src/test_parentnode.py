import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_simple_children(self):
        """Test ParentNode with simple LeafNode children."""
        node = ParentNode(
            tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>Italic text</i></p>"
        self.assertEqual(node.to_html(), expected)

    def test_nested_children(self):
        """Test ParentNode with nested ParentNode as children."""
        nested_node = ParentNode(
            tag="span",
            children=[
                LeafNode("b", "Bold"),
                LeafNode(None, " and normal text"),
            ],
        )
        node = ParentNode(
            tag="div",
            children=[
                nested_node,
                LeafNode(None, "More text outside the span."),
            ],
        )
        expected = "<div><span><b>Bold</b> and normal text</span>More text outside the span.</div>"
        self.assertEqual(node.to_html(), expected)

    def test_with_attributes(self):
        """Test ParentNode with props (attributes)."""
        node = ParentNode(
            tag="section",
            props={"class": "content", "id": "main"},
            children=[
                LeafNode("h1", "Title", {"class": "heading"}),
                LeafNode("p", "This is a paragraph.", {"class": "paragraph"}),
            ],
        )
        expected = "<section class='content' id='main'><h1 class='heading'>Title</h1><p class='paragraph'>This is a paragraph.</p></section>"
        self.assertEqual(node.to_html(), expected)

    def test_empty_children(self):
        """Test ParentNode with no children."""
        with self.assertRaises(ValueError):
            node = ParentNode(tag="div", children=list())

    def test_invalid_tag(self):
        """Test ParentNode with invalid or missing tag."""
        with self.assertRaises(ValueError):
            ParentNode(tag=None, children=[]).to_html()

    def test_no_props(self):
        """Test ParentNode without any props."""
        node = ParentNode(
            tag="article",
            children=[
                LeafNode("h1", "No Props Example"),
                LeafNode("p", "This has no attributes."),
            ],
        )
        expected = (
            "<article><h1>No Props Example</h1><p>This has no attributes.</p></article>"
        )
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()
