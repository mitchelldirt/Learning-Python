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

    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly this far south")

    def quack(self):
        print("Are you 'aving a larf? I'm a penguin!")
    def aviate(self):
        print("I won the lottery and bought a learjet")


class Mallard(Duck):
    pass


class Flock(object):

    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        # Never use type() to check class instances in python. This isn't the best way to do it either. Pythonic way
        # is the duck test i.e. check if it fly's instead of what it is. "If it quacks like a duck".
        # if isinstance(duck, Duck):

        fly_method = getattr(duck, 'fly', None)
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure it's not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                # TODO Below is a test exception. In real code you would remove this before release.
                raise AttributeError("Testing exception handler in migrate")
            except AttributeError as e:
                print("One duck down!")
                problem = e
        if problem:
            raise problem


if __name__ == '__main__':
    donald = Duck()
    donald.fly()
