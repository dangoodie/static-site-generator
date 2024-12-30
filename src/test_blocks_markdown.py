import unittest, textwrap

from blocks_markdown import *


class TestBlocksMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = textwrap.dedent(
            """\
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """
        )

        blocks = markdown_to_blocks(markdown)

        self.assertEqual(blocks[0], "# This is a heading")
        self.assertEqual(
            blocks[1],
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
        )
        self.assertEqual(
            blocks[2],
            """* This is the first list item in a list block\n* This is a list item\n* This is another list item""",
        )

    def test_block_to_block_type_heading(self):
        block = "###### This is a heading"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading2(self):
        block = "### "
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading3(self):
        block = "###No Space"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_heading4(self):
        block = "a ### wow"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.HEADING)

    def test_block_to_block_type_code(self):
        block = "```\nsome code\n```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_code2(self):
        block = "```just one line```"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.CODE)

    def test_block_to_block_type_quote(self):
        block = ">This is the first line\n>This is the second line"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.QUOTE)

    def test_block_to_block_type_ul(self):
        block = "- This is the first line\n- This is the second line"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ul2(self):
        block = "* This is the first line\n* This is the second line"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ul3(self):
        block = "* This is the first line\n- This is the second line"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ol(self):
        block = "1. First\n2. Second\n3. Third"
        block_type = block_to_block_type(block)
        self.assertEqual(block_type, BlockType.ORDERED_LIST)

    def test_block_to_block_type_ol2(self):
        block = "2. Second\n3. Third"
        block_type = block_to_block_type(block)
        self.assertNotEqual(block_type, BlockType.ORDERED_LIST)