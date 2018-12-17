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

