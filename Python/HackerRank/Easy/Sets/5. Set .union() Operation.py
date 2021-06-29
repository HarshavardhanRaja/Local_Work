# https://www.hackerrank.com/challenges/py-set-union/problem


#concepts
"""
.union():
    The .union() operator returns the union of a set and the set of elements in an iterable.
    Sometimes, the | operator is used in place of .union() operator, but it operates only on the set of elements in set.
    Set is immutable to the .union() operation (or | operation).


"""


n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
print(len(a.union(b)))