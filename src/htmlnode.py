class HTMLNode:
    # represents a "node" in HTML document tree 
    # it can be block level or inline, and it is designed to only output HTML

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        # a string representing the HTML tag name
        self.value = value
        # a string representing the value of the HTML
        self.children = children
        # a list of HTML node objects representing the children of this node
        self.props = props
        # a dict of key value pairs representing the attributes of the HTML tag

    def to_html(self):
        # child classes will override this method to render themselves as HTMl
        raise NotImplementedError

    def props_to_html(self):
        # returns a formatted string representing the HTML attributes of the node
        if not self.props or self.props is None:
            return f""
        return "".join(f' {k}="{v}"' for k, v in self.props.items())

    def __repr__(self):
        # a way to print HTMl node
        return f"tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props}"

    