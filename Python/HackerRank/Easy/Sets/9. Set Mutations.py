# https://www.hackerrank.com/challenges/py-set-mutations/problem


# Concepts

"""
We have seen the applications of union, intersection, difference and symmetric difference operations, 
but these operations do not make any changes or mutations to the set.


.update() or |= :
    Update the set by adding elements from an iterable/another set.

.intersection_update() or &= :
    Update the set by keeping only the elements found in it and an iterable/another set.

.difference_update() or -= :
    Update the set by removing elements found in an iterable/another set.

.symmetric_difference_update() or ^= :
    Update the set by only keeping the elements found in either set, but not in both.



"""


n = int(input())
a = set(map(int, input().split()))
r = int(input())

for i in range(r):
    task = input().split()
    b = set(map(int, input().split()))
    if task[0] == 'intersection_update':
        a.intersection_update(b)
    elif task[0] == 'update':
        a.update(b)
    elif task[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(b)
    elif task[0] == 'difference_update':
        a.difference_update(b)
        
print(sum(a))