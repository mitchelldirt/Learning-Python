class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)
print(hamilton.price)
print(hamilton.make)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make}, {1.price}".format(kenwood, hamilton))

"""
Class: Template for creating objects. All objects created using the same class will have the same characteristics
Object: An instance of a class
Instantiate: Create an instance of a class
Method: A functioned defined in a class
Attribute: A variable bound to an instance of a class
***EVERY TYPE IS A CLASS IN PYTHON***
"""

# False until we activate the switch_on method
print(hamilton.on)
# Automatically fills in the self parameter
hamilton.switch_on()
# Now the hamilton kettle is on
print(hamilton.on)

# Calling the method using the class itself
Kettle.switch_on(kenwood)
# Now the kenwood kettle is on
print(kenwood.on)

print("*" * 80)

# Instance variable power is added to the kenwood class object
kenwood.power = 1.5
print(kenwood.power)

# Will receive error message because there is no variable for power in the hamilton class object
# print(hamilton.power)

# Updating the power source attribute to be atomic.
print("Switch to atomic power")
Kettle.power_source = "Atomic"
print(Kettle.power_source)
print(kenwood.power_source)

# Switching the instance variable for power_source to gas for the hamilton object. Be careful not to shadow
# global attributes.
print("\nSwitch hamilton to gas")
hamilton.power_source = "gas"
print(hamilton.power_source)

# Access the dictionaries of the Kettle class, kenwood object, and hamilton object
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)
