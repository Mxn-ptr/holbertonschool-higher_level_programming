#!/usr/bin/python3

""" Define a splited text function """

def text_indentation(text):
    """ Function text_indentation
        Args:
            text (str): text to split
        Raise:
            TypeError: if text is not a string
        No return just print the splited text """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text) and text[i] == " ":
        i += 1
    
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
    