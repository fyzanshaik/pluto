# Hey, I'm Faizan!

Welcome to my weird little static site.  
This whole thing is built with my own Python SSG (static site generator).  
You’re looking at a page that was generated from markdown, using my own code.  
Check out my [GitHub](https://github.com/fyzanshaik) if you want to see more of my stuff.

---

So what is this?  
Basically, I wrote a Python script that takes markdown files (like this one),  
turns them into HTML using a bunch of classes (nodes and stuff),  
and spits out a website.  
It copies over images and CSS too, so it looks half-decent.

---

How does it work?

You write your content in markdown files inside the `content/` folder.  
When you run the build script, my Python code does this:

1. **Copies static files:**  
   All images, CSS, and other assets from `static/` to the output folder (`docs/`).

2. **Reads each markdown file:**  
   It goes through every `.md` file in `content/` (including subfolders).

3. **Splits the markdown into blocks:**  
   Each block is a paragraph, heading, list, or quote.

4. **Classifies each block:**  
   Figures out if it’s a heading, paragraph, list, or quote.

5. **Converts blocks to nodes:**  
   Each block becomes a tree of “nodes” (objects representing HTML elements).

6. **Handles inline markdown:**  
   Inside each block, it finds bold, italic, code, links, and images, and turns them into the right nodes.

7. **Builds the HTML:**  
   All the nodes are combined into a single HTML tree.

8. **Injects into a template:**  
   The HTML and page title are inserted into a template file, along with CSS.

9. **Writes the output:**  
   The final HTML files are saved in the `docs/` folder, ready to deploy.

---

### Example: Markdown to HTML Flow

**Markdown input:**

```
# Hello World

This is **bold** and _italic_ and a [link](https://example.com).

- Item 1
- Item 2
```

↓

**Split into blocks:**

-  Block 1: `# Hello World`
-  Block 2: `This is **bold** and _italic_ and a [link](https://example.com).`
-  Block 3:
   ```
   - Item 1
   - Item 2
   ```

↓

**Classify blocks:**

-  Block 1: Heading
-  Block 2: Paragraph
-  Block 3: Unordered List

↓

**Convert to nodes:**

-  Heading block → `ParentNode("h1", [LeafNode(None, "Hello World")])`
-  Paragraph block →
   `ParentNode("p", [LeafNode(None, "This is "), LeafNode("b", "bold"), LeafNode(None, " and "), LeafNode("i", "italic"), LeafNode(None, " and a "), LeafNode("a", "link", {"href": "https://example.com"})])`
-  List block → `ParentNode("ul", [ParentNode("li", [LeafNode(None, "Item 1")]), ParentNode("li", [LeafNode(None, "Item 2")])])`

↓

**Final HTML output:**

```html
<h1>Hello World</h1>
<p>This is <b>bold</b> and <i>italic</i> and a <a href="https://example.com">link</a>.</p>
<ul>
	<li>Item 1</li>
	<li>Item 2</li>
</ul>
```

---

That’s the whole flow:  
Markdown → Blocks → Nodes → HTML → Static Site!

---

How do you build it?  
Just run my `main.sh` or `build.sh` scripts.  
They clean up the old build, run the generator, and copy everything to the right place.  
Then you can serve it with Python or push it to GitHub Pages.

---

What did I learn?

-  How to walk through folders and files in Python
-  How to use OOP to make a tree of nodes (like HTMLNode, ParentNode, LeafNode)
-  How to turn markdown into nodes, and then into HTML
-  How to handle inline markdown (bold, italic, code, links, images) and block elements (headings, paragraphs, lists, quotes)
-  How to deal with all the annoying little details (paths, links, images, etc)
-  That static site generators are actually pretty fun to make

---

What are the limitations?

-  Only supports basic markdown:
   -  Headings (`#` through `######`)
   -  Paragraphs
   -  Bold (`**bold**`)
   -  Italic (`_italic_`)
   -  Inline code (`` `code` ``)
   -  Links (`[text](url)`)
   -  Images (`![alt](src)`)
   -  Unordered lists (`- item`)
   -  Ordered lists (`1. item`)
   -  Blockquotes (`> quote`)
-  No support for:
   -  Fenced code blocks (triple backticks)
   -  Tables
   -  HTML passthrough
   -  Nested lists
   -  Escaping special characters
-  If you mess up your markdown, it might just crash
-  The code is messy, but hey, it works

---

Here's a picture of the architecture (fancy, right?):

![SSG Architecture Overview](/images/1754138103189.png)

And here's how markdown gets turned into nodes and then into HTML:

![Markdown to Node Conversion](/images/1754335149146.png)

---

Anyway, thanks for stopping by.  
If you want to make your own, fork my repo and go wild.  
It's all on [GitHub](https://github.com/fyzanshaik/pluto).

---

See ya!
