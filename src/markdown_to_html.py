from blocks_markdown import *

def markdown_to_html_node(markdown):
    # break the markdown into blocks
    blocks = markdown_to_blocks(markdown)

    html_nodes = list()
    
    # loop over the blocks
    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                pass
            case BlockType.HEADING:
                pass
            case BlockType.CODE:
                pass
            case BlockType.QUOTE:
                pass
            case BlockType.UNORDERED_LIST:
                pass
            case BlockType.ORDERED_LIST:
                pass
