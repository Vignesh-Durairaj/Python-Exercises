# This one talks about creating classes and objects from it. It is more like Java

class Car:

    wheels = 4 # Initialized attribute with a pre-defined value

    def __init__(self, name, transmission, year):
        self.name = name
        self.transmission = transmission
        self.year = year

    def run(self):
        print("Starting " + str(self.name))
        print("getting transmitted for movement by " + str(self.transmission))
        print("Vroooom !!!")

maruti = Car("Alto", "Manual", 2008)
suzuki = Car("Swift", "Automatic", 2016)
Hyundai = Car("Grand i10", "Manual", 2016)

print(maruti)
print(maruti.transmission)
print(maruti.name)
print(maruti.year)
print(maruti.wheels)
print(Car.wheels)

maruti.run()
Car.run(suzuki)

"""
Trying to access an attribute of an instance that isn't defined causes an AttributeError.
The same has been applied to, when an undefined method has been called
"""