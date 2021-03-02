import bird as b

class Penguin(b.Bird):

    def __init__(self, name):

        super().__init__()

        self.name = name

    def get_attribute(self):
        return f"{self.name} {super().get_attribute()}"

    def whoisThis(self):
         print("Penguin")

    def run(self):
         print("Run faster")

    def fly(self):
         print("Penguin  can't fly")

