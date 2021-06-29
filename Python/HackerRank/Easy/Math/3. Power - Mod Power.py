# https://www.hackerrank.com/challenges/python-power-mod-power/problem

"""
Powers or exponents in Python can be calculated using the built-in power function.
Call the power function  as shown below:
    >>> pow(a,b) 
    or 
    >>> a**b
    

It's also possible to calculate a^b mod(m)
    >>> pow(a,b,m)  
"""


a =int(input())
b =int(input())
m =int(input())

print(a**b)
print(pow(a,b,m))