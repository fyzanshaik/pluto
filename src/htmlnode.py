class HTMLNode():
    """
    tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
    value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
    children - A list of HTMLNode objects representing the children of this node
    props - A dictionary of key-value pairs representing the attributes of the HTML tag. For example, a link (<a> tag) might have {"href": "https://www.google.com"}
    """
    def __init__(self, tag:str = None, value:str = None, children: list = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props = self.props
        return f' href="{props.href}" anchor="{props.target}"'
    
    def __eq__(self, value):
        if(self.tag == value.tag and self.value == value.value):
            return True
        return False
    
    def __repr__(self):
        tag = self.tag
        value = self.value
        children = self.children
        props = self.props
        
        print("HTML Node: ")
        print(f"Tag: {tag}")
        print(f"Value: {value}")
        print("Children: ")
        for child in children:
            print(child,end=" ")
        print("Props: ")
        for prop in props:
            print(prop)
    
        
     
        