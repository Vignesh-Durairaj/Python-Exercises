# Here's the interesting part. File processing !!!

# Let us try opening a file
dataFile = open('data.txt')

# And it is advisable to close the file once opened
dataFile.close()
del dataFile

"""
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default. 
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

The default mode is "r" read mode.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
For example:
# write mode
open("filename.txt", "w")

# read mode
open("filename.txt", "r")
open("filename.txt")

# binary write mode
open("filename.txt", "wb")
"""

# Let us try read the whole file content again
myFile = open('data.txt', 'r')
fileData = myFile.read()
print(fileData)
print(type(fileData))
myFile.close()

# Files can be read for certain amount of bytes as below
newFile = open('data.txt', 'r')
print(newFile.read(10))
print(newFile.read(3))
print(newFile.read(2))

# Reading the rest of the file
print(newFile.read(-2))

print("Trying the read the file after the end")
print(newFile.read())
newFile.close()

# Files can be read line by line as well
file_obj = open('data.txt')
print(file_obj.printlines()) # Exclusive to Python 3.x and it raises AttributeError in older versions
file_obj.close()

# Or better, it can be iterated for lines
file = open('data.txt')
line_num = 0
for i in file:
    line_num += 1
    print('Data in line number %s' % line_num)
    print(i)
file.close()


# How about writing some data into the file.
# But this re-create the file, after removing the old contents

file_item = open('new_data.txt', 'w')
data_written = file_item.write('| PRANOV            | SARAVANAN         | POLLACHI          |')
print(data_written) # this prints the number of bytes written
file_item.close()

# And it always recommended to handled the Exception cases, while working with the files
try:
    new_file = open('new_data.txt', 'r')
    print(new_file.read())
finally:
    new_file.close();

# Else better use 'with' which automatically closes the file instance
with open('new_data.txt', 'r') as file_contents:
    print(file_contents.read())