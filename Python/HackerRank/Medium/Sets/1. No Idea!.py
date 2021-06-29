# https://www.hackerrank.com/challenges/no-idea/problem

n,m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happines = 0
for ar in arr:
    if ar in a:
        happines += 1
    elif ar in b:
        happines -=1
        
# for i in a:
#     if i in arr:
#         happines +=1
# for i in b:
#     if i in arr:
#         happines -= 1
        
print(happines)