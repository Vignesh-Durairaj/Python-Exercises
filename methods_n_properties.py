"""
Methods of objects we've looked at so far are called by an instance of a class, which is then passed to the self
parameter of the method. Class methods are different - they are called by a class, which is passed to the cls parameter
of the method.

A common use of these are factory methods, which instantiate an instance of a class, using different parameters than
those usually passed to the class constructor.

Class methods are marked with a classmethod decorator.

Technically, the parameters self and cls are just conventions; they could be changed to anything else. However, they
are universally followed, so it is wise to stick to using them.
"""

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.length * self.width

    @classmethod
    def init_square(cls, side_unit):
        return cls(side_unit, side_unit)


my_rect = Rectangle(10, 20)
print(my_rect.calc_area())

my_square = Rectangle.init_square(10)
print(my_square.calc_area())

"""
Static methods are similar to class methods, except they don't receive any additional arguments; they are identical to 
normal functions that belong to a class. 

They are marked with the staticmethod decorator.
"""

class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

try:
    ingredients = ["cheese", "onions", "spam"]
    if all(Pizza.validate_topping(i) for i in ingredients):
        pizza = Pizza(ingredients)
except ValueError:
    print("Unwanted ingredient shown up !")

"""
Properties provide a way of customizing access to instance attributes. They are created by putting the property 
decorator above a method, which means when the instance attribute with the same name as the method is accessed, 
the method will be called instead. 

One common use of a property is to make an attribute read-only. Like in final attribute in 

Properties can also be set by defining setter/getter functions.
* The setter function sets the corresponding property's value.
* The getter gets the value.
* To define a setter, you need to use a decorator of the same name as the property, followed by a dot and the setter 
keyword.
* The same applies to defining getter functions.
"""

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self.pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self.pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            print("Let us allow pineapple slices for Pizzas")
            self._pineapple_allowed = True
        else:
            print("Pineapple is not allowed in Pizzas")

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
# pizza.pineapple_allowed = True --> This throws AttributeError: can't set attribute
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)