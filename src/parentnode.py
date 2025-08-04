from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children,props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag if missing for Parent node")
        if not self.children:
            raise ValueError("Children Nodes are missing for Parent Node")
        
        allChildren = ""
        for child in self.children:
            allChildren += child.to_html()
        
        return f"<{self.tag}>{allChildren}</{self.tag}>"
        
        
        