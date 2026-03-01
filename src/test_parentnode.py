import unittest

from parentnode import ParentNode
from leafnode import LeafNode
from htmlnode import HTMLNode

class TestParentNode(unittest.TestCase):
    
    def test_to_html_with_children(self):
        # Case 1: A parent with standard leaf node children
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_to_html_with_grandchildren(self):
        # Case 2: A parent whose children are ALSO parents (testing recursion)
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_props(self):
        # Case 3: A parent node that has properties
        node = ParentNode(
            "div",
            [LeafNode("p", "Hello")],
            {"class": "container"}
        )
        self.assertEqual(
            node.to_html(),
            '<div class="container"><p>Hello</p></div>'
        )

    def test_to_html_missing_tag(self):
        # Case 4: Parent missing a tag
        node = ParentNode(None, [LeafNode("p", "Hello")])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html_missing_children(self):
        # Case 5: Parent missing children
        node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            node.to_html()

if __name__ == "__main__":
    unittest.main()