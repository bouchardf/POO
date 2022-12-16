class rectangle():
    def __init__(self):
        self.long = 10
        self.large = 2
        self.airerectangle = self.long * self.large

    def set_airerectangle(self, airerectangle):
        self.airerectangle = airerectangle

    def print_airerectangle(self):
        print(self.airerectangle)



rectangle().print_airerectangle()