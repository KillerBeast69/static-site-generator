import unittest

from leafnode import LeafNode
from htmlnode import HTMLNode

class TestLeadNode(unittest.TestCase):

    def test_leaf_to_html_p(self):
        # case 0
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_props(self):
        # Case 1: Standard tag with no properties
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_no_tag(self):
        # Case 2: No tag, should just return the raw text value
        node = LeafNode(None, "Just some raw text!")
        self.assertEqual(node.to_html(), "Just some raw text!")

    def test_to_html_with_props(self):
        # Case 3: Tag with properties
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_no_value(self):
        # Case 4: Missing value should raise a ValueError
        node = LeafNode("p", None)
        # We use assertRaises to verify the error is triggered
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()