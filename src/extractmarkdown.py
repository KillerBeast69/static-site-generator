import re
from textnode import TextType, TextNode

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    return re.findall(pattern, text)

def split_nodes_image(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_list.append(node)
            continue
        list_of_tuples = extract_markdown_images(node.text)
        if not list_of_tuples:
            new_list.append(node)
            continue
        orignal_text = node.text
        for tup in list_of_tuples:
            alt, link = tup
            sections = orignal_text.split(f"![{alt}]({link})", 1)
            
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")

            if sections[0]:
                new_list.append(TextNode(sections[0], TextType.PLAIN))

            new_list.append(TextNode(alt, TextType.IMAGE, link))
            orignal_text = sections[1]
        if orignal_text:
            new_list.append(TextNode(orignal_text, TextType.PLAIN))

    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_list.append(node)
            continue
        list_of_tuples = extract_markdown_links(node.text)
        if not list_of_tuples:
            new_list.append(node)
            continue
        orignal_text = node.text
        for tup in list_of_tuples:
            alt, link = tup
            sections = orignal_text.split(f"[{alt}]({link})", 1)
            
            if len(sections) != 2:
                raise ValueError("Invalid markdown, link section not closed")

            if sections[0]:
                new_list.append(TextNode(sections[0], TextType.PLAIN))

            new_list.append(TextNode(alt, TextType.LINK, link))
            orignal_text = sections[1]
        if orignal_text:
            new_list.append(TextNode(orignal_text, TextType.PLAIN))

    return new_list