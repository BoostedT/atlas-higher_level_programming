#!/usr/bin/python3
"""Module that contains a function that prints
text with two newlines after each of
these characters {'.', '?', ':'}."""


def text_indentation(text):
    """Prints text with two newlines after '.', '?', and ':'."""
    
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    """
     prints a text with 2 new lines after each
     of these characters: ., ? and :
    """

    formatted_text = ""

    i = 0
    while i < len(text):
        formatted_text += text[i]
        if text[i] in ".:?":
            formatted_text += "\n\n"
            i += 1

        while i < len(text) and text[i] == ' ':
                i += 1
        continue
        i += 1
    print(formatted_text, end="")
