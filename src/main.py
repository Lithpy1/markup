
from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode


def main():
    dummynode = TextNode("its a node of text", "bold", "https://www.boot.dev")
    print(dummynode)

def text_node_to_html_node(text_node):
    print("Testing : ", repr(text_node))
    if text_node.text_type == "text":
        return LeafNode(None, text_node.text, None)
    if text_node.text_type == "bold":
        return LeafNode("b", text_node.text, None)
    if text_node.text_type == "italic":
        return LeafNode("i", text_node.text, None)
    if text_node.text_type == "code":
        return LeafNode("code", text_node.text, None)
    if text_node.text_type == "link":
        return LeafNode("a", text_node.text, {"href":f"{text_node.url}"})
    if text_node.text_type == "image":
        return LeafNode("img", "", {"src":f"{text_node.url}", "alt":f"{text_node.text}"})
    raise Exception("Unexpected formatting input")

if __name__ == "__main__":
    main()