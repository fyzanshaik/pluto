from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag,value,[],props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return self.value
        if self.props is not None:
            attribute_string = " ".join(f'{key}="{value}"' for key, value in self.props.items())
            return f"<{self.tag} {attribute_string}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"