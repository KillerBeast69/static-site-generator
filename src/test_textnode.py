#this is where i write our test cases for the TextNode class
import unittest

from textnode import TextNode, TextType


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

if __name__ == "__main__":
    unittest.main()
