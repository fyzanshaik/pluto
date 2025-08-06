import unittest
from textnode import TextNode, TextType
from util import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_full_example(self):
        text = (
            "This is **text** with an _italic_ word and a `code block` and an "
            "![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        expected = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_no_markdown(self):
        text = "Just plain text."
        expected = [TextNode("Just plain text.", TextType.PLAIN)]
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_only_bold(self):
        text = "**bold**"
        expected = [TextNode("bold", TextType.BOLD)]
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_only_italic(self):
        text = "_italic_"
        expected = [TextNode("italic", TextType.ITALIC)]
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_only_code(self):
        text = "`code`"
        expected = [TextNode("code", TextType.CODE)]
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_only_image(self):
        text = "![alt](url)"
        expected = [TextNode("alt", TextType.IMAGE, "url")]
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_only_link(self):
        text = "[anchor](url)"
        expected = [TextNode("anchor", TextType.LINK, "url")]
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_multiple_types(self):
        text = "**bold** and _italic_ and `code` and ![img](url) and [link](url)"
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" and ", TextType.PLAIN),
            TextNode("img", TextType.IMAGE, "url"),
            TextNode(" and ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "url"),
        ]
        self.assertListEqual(text_to_textnodes(text), expected)

    def test_empty_string(self):
        text = ""
        expected = []
        self.assertListEqual(text_to_textnodes(text), expected)

if __name__ == "__main__":
    unittest.main()