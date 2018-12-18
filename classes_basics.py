# This one talks about creating classes and objects from it. It is more like Java

class car:

    wheels = 4 # Initialized attribute with a pre-defined value

    def __init__(self, name, transmission, year):
        self.name = name
        self.transmission = transmission
        self.year = year

    def run(self):
        print("Starting " + str(self.name))
        print("getting transmitted for movement by " + str(self.transmission))
        print("Vroooom !!!")

maruti = car("Alto", "Manual", 2008)
suzuki = car("Swift", "Automatic", 2016)
Hyundai = car("Grand i10", "Manual", 2016)

print(maruti)
print(maruti.transmission)
print(maruti.name)
print(maruti.year)
print(maruti.wheels)
print(car.wheels)

maruti.run()
car.run(suzuki)

"""
Trying to access an attribute of an instance that isn't defined causes an AttributeError.
The same has been applied to, when an undefined method has been called
"""