# https://www.hackerrank.com/challenges/py-set-add/problem


# Concept
"""
If we want to add a single element to an existing set, we can use the .add() operation.
It adds the element to the set and returns 'None'.
"""


n = int(input())
country_stamps = set()
for i in range(n):
    country_stamps.add(input())

print(len(country_stamps))