# Welcome to the world of functional programming
"""
Functional programming is a style of programming that (as the name suggests) is based around functions.

A key part of functional programming is higher-order functions. We have seen this idea briefly in the previous lesson
on functions as objects. Higher-order functions take other functions as arguments, or return them as results.
"""

# Let's consider the below case

def print_twice(in_str):
    print((in_str + "\n") * 2)

def func_caller(func, in_arg):
    return func(in_arg)

func_caller(print_twice, "Welcome Vignesh")

"""
Functional programming seeks to use pure functions. Pure functions have no side effects, and return a value 
that depends only on their arguments.

This is how functions in math work: 
for example, The cos(x) will, for the same value of x, always return the same result.

Using pure functions has both advantages and disadvantages. 
Pure functions are:
- easier to reason about and test.
- more efficient. Once the function has been evaluated for an input, 
the result can be stored and referred to the next time the function of that input is needed, 
reducing the number of times the function is called. This is called memoization.
- easier to run in parallel.
-The main disadvantage of using only pure functions is that they majorly complicate the otherwise simple task of I/O, 
since this appears to inherently require side effects. 
They can also be more difficult to write in some situations.
"""

# Lambdas
# Considering the above example, that takes in one function with single arguement
val = func_caller(lambda x: x * 2, 24) # Equal to fun name(x): return x*2; name(24)
print(val)

# Let us transform the below named function into a lambda
def polynomial(x):
    return x**2 + 5*x + 4

print(polynomial(-4))

# Converting to Lambda
print((lambda x: x**2 + 5*x + 4) (-4))

# Lambda's can be assigned to variables to, like named functions
square = (lambda x: x**2)
print(square(4))

# The map function takes a function and an iterable as arg and returns a new iterable object,
# with that function applied.
# This is similar to Streamable.stream().map(converter<>) in Java 8

nums = list(range(1, 11))
print(nums)

doubled_nums = list(map(lambda x: x * 2, nums))
print(doubled_nums)

# Filter function
filtered_nums = list(filter(lambda x : x > 10, doubled_nums))
print(filtered_nums)

"""
Generators are a type of iterable, like lists or tuples. 
Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops. 
They can be created using functions and the yield statement.
"""

def count_down():
    i = 5
    while i > 0:
        yield i
        i -= 1

print(count_down())
for i in count_down():
    print(i)

# Finite generators can be converted into lists by passing them as arguments to the list function.
print(list(count_down()))

"""
Decorators provide a way to modify functions using other functions. 
This is ideal when you need to extend the functionality of functions that you don't want to modify.

This sounds more like the decorator pattern
"""

def my_decorator(func, name):
    def cover():
        print("=================")
        func(name)
        print("=================")
    return cover

def say_hello(name):
    print("Hello " + name + " !")

decor = my_decorator(say_hello, "Vikhi")
decor()

def new_decorator(func):
    def new_wrap():
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
        func()
        print("~~~~~~~~~~~~~~~~~~~~~~~~")
    return new_wrap()

# Another way to decorate a function
# The above annotated statement itself calls the decorated functions
@new_decorator
def print_name():
    print("Another shout out to Python 3 !")

"""
Recursion is a very important concept in functional programming. 
The fundamental part of recursion is self-reference - functions calling themselves. It is used to solve problems that 
can be broken up into easier sub-problems of the same type.

A classic example of a function that is implemented recursively is the factorial function, which finds the product of 
all positive integers below a specified number. For example, 5! (5 factorial) is 5 * 4 * 3 * 2 * 1 (120). To implement 
this recursively, notice that 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, and so on. Generally, n! = n * (n-1)!. 
Furthermore, 1! = 1. This is known as the base case, as it can be calculated without performing any more factorials. 
"""

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))

"""
Sets are data structures, similar to lists or dictionaries. They are created using curly braces, or the set function. 
They share some functionality with lists, such as the use of in to check whether they contain a particular item.

* Set are un-ordered, i.e., it can't be indexed
* Set cannot contain duplications
* It's kinda sorted (refer first point)
* append cannot be used in this iteable type, and instead add can be used
* remove - removes an element specified
* pop - removes the arbitraty elements
"""

num_set = {1, 2, 3, 4, 5, 6, 8, 7, 6}
print(num_set)
print(4 in num_set) # True
print(12 in num_set) # False
num_set.remove(6)
print(num_set) # {1, 2, 3, 4, 5, 7, 8}
num_set.pop()
print(num_set) # {2, 3, 4, 5, 7, 8}
num_set.add(1)
num_set.add(6)
print(num_set) # Original Set

# Set can be used for mathematical operations like
# union - |,
# intersection - &,
# difference - '-',
# symmetric_difference - ^

another_set = {5, 6, 7, 8, 9, 10}
print(another_set)
print(num_set | another_set)
print(num_set & another_set)
print(num_set - another_set)
print(num_set ^ another_set)

# itertools
"""
The module itertools is a standard library that contains several functions that are useful in functional programming. 
One type of function it produces is infinite iterators. 
The function count counts up infinitely from a value. 
The function cycle infinitely iterates through an iterable (for instance a list or string). 
The function repeat repeats an object, either infinitely or a specific number of times.
"""

from itertools import count
for i in count(10): # Count(10) - counter starts from 10. If left empty it starts from 0
    print(i)
    if count >= 30:
        break;

# certain other itertools are used for functional programming as in below
#
# itertools.accumulate - returns a running total of values in an iterable
# itertools.takewhile - takes items from an iterable while a predicate function remains true
# itertools.chain - combines several iterables into one long one

from itertools import accumulate, takewhile, chain, product, permutations

nums_sum = list(accumulate(num_set))
print(nums_sum)

nums_sum_new = list(takewhile(lambda x: x % 9 != 0, nums_sum))
print(nums_sum_new)

letters = ("A", "B")
numbers = ("2", "4")
print(list(product(letters, numbers)))
print(list(permutations(letters)))
print(list(permutations(numbers)))
print(list(product(permutations(letters), permutations(numbers))))