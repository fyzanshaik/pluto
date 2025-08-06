import unittest
from textnode import TextNode, TextType
from util import split_nodes_delimiter  

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_split(self):
        node = TextNode("This is `code` text", TextType.PLAIN)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.PLAIN),
        ]
        self.assertEqual(result, expected)

    def test_no_delimiter(self):
        node = TextNode("No code here", TextType.PLAIN)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("No code here", TextType.PLAIN)]
        self.assertEqual(result, expected)

    def test_multiple_delimiters(self):
        node = TextNode("A `b` c `d` e", TextType.PLAIN)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("A ", TextType.PLAIN),
            TextNode("b", TextType.CODE),
            TextNode(" c ", TextType.PLAIN),
            TextNode("d", TextType.CODE),
            TextNode(" e", TextType.PLAIN),
        ]
        self.assertEqual(result, expected)

    def test_unmatched_delimiter_raises(self):
        node = TextNode("A `b c", TextType.PLAIN)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_non_plain_node(self):
        node = TextNode("bold", TextType.BOLD)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [TextNode("bold", TextType.BOLD)]
        self.assertEqual(result, expected)

    def test_empty_string(self):
        node = TextNode("", TextType.PLAIN)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = []
        self.assertEqual(result, expected)

    def test_delimiter_at_start_and_end(self):
        node = TextNode("`code`", TextType.PLAIN)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("code", TextType.CODE),
        ]
        self.assertEqual(result, expected)

    def test_delimiter_with_empty_between(self):
        node = TextNode("``", TextType.PLAIN)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = []
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()