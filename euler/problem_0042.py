# Coded triangle numbers
#
# The n-th term of the sequence of triangle numbers is given by, tn = n(n+1)/2; so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we
# form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
# number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common
# English words, how many are triangle words?

"""
Solution Approach :
===================
* This one is pretty simple and straight forward
* Assumption made was that the longest common English word is 100 characters of length, let's generate a sequence of
integers that are triangular till 2600
* Initialize another array of alphabets in upper case, with blank as first char and then followed by 'A' to 'Z'
* Calculate a words numeric equivalent from the alphabet list
* Parse the file and get the list of words
* Filter the list whose equivalent numeric value is summing up for a triangular number
* Get the length of the filtered list, which is the solution
"""


def get_triangle_seq(max_cap):
    triangle_sequence, n = [], 1
    while True:
        triangle_num = n * (n + 1) // 2
        triangle_sequence.append(triangle_num)
        if triangle_num > max_cap: break
        else: n += 1
    return triangle_sequence


alphabets = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X', 'Y', 'Z']
triangle_seq = get_triangle_seq(2600) # Considering the largest common english word is 100 characters of length


def is_triangle_word(word):
    char_val = 0
    for char in word:
        char_val += alphabets.index(char)
    return True if char_val in triangle_seq else False


def get_triangular_word_count():
    f = open('p042_words.txt', 'r');
    data = f.read()
    f.close()
    all_words = list(map(lambda word: word.replace('"', ''), data.split(',')))
    triangular_words = list(filter(is_triangle_word, all_words))
    return len(triangular_words)


print(get_triangular_word_count())
