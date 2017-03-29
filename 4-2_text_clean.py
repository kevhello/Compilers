#!/usr/bin/env python3
# Assignment #4, Program 2
# Professor Ahmadnia
# Group: Kevin Vuong, Anika Corpus, Christopher Grant
# Due: 2/23/17
# Description: This program takes an input file and removes all comment lines, extra spaces, and places a space
#              before and after each token. These changes are then saved to a new file.

import re

def space_formatter(expr):
    """
    Formats the spaces of a line of text
    
    Arguments:
        expr: a line of text
    
    Returns:
        line: the line of processed text
    
    """
    tokenList = expr.split(" ")
    line = ''
    content = ''
    pattern = r'(\=|\*|\-|\,|\:|\(|\)|\<\=|\+)'

    for token in tokenList:
        if token == '':
            continue
        content = content + token

    for char in content:
        if char == '\n':
            continue
        if char == ';':
            line = line + ' '
            line = line+char
            line = line +'\n'
        elif re.match(pattern, char):
            line = line + ' '
            line = line + char
            line = line + ' '
        else:
            line = line + char
            
    return line


def clean_text(file):
    """
    Cleans the text of comments and formatting all the spaces
    
    Arguments:
        file: the file to be read
    
    Returns:
        lines_content: The content of the text, properly formatted and cleaned
    
    """
    lines_read = file.readlines()
    lines_content = ''
    comments_PATTERN = r'//.*'
    for line in lines_read:
        
        # Ignore the comments
        line = re.sub(comments_PATTERN, r'', line)
        
        # Ignore lines that only contain the newline character
        if re.match(pattern=r'^\n$', string=line):
            continue
        
        # Checks if a statement ends with a semicolon
        if re.match(pattern=r'.*;', string=line) == None:
            print(line,end='')
            print('Syntax error: Missing ; after end of statement')
            exit(1)
    
        line = space_formatter(line)
        lines_content = lines_content + line
        
    print(lines_content)
    return lines_content

def main():
    with open("data.txt") as f:
        content = clean_text(f)
        new_file = open('newdata.txt', mode='w', encoding='utf-8')
        new_file.writelines(content)
        new_file.close()
        
if __name__ == "__main__":
    main()