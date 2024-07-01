from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

all_types = {
    text_type_bold : '**', 
    text_type_text : None, 
    text_type_italic : '*', 
    text_type_code : '`', 
    text_type_image : None, 
    text_type_link : None
    }

import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    return_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            return_nodes.append(old_node)
            #print(f"  TEST: old node wasnt text, appending {repr(old_node)}")
            continue
        split_nodes = []
        splits = old_node.text.split(delimiter)
        #print(f"TEST: This is the initial text split: {splits} with the {delimiter} delimiter")
        if len(splits) % 2 == 0:
            raise ValueError("You're forgetting to close something")
        for i in range(len(splits)):
            if splits[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(splits[i], text_type_text))
                #print(f"   TEST: i % 2 == 0, appending splits[i] ({splits[i]}) with {text_type_text}")
            else:
                split_nodes.append(TextNode(splits[i], text_type))
                #print(f"   TEST: Passed all the ifs, appending splits[i] ({splits[i]}) with text type: {text_type}")
        return_nodes.extend(split_nodes)
    return return_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    if matches:
        return matches
    else:
        return None, None

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    if matches:
        return matches
    else:
        return None, None

def split_nodes_image(old_nodes):
    new_nodes = []
    text = old_nodes
    split_nodes = []
    image_tuple_list = extract_markdown_images(old_nodes)
    for image_tuple in image_tuple_list:
        image_markup = f'![{image_tuple[0]}]({image_tuple[1]})'
        parts = text.split(image_markup, 1)
        if parts[0]:
            split_nodes.append(parts[0])
        split_nodes.append(image_markup)
        text = parts[1]
    if text:
        split_nodes.append(text)
    for pieces in split_nodes:
        #print(f' Printing Pieces: {pieces}')
        if pieces.startswith('!['):
            image_tuple = extract_markdown_images(pieces)[0]
            if image_tuple != (None, None):
                #print(f'extracted image tuple: {image_tuple}')
                new_nodes.append(TextNode(image_tuple[0], text_type_image, image_tuple[1]))
            else:
                print(f'Error: INvalid image format in {pieces}')
        else:
            new_nodes.append(TextNode(pieces, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    text = old_nodes
    split_nodes = []
    link_tuple_list = extract_markdown_links(old_nodes)
    for link_tuple in link_tuple_list:
        link_markup = f'[{link_tuple[0]}]({link_tuple[1]})'
        parts = text.split(link_markup, 1)
        if parts[0]:
            split_nodes.append(parts[0])
        split_nodes.append(link_markup)
        text = parts[1]
    if text:
        split_nodes.append(text)
    for pieces in split_nodes:
        #print(f' Printing Pieces: {pieces}')
        if pieces.startswith('['):
            link_tuple = extract_markdown_links(pieces)[0]
            if link_tuple != (None, None):
                #print(f'extracted link tuple: {link_tuple}')
                new_nodes.append(TextNode(link_tuple[0], text_type_link, link_tuple[1]))
            else:
                print(f'Error: INvalid link format in {pieces}')
        else:
            new_nodes.append(TextNode(pieces, text_type_text))
    return new_nodes
            
def text_to_textnodes(text):
    textnodesplit = split_nodes_image(text)
    for node in textnodesplit:
        if node.text_type == text_type_text and extract_markdown_links(node.text)[0] != None:
            print(split_nodes_link(node.text))
            
        
