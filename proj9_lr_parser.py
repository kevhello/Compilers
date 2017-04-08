#!usr/bin/env python3

# Project No.9
# Professor Ahmadnia
# Group: Kevin Vuong, Anika Corpus, Christopher Grant
# Due: 4/13/17
# Description: This program uses the LR Parsing table to trace an input string.


def lr_parser(input_str, lr_table, prod):
    """
    Parses an input string using the LR table and production rules provided as input.
    
    :param input_str: The string to parse. 
    :param lr_table: The LR table 
    :param prod: Production rules for the corresponding LR table
    :return: Returns 1 for accept, Returns -1 for reject
    """
    print('Parsing: ' + input_str)
    stack = [0]  # Push state 0 (starting state)
    i = 0  # Keeps track of incoming token

    while True:
        top = stack[len(stack)-1]
        inc_token = input_str[i]
        X = lr_table[top][inc_token]

        if X[0] == 'S':  # Shift
            stack.append(inc_token)  # Push incoming token onto stack
            stack.append(int(X[1:]))  # Enter the state by pushing it onto the stack
            i = i + 1
        elif X[0] == 'R':  # Reduce
            right_side = prod[int(X[1:])][1]  # The right hand side of the production rule
            left_side = prod[int(X[1:])][0]  # The left hand side of the production rule
            pop_number = 2 * len(right_side)

            # pop 2 * k symbols of the right hand side
            for j in range(0, pop_number):
                stack.pop()

            new_top = stack[len(stack) - 1]  # The state on top of stack after popping
            stack.append(left_side)  # Push the left hand side of the
            stack.append(lr_table[new_top][left_side])

        elif X == 'z':  # Accept state
            print('Input string ' + input_str + ' has been accepted')
            return 1
        else:  # Reject state
            print('Input string: ' + input_str + ' is rejected')
            return -1

        print(stack)


def main():
    str1 = '(i+i)*i$'
    str2 = '(i*)$'

    # Note: 'a' means empty entry, 'z' means accept state
    lr_table = {
        0:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 1,   'T': 2,   'F': 3},
        1:  {'i': 'a',  '+': 'S6', '-': 'S7', '*': 'a',  '/': 'a',  '(': 'a',  ')': 'a',  '$': 'z',  'E': 'a', 'T': 'a', 'F': 'a'},
        2:  {'i': 'a',  '+': 'R3', '-': 'R3', '*': 'S8', '/': 'S9', '(': 'a',  ')': 'R3', '$': 'R3', 'E': 'a', 'T': 'a', 'F': 'a'},
        3:  {'i': 'a',  '+': 'R6', '-': 'R6', '*': 'R6', '/': 'R6', '(': 'a',  ')': 'R6', '$': 'R6', 'E': 'a', 'T': 'a', 'F': 'a'},
        4:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 10,  'T': 2,   'F': 3},
        5:  {'i': 'a',  '+': 'R8', '-': 'R8', '*': 'R8', '/': 'R8', '(': 'a',  ')': 'R8', '$': 'R8', 'E': 'a', 'T': 'a', 'F': 'a'},
        6:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 'a', 'T': 11,  'F': 3},
        7:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 'a', 'T': 12,  'F': 3},
        8:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 'a', 'T': 'a', 'F': 13},
        9:  {'i': 'S5', '+': 'a',  '-': 'a',  '*': 'a',  '/': 'a',  '(': 'S4', ')': 'a',  '$': 'a',  'E': 'a', 'T': 'a', 'F': 14},
        10: {'i': 'a',  '+': 'S6', '-': 'S7', '*': 'a',  '/': 'a',  '(': 'a',  ')': 'S15','$': 'a',  'E': 'a', 'T': 'a', 'F': 'a'},
        11: {'i': 'a',  '+': 'R1', '-': 'R1', '*': 'S8', '/': 'S9', '(': 'a',  ')': 'R1', '$': 'R1', 'E': 'a', 'T': 'a', 'F': 'a'},
        12: {'i': 'a',  '+': 'R2', '-': 'R2', '*': 'S8', '/': 'S9', '(': 'a',  ')': 'R2', '$': 'R2', 'E': 'a', 'T': 'a', 'F': 'a'},
        13: {'i': 'a',  '+': 'R4', '-': 'R4', '*': 'R4', '/': 'R4', '(': 'a',  ')': 'R4', '$': 'R4', 'E': 'a', 'T': 'a', 'F': 'a'},
        14: {'i': 'a',  '+': 'R5', '-': 'R5', '*': 'R5', '/': 'R5', '(': 'a',  ')': 'R5', '$': 'R5', 'E': 'a', 'T': 'a', 'F': 'a'},
        15: {'i': 'a',  '+': 'R7', '-': 'R7', '*': 'R7', '/': 'R7', '(': 'a',  ')': 'R7', '$': 'R7', 'E': 'a', 'T': 'a', 'F': 'a'},
    }

    productions = {
        1: ['E', 'E+T'],
        2: ['E', 'E-T'],
        3: ['E', 'T'],
        4: ['T', 'T*F'],
        5: ['T', 'T/F'],
        6: ['T', 'F'],
        7: ['F', '(E)'],
        8: ['F', 'i'],
    }

    lr_parser(str1, lr_table, productions)
    print('')
    lr_parser(str2, lr_table, productions)

if __name__ == '__main__':
    main()
