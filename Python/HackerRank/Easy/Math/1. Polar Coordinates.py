# https://www.hackerrank.com/challenges/polar-coordinates/problem


import cmath
point = complex(input())
r = cmath.sqrt(point.real**2 + point.imag**2)
phi = cmath.phase(complex(point.real,point.imag))
print(r.real)
print(phi)