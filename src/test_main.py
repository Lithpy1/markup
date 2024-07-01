import unittest

from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode
from main import text_node_to_html_node

class TestNodeToHtml(unittest.TestCase):
    def TestNode(self):
        node = TextNode("This is a text node", "text")
        node3 = TextNode("This is another test", "italic", "url.com")
        print(repr(node3))
        print(repr(text_node_to_html_node(node3)))

    
        
if __name__ == "__main__":
    unittest.main()