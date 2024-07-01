import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_edit(self):
        #htmltest = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        #htmltest2 = HTMLNode("h1", props={"img": "https://xxxnudes.com", "target": "allgoodinthehood"})
        #print(htmltest2.props_to_html())
        #print(htmltest.props)
        #print(repr(htmltest2))
        #print(repr(htmltest))
        leaftest1 = LeafNode(tag="a", value = "Value", props={"href":"https://poohbear.com"})
        leaftest2 = LeafNode(tag="p", value="this is where you find thought provoking commentary")
        #print(repr(leaftest1))
        #print(repr(leaftest2))
        print(leaftest1.to_html())
        print(leaftest2.to_html())
        #print(repr(leaftest1))
        #print(repr(leaftest2))

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_parent_to_html(self):
        newparent = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        print("BELOW IS NEWPARENT TO HTML")
        print(newparent.to_html())
        print(repr(newparent))


    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


if __name__ == "__main__":
    unittest.main()