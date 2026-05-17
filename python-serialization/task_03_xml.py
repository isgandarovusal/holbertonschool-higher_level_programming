#!/usr/bin/env python3
"""
Module for serializing and deserializing a dictionary with XML.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serializes a Python dictionary into XML and saves it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Reads XML data from a file and returns a deserialized Python dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The reconstructed dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        # Reconstruct the dictionary from child elements
        return {child.tag: child.text for child in root}
    except FileNotFoundError:
        return None
    except Exception:
        return None
