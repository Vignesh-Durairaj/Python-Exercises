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
"""

pattern = r'sp.m'
print(re.match(pattern, "spam"))
print(re.match(pattern, "spAm"))
print(re.match(pattern, "sp1m"))

pattern = r"^gr.y$"
print(re.match(pattern, "gray"))
print(re.match(pattern, "grey"))
print(re.match(pattern, "stingray"))

pattern = r"[aeiouAEIOU]"
print(re.match(pattern, "Grey"))
print(re.match(pattern, "Ant"))
print(re.match(pattern, "Myth"))

pattern = r"[a-z][A-Z][0-9]"
print(re.match(pattern, "Ab1"))
print(re.match(pattern, "cZ3"))
print(re.match(pattern, "Mo12"))

pattern = r"[^0-9]"
print(re.search(pattern, "ABC"))
print(re.search(pattern, "abc12"))
print(re.search(pattern, "123433"))
