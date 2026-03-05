import os
import shutil
import string
import pathlib
from textnode import TextType, TextNode
from markdowntohtmlnode import markdown_to_html_node
from htmlnode import HTMLNode

def main():
    source = "static"
    destination = "public"

    print("beginning static site generation")
    clean_and_copy(source, destination)
    print("finished copying static files!")

    from_path = "content"
    template_path = "template.html"
    dest_path = "public"

    print("starting to generate pages recursively")
    generate_pages_recursive(from_path, template_path, dest_path)


def clean_and_copy(source_path, destination_path):
    if os.path.exists(destination_path):
        print(f"deleting existing directory: {destination_path}")
        shutil.rmtree(destination_path)

    print(f"creating fresh directory: {destination_path}")
    os.mkdir(destination_path)

    copy_recursive(source_path, destination_path)

def copy_recursive(source_path, destination_path):
    contents = os.listdir(source_path)

    for item in contents:
        src_item_path = os.path.join(source_path, item)
        dest_item_path = os.path.join(destination_path, item)

        print(f" * copying: {src_item_path} -> {dest_item_path}")

        if os.path.isfile(src_item_path):
            shutil.copy(src_item_path, dest_item_path)
        else:
            os.mkdir(dest_item_path)

            copy_recursive(src_item_path, dest_item_path)

def extract_title(markdown):
    lines = markdown.split("\n")
    
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()

    raise Exception("markdown does not conatin h1 header")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r") as f:
        from_contents = f.read()
    with open(template_path, "r") as t:
        template_contents = t.read()
    
    node = markdown_to_html_node(from_contents)
    html_string = node.to_html()

    title = extract_title(from_contents)
    
    new_template = template_contents.replace("{{ Title }}", title)
    final_template = new_template.replace("{{ Content }}", html_string)

    dest_dir_path = os.path.dirname(dest_path)
    os.makedirs(dest_dir_path, exist_ok=True)

    with open(dest_path, "w") as d:
        d.write(final_template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    for file_name in contents:
        from_path = os.path.join(dir_path_content, file_name) 
        dest_path = os.path.join(dest_dir_path, file_name)
        if os.path.isfile(from_path):
            if from_path.endswith(".md"):

                dest_path = str(pathlib.Path(dest_path).with_suffix(".html"))
                generate_page(from_path, template_path, dest_path)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

if __name__ == "__main__":
    main()