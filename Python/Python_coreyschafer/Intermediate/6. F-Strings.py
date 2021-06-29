# F-Strings are a new way to format strings in python 3.6 and above

first_name = 'Anthony'
last_name = 'Stark'


"""
using  .format()
sentence = 'I am {} {}'.format(first_name,last_name)
print(sentence)

using f-strings
sentence = f'I am {first_name} {last_name}'
sentence = f'I am {first_name.upper()} {last_name.upper()}'
print(sentence)

"""




# Printing dictonaries values using f string
"""
using .format()
person = {'first_name' : 'Iron', 'Last_name':'Man'}
sentence = 'And I am {} {}'.format(person['first_name'], person['Last_name'])

using f-strings
sentence = f'And I am {person["first_name"]} {person["Last_name"]}'

"""


# calculation
calculation = f'4 times 11 equal to {4*11}'
print(calculation)


# adding padding
"""
for n in range(1,11):
    sentence = f'The values is {n}'
    sentence = f'The values is {n:02}'      # adds 0 padding till 2 digits
    print(sentence)
"""

# working with floating point values
"""
pi = 3.14159265
sentence = f'Pi is equal to {pi}'
sentence = f'Pi is equal to {pi:.4f}'   # rounds to 4 digits after .

"""


# Formatting and printing dates
"""
from datetime import datetime
birthday = datetime(1997,8,6)
sentence = f'Tony has an birthday on {birthday}'
sentence = f'Tony has an birthday on {birthday:%B %d, %Y}'

"""

