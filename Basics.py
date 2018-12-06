# A sample comment line. Below is my very first code in python
print ("Hello World !")
print ("Welcome to the world of python")
print ("Whatever you type within the 'print' function, it will be shown in the console")
print ("And by the way.... remember SPAM and EGGS");

# Let's do some mathematical operation and pring them in the console.
print ("\n")
print (12 / 7)
print ("Adding 2 and 7 : " + str(2 + 7))
print ("Subtracting 2 and 7 : " + str(2 - 7))
print ("Multiuplying 2 and 7.0 :"  + str (2 * 7.0))
print ("Dividing 2 and 7.0 :"  + str (2 / 7.0))
print ("Remainder while dividing 1.25 with 0.5 : " + str (1.25 % 0.5))
print ("Quotient while dividing 1.25 with 0.5 : " + str (1.25 // 0.5))
print ("2 to the power of 7 : " + str(2 ** 7))

# And some String operations
print ("\n")
print ("A new string with \"escaped character\"")
print ("""Text one; 
	Text Two""")

# Input - Output Operations
print ("\n")
input ("Enter Something : ")
print ("Hello" + ' ' + 'World' + "!")
print ("Let me print this 21 times!\n" * 21)
print (3 * 'Spam and Eggs;')
print (str(1) + str (2))
print (int('21') + int ('3'))
print (str (2) * int ('4'))
print(int(input("Enter Number 1 : ")) + int (input("Enter Number 2 : ")))

# Let's know about variables and its usages
print("\n")
x = 7
print (x)
print (x + 3)
x = "A sample String"
print(x)

del x
x = int(input("Enter a number : "))
y = int(input("Enter another number : "))
print ("The product of %s and %s is %s" % (x, y, x*y))

number = 3
print (number) # 3
number += 2
print (number) # 5
number =+ 2
print (number) # 2. since the variable has been assigned to positive (+) 2.

# It's showtime..... Well some modular quiz
spam = "7"
spam = spam + "0"
eggs = int(spam) + 3
print(float(eggs)) # and the answer is 73.0

word = input("Enter a word : ")
print (word + ' shop') # if the 'Enter a word : ' was 'cheese', then the answer is 'cheese shop'

x = 5
y = x + 3
y = int(str(y) + "2")
print (y) # And it prints 82 in the console

x = 3
num = 17
print(num % x) # 2