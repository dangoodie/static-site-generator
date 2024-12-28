import unittest

from inline_markdown import *
from textnode import TextNode, TextType


class TestInlineMarkdown(unittest.TestCase):
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

    def test_extract_markdown_images(self):
        """Test extraction from markdown of a single image"""
        text = "![alt text](https://www.google.com)"
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 1)
        self.assertEqual(images[0], ("alt text", "https://www.google.com"))

    def test_extract_markdown_images_multiple(self):
        """Test extraction from markdown of multiple images"""
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 2)
        self.assertEqual(images[0], ("rick roll", "https://i.imgur.com/aKaOqIh.gif"))
        self.assertEqual(images[1], ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg"))

    def test_extract_markdown_images_no_images(self):
        """Test extraction from markdown with no images"""
        text = "This is text with no images"
        images = extract_markdown_images(text)
        self.assertEqual(len(images), 0)

    def test_extract_markdown_link(self):
        """Test extraction from markdown of a single image"""
        text = "[my website](https://dangoodie.github.io)"
        links = extract_markdown_links(text)
        self.assertEqual(len(links), 1)
        self.assertEqual(links[0], ("my website", "https://dangoodie.github.io"))

    def test_extract_markdown_links_multiple(self):
        """Test extraction from markdown of multiple images"""
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        self.assertEqual(len(links), 2)
        self.assertEqual(links[0], ("to boot dev", "https://www.boot.dev"))
        self.assertEqual(
            links[1], ("to youtube", "https://www.youtube.com/@bootdotdev")
        )

    def test_extract_markdown_links_no_links(self):
        """Test extraction from markdown with no images"""
        text = "This is text with no links"
        links = extract_markdown_links(text)
        self.assertEqual(len(links), 0)


if __name__ == "__main__":
    unittest.main()
