class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if self.props is None:
            return ""
        return_string = ""
        for k in self.props:
            return_string = f'{return_string} {k}="{self.props[k]}"'
        return return_string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, kids: {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.children != None:
            raise ValueError("No children allowed")
        if self.value is None:
            raise ValueError("You need a value")
        if self.tag == None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        if not tag:
            raise ValueError("Tag required")
        if not children:
            raise ValueError("You cant come to chuck e cheese without a child")
        super().__init__(tag, children=children)       
    
    def to_html(self):
        horrificstringofchildren = ''.join(sacrifice.to_html() for sacrifice in self.children)
        return f"<{self.tag}>{horrificstringofchildren}</{self.tag}>"
    
    def __repr__(self):
        return f'ParentNode({self.tag}, {self.children}, {self.props})'

