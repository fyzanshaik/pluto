## Pluto

A Server-Side-Generated(SSG) web framework to generate HTLM using markdown.

Popular SSG frameworks are Nextjs,Hugo,Astro etc. This is built upon the fundamental process as those frameworks work on.

Written in Python3!

### Flow of working:

![1754138103189](image/README/1754138103189.png)

-  Markdown files are in the /content directory. A template.html file is in the root of the project.
-  The static site generator (the Python code in src/) reads the Markdown files and the template file.
-  The generator converts the Markdown files to a final HTML file for each page and writes them to the /public directory.
-  We start the built-in Python HTTP server (a separate program, unrelated to the generator) to serve the contents of the /public directory on http://localhost:8888 (our local machine).
-  We open a browser and navigate to http://localhost:8888 to view the rendered site.

### SSG Process:

1. Delete everything in `/public` folder.
2. Copy any static assets to the `/public` directory.
3. Generate an HTLM page for each MARKDOWN(**.md**) file in `/content` directory. For each markdown file:
   -  Open the file & read its contents
   -  Split the markdown into "blocks" (e.g. paragraphs, headings, lists, etc.).
   -  Convert each block into a tree of `HTLMNode` objects. For inline elements (like bold text, links, etc.) we will convert: `Raw markdown -> TextNode -> HTMLNode`
   -  Join all `HTMLNode` blocks under one large parent HTMLNode for the pages.
   -  Use a recursive `to_htlm()` method to convert the HTLMNode and all its nested node in a giant string to inject in a template as body
   -  Write the full HTML string to a file for that page in the `/public` directory.

![1754335149146](image/README/1754335149146.png)
