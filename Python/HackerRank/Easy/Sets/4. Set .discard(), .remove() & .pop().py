# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem


#Concept:
"""
.remove(x):
    This operation removes element  from the set.
    If element  does not exist, it raises a KeyError.
    The .remove(x) operation returns None.

.discard(x):
    This operation also removes element  from the set.
    If element x does not exist, it does not raise a KeyError.
    The .discard(x) operation returns None.

pop():
    This operation removes and return an arbitrary element from the set.
    If there are no elements to remove, it raises a KeyError.


"""

n = int(input())
s = set(map(int, input().split()))
commands = int(input())

for i in range(commands):
    task = input().split()
    if task[0] == 'pop':
        s.pop()
    elif task[0] == 'remove':
        s.remove(int(task[1]))
    elif task[0] == 'discard':
        s.discard(int(task[1]))
        
print(sum(s))