import os
import shutil
from textnode import TextNode,TextType

"""_summary_
This is a recursive function to copy everything from static folder to public folder
"""
def syncDirectories(source="static",destination="public"):
    #First delete everything from destination folder
    source_absolute_path = os.path.abspath(source)
    destination_absolute_path = os.path.abspath(destination)
    print(source_absolute_path, destination_absolute_path)
    
    pathExists = os.path.exists(source_absolute_path)
    if not pathExists:
        raise NotADirectoryError("Source doesn't exist")
    
    pathExists = os.path.exists(destination_absolute_path)
    containsData = True
    if not pathExists:
        containsData = False
        print("Creating directory: "+destination)
        os.mkdir(destination_absolute_path)
    
    if containsData:
        print("Remove destination tree idk what ")
        # shutil.rmtree(f"{destination_absolute_path}/")
        all_contents = os.listdir(destination_absolute_path)
        for content in all_contents:
            constructed_abs_path = f"{destination_absolute_path}/{content}"
            print(constructed_abs_path)
            if os.path.isfile(constructed_abs_path):
                os.remove(constructed_abs_path)
            elif os.path.isdir(constructed_abs_path):
                os.rmdir(constructed_abs_path)
    
    #Now to copy
    

def main():
    syncDirectories("static","public")
    

if __name__ == "__main__":
    main()