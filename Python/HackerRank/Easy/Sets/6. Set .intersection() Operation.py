# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem


#Concepts:
"""
.intersection():
    The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
    Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
    The set is immutable to the .intersection() operation (or & operation).
"""

n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
print(len(a.intersection(b)))