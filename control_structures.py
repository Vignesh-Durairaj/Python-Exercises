# And we start with some Booleans and relational operators
boolean_a = True
print (boolean_a)

print ('Str' == 'Str')
print (1 == 2)

print ('Str' != 'Str')
print (2 > 1)
print (str(31 >= 31))

# ooooh.... It checks the Lexicographical order too
print ('z' > 'c')
print ('ABSOLUTE' < 'absolution')

# Lets work upon some control structures in python programming language
if boolean_a:
    print ('Variable Boolean_a was initialized as True')
    print ('Still inside the if block')
else:
    print ('Variable Boolean_b was initialized as False')

print ('Outside the IF block !')  # And notice these indentations

spam = 7
if spam > 5:
    print("five")
    if spam > 6:
        print ("Greater than six")
elif spam > 6:
    print ("Again it is greater than six")
if spam > 8:
    print("eight")

num = 7
if num == 5:
  print("Number is 5")
else:
  if num == 11:
    print("Number is 11")
  else:
    if num == 7:
      print("Number is 7")
    else:
      print("Number isn't 5, 11 or 7")

if not (1 == 2):
    print("Yes! One is not equal to two")

# And note that... when it comes to order of precedence == and the != has the higher order of precedence than the AND or OR operators

print (False == True or False) # This should give False
print (False == (True or False)) # This will give out False as well, since False is  not equal to True
print ((False == False) and True) # False again

# Now coming to whole loops.
i = 10
while i >= 1:
    print ("Value of I is : " + str(i))
    i -= 1;
    if i == 2:
        print("Breaking at 2")
        break
    elif i == 4:
        print("skipping the Holla at 4")
        continue

    print ("Holla !")
print ("Out of the while loop now !")

i = 5
while True:
  print(i)
  i = i - 1
  if i <= 2:
    break


# Here comes the Lists.
my_list = ["Apples", "Oranges", "Bananas"]
for fruits in my_list:
    print(fruits)

print (my_list[0] + " & " + my_list[1])

another_list = []
print(my_list)
print(another_list)

number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])
print(things[0][3])

my_list[2] = 'Grapes'
print(my_list)

my_list += ['Bananas']
print(my_list)
my_list *= 2
print(my_list)

print ('Grapes' in my_list)
print ('Grapes' in another_list)
print ('Pears' not in my_list)
print (not 'Grapes' in my_list)