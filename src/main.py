import os
import shutil
from textnode import TextNode,TextType
from util import markdown_to_html_node

"""_summary_
This is a recursive function to copy everything from static folder to public folder, and also to delete stuff
"""
def delete_contents(path):
    for item in os.listdir(path=path):
        item_path = os.path.join(path,item)
        if os.path.isfile(item_path) or os.path.islink(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            delete_contents(item_path)
            os.rmdir(item_path)

def copy_contents(src,dst):
    for item in os.listdir(src):
        s = os.path.join(src,item)
        d = os.path.join(dst,item)
        
        if os.path.isdir(s):
            os.makedirs(d,exist_ok=True)
            copy_contents(s,d)
        else:
            shutil.copy2(s,d)
            print(f"Copied {s} -> {d}")

def syncDirectories(source="static", destination="public"):
    source_absolute_path = os.path.abspath(source)
    destination_absolute_path = os.path.abspath(destination)
    print(source_absolute_path, destination_absolute_path)

    if not os.path.exists(source_absolute_path):
        raise NotADirectoryError("Source doesn't exist")

    if not os.path.exists(destination_absolute_path):
        print("Creating directory: " + destination)
        os.makedirs(destination_absolute_path)
    else:
        print("Removing all contents from destination...")
        delete_contents(destination_absolute_path)

    print("Copying contents...")
    copy_contents(source_absolute_path, destination_absolute_path)
    print("Sync complete.")



def extract_title(markdown):
    # Dividie the entire markdown string by lines
    lines = markdown.split("\n\n")
    expectedTitleLine = lines[0]
    print("Expected String to contain the Header: ",lines[0])
    flag = expectedTitleLine.startswith('#')
    if not flag:
        raise Exception("Header and title do not exist")
    
    return expectedTitleLine.split('#')[1].strip()


def generate_page(from_path,template_path,dest_path):
    from_path_abs = os.path.abspath(from_path)
    template_path_abs = os.path.abspath(template_path)
    dest_path_abs = os.path.abspath(dest_path)
    
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    markdown_content = ""
    template_html = ""
    print(f"Reading markdown content and template html file")
    with open(from_path_abs,'r') as file:
        markdown_content = file.read()
    with open(template_path_abs,'r') as file:
        template_html = file.read()
    
    print(f"Markdown content first 100 chars: {markdown_content[:101]} Template HTML: {template_html[:101]}")
    print("Converting markdown string to HTML Node ")
    html_node = markdown_to_html_node(markdown_content)
    # print(f"HTML Node array: {html_node}")
    html_content = html_node.to_html()
    print(f"HTML Content after converting HTML node to text: {html_content[:101]}")
    title = extract_title(markdown_content)
    
    print(f"Extracted title: {title}")
    
    title_placeholder = '{{ Title }}'
    content_placeholder = '{{ Content }}' 
    
    
    template_html = template_html.replace(title_placeholder, title)
    template_html = template_html.replace(content_placeholder, html_content)
    
    print(f"Template HTML after replacing(100 chars): {template_html[:101]}")
    
    print(f"Writing file with path {dest_path_abs}")
    with open(dest_path_abs,'w') as file:
        file.write(template_html)
    print(f"File writing done!\n Succesfully generated a page!")
    


def generate_pages_recursive(dir_path_content,template_path,dest_dir_path):
    for entry in os.listdir(dir_path_content):
        entry_path = os.path.join(dir_path_content,entry)
        dest_entry_path = os.path.join(dest_dir_path,entry)
        
        if os.path.isdir(entry_path):
            if not os.path.exists(dest_entry_path):
                os.makedirs(dest_entry_path)
            generate_pages_recursive(entry_path, template_path, dest_entry_path)
        elif os.path.isfile(entry_path) and entry_path.endswith(".md"):
            dest_file = os.path.splitext(entry)[0] + ".html"
            dest_file_path = os.path.join(dest_dir_path, dest_file)
            print(f"Generating page from {entry_path} to {dest_file_path} using {template_path}")
            generate_page(entry_path, template_path, dest_file_path)

def main():
    print("Directory syncing(deletion & copying): ")
    syncDirectories("static","public")
    # generate_page("content/index.md","template.html","public/index.html")
    generate_pages_recursive("content","template.html","public")
if __name__ == "__main__":
    main()