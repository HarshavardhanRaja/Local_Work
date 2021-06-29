# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem


# concepts
"""
.symmetric_difference():
    The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
    Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
    The set is immutable to the .symmetric_difference() operation (or ^ operation).

it is nothing but 

(a.difference(b))union(b.difference(a))
"""


n = int(input())
a = set(map(int, input().split()))
m = int(input())
b = set(map(int, input().split()))
print(len(a.symmetric_difference(b)))