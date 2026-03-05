import os
import shutil
from textnode import TextType, TextNode

def main():
    source = "static"
    destination = "public"

    print("beginning static site generation")
    clean_and_copy(source, destination)
    print("finished copying static files!")


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

if __name__ == "__main__":
    main()