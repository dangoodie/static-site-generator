import os
from copy_static import *
from generate_page import generate_page

def main():
    project_root = get_project_root()
    source = os.path.join(project_root, "static/")
    dest = os.path.join(project_root, "public/")
    content = os.path.join(project_root, "content/")

    # Check if exists and mkdir if not
    check_dest(dest)

    # Recursively delete from the destination folder
    delete_from_dest(dest)

    # Recursively copy the source folder to the destination
    copy_source_to_dest(source, dest)

    markdown = os.path.join(content, "index.md")
    template = os.path.join(project_root, "template.html")
    generate_page(markdown, template, dest)


if __name__ == "__main__":
    main()
