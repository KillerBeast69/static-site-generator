#this is where i write our test cases for the TextNode class
import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node1, node2) #if the inputs are equal the test passes
        #self.assertNotEqual(node1, node2) #if the inputs are not equal the test passes
    
    def test_same_text_diff_type(self):
        node1 = TextNode("this is a text node", TextType.ITALIC)
        node2 = TextNode("this is a text node", TextType.PLAIN)
        #self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node2)

    def test_diff_text_same_type(self):
        node1 = TextNode("this is a text node", TextType.ITALIC)
        node2 = TextNode("this is not a text node", TextType.ITALIC)
        #self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node2)
    
    def test_both_diff(self):
        node1 = TextNode("this is a text node", TextType.ITALIC)
        node2 = TextNode("this is not a text node", TextType.BOLD)
        #self.assertEqual(node1, node2)
        self.assertNotEqual(node1, node2)

    def test_with_url(self):
        node1 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

    def test_italic(self):
        node = TextNode("This is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is italic")

    def test_code(self):
        node = TextNode("This is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is code")

    def test_link(self):
        node = TextNode("Click here", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Click here")
        self.assertEqual(html_node.props, {"href": "https://www.boot.dev"})

    def test_image(self):
        node = TextNode("An image description", TextType.IMAGE, "https://www.boot.dev/image.png")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev/image.png", "alt": "An image description"},
        )

    def test_invalid_text_type(self):
        # We test that passing an invalid type raises the exact Exception we wrote
        with self.assertRaises(Exception):
            node = TextNode("This is an invalid type", "invalid_type")
            text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
