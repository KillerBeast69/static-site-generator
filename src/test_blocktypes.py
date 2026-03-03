import unittest
# Make sure to import your function and Enum
from blocktypes import block_to_block_type, BlockType 

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        
        block = "```\ncode block\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        
        block = ">quote\n>more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
        
    def test_block_to_block_type_edge_cases(self):
        # Paragraph instead of heading because no space after #
        block = "####### invalid heading"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

        # Paragraph instead of ordered list because it skips a number
        block = "1. list\n3. items"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()