from enum import Enum
from leafnode import LeafNode

class TextType(Enum):
    PLAIN = "plain"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    #Constructor
    def __init__(self, TEXT,TEXT_TYPE:TextType,URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL
    
    #Compare TextNode objects if equal return True
    def __eq__(self, value):
        if (self.text == value.text and self.text_type == value.text_type and self.url == value.url):
            return True
        return False

    #Returns a string representation of TextNode in format:  TextNode(TEXT, TEXT_TYPE, URL)
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    


def text_node_to_html_node(text_node: TextNode):
    text_type = text_node.text_type
    match text_type:
        case TextType.PLAIN:
            return LeafNode(None,text_node.text)
        case TextType.BOLD:
            return LeafNode('b',text_node.text)
        case TextType.ITALIC:
            return LeafNode('i',text_node.text)
        case TextType.CODE:
            return LeafNode('code',text_node.text)
        case TextType.LINK:
            return LeafNode('a',text_node.text,{'href':text_node.url})
        case TextType.IMAGE:
           src = text_node.url
           if src.startswith("/"):
                src = "." + src
                return LeafNode('img', "", {'src': src, 'alt': text_node.text})
        case _:
            raise Exception("Invalid Text Type")
          
    