import unittest

from textnode import TextNode, split_nodes_delimiter
from main import text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "text", "url.com")
        node2 = TextNode("This is a text node", "text")
        #self.assertEqual(node, node2)
        node3 = TextNode("This is another test", "italic", "url.com")
        node4 = TextNode("This is another test", "italic", "url.com")
        self.assertEqual(node3, node4)
        print(repr(node))
        print(repr(node3))
        print(repr(text_node_to_html_node(node)))
        splitnodestest = TextNode("this will be `coded", "text")
        for textnodes in split_nodes_delimiter(splitnodestest, "`", "text"):
            print(repr(textnodes))


if __name__ == "__main__":
    unittest.main()
