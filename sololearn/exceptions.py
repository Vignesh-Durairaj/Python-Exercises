# Getting started with the Exceptions in Python language
"""
Exception occurs in case of undesirable inputs or unexpected code lines.
Like in other programming languages, Exceptions can be handled in python as well.
"""

try:
    num_one = 7
    num_two = 0
    print(num_one / num_two)
    print('End of TRY block')
except ZeroDivisionError:
    print ("number cannot be divided by zero")

# Multiple exception can be handled based on the exception type

try:
    var_one = 'abc'
    var_two = 10
    print(var_two + var_one)
    print(var_one + var_two)
except ValueError:
    print("Invalid values specified in the function arguments")
except TypeError:
    print("Invalid types of arguments specified")
except (SyntaxError, NameError):
    print("Invalid code statement / variables used")
except:
    print("Any other exception occurred")
print("End of program")

# Guess what, we can have some finally statement too, as in Java.
# And it runs even in case of uncaught exceptions too, but exception will be raised
try:
    print("5" + 2)
except TypeError:
    print("Invalid type specified")
except ValueError:
    print("Invalid value specified")
finally:
    print("Whatever happens, I execute before I move out !")

# We can raise an exception explicitly as in the below
print(1)
raise TypeError
print(2)

# Both Errors will be raised when we raise one in the catch block
try:
  print(1 / 0)
except ZeroDivisionError:
  raise ValueError

# Exception can be raised with customer messages as arguments
name = '123'
raise NameError("Variable name should not be simply 'name'")