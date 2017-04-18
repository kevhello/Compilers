#!usr/bin/env python3

# FINAL PROJECT
# Professor Ahmadnia
# Group: Kevin Vuong, Anika Corpus, Christopher Grant
# Due: 4/6/17
# Description: This program traces input string(s) using the Predictive Parsing table(s) and returns
#              whether the input string is a valid string based on the Predictive Parsing table.

import re

from token import *


def predictive_parser(token_list, predict_table, terminal_list, starting_symbol):
    """
    Determines whether the input string is accepted or rejected based on the prediction table.
    
    :param token_list: a list of tokens to parse (basically, the input string in tokenized form)
    :param predict_table: the prediction table being used
    :param terminal_list: a list of terminals for the grammar
    :param starting_symbol: the symbol to which the grammar starts with
    :return: Returns -1 if input string is rejected, otherwise returns 0 if accepted
    """

    stack = ['$', starting_symbol]  # Push the end-of-input symbol and the starting symbol
    i = 0  # Keeps track which token is currently being read

    # Add ending symbol to the end of the input
    ending_symbol = Token('$', '$')
    token_list.append(ending_symbol)

    while stack:  # loop until stack is empty

        top_of_stack = stack[len(stack) - 1]
        token_read = token_list[i]
        char_read = token_read.get_value()  # Gets the actual terminal of the token

        if top_of_stack in terminal_list:  # Terminal
            if top_of_stack == token_read.get_value():
                stack.pop()
                i = i + 1
            else:
                print('\n1: The grammar has rejected the input string\n')
                return -1
        else:   # Non-terminal
            if predict_table[top_of_stack][char_read] is not 'aaa':  # If table entry is not an empty entry
                entry = stack.pop()
                if predict_table[entry][char_read] is not 'lambda':
                    # Push the entry into the stack in reverse order
                    for symbol in reversed(predict_table[entry][char_read].split()):
                        if re.match(r'PROGRAM|BEGIN|END\.|INTEGER|PRINT', symbol):
                            stack.append(symbol)
                        else:
                            for non_terminal in reversed(symbol):
                                stack.append(non_terminal)
            else:
                print('2: The grammar has rejected the input string')
                print(top_of_stack, char_read)
                return -1
        print(stack)

    print('The grammar has accepted the input string\n')
    return 0


def main():
    input_str1 = '(i+i)*i$'
    input_str2 = 'i*(i-i)$'
    input_str3 = 'i(i+i)$'

    # Note: Empty slot = 'aaa'
    predict_table1 = {
        'E': {'i': 'TQ', '+': 'aaa', '-': 'aaa', '*': 'aaa', '/': 'aaa', '(': 'TQ', ')': 'aaa', '$': 'aaa'},
        'Q': {'i': 'aaa', '+': '+TQ', '-': '-TQ', '*': 'aaa', '/': 'aaa', '(': 'aaa', ')': 'lambda', '$': 'lambda'},
        'T': {'i': 'FR', '+': 'aaa', '-': 'aaa', '*': 'aaa', '/': 'aaa', '(': 'FR', ')': 'aaa', '$': 'aaa'},
        'R': {'i': 'aaa', '+': 'lambda', '-': 'lambda', '*': '*FR', '/': '/FR', '(': 'aaa', ')': 'lambda', '$': 'lambda'},
        'F': {'i': 'i', '+': 'aaa', '-': 'aaa', '*': 'aaa', '/': 'aaa', '(': '(E)', ')': 'aaa', '$': 'aaa'}}

    terminal_list1 = ['i', '+', '-', '*', '/', '(', ')', '$']
    predictive_parser(input_str1, predict_table1, terminal_list1, 'E')
    predictive_parser(input_str2, predict_table1, terminal_list1, 'E')
    predictive_parser(input_str3, predict_table1, terminal_list1, 'E')

    predict_table2 = {
        'S': {'a': 'a=E', 'b': 'aaa', '(': 'aaa', ')': 'aaa', '/': 'aaa', '*': 'aaa', '+': 'aaa', '-': 'aaa', '=': 'aaa', '$': 'aaa'},
        'E': {'a': 'TQ', 'b': 'TQ', '(': 'TQ', ')': 'aaa', '/': 'aaa', '*': 'aaa', '+': 'aaa', '-': 'aaa', '=': 'aaa', '$': 'aaa'},
        'Q': {'a': 'aaa', 'b': 'aaa', '(': 'aaa', ')': 'lambda', '/': 'aaa', '*': 'aaa', '+': '+TQ', '-': '-TQ', '=': 'aaa', '$': 'lambda'},
        'T': {'a': 'FR', 'b': 'FR', '(': 'FR', ')': 'aaa', '/': 'aaa', '*': 'aaa', '+': 'aaa', '-': 'aaa', '=': 'aaa', '$': 'aaa'},
        'R': {'a': 'aaa', 'b': 'aaa', '(': 'aaa', ')': 'lambda', '/': '/FR', '*': '*FR', '+': 'lambda', '-': 'lambda', '=': 'aaa', '$': 'lambda'},
        'F': {'a': 'a', 'b': 'b', '(': '(E)', ')': 'aaa', '/': 'aaa', '*': 'aaa', '+': 'aaa', '-': 'aaa', '=': 'aaa', '$': 'aaa'}}

    terminal_list2 = ['a', 'b', '(', ')', '/', '*', '+', '-', '=', '$']
    input_str4 = 'a=(a+a)*b$'
    input_str5 = 'a=a*(b-a)$'
    input_str6 = 'a=(a+a)b$'
    predictive_parser(input_str4, predict_table2, terminal_list2, 'S')
    predictive_parser(input_str5, predict_table2, terminal_list2, 'S')
    predictive_parser(input_str6, predict_table2, terminal_list2, 'S')


if __name__ == "__main__":
    main()
