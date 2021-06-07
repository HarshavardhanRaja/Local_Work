
print('===================================start==============================================')
# passing text value directly to print function
print('Hello World')


# passing text value using an variable
message = 'Hello World'
print(message)


# Create muti line string
multi_line_string = """Hello World
sorry Hello Earth"""
print(multi_line_string)


# find out number of characters in a string
print(len(message))
print(len(multi_line_string))


# accessing string charecters individually
print(message[0])       # print first character
print(message[-1])      # print Last character
print(message[0:5])     # print characters in range of a:b (Note a is inclusive but b is not)
print(message[5:])      # print charachters from a to last character 
print(message[:5])      # print characters from first to a



# Important methods/functions of strings
print(message.lower())              # converts all characters to lower case
print(message.upper())              # converts all characters to upper case
print(message.count('hell'))        # count substring occurances
print(multi_line_string.count('hell'))
print(message.find('world'))        # Returns the first index position of the sub-string

# Replace a certain number of characters in a string with other
print(message.replace('world', 'universe'))

# Concatinate strings
greeting = 'Hello'
name = 'Harsha'

# 3 ways of concatinating strings
new_message = greeting + ', ' +  name + '. Welcome!'
new_message1 = '{}, {}. Welcome'.format(greeting, name)     # using format method
new_message2 = f'{greeting}, {name}. Welcome'               # using fstring available only on python with versions > 6

print(new_message)
print(new_message1)
print(new_message1)


# print(dir(name))    # If we pass a variable to dir method then it will show us the all of the attributes and methods that we have access to with that variable
# print(help(str))    # this gives all the methods and attributes assosiated with str in python

# print(help(str.lower))  # to get description of a particular method
print('============================END======================================')

