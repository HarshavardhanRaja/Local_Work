# https://www.hackerrank.com/challenges/py-check-subset/problem


Test_Cases = int(input())

for i in range(Test_Cases):
    n = int(input())
    a = set(map(int, input().split()))
    m = int(input())
    b = set(map(int, input().split()))
    if a.intersection(b) == a:
        print(True)
    else:
        print(False)