
name = input('Enter your name:')
print('Hello', name.title())

# input method takes string as a input by default
# if you want to use a number then you have to wrap input method with int or float

int_num = int(input('Enter an Integer:'))
int_num +=10
print(int_num)


dec_num = float(input('Enter a decimal:'))
dec_num +=12.2
print(dec_num)

# if you want an integer but given float then you can use,
# int_from_float = int(float(input('Enter a number:)))

"""
The eval() method parses the expression passed to this method and runs python expression (code) within the program.
In simple terms, the eval() function runs the python code (which is passed as an argument) within the program.


x = 1
print(eval('x + 1'))

output => 2

evaluates a string as a line in python
you can even include variables in a string like this
"""

x = eval(input('Enter an expression: '))
print(x)


num = 30 
x = eval('num + 42')
print(x)



