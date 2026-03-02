from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    list_of_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            list_of_nodes.append(node)
            continue
        split_text = node.text.split(delimiter)
        if not len(split_text) % 2:
            raise Exception("Invalid markdown, formatted section not closed")
        for i in range(len(split_text)):
            if not split_text[i]:
                continue
            if i % 2:
                new_text_node = TextNode(split_text[i], text_type)
                list_of_nodes.append(new_text_node)
            else:
                new_text_node = TextNode(split_text[i], TextType.PLAIN)
                list_of_nodes.append(new_text_node)
    return list_of_nodes
            
