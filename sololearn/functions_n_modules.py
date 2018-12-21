# Let's get to know a little about FUNCTIONS in python.

import random
from math import sqrt as square_root_func, pi # This is like static imports in Java, where we import particular class components

def hello(name):
    print('Hello ' + str(name))

def repeat_hello(name, number):
    for x in range(0, int(number)): # use 'xrange' instead of range for 3.x interpreter
        hello(name)

# Below is the cleaner version of the same function
def clean_repeat_hello(name, number):
    """
    A sample function to repeat the input string for a certain number of times, each in a new line.

    :param name: Any string value to be printed
    :param number: Number of times the NAME parameter should be printed
    :return: No value / void
    """
    print((name + '\n') * int(number))

hello('Vignesh')
hello ('Durairaj')

repeat_hello('Vignesh', 5)
clean_repeat_hello('Durairaj', 3)
# And remember, python interpreter reads the code from top to bottom.
# So it's better to define the function before using them.

# Everything is fine. But how to we get the value back from a function
def min(x, y):
    if x < y:
        return x
    else:
        return y

    print ('Whatever comes here will not be executed.')

print(min(-1, 0))
print(min(-1, -30))
print(min(1, 2))
print(min('A', 'a'))

# Did you know that we can assign a function to a variable too !!
smaller = min
print(smaller(10, 11))

# Also you can use a function as a parameter too !
clean_repeat_hello('A string', smaller(3, 2))

# And the function as a object can be used in the parameter !
def function_caller(func_name, arg_one, arg_two):
    print(func_name(arg_one, arg_two))

function_caller(smaller, 10, -10)

# Let's get introduced to MODULES in python programming

for x in range(0, 5):
    print(random.randint(10, 100)) # In this line, the 'random' is a module and we are using its function 'randint'

print(pi)
print(square_root_func(81))

"""
There are three main types of modules in Python, those you write yourself, those you install from external sources, 
and those that are pre-installed with Python. The last type is called the standard library, and contains many useful 
modules. Some of the standard library's useful modules include string, re, datetime, math, random, os, multiprocessing, 
subprocess, socket, email, json, doctest, unittest, pdb, argparse and sys.

Tasks that can be done by the standard library include string parsing, data serialization, testing, debugging and 
manipulating dates, emails, command line arguments, and much more! Python's extensive standard library is one of its 
main strengths as a language.
"""

# PyPI - Python package index
# pip - The program used to install those PyPI