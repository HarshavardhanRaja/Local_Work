person = {'name': 'Jenn', 'age': 23}

# sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
# print(sentence)


# sentence = 'My name is {} and I am {} years old.'.format(person['name'], person['age'])
# print(sentence)


# sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# print(sentence)

# sentence = 'My name is {0[name]} and I am {1[age]} years old.'.format(person, person)
# print(sentence)

# sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person )
# print(sentence)


# tag = 'h1'
# text = 'This is a headline'

# sentence = '<{0}>{1}</{0}>'.format(tag, text)
# print(sentence)


sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
print(sentence)


class Person():

    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Jack', '33')

sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)

# sentence = 'My name is {name} and I am {age} years old.'.format(name='Jenn', age='30')
# print(sentence)

#unpacking dictonary and print the values of keys 
# sentence = 'My name is {name} and I am {age} years old.'.format(**person)
# print(sentence)



# for i in range(1, 11):
#     sentence = 'The value is {}'.format(i)
#     print(sentence)

# if you want the numbers to be printed with two digits
# sentence = 'The value is {:2}'.format(i)  here 2 => 2 digits


# pi = 3.14159265

# sentence = 'Pi is equal to {:.2f}'.format(pi)  2f=> s decimal places

# print(sentence)


sentence = '1 MB is equal to {:,} bytes'.format(1000**2)

print(sentence)

sentence = '1 MB is equal to {:,.3f} bytes'.format(1000**2)

print(sentence)

import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

# print(my_date)

# March 01, 2016

sentence = '{:%B %d, %Y}'.format(my_date)

print(sentence)

# March 01, 2016 fell on a Tuesday and was the 061 day of the year.
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)

print(sentence)