
# Let's have a simple calculator

__author__ = "Vignesh Durairaj <vignesh87.srkv@gmail.com>"

import os

while True:

    os.system('clr')
    os.system('clear')

    print("Options:")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to end the program")
    user_input = input("Operation : ")

    if user_input == "quit":
        break
    elif user_input in ['add', 'subtract', 'multiply', 'divide']:
        num_one = input("Enter value for number 1 : ")
        num_two = input("Enter value for number 2 : ")

        if user_input == "add":
            print("The addition of " + str(num_one) + " and " + str(num_two) + " : " + str(num_one + num_two))
        elif user_input == "subtract":
            print("The subtraction of " + str(num_one) + " and " + str(num_two) + " : " + str(num_one - num_two))
        elif user_input == "multiply":
            print("The product of " + str(num_one) + " and " + str(num_two) + " : " + str(num_one * num_two))
        elif user_input == "divide":
            print("The division of " + str(num_one) + " and " + str(num_two) + " : " + str(num_one / num_two))
    else:
        print("Unknown input")

    dummy = raw_input('Press Enter to move on...')