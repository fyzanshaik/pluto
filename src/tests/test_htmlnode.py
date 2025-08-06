import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('<p>','some para')
        node2 = HTMLNode('<p>','some para')
        self.assertEqual(node, node2)
    def test_not_eq(self):
        node = HTMLNode('<h>','some para')
        node2 = HTMLNode('<p>','some para')
        self.assertNotEqual(node,node2)
    
    def test_not_eq2(self):
        node = HTMLNode('<p>','some para')
        node2 = HTMLNode('<h>','some para')
        self.assertNotEqual(node,node2)

if __name__ == "__main__":
    unittest.main()