from blocks_markdown import *
from parentnode import ParentNode
from leafnode import LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node



def markdown_to_html_node(markdown):
    # break the markdown into blocks
    blocks = markdown_to_blocks(markdown)

    html_nodes = list()

    # loop over the blocks
    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                node = process_paragraph(block)
                html_nodes.append(node)
            case BlockType.HEADING:
                node = process_heading(block)
                html_nodes.append(node)
            case BlockType.CODE:
                node = process_code(block)
                html_nodes.append(node)
            case BlockType.QUOTE:
                node = process_quote(block)
                html_nodes.append(node)
            case BlockType.UNORDERED_LIST:
                node = process_ul(block)
                html_nodes.append(node)
            case BlockType.ORDERED_LIST:
                node = process_ol(block)
                html_nodes.append(node)
            case _:
                raise Exception("Error parsing block")

    return ParentNode(tag="div", children=html_nodes)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)

    children = list()
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)

    return children


def process_paragraph(text):
    return ParentNode(tag="p", children=text_to_children(text))

def process_heading(text):
    num_hashes = len(text) - len(text.lstrip("#"))
    heading_level = min(num_hashes, 6)

    heading_content = text.lstrip("#").strip()

    return ParentNode(tag=f"h{heading_level}", children=text_to_children(heading_content))

def process_code(text):
    code_content = text.strip("```")

    code_block = LeafNode(tag="code", value=code_content)
    return ParentNode(tag="pre", children=[code_block])

def process_quote(text):
    lines = [line.lstrip(">") for line in text.split("\n")]
    quote_content = "\n".join(lines).strip()
    return ParentNode(tag="blockquote", children=text_to_children(quote_content))
        

def process_ul(text):
    lines = text.split("\n")
    children = list()
    for line in lines:
        line = line.lstrip("* ").lstrip("- ")
        node = ParentNode(tag="li", children=text_to_children(line))
        children.append(node)

    return ParentNode(tag="ul", children=children)

def process_ol(text):
    lines = text.split("\n")
    children = list()
    for line in lines:
        line = line.lstrip("0123456789. ")
        node = ParentNode(tag="li", children=text_to_children(line))
        children.append(node)

    return ParentNode(tag="ol", children=children)