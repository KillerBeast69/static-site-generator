import unittest
from markdowntoblocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
    """
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
            )

        def test_markdown_to_blocks_excessive_newlines(self):
        # Tests if the function successfully drops empty blocks 
        # caused by more than two newlines in a row
            md = """This is a block.



This is another block with too many blank lines above it."""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is a block.",
                    "This is another block with too many blank lines above it.",
                ],
            )

        def test_markdown_to_blocks_empty_string(self):
            # Tests if a string of pure whitespace/newlines correctly returns an empty list
            md = "   \n\n  \n \n   "
            blocks = markdown_to_blocks(md)
            self.assertEqual(blocks, [])

        def test_markdown_to_blocks_single_block(self):
            # Tests if a single line without any double newlines is handled properly
            md = "Just one single block here with trailing spaces.   "
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks, 
                ["Just one single block here with trailing spaces."]
            )

if __name__ == "__main__":
    unittest.main()