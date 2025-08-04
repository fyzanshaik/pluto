# import unittest
# from util import markdown_to_html_node  

# class TestMarkdownToHtmlNode(unittest.TestCase):
#     def test_paragraphs(self):
#         md = """
# This is **bolded** paragraph
# text in a p
# tag here

# This is another paragraph with _italic_ text and `code` here

# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
#         )

#     def test_codeblock(self):
#         md = """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
#         )

#     def test_heading(self):
#         md = """
# # Heading 1

# ## Heading 2

# ### Heading 3
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>",
#         )

#     def test_unordered_list(self):
#         md = """
# - Item one
# - Item two
# - Item three
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><ul><li>Item one</li><li>Item two</li><li>Item three</li></ul></div>",
#         )

#     def test_ordered_list(self):
#         md = """
# 1. First
# 2. Second
# 3. Third
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>",
#         )

#     def test_blockquote(self):
#         md = """
# > This is a quote
# > that spans multiple lines
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><blockquote>This is a quote that spans multiple lines</blockquote></div>",
#         )

#     def test_mixed_blocks(self):
#         md = """
# # Title

# Some paragraph text.

# - List item 1
# - List item 2

# 1. First
# 2. Second

# > A quote
# """
#         node = markdown_to_html_node(md)
#         html = node.to_html()
#         self.assertEqual(
#             html,
#             "<div><h1>Title</h1><p>Some paragraph text.</p><ul><li>List item 1</li><li>List item 2</li></ul><ol><li>First</li><li>Second</li></ol><blockquote>A quote</blockquote></div>",
#         )
# """

# if __name__ == "__main__":
#     unittest.main()