import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        """Test a basic leaf node"""
        node = LeafNode("p", "This is a paragraph of text.")
        value = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), value)

    def test_to_html2(self):
        """Test a leaf node with a prop"""
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        value = "<a href='https://www.google.com'>Click me!</a>"
        self.assertEqual(node.to_html(), value)

    def test_to_html3(self):
        """Test a leaf node with text only"""
        node = LeafNode(None, "This is a text only node.")
        value = "This is a text only node."
        self.assertEqual(node.to_html(), value)

    def test_value2(self):
        """Test that an error is raised when there is no value"""
        with self.assertRaises(ValueError):
            LeafNode(None, None)


if __name__ == "__main__":
    unittest.main()
