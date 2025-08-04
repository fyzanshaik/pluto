import re
from textnode import TextNode, TextType,text_node_to_html_node
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def extract_markdown_images(text):
    """
    Extracts all markdown images from the text.
    Returns a list of (alt, url) tuples.
    """
    regex = r'!\[([^\[\]]*)\]\(([^\(\)]*)\)'
    return re.findall(regex, text)

def extract_markdown_links(text):
    """
    Extracts all markdown links from the text (not images!).
    Returns a list of (anchor, url) tuples.
    """
    regex = r'(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)'
    return re.findall(regex, text)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    """
    Splits TextNode objects of type PLAIN in old_nodes by the given delimiter,
    creating new TextNodes of the given text_type for text between delimiters.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise Exception(
                f"Unmatched delimiter '{delimiter}' in text: {node.text}"
            )

        for i, part in enumerate(parts):
            if part == "":
                continue
            if i % 2 == 0:
                new_nodes.append(TextNode(part, TextType.PLAIN))
            else:
                new_nodes.append(TextNode(part, text_type))
    return new_nodes

def split_nodes_image(old_nodes):
    """
    Splits TextNode objects of type PLAIN in old_nodes by markdown images,
    creating new TextNodes of type IMAGE for each image found.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        text = node.text
        images = extract_markdown_images(text)
        if not images:
            if text:
                new_nodes.append(node)
            continue

        curr_text = text
        for alt, url in images:
            image_md = f"![{alt}]({url})"
            sections = curr_text.split(image_md, 1)
            before = sections[0]
            after = sections[1] if len(sections) > 1 else ""

            if before:
                new_nodes.append(TextNode(before, TextType.PLAIN))
            new_nodes.append(TextNode(alt, TextType.IMAGE, url))
            curr_text = after

        if curr_text:
            new_nodes.append(TextNode(curr_text, TextType.PLAIN))

    return [node for node in new_nodes if node.text]

def split_nodes_link(old_nodes):
    """
    Splits TextNode objects of type PLAIN in old_nodes by markdown links,
    creating new TextNodes of type LINK for each link found.
    """
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            new_nodes.append(node)
            continue

        text = node.text
        links = extract_markdown_links(text)
        if not links:
            if text:
                new_nodes.append(node)
            continue

        curr_text = text
        for anchor, url in links:
            link_md = f"[{anchor}]({url})"
            sections = curr_text.split(link_md, 1)
            before = sections[0]
            after = sections[1] if len(sections) > 1 else ""

            if before:
                new_nodes.append(TextNode(before, TextType.PLAIN))
            new_nodes.append(TextNode(anchor, TextType.LINK, url))
            curr_text = after

        if curr_text:
            new_nodes.append(TextNode(curr_text, TextType.PLAIN))

    return [node for node in new_nodes if node.text]

def text_to_textnodes(text):
    """
    Converts a markdown string to a list of TextNode objects,
    splitting by images, links, code, bold, and italic in the correct order.
    """

    nodes = [TextNode(text, TextType.PLAIN)]

    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)

    return [node for node in nodes if node.text]

def markdown_to_blocks(markdown):
    """
    Splits a markdown document into blocks separated by one or more blank lines.
    Strips leading/trailing whitespace from each block and removes empty blocks.
    """
    potential_blocks = markdown.split('\n\n')
    blocks = []
    for block in potential_blocks:
        stripped_block = block.strip()
        if stripped_block != "":
            blocks.append(stripped_block)
    return blocks


def block_to_block_type(block):
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE

    if block.startswith("#"):
        i = 0
        while i < len(block) and block[i] == "#":
            i += 1
        if 1 <= i <= 6 and i < len(block) and block[i] == " ":
            return BlockType.HEADING

    lines = block.split("\n")

    is_quote = True
    for line in lines:
        if not line.startswith(">"):
            is_quote = False
            break
    if is_quote:
        return BlockType.QUOTE

    is_unordered = True
    for line in lines:
        if not line.startswith("- "):
            is_unordered = False
            break
    if is_unordered:
        return BlockType.UNORDERED_LIST

    is_ordered = True
    for idx, line in enumerate(lines):
        expected_prefix = f"{idx+1}. "
        if not line.startswith(expected_prefix):
            is_ordered = False
            break
    if is_ordered and len(lines) > 0:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType
from enum import Enum


def text_to_children(text):
    """
    Converts a string of markdown text to a list of HTMLNode children,
    handling inline markdown (bold, italic, code, links, images).
    """
    text_nodes = text_to_textnodes(text)
    children = []
    for node in text_nodes:
        html_node = text_node_to_html_node(node)
        children.append(html_node)
    return children

def block_to_html_node(block, block_type):
    """
    Converts a markdown block and its type to an HTMLNode.
    """
    if block_type == BlockType.PARAGRAPH:
        children = text_to_children(block)
        return HTMLNode("p", children=children)
    elif block_type == BlockType.HEADING:
        i = 0
        while i < len(block) and block[i] == "#":
            i += 1
        level = i
        text = block[level:]
        if text.startswith(" "):
            text = text[1:]
        children = text_to_children(text)
        return HTMLNode("h" + str(level), children=children)
    elif block_type == BlockType.CODE:
        code = block.strip("`")
        code = code.strip()
        code_node = text_node_to_html_node(TextNode(code + "\n", TextType.CODE))
        code_children = [code_node]
        code_html_node = HTMLNode("code", children=code_children)
        pre_children = [code_html_node]
        return HTMLNode("pre", children=pre_children)
    elif block_type == BlockType.QUOTE:
        lines = block.split("\n")
        quote_text = ""
        for idx, line in enumerate(lines):
            if line.startswith(">"):
                line = line[1:]
                if line.startswith(" "):
                    line = line[1:]
            if idx > 0:
                quote_text += " "
            quote_text += line
        children = text_to_children(quote_text)
        return HTMLNode("blockquote", children=children)
    elif block_type == BlockType.UNORDERED_LIST:
        lines = block.split("\n")
        li_nodes = []
        for line in lines:
            if line.startswith("- "):
                item = line[2:]
                children = text_to_children(item)
                li_node = HTMLNode("li", children=children)
                li_nodes.append(li_node)
        return HTMLNode("ul", children=li_nodes)
    elif block_type == BlockType.ORDERED_LIST:
        lines = block.split("\n")
        li_nodes = []
        for line in lines:
            dot_index = line.find(". ")
            if dot_index != -1:
                item = line[dot_index+2:]
                children = text_to_children(item)
                li_node = HTMLNode("li", children=children)
                li_nodes.append(li_node)
        return HTMLNode("ol", children=li_nodes)
    else:
        raise Exception("Unknown block type: " + str(block_type))

def markdown_to_html_node(markdown):
    """
    Converts a full markdown document into a single parent HTMLNode (<div>).
    """
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_node = block_to_html_node(block, block_type)
        children.append(html_node)
    parent = HTMLNode("div", children=children)
    return parent

def main():
    text = (
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) "
        "and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) "
        "and a [link](https://example.com)!"
    )
    node = TextNode(text, TextType.PLAIN)

    print("Extracted images:")
    print(extract_markdown_images(text))

    print("\nSplit nodes (images):")
    image_nodes = split_nodes_image([node])
    for n in image_nodes:
        print(n)

    print("\nSplit nodes (links):")
    link_nodes = split_nodes_link(image_nodes)
    for n in link_nodes:
        print(n)

if __name__ == "__main__":
    main()