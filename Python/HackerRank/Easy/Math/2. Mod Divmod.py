# https://www.hackerrank.com/challenges/python-mod-divmod/problem


"""
One of the built-in functions of Python is divmod, 
which takes two arguments a and b and 
returns a tuple containing the quotient of a/b first and then the remainder a.
"""

a = int(input())
b = int(input())

print(a//b)
print(a%b)
print(divmod(a,b))