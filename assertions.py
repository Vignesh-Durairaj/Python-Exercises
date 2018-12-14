# An assertion is a sanity-check that you can turn on or turn off when you have finished testing the program

def multiply(a, b):
    return a * b

assert multiply(2, 2) == 4
assert multiply(1, 1) == 2, 'Multiplication function fails' # This will raise an AssertionError