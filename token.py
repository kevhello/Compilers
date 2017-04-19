class Token:
    """
    A token class that categorizes a string. The 'token' is the category and the 'value' is the specific string of the
    category.
    """
    def __init__(self, token, value):
        self.token = token
        self.value = value

    def get_type(self):
        return self.token

    def get_value(self):
        return self.value
