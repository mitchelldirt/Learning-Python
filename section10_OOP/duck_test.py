class Wing(object):

    def __init__(self, ratio):
        self.ratio = ratio

    def fly(self):
        if self.ratio > 1:
            print("Weee, this is fun")
        elif self.ratio == 1:
            print("This is hard work, but I'm flying")
        else:
            print("I'll just walk ):")


class Duck(object):

    # Any new duck objects will have the wing attribute. This is composition. Rather than rewrite the code of inheriting
    # it you can compose an attribute to the class.
    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle waddle waddle")

    def swim(self):
        print("Come on in, the waters lovely")

    def quack(self):
        print("quack quack")

    def fly(self):
        self._wing.fly()

class Penguin(object):
    def walk(self):
        print("Waddle waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far south")

    def quack(self):
        print("Are you 'aving a larf? I'm a penguin!")


# def test_duck(Duck):
#     Duck.walk()
#     Duck.swim()
#     Duck.quack()

if __name__ == '__main__':
    donald = Duck()
    donald.fly()
    # percy = Penguin()
    # test_duck(percy)