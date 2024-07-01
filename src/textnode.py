from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    url = None
    def __init__(self, text, text_type, url = False):
        self.text = text 
        self.text_type = text_type 
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node):
    print("Testing : ", repr(text_node))
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text, None)
    if text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text, None)
    if text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text, None)
    if text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text, None)
    if text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href":f"{text_node.url}"})
    if text_node.text_type == text_type_image:
        return LeafNode("img", "", {"src":f"{text_node.url}", "alt":f"{text_node.text}"})
    raise Exception(f"Unexpected formatting input: {text_node.text_type}")

def get_text_type(delimiter):
    if delimiter == "*":
        return text_type_bold
    if delimiter == "`":
        return text_type_code
    if delimiter == "**":
        return text_type_italic
    


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_nodes = []
    return_nodes.clear()
    if old_nodes.text_type != text_type_text:
        return return_nodes.append(old_nodes)
    string_list = old_nodes.text.split(delimiter)
    print(string_list)
    if old_nodes.text.startswith(delimiter):
        if len(string_list) < 3:
            raise ValueError("Something didnt get closed")
        return_nodes.append(TextNode(f"{string_list[1]}", get_text_type(delimiter)))
        return_nodes.append(TextNode(f"{string_list[2]}", text_type_text))
        return return_nodes
    if old_nodes.text.endswith(delimiter):
        if len(string_list) < 3:
            raise ValueError("Something didnt get closed")
        return_nodes.append(TextNode(f"{string_list[0]}", text_type_text))
        return_nodes.append(TextNode(f"{string_list[1]}", get_text_type(delimiter)))
        return return_nodes
    if len(string_list) != 3:
        raise ValueError("Something didnt get closed")
    return_nodes.append(TextNode(f"{string_list[0]}", text_type_text))
    return_nodes.append(TextNode(f"{string_list[1]}", get_text_type(delimiter)))
    return_nodes.append(TextNode(f"{string_list[2]}", text_type_text))
    return return_nodes
            



	
