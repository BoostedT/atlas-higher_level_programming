#!/usr/bin/python3
"""
MODULE: text_indentation
"""

def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    # Replace sentence-ending punctuation with punctuation followed by two newlines
    text = text.replace('.', '.\n\n').replace('?', '?\n\n').replace(':', ':\n\n')
    
    # Split the text into lines, preserving newlines
    lines = text.splitlines()

    # Print each non-blank line
    for line in lines:
        if line.strip():  # Only print non-empty lines
            print(line.strip())
            print()
        else:
            if line.endswith(('.', '?', ':')):
                print()
    return
