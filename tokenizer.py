
import re

from token import *


def tokenizer(string):
    """
    
    :param string: The source code
    :return: A list of tokens. Returns -1 if a token is not recognizable.
    """
    content = string.split()
    token_list = []
    reserved_pattern = r'^(PROGRAM|INTEGER|PRINT|BEGIN|END\.)$'
    symbol_pattern = r'^(=|\/|\*|\+|\-|\;|\:|\,|\(|\))$'
    number_pattern = r'^(\+|\-)?[0-9]+$'
    identifier_pattern = r'^(P|Q|R|S)+(P|Q|R|S|[0-9])*$'

    for word in content:
        if re.match(reserved_pattern, word):  # Check for reserved word token
            reserved = Token('RESERVED', word)
            token_list.append(reserved)

        elif re.match(number_pattern, word):  # Check for number token
            for symbol in word:
                if re.match('(\+|-)', symbol):
                    sign = Token('SIGN', symbol)
                    token_list.append(sign)
                elif re.match('[0-9]', symbol):
                    digit = Token('DIGIT', symbol)
                    token_list.append(digit)

        elif re.match(symbol_pattern, word):  # Check for symbol token
            symbol = Token('SYMBOL', word)
            token_list.append(symbol)

        elif re.match(identifier_pattern, word):  # Check for identifier token
            for symbol in word:
                if re.match(r'(P|Q|R|S)', symbol):
                    id = Token('ID', symbol)
                    token_list.append(id)
                elif re.match(r'[0-9]', symbol):
                    more_id_digit = Token('MORE_ID_DIGIT', symbol)
                    token_list.append(more_id_digit)
        else:
            print('Unknown word: ' + word)
            return -1

    # For debug purposes
    # for token in token_list:
    #     print(token.get_type(), ':', token.get_value())

    return token_list


