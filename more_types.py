# Let's get to know more about types in Python Programming

"""
The 'None' object is used to represent the absence of a value.
It is similar to null in other programming languages.
Like other "empty" values, such as 0, [] and the empty string, it is False when converted to a Boolean variable.
When entered at the Python console, it is displayed as the empty string.

PS : 'None' is a keyword and is case-sensitive. Typing 'none' will be considered a different variable
"""

print(None)                 # None
print(type(None))           # <class 'NoneType'>
print(str(None))            # 'None'
print(str(None) == '')      # False
print(str(None) == 'None')  # True
print(bool(None))           # False

# This 'None' type will be returned by any function with no return value
def none_ret_func():
    print('Inside the function !')

print(none_ret_func())

# Now we get into the 'Dictionaries' type
"""
Dictionaries are data structures used to map arbitrary keys to values. 
Lists can be thought of as dictionaries with integer keys within a certain range.
Dictionaries can be indexed in the same way as lists, using square brackets containing keys.

PS : Does this sounds familiar.... yes it is like the Map<?, ?> in Java
"""

nums = {1:"One", 2:"Two", 3:"Three"}
print(nums[1])
print('The string equivalent of 3 is ' + str(nums[3]))
print(nums[4]) # Oh !!! This one throws KeyError, something like out of bound index

# Only immutable objects can be used as keys. Else it raises an TypeError
colors = {"Red":[255, 0, 0], "Green":[0, 255, 0], "Blue": [0, 0, 255]}
print(colors["Red"][0])
print(colors["Red"][1])
print(colors["Blue"][2])

# Assigning new values to dictionaries
colors["max"] = [255, 255, 255]
colors["min"] = [0, 0, 0]
print(colors)

print("Yellow" in colors)
print("Green" in colors)

if "Yellow" not in colors:
    colors["Yellow"] = [255, 255, 0]
print(colors)

# Items from the dictionaries can be obtained using 'get' function too. But for unavailable keys too
print(colors.get("Yellow"))
print(colors.get("min"))
print(colors.get("mid")) # Returns None type
print(colors.get("new", "This key is not found in colors dictionary")) # Prints the message instead of 'None'

# Here comes the 'Tuples' - Immutable lists - Arrays.asList({}) in Java
"""
Tuples are very similar to lists, except that they are immutable (they cannot be changed). 
Also, they are created using parentheses, rather than square brackets. 
"""

words = ('Spam', 'Eggs', 'Sausages')
print(words)
print('Spam' in words)      # True
print('Bacon' in words)     # False
print(words[2])             # 'Sausages'

# Re-assigning an existing value
words[2] = 'Lettuce' # This will raise a TypeError :
print(words[2])

# Another way of creating a tuple
another_tuple = "One", "Two", "Three"
print(another_tuple)

# List Slices
"""
List slices provide a more advanced way of retrieving values from a list. Basic list slicing involves indexing a 
list with two colon-separated integers. 

This returns a new list containing all the values in the old list between the indices.
"""

my_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
sliced_list = my_list[3:8] # the second index is exclusive, same as list-range
print(my_list)
print(sliced_list)

print(my_list[:5]) # Equal to my_list[0:5]
print(my_list[5:]) # Equal to my_list[5:len(my_list)]

# A third parameter can be used to specify the interval to be retrieved in the slice
print(my_list[1::2]) # To print the second number from its first index - Even numbers
print(my_list[2:10:3]) # To print the third index from the previous one - Multiples of three
print(my_list[::-1]) # Reverse slicing - reverses the list
print(my_list[-1:2]) # Prints the last value in the list

# List Comprehension - Used to create simple list obeying certain simple rules
print([i * 3 for i in range(0,11)])

# we can also comprehend the list using IF statement
comp_list = [i ** 2 for i in range(1, 11) if i ** 2 % 2 == 0] # List of square numbers that are even numbers
print(comp_list)
print(add(comp_list))

# Beware... the comprehension cannot be used for extensive range

# Now it's time for some String formatting operations
print("Some of the values in my_list object are {0}, {2} and {1}".format(my_list[0], my_list[1], my_list[2]))
print("Another kind of formatted values are {one} and {two}".format(one=sliced_list[2], two=sliced_list[3]))

# String Functions
"""
Python contains many useful built-in functions and methods to accomplish common tasks. 
join - joins a list of strings with another string as a separator. 
replace - replaces one substring in a string with another.
startswith and endswith - determine if there is a substring at the start and end of a string, respectively. 
To change the case of a string, you can use lower and upper.
The method split is the opposite of join, turning a string with a certain separator into a list.
"""

print("|".join(my_list))
print("Hello World !".replace("World", "Vignesh"))
print("Vignesh".startswith("V"))     # True
print("Vignesh".startswith("v"))     # False
print("Vignesh".endswith("h"))      # True
print(''.join(list("Vignesh")[::-1])) # Reverses the string
print('Test'.upper())
print('HELLO'.lower())

# Numerical Functions
"""
To find the maximum or minimum of some numbers or a list, you can use max or min.
To find the distance of a number from zero (its absolute value), use abs.
To round a number to a certain number of decimal places, use round.
To find the total of a list, use sum.
"""

print(min(1, 2, 3, 4, 0, 2, 1))
print(max([1, 4, 9, 2, 5, 6, 8]))
print(abs(-99))
print(abs(42))
print(round(1.45))
print(sum([1, 2, 3, 4, 5]))

# List Functions
"""
Often used in conditional statements, all and any take a list as an argument, and return True if all 
or any (respectively) of their arguments evaluate to True (and False otherwise). 

The function enumerate can be used to iterate through the values and indices of a list simultaneously.
"""

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(all([i < 11 for i in num_list])) # True - Since all are less than 11
print(all([i == 1 for i in num_list])) # False - All except 1 are not equal to 1
print(any([i % 3 == 0 for i in num_list])) # True - , 6 and 9 are satisfying the condition

for v in enumerate(num_list):
    print(v)

# Text Analyzer
sample_text = "lorem ipsum dolor"
for char in sample_text:
    print(char)