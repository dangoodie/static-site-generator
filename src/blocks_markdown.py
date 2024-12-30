import re
from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):

    # Split the markdown by two or more newlines
    blocks = re.split(r"\n\s*\n", markdown)

    # Remove leading and trailing whitespace from each block
    blocks = [block.strip() for block in blocks if block.strip()]

    return blocks


def block_to_block_type(block):

    # Match for headings
    heading_regex = r"^#{1,6} "
    if re.match(heading_regex, block) and len(block) > (block.find(" ") + 1):
        return BlockType.HEADING

    # Match for code blocks
    lines = block.split("\n")
    if lines[0].strip().startswith("```") and lines[-1].strip().startswith("```"):
        return BlockType.CODE

    # Match for quotes
    if all(line.strip().startswith(">") for line in lines):
        return BlockType.QUOTE

    # Match for unordered lists
    if all(line.strip().startswith("* ") or line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    # Match for ordered lists
    if all(lines[i].strip().startswith(f"{i + 1}. ") for i in range(0, len(lines))):
        return BlockType.ORDERED_LIST 

    # if none it must be paragraph!
    return BlockType.PARAGRAPH
