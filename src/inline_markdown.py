import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """Split nodes by a delimiter"""
    new_nodes = list()
    for node in old_nodes:
        parts = node.text.split(delimiter)

        toggle = node.text.startswith(delimiter)

        for part in parts:
            if part:
                new_node = TextNode(part, text_type if toggle else node.text_type)
                new_nodes.append(new_node)
            toggle = not toggle

    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)

    for match in matches:
        if len(match) != 2:
            raise ValueError("Invalid image markdown")

    return matches


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)

    for match in matches:
        if len(match) != 2:
            raise ValueError("Invalid link")
        
    return matches

def split_nodes_image(old_nodes):
    new_nodes = list()
    for node in old_nodes:
        matches = extract_markdown_images(node.text)
        remaining_text = node.text
        for match in matches:
            markdown_image_str = f"![{match[0]}]({match[1]})"
            parts = remaining_text.split(markdown_image_str, 1)

            # add the text before the image if not empty
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))
            new_nodes.append(TextNode(match[0], TextType.IMAGE, match[1]))
            remaining_text = parts[1]
        
        # add the remaining text if not empty
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))

        return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = list()
    for node in old_nodes:
        matches = extract_markdown_links(node.text)
        remaining_text = node.text
        for match in matches:
            markdown_link_str = f"[{match[0]}]({match[1]})"
            parts = remaining_text.split(markdown_link_str, 1)

            # add the text before the link if not empty
            if parts[0] != "":
                new_nodes.append(TextNode(parts[0], TextType.NORMAL))
            new_nodes.append(TextNode(match[0], TextType.LINK, match[1]))
            remaining_text = parts[1]
        
        # add the remaining text if not empty
        if remaining_text != "":
            new_nodes.append(TextNode(remaining_text, TextType.NORMAL))

        return new_nodes


def reconstruct_markdown_image_str(text, url):
    return f"![{text}]({url})"