import bird as b
class Parrot(b.Bird):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def get_attribute(self):
        return f"{self.name} {super().get_attribute()}"

    def flying_test(bird):
        print("Parrot can fly")