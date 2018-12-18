# Let us consider the below example for inheritance

"""
Inheritance

A class that inherits from another class is called a subclass.
A class that is inherited from is called a superclass.
If a class inherits from another with the same attributes or methods, it overrides them.
"""

class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

    def run(self):
        print("Running with " + str(self.wheels) + " wheels. Vrooooom !")

    def apply_brake(self):
        print("Applying brake on all the wheel")


class Bike(Vehicle):
    def __init__(self):
        Vehicle.__init__(self, 2)

    def apply_brake(self):
        print("Applying the brake only for the available two wheels")

class Car(Vehicle):
    def __init__(self):
        super(Car, self).__init__(4)

alto = Car()
alto.run()
alto.apply_brake()

pulsar = Bike()
pulsar.run()
pulsar.apply_brake()