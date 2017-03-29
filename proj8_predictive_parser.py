#!usr/bin/env python3

# Project No.8 Part 1 & Part 2
# Professor Ahmadnia
# Group: Kevin Vuong, Anika Corpus, Christopher Grant
# Due: 4/6/17
# Description: This program traces input string(s) using the Predictive Parsing table(s) and returns
#              whether the input string is a valid string based on the Predictive Parsing table.


def predictive_parser(input_str, predict_table, terminal_list, starting_symbol):
    '''
    Determines whether the input string is accepted or rejected based on the prediction table.

    :param input_str: the string to parse
    :param predict_table: the prediction table being used
    :param terminal_list: a list of terminals for the grammar
    :param starting_symbol: the symbol to which the grammar starts with
    :return: Returns -1 if input string is rejected, otherwise returns 0 if accepted
    '''
    print('Parsing: ' + input_str)
    stack = ['$']
    stack.append(starting_symbol)
    i = 0   # Keeps track which character the of the input string is currently being read.
    while stack:
        top_of_stack = stack[len(stack)-1]
        char_read = input_str[i]
        if top_of_stack in terminal_list:
            if top_of_stack is char_read:
                stack.pop()
                i = i + 1
            else:
                print('\nThe grammar has rejected the input string\n')
                return -1
        else:
            if predict_table[top_of_stack][char_read] is not 'aaa':
                entry = stack.pop()
                if predict_table[entry][char_read] is not 'lambda':
                    for symbol in reversed(predict_table[entry][char_read]):
                        stack.append(symbol)
            else:
                print('The grammar has rejected the input string\n')
                return -1
        print(stack)
    print('The grammar has accepted the input string\n')
    return 0


def main():
    input_str1 = '(i+i)*i$'
    input_str2 = 'i*(i-i)$'
    input_str3 = 'i(i+i)$'

    # Note: Empty slot = 'aaa'
    predict_table1 = {'E': {'i': 'TQ', '+': 'aaa', '-': 'aaa', '*': 'aaa', '/': 'aaa', '(': 'TQ', ')': 'aaa', '$': 'aaa'},
                     'Q': {'i': 'aaa', '+': '+TQ', '-': '-TQ', '*': 'aaa', '/': 'aaa', '(': 'aaa', ')': 'lambda', '$': 'lambda'},
                     'T': {'i': 'FR', '+': 'aaa', '-': 'aaa', '*': 'aaa', '/': 'aaa', '(': 'FR', ')': 'aaa', '$': 'aaa'},
                     'R': {'i': 'aaa', '+': 'lambda', '-': 'lambda', '*': '*FR', '/': '/FR', '(': 'aaa', ')': 'lambda', '$': 'lambda'},
                     'F': {'i': 'i', '+': 'aaa', '-': 'aaa', '*': 'aaa', '/': 'aaa', '(': '(E)', ')': 'aaa', '$': 'aaa'}}

    terminal_list1 = ['i', '+', '-', '*', '/', '(', ')', '$']
    predictive_parser(input_str1, predict_table1, terminal_list1, 'E')
    predictive_parser(input_str2, predict_table1, terminal_list1, 'E')
    predictive_parser(input_str3, predict_table1, terminal_list1, 'E')

    predict_table2 = {'S': {'a': 'a=E', 'b': 'aaa', '(': 'aaa', ')': 'aaa', '/': 'aaa', '*': 'aaa', '+': 'aaa', '-': 'aaa', '=': 'aaa', '$': 'aaa'},
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
