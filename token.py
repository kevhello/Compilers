class Token:
    def __init__(self, token, value):
        self.token = token
        self.value = value

    def get_type(self):
        return self.token

    def get_value(self):
        return self.value
