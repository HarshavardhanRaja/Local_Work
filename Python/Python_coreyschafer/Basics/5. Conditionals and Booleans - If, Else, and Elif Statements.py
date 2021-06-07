
"""
if condition:
    action



if condition:
    action
else:
    action



if condition:
    action
elif condition:
    action
elif condition:
    action
else:
    action
"""

language = 'python'

if language == 'python':
    print('Conditional is true')


if language == 'python':
    print('Language is python')
else:
    print('language is not python')

language = 'java'
if language == 'python':
    print('Language is python')
elif language == 'java':
    print('Language is java')
elif language == 'js':
    print('Language is js')
else : 
    print('not found')



# Comparissions
# Equal:                        ==
# Not Equal:                    !=           
# Greater than:                 >
# Less than:                    <
# Greater or equal :            >=
# Less or equal :               <=
# Object identity:              is


# Boolean operations 
# and, or, not

user = 'Admin'
looged_in = True

if user == 'Admin' and looged_in == True:
    print(user)
else:
    print('not a valid user')

looged_in = False
if user == 'Admin' and looged_in == True:
    print(user)
else:
    print('not a valid user')

if user == 'Admin' or looged_in == True:
    print(user)
else:
    print('not a valid user')

if not looged_in:
    print('Please log in')
else:
    print('Welcome')





a = [1,2,3]
b = [1,2,3]

print('a=b:', a==b)

print('a is b:', a is b)
print(id(a))
print(id(b))

# a and b though have same values but two different objects
# is checks if both the objects are same or not i.e checks the id not values
# is ---> id(a) == id(b)

a = [1,2,3]
b = a

print('a=b:', a==b)

print('a is b:', a is b)
print(id(a))
print(id(b))



# values python evaluates as False
"""
    -> False
    -> None
    -> Zero of any numeric type
    -> Any empty sequence. For example, '', (), []
    -> Any empty mapping. For example, {}

All other things are considered as true 
"""

