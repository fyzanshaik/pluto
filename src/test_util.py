import unittest
from util import extract_markdown_images

class TestExtractMarkdownImages(unittest.TestCase):
    def test_single_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")], matches
        )

    def test_multiple_images(self):
        matches = extract_markdown_images(
            "![img1](url1) some text ![img2](url2)"
        )
        self.assertListEqual(
            [("img1", "url1"), ("img2", "url2")], matches
        )

    def test_no_images(self):
        matches = extract_markdown_images(
            "This is just text with no images."
        )
        self.assertListEqual([], matches)

    def test_empty_alt(self):
        matches = extract_markdown_images(
            "![  ](https://example.com/img.png)"
        )
        self.assertListEqual(
            [("  ", "https://example.com/img.png")], matches
        )

    def test_empty_url(self):
        matches = extract_markdown_images(
            "![alt text]()"
        )
        self.assertListEqual(
            [("alt text", "")], matches
        )

    # def test_special_characters(self):
    #     matches = extract_markdown_images(
    #         "![a!@#$_-+=[]{};:,.<>?~`|](http://weird.url/!@#$.png)"
    #     )
    #     self.assertListEqual(
    #         [("a!@#$_-+=[]{};:,.<>?~`|", "http://weird.url/!@#$.png")], matches
    #     )

    def test_image_at_start(self):
        matches = extract_markdown_images(
            "![start](url) and some text"
        )
        self.assertListEqual(
            [("start", "url")], matches
        )

    def test_image_at_end(self):
        matches = extract_markdown_images(
            "Some text and ![end](url)"
        )
        self.assertListEqual(
            [("end", "url")], matches
        )

    def test_image_with_spaces(self):
        matches = extract_markdown_images(
            "![alt text with spaces](https://example.com/img.png)"
        )
        self.assertListEqual(
            [("alt text with spaces", "https://example.com/img.png")], matches
        )

if __name__ == "__main__":
    unittest.main()