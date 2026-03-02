import unittest
from textnode import TextNode, TextType
from splitdelimeter import split_nodes_delimiter 

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_split_code(self):
        node = TextNode("This is text with a `code block` word", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is text with a ", TextType.PLAIN),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.PLAIN),
            ]
        )

    def test_split_bold(self):
        node = TextNode("This is **bolded** text", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("This is ", TextType.PLAIN),
                TextNode("bolded", TextType.BOLD),
                TextNode(" text", TextType.PLAIN),
            ]
        )

    def test_split_italic_start_and_end(self):
        # This tests what happens when the delimiter is at the very edges
        
        node = TextNode("_italic everywhere_", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(
            new_nodes,
            [
                TextNode("italic everywhere", TextType.ITALIC),
            ]
        )

    def test_multiple_delimiters(self):
        # Tests when there are multiple of the SAME delimiter in a string
        node = TextNode("A `code` and `more code`", TextType.PLAIN)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(
            new_nodes,
            [
                TextNode("A ", TextType.PLAIN),
                TextNode("code", TextType.CODE),
                TextNode(" and ", TextType.PLAIN),
                TextNode("more code", TextType.CODE),
            ]
        )

    def test_ignores_non_plain_nodes(self):
        # Ensures that a node that is already bold doesn't get messed with
        node = TextNode("Already bold", TextType.BOLD)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(
            new_nodes,
            [
                TextNode("Already bold", TextType.BOLD),
            ]
        )

    def test_unclosed_delimiter(self):
        # Uses assertRaises to ensure your Exception actually fires
        node = TextNode("This is `unclosed", TextType.PLAIN)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

if __name__ == "__main__":
    unittest.main()