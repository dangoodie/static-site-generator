import unittest

from generate_page import *

class TestGeneratePage(unittest.TestCase):
    def test_extract_title(self):
        markdown = "# Hello"
        title = "Hello"

        result = extract_title(markdown)

        self.assertEqual(title, result)

    def test_extract_title_exception(self):
        with self.assertRaises(Exception) as context:
            markdown = "## This is not a proper title"
            result = extract_title(markdown)

        self.assertEqual(str(context.exception), "No header! Please include H1 level header")

