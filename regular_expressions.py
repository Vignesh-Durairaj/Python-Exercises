"""
Regular expressions are a powerful tool for various kinds of string manipulation. They are a domain specific language
(DSL) that is present as a library in most modern programming languages, not just Python.

They are useful for two main tasks:
- verifying that strings match a pattern (for instance, that a string has the format of an email address),
- performing substitutions in a string (such as changing all American spellings to British ones).

Domain specific languages are highly specialized mini programming languages.
Regular expressions are a popular example, and SQL (for database manipulation) is another.
Private domain-specific languages are often used for specific industrial purposes.

Regular expressions in Python can be accessed using the re module, which is part of the standard library.

After you've defined a regular expression, the re.match function can be used to determine whether it matches at the
beginning of a string.
If it does, match returns an object representing the match, if not, it returns None.
To avoid any confusion while working with regular expressions, we would use raw strings as r"expression".
Raw strings don't escape anything, which makes use of regular expressions easier.
"""
import re

pattern = r"spam"

if re.match(pattern, "spamEggSpam"):
    print("Match")
else:
    print("No Match")

print(re.match(pattern, "eggspam")) # Returns None type, since the input string not starting with the pattern

"""
Other functions to match patterns are re.search and re.findall. 
The function re.search finds a match of a pattern anywhere in the string.
The function re.findall returns a list of all substrings that match a pattern.
The function re.finditer does the same thing as re.findall, except it returns an iterator, rather than a list.
The function re.sub searches and substitutes the matching words with the new word

The regex search returns an object with several methods that give details about it. 
These methods include group which returns the string matched, start and end which return the start and ending positions 
of the first match, and span which returns the start and end positions of the first match as a tuple.
"""

searches = re.search(pattern, "eggspam")
matches = re.findall(pattern, "My spam is the tastiest spam")
if len(matches) > 0:
    print("Able to find the matching REGEX pattern")
else:
    print("No Matches found")

print(matches) # ['spam', 'spam']
print(searches)
print(searches.group())
print(searches.start())
print(searches.end())
print(searches.span())

newStr = re.sub(pattern, "eggs", "spamspamspamspam")
print(newStr)

"""
Metacharacters

Metacharacters are what make regular expressions more powerful than normal string methods. They allow you to create 
regular expressions to represent concepts like "one or more repetitions of a vowel". 

The existence of metacharacters poses a problem if you want to create a regular expression (or regex) that matches a 
literal metacharacter, such as "$". You can do this by escaping the metacharacters by putting a backslash in front of 
them. However, this can cause problems, since backslashes also have an escaping function in normal Python strings. This 
can mean putting three or four backslashes in a row to do all the escaping. To avoid this, you can use a raw string, 
which is a normal string with an "r" in front of it. We saw usage of raw strings in the previous lesson.

Below are some of the useful Meta-Characters

* .(dot) - This matches any character other than a new line
* set of ^(caret) and $(dollar-sign) - Matches the start and end of string
* [] (square braces) - Character classes - Matching any of the character in the set
* [-] (character classes with Hyphen) - Matching any characters in the range specified
* ^ (caret only) - The invert the character class, when placed first in it. I.E., any character other than the array
* * (asterix) - Zero or more repetitions of the previous thing, which can be anything in parentheses (())
* + (plus) - One or more repetitions of the previous thing, which can be anything
* ? (Quetion mark) - Zero or One repetitions
* {} (curly braces) - Represents the number of repetitions between two numbers. Eg:{2, 4} - Two to four repetitions.
* | (Pipe symbol) - Like this or than. 'Text1|Text2' = Either 'Text1' or 'Text2'
If first number is missing it will be taken as 0. And if second is missing, it will be considered infinity
"""

pattern = r'sp.m'
print(re.match(pattern, "spam"))
print(re.match(pattern, "spAm"))
print(re.match(pattern, "sp1m")) # Returns None

pattern = r"^gr.y$"
print(re.match(pattern, "gray"))
print(re.match(pattern, "grey"))
print(re.match(pattern, "stingray")) # Returns None

pattern = r"[aeiouAEIOU]"
print(re.match(pattern, "Grey"))
print(re.match(pattern, "Ant"))
print(re.match(pattern, "Myth")) # Returns None

pattern = r"[a-z][A-Z][0-9]"
print(re.match(pattern, "Ab1")) # Returns None
print(re.match(pattern, "cZ3"))
print(re.match(pattern, "Mo12")) # Returns None

pattern = r"[^0-9]"
print(re.search(pattern, "ABC"))
print(re.search(pattern, "abc12"))
print(re.search(pattern, "123433")) # Returns None

pattern = r"test([0-9])*"
print(re.match(pattern, "test"))
print(re.match(pattern, "test123"))
print(re.match(pattern, "123_test_new")) # Returns None

pattern = r"test[0-9]+"
print(re.match(pattern, "test")) # Returns None
print(re.match(pattern, "test123"))
print(re.match(pattern, "test_new")) # Returns None

pattern = r"first(-)?name"
print(re.match(pattern, "firstname"))
print(re.match(pattern, "first-name"))
print(re.match(pattern, "first--name")) # Returns None

pattern = r"9(1){1,2}$"
print(re.match(pattern, "91"))
print(re.match(pattern, "911"))
print(re.match(pattern, "9111")) # Returns None
print(re.match(pattern, "911-Emergency")) # Returns None

pattern = r"([a-z]|[0-9])+"
print(re.match(pattern, "test"))
print(re.match(pattern, "123"))
print(re.match(pattern, "TEST")) # returns None
print(re.match(pattern, "*&%")) # returns None

"""
Groups
======

A group can be created by surrounding part of a regular expression with parentheses. This means that a group can be 
given as an argument to metacharacters such as * and ?. Refer few of the above examples.

The content of groups in a match can be accessed using the group function.

A call of group(0) or group() returns the whole match.
A call of group(n), where n is greater than 0, returns the nth group from the left.
The method groups() returns all groups up from 1.

There are several kinds of special groups. 
Two useful ones are 'named groups' and 'non-capturing groups'.

Named groups have the format (?P<name>...), where name is the name of the group, and ... is the content. They behave 
exactly the same as normal groups, except they can be accessed by group(name) in addition to its number.

Non-capturing groups have the format (?:...). They are not accessible by the group method, so they can be added to an 
existing regular expression without breaking the numbering.
"""

pattern = r"a(bc)(de)(f(g)h)i"
match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(2))
   print(match.groups())

pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())

"""
Special Sequences :
===================

There are various special sequences you can use in regular expressions. They are written as a backslash followed by 
another character. One useful special sequence is a backslash and a number between 1 and 99, e.g., \1 or \17. This 
matches the expression of the group of that number. To put that simpler, this matches the pattern for the number of
times ihe group gets repeated

More useful special sequences are \d, \s, and \w. These match digits, whitespace, and word characters respectively. 
In ASCII mode they are equivalent to [0-9], [ \t\n\r\f\v], and [a-zA-Z0-9_]. In Unicode mode they match certain other 
characters, as well. For instance, \w matches letters with accents. Versions of these special sequences with upper case 
letters - \D, \S, and \W - mean the opposite to the lower-case versions. For instance, \D matches anything that isn't a 
digit.

Additional special sequences are \A, \Z, and \b.
The sequences \A and \Z match the beginning and end of a string, respectively. 
The sequence \b matches the empty string between \w and \W characters, or \w characters and the beginning or end of the 
string. Informally, it represents the boundary between words.
The sequence \B matches the empty string anywhere else.
"""

pattern = r"([0-9])\1"
print(re.match(pattern, "999"))
print(re.match(pattern, "111"))
print(re.match(pattern, "344")) # Return None

pattern = r"\D\d"
print(re.match(pattern, "*1"))
print(re.match(pattern, "a1"))
print(re.match(pattern, "21")) # Returns None

"""
Email Extraction :
==================

pattern =  r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
"""

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
   print(match.group())