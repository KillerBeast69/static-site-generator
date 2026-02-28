from textnode import TextType, TextNode

def main():
    text_node_object = TextNode("This is some anchor text", "link", "https://www.boot.dev")
    print(text_node_object.__repr__)    


if __name__ == "__main__":
    main()