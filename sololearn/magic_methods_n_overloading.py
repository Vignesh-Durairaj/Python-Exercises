# What are those 'Magic Methods'.
"""
Magic methods are special methods which have double underscores at the beginning and end of their names.
They are also known as dunders.
So far, the only one we have encountered is __init__, but there are several others.
They are used to create functionality that can't be represented as a normal method.

One common use of them is operator overloading.
This means defining operators for custom classes that allow operators such as + and * to be used on them.
An example magic method is __add__ for +

More magic methods for common operators:

__add__ for +
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |

Python also provides magic methods for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__.
There are no other relationships between the other operators.

There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions,
and __int__, __str__, and the like, for converting objects to built-in types.
"""

# Below is to override the subtraction operator '-'
class CustomMath:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def __sub__(self, other):
        return CustomMath(self.x - other.x, self.y - other.y)

first = CustomMath(10, 20)
second = CustomMath(15, 27)
difference = first - second
another_difference = second - first

print (str(difference.x) + " & " + str(difference.y))
print (str(another_difference.x) + " & " + str(another_difference.y))

# And completely altering the behavior of division
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other):
    line = "=" * len(other.cont)
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

# Now overriding the greater than operator as in below
class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __gt__(self, other):
    for index in range(len(other.cont)+1):
      result = other.cont[:index] + ">" + self.cont
      result += ">" + other.cont[index:]
      print(result)

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

# For overriding other class methods
import random

class VagueList:
  def __init__(self, cont):
    self.cont = cont

  def __getitem__(self, index):
    return self.cont[index + random.randint(-1, 1)]

  def __len__(self):
    return random.randint(0, len(self.cont)*2)

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

"""
Object Life-cycles
______ ___________
~~~~~~ ~~~~~~~~~~~

The lifecycle of an object is made up of its 
* creation, 
* manipulation, and 
* destruction.

The first stage of the life-cycle of an object is the definition of the class to which it belongs.

The next stage is the instantiation of an instance, when __init__ is called. Memory is allocated to store the instance. 
Just before this occurs, the __new__ method of the class is called. This is usually overridden only in special cases.

After this has happened, the object is ready to be used.

Other code can then interact with the object, by calling functions on it and accessing its attributes. 
Eventually, it will finish being used, and can be destroyed.



"""