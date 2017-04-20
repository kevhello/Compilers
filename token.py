class Token:
    """
    A token class that categorizes a string. The 'token' is the category and the 'value' is the specific string of the
    category.
    """
    def __init__(self, token, value, line_number):
        self.token = token
        self.value = value
        self.line_number = line_number

    def get_type(self):
        return self.token

    def get_value(self):
        return self.value

    def get_line_num(self):
        return self.line_number
