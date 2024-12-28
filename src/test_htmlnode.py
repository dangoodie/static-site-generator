import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag="a", value="Google", props={"href": "https://www.google.com"}
        )
        value = " href='https://www.google.com'"
        self.assertEqual(node.props_to_html(), value)

    def test_props_to_html2(self):
        node2 = HTMLNode(
            tag="img", props={"src": "image.jpg", "alt": "description of the image"}
        )
        value2 = " src='image.jpg' alt='description of the image'"
        self.assertEqual(node2.props_to_html(), value2)

    def test_props_to_html3(self):
        node3 = HTMLNode(
            tag="input", props={"type": "text", "placeholder": "Enter your name"}
        )
        value3 = " type='text' placeholder='Enter your name'"
        self.assertEqual(node3.props_to_html(), value3)

    # Test the leading space
    def test_props_to_html_ne(self):
        node = HTMLNode(
            tag="a", value="Google", props={"href": "https://www.google.com"}
        )
        value = "href='https://www.google.com'"
        self.assertNotEqual(node.props_to_html(), value)



if __name__ == "__main__":
    unittest.main()
