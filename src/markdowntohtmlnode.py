from textnode import text_node_to_html_node, TextNode, TextType
from texttotextnodes import text_to_textnodes
from parentnode import ParentNode
from leafnode import LeafNode
from markdowntoblocks import markdown_to_blocks
from blocktypes import block_to_block_type, BlockType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    final_nodes = []

    for block in blocks:
        block_type = block_to_block_type(block)

        match block_type:
            case BlockType.PARAGRAPH:
                final_nodes.append(paragraph_to_html_node(block))
            case BlockType.HEADING:
                final_nodes.append(heading_to_html_node(block))
            case BlockType.CODE:
                final_nodes.append(code_to_html_node(block))
            case BlockType.QUOTE:
                final_nodes.append(quote_to_html(block))
            case BlockType.UNORDERED_LIST:
                final_nodes.append(unordered_list_to_html_node(block))
            case BlockType.ORDERED_LIST:
                final_nodes.append(ordered_list_to_node(block))
            case _:
                raise Exception("invalid case")
    return ParentNode("div", final_nodes)


def text_to_children(text):
    text_nodes = text_to_textnodes(text)

    html_nodes = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        html_nodes.append(html_node)

    return html_nodes

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)

    children = text_to_children(paragraph)

    return ParentNode("p", children)

def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break

    text = block[level + 1:]

    children = text_to_children(text)

    return ParentNode(f"h{level}", children)

def quote_to_html(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        new_lines.append(line.lstrip(">").strip())
    
    final_text = " ".join(new_lines)
    children = text_to_children(final_text)

    return ParentNode("blockquote", children)

def unordered_list_to_html_node(block):
    lines = block.split("\n")
    final_list = []
    for line in lines:
        text = line[2:]
        children = text_to_children(text)
        final_list.append(ParentNode("li", children))

    return ParentNode("ul", final_list)

def ordered_list_to_node(block):
    lines = block.split("\n")
    final_list = []
    for line in lines:
        text = line.split(" ", 1)[1]
        children = text_to_children(text)
        final_list.append(ParentNode("li", children))

    return ParentNode("ol", final_list)

def code_to_html_node(block):
    text = block[4:-3]

    text_node = TextNode(text, TextType.PLAIN)

    html_node = text_node_to_html_node(text_node)

    code_node = ParentNode("code", [html_node])

    return ParentNode("pre", [code_node])
    