import os

from blocks_markdown import *
from markdown_to_html import markdown_to_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)

    for block in blocks:
        if block_to_block_type(block) != BlockType.HEADING:
            continue

        num_hashes = len(block) - len(block.lstrip("#"))
        if num_hashes == 1:
            return block.lstrip("#").strip()

    raise Exception("No header! Please include H1 level header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Open files and extract text
    with open(from_path, "r", encoding="utf-8") as markdown_file:
        markdown = markdown_file.read()

    with open(template_path, "r", encoding="utf-8") as template_file:
        template = template_file.read()


    # Convert to html and extract the title
    converted_html = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)

    # Replace placeholders
    page_html_string = template.replace(r"{{ Title }}", title).replace(r"{{ Content }}", converted_html)

    file_name = os.path.splitext(os.path.basename(from_path))[0]
    output_file_path = os.path.join(dest_path, f"{file_name}.html")

    with open(output_file_path, "w", encoding="utf-8") as page:
        page.write(page_html_string)

    print(f"Page successfully generated at: {output_file_path}")


