import unittest

from textnode import *
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        """Test equality of two TextNode objects."""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        """Test equality of two TextNode objects with None as the link."""
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertEqual(node, node2)

    def test_eq_3(self):
        """Test equality of two TextNode objects with None as the link."""
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL, None)
        self.assertEqual(node, node2)

    def test_ne(self):
        """Test inequality of two TextNode objects."""
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_link(self):
        """Test equality of two TextNode objects with a link."""
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        self.assertEqual(node, node2)

    def test_ne_link(self):
        """Test inequality of two TextNode objects with different links."""
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        node2 = TextNode(
            "This is a text node", TextType.LINK, "https://www.facebook.com"
        )
        self.assertNotEqual(node, node2)

    def test_normal_text_node_to_html_node(self):
        """Test the conversion of normal TextNode to HTMLNode"""
        text_node = TextNode("This is a normal text node", TextType.NORMAL)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(isinstance(html_node, LeafNode), True)
        self.assertEqual(html_node.tag, "")
        self.assertEqual(html_node.value, "This is a normal text node")
        self.assertEqual(html_node.props, {})
        self.assertEqual(html_node.children, [])

    def test_bold_text_node_to_html_node(self):
        """Test the conversion of bold TextNode to HTMLNode"""
        text_node = TextNode("This is a bold text node", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(isinstance(html_node, LeafNode), True)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold text node")
        self.assertEqual(html_node.props, {})
        self.assertEqual(html_node.children, [])

    def test_italic_text_node_to_html_node(self):
        """Test the conversion of italic TextNode to HTMLNode"""
        text_node = TextNode("This is an italic text node", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(isinstance(html_node, LeafNode), True)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic text node")
        self.assertEqual(html_node.props, {})
        self.assertEqual(html_node.children, [])

    def test_code_text_node_to_html_node(self):
        """Test the conversion of code TextNode to HTMLNode"""
        text_node = TextNode("This is a code text node", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(isinstance(html_node, LeafNode), True)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code text node")
        self.assertEqual(html_node.props, {})
        self.assertEqual(html_node.children, [])

    def test_link_text_node_to_html_node(self):
        """Test the conversion of link TextNode to HTMLNode"""
        text_node = TextNode(
            "This is a link text node", TextType.LINK, "https://www.google.com"
        )
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(isinstance(html_node, LeafNode), True)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link text node")
        self.assertEqual(html_node.props, {"href": "https://www.google.com"})
        self.assertEqual(html_node.children, [])

    def test_image_text_node_to_html_node(self):
        """Test the conversion of image TextNode to HTMLNode"""
        text_node = TextNode("This is an image text node", TextType.IMAGE, "image.jpg")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual(isinstance(html_node, LeafNode), True)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props, {"src": "image.jpg", "alt": "This is an image text node"}
        )
        self.assertEqual(html_node.children, [])

    def test_split_nodes_bold_delimiter(self):
        """Test splitting of nodes by a bold delimiter."""
        old_nodes = [TextNode("This is a **bold** text node", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is a ", TextType.NORMAL))
        self.assertEqual(new_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(" text node", TextType.NORMAL))

    def test_split_nodes_italic_delimiter(self):
        """Test splitting of nodes by an italic delimiter."""
        old_nodes = [TextNode("This is an *italic* text node", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(old_nodes, "*", TextType.ITALIC)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is an ", TextType.NORMAL))
        self.assertEqual(new_nodes[1], TextNode("italic", TextType.ITALIC))
        self.assertEqual(new_nodes[2], TextNode(" text node", TextType.NORMAL))

    def test_split_nodes_code_delimiter(self):
        """Test splitting of nodes by a code delimiter."""
        old_nodes = [TextNode("This is a `code` text node", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(old_nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0], TextNode("This is a ", TextType.NORMAL))
        self.assertEqual(new_nodes[1], TextNode("code", TextType.CODE))
        self.assertEqual(new_nodes[2], TextNode(" text node", TextType.NORMAL))

    def test_split_nodes_multiple_delimiter(self):
        """Test splitting of nodes by multiple delimiters."""
        old_nodes = [
            TextNode(
                "This is a **bold** and *italic* text node with `code in it` also.",
                TextType.NORMAL,
            )
        ]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "*", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        self.assertEqual(len(new_nodes), 7)
        self.assertEqual(new_nodes[0], TextNode("This is a ", TextType.NORMAL))
        self.assertEqual(new_nodes[1], TextNode("bold", TextType.BOLD))
        self.assertEqual(new_nodes[2], TextNode(" and ", TextType.NORMAL))
        self.assertEqual(new_nodes[3], TextNode("italic", TextType.ITALIC))
        self.assertEqual(new_nodes[4], TextNode(" text node with ", TextType.NORMAL))
        self.assertEqual(new_nodes[5], TextNode("code in it", TextType.CODE))
        self.assertEqual(new_nodes[6], TextNode(" also.", TextType.NORMAL))

    def test_split_nodes_no_delimiter(self):
        """Test splitting of nodes by a delimiter that doesn't exist."""
        old_nodes = [TextNode("This is a text node", TextType.NORMAL)]
        new_nodes = split_nodes_delimiter(old_nodes, "**", TextType.BOLD)
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0], TextNode("This is a text node", TextType.NORMAL))


if __name__ == "__main__":
    unittest.main()
