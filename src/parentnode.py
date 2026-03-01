from htmlnode import HTMLNode

class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag")
        if self.children is None:
            raise ValueError("children is missing value")
        string = ""
        for child in self.children:
            string += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{string}</{self.tag}>'
        
