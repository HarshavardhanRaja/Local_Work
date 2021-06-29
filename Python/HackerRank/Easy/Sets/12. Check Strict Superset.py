# https://www.hackerrank.com/challenges/py-check-strict-superset/problem


a = set(map(int, input().split()))
no_sets = int(input())
temp = 0
for i in range(no_sets):
    b = set(map(int, input().split()))
    if b.intersection(a) == b and len(b)<len(a):
        temp +=1
    else:
        temp = 0
        print(False)
        break

if temp:
    print(True)