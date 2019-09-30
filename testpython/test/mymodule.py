
def print_all(*params):
    for param in params:
        print('- ' + str(param))


class Hero:
    def __init__(self, name):
        self.name = name;

    def fight(self):
        print("Hero " + self.name + " is fighting..")

