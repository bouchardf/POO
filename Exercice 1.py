class StringFoo():
    def __init__(self):
        self.string = "ce text devrait être en majuscule"
    def set_string(self, string):
        self.string = string
    def print_string(self):
        print(self.string.upper())

StringFoo().print_string()