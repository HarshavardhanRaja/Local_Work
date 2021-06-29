# https://www.programiz.com/python-programming/regex
# https://www.w3schools.com/python/python_regex.asp
# https://www.tutorialspoint.com/python/python_reg_expressions.htm

# How to Write and Match Regular Expressions (Regex)
# Regualr Expressions are used search for text patterns within text editors, etc
# allow us to search for and match specific patterns of text
import re
from typing import Pattern


text_to_search = '''
abcdefghijklmnopqurtuvwxyz 
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''




"""
# Raw String:
# raw string in python is just a string prefixed with an r
# that tells python not to handle backslaches in any special way
print('\t Tab')
print(r'\t Tab')


# re.compile method allows us to seperate out our patterns into a variable 
# and also we'll use that variable to perform multiple searches 

pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)
# span(1,4) => begining and end index of the matched pattern
print(text_to_search[1:4])
"""


# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )
# If we want to search for above meta charecters then we need to add backslash to the raw text
# pattern = re.compile(r'\.')          
# pattern = re.compile(r'coreyms\.ms')      here we are trying to find coreyms.com


"""
# pattern = re.compile(r'\d\d\d')
# pattern = re.compile(r'\d\d\d.')

pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')           # using charecter set ==> [characters to be matched]
pattern = re.compile(r'[8-9]00[-.]\d\d\d[-.]\d\d\d\d')          # prints numbers starting with 800/900

wthtin character set '-' is special charecter as well,
i.e when it is put at the beginning or end it will just match the literal - charecter
but when placed between values it specifies a range of values
ex:- [1-5]->digits between 1 to 5, [a-z], [A-Z], [a-zA-Z]

'^' -> caret symbol negates the things specified in charecter set 
i.e [^1-5] => finds every digit except between the range 1 to 5

Quantifiers: used to match multiple charecters at a time
pattern = re.compile(r'Mr\.?\s[A-Z]\w*')


group:
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')


matches = pattern.finditer(text_to_search)
for match in matches:
    print(match)
"""


# parse out phone numbers from text file in raw code
with open('./Raw_code/data.txt', 'r') as f:
    contents = f.read()

    pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    matches = pattern.finditer(contents)
    for match in matches:
        print(match)
