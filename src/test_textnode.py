import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_2(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.ITALIC, None)
        self.assertEqual(node, node2)

    def test_eq_3(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = TextNode("This is a text node", TextType.NORMAL, None)
        self.assertEqual(node, node2)

    def test_ne(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_eq_link(self):
        node = TextNode(
            "This is a text node", TextType.LINK, "https://www.google.com"
        )
        node2 = TextNode(
            "This is a text node", TextType.LINK, "https://www.google.com"
        )
        self.assertEqual(node, node2)

    def test_ne_link(self):
        node = TextNode(
            "This is a text node", TextType.LINK, "https://www.google.com"
        )
        node2 = TextNode(
            "This is a text node", TextType.LINK, "https://www.facebook.com"
        )
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
