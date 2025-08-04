import unittest
from util import markdown_to_blocks
class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = (
            "This is **bolded** paragraph\n\n"
            "This is another paragraph with _italic_ text and `code` here\n"
            "This is the same paragraph on a new line\n\n"
            "- This is a list\n"
            "- with items\n"
        )
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_leading_and_trailing_newlines(self):
        md = "\n\nFirst block\n\nSecond block\n\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["First block", "Second block"])

    def test_multiple_blank_lines(self):
        md = "Block 1\n\n\n\nBlock 2\n\n\nBlock 3"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Block 1", "Block 2", "Block 3"])

    def test_empty_string(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_only_blank_lines(self):
        md = "\n\n\n"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

if __name__ == "__main__":
    unittest.main()