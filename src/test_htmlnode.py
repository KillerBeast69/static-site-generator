import unittest 

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_none(self):
        # Case 1: Test when props is completely omitted (defaults to None)
        node = HTMLNode(tag="p", value="hello world")
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_empty_dict(self):
        # Case 2: Test when props is an empty dictionary
        node = HTMLNode(tag="p", value="Hello World", props={})
        self.assertEqual(node.props_to_html(), "")

    def test_props_to_html_single_prop(self):
        # Case 3: Test with exactly one property
        node = HTMLNode(
            tag="a", 
            value="Click me", 
            props={"href": "https://youtube.com"}
        )
        self.assertEqual(node.props_to_html(), ' href="https://youtube.com"')

    def test_props_to_html_multiple_props(self):
        # Case 4: Test with multiple properties 
        node = HTMLNode(
            tag="a", 
            value="Click me", 
            props={
                "href": "https://youtube.com", 
                "target": "_blank",
                "class": "primary-link"
            }
        )

        expected_string = ' href="https://youtube.com" target="_blank" class="primary-link"'
        self.assertEqual(node.props_to_html(), expected_string)

if __name__ == "__main__":
    unittest.main()