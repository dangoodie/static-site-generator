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
