import unittest
from markdown_to_html import markdown_to_html_node


class TestMarkdownToHTML(unittest.TestCase):

    def test_paragraph_simple(self):
        markdown = "This is a simple paragraph."
        expected_html = "<div><p>This is a simple paragraph.</p></div>"
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, expected_html)

    def test_paragraph_with_inline_markdown(self):
        markdown = "This is a *italic* and **bold** paragraph."
        expected_html = (
            "<div><p>This is a <i>italic</i> and <b>bold</b> paragraph.</p></div>"
        )
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, expected_html)

    def test_heading(self):
        markdown = "# Heading 1"
        expected_html = "<div><h1>Heading 1</h1></div>"
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, expected_html)

    def test_heading_with_inline_markdown(self):
        markdown = "## This is a **bold** heading"
        expected_html = "<div><h2>This is a <b>bold</b> heading</h2></div>"
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, expected_html)

    def test_code_single_line(self):
        markdown = """```
print(\"Hello, World!\")
```"""
        expected_html = '<div><pre><code>\nprint("Hello, World!")\n</code></pre></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, expected_html)

    def test_code_multi_line(self):
        markdown = """```
def hello():
    print(\"Hello, World!\")
```"""
        expected_html = '<div><pre><code>\ndef hello():\n    print("Hello, World!")\n</code></pre></div>'
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, expected_html)

    def test_blockquote(self):
        markdown = "> This is a blockquote."
        expected_html = "<div><blockquote>This is a blockquote.</blockquote></div>"
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, expected_html)

    def test_blockquote_multi_line(self):
        markdown = "> This is a blockquote.\n> It spans multiple lines."
        expected_html = "<div><blockquote>This is a blockquote.\n It spans multiple lines.</blockquote></div>"
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, expected_html)

    def test_unordered_list(self):
        markdown = "- Item 1\n- Item 2"
        expected_html = "<div><ul><li>Item 1</li><li>Item 2</li></ul></div>"
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, expected_html)

    def test_ordered_list(self):
        markdown = "1. First Item\n2. Second Item"
        expected_html = "<div><ol><li>First Item</li><li>Second Item</li></ol></div>"
        result = markdown_to_html_node(markdown).to_html()
        self.assertEqual(result, expected_html)

    def test_mixed_content(self):
        markdown = """# Heading 1

This is a paragraph with *italic* and **bold** text.

- Item 1
- Item 2

> This is a blockquote.

```
def hello():
    print(\"Hello, World!\")
```"""
        expected_html = """<div><h1>Heading 1</h1><p>This is a paragraph with <i>italic</i> and <b>bold</b> text.</p><ul><li>Item 1</li><li>Item 2</li></ul><blockquote>This is a blockquote.</blockquote><pre><code>
def hello():
    print("Hello, World!")
</code></pre></div>"""

        result = markdown_to_html_node(markdown).to_html()
        print()
        print(result)
        print()
        self.assertEqual(result, expected_html)


if __name__ == "__main__":
    unittest.main()
