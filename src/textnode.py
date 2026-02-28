from enum import Enum

class TextType(Enum):
    PLAIN = "text (plain)"
    BOLD = "**Bold text**"
    ITALIC = "_Italic text_"
    CODE = "`Code text`"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        #returns true if all the properties of self and other are equal
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):        
        #returns a string representaion of the TextNode object
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

    



