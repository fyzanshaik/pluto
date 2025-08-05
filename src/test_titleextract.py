import unittest
from main import extract_title
import os
class TestMarkdowntoTitle(unittest.TestCase):
    def test_equal(self):
        markdownString = ""
        with open("./content/index.md",'r') as file:
            markdownString = file.read()
        
        title = extract_title(markdownString)
        
        self.assertEqual(title,"Tolkien Fan Club");



if __name__ == "__main__":
    unittest.main()