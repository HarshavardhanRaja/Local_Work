# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem
"""
A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
Basically, sets are used for membership testing and eliminating duplicate entries.
"""

def average(array):
    # your code goes here
    array = set(array)
    return round(sum(array)/len(array),3)
    #print(round(mean(array),3))
    # return average(array)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)