# https://www.hackerrank.com/challenges/py-set-difference-operation/problem


# Concepts
"""
.difference():
    The tool .difference() returns a set with all the elements from the set that are not in an iterable.
    Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
    Set is immutable to the .difference() operation (or the - operation).


"""


n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
print(len(a.difference(b)))