from enum import Enum


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
    