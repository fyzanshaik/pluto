import unittest
from util import extract_markdown_links


class TestExtractMarkdownLinks(unittest.TestCase):
    def test_single_link(self):
        matches = extract_markdown_links(
            "This is a [link](https://example.com)"
        )
        self.assertListEqual(
            [("link", "https://example.com")], matches
        )

    def test_multiple_links(self):
        matches = extract_markdown_links(
            "[first](url1) some text [second](url2)"
        )
        self.assertListEqual(
            [("first", "url1"), ("second", "url2")], matches
        )

    def test_no_links(self):
        matches = extract_markdown_links(
            "This is just text with no links."
        )
        self.assertListEqual([], matches)

    def test_empty_anchor(self):
        matches = extract_markdown_links(
            "[](https://example.com)"
        )
        self.assertListEqual(
            [("", "https://example.com")], matches
        )

    def test_empty_url(self):
        matches = extract_markdown_links(
            "[anchor]()"
        )
        self.assertListEqual(
            [("anchor", "")], matches
        )

    # def test_special_characters(self):
    #     matches = extract_markdown_links(
    #         "[a!@#$_-+=[]{};:,.<>?~`|](http://weird.url/!@#$.png)"
    #     )
    #     self.assertListEqual(
    #         [("a!@#$_-+=[]{};:,.<>?~`|", "http://weird.url/!@#$.png")], matches
    #     )

    def test_link_at_start(self):
        matches = extract_markdown_links(
            "[start](url) and some text"
        )
        self.assertListEqual(
            [("start", "url")], matches
        )

    def test_link_at_end(self):
        matches = extract_markdown_links(
            "Some text and [end](url)"
        )
        self.assertListEqual(
            [("end", "url")], matches
        )

    def test_link_with_spaces(self):
        matches = extract_markdown_links(
            "[anchor text with spaces](https://example.com)"
        )
        self.assertListEqual(
            [("anchor text with spaces", "https://example.com")], matches
        )

    # def test_image_not_matched(self):
    #     matches = extract_markdown_links(
    #         "This is an image ![alt](https://img.com/img.png) and a [link](url)"
    #     )
    #     self.assertListEqual(
    #         [("link", "url")], matches
    #     )

if __name__ == "__main__":
    unittest.main()