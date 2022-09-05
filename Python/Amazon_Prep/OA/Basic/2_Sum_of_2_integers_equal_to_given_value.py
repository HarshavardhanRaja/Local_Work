"""
Given an array of integers and a value, 
determine if there are any two integers in the array whose sum is equal to the given value. 
Return true if the sum exists and return false if it does not. 

Consider this array and the target sums:
a = [5, 7, 1, 2, 8, 4, 3]
target_sum = 10 or target_sum = 19
"""

from operator import le


def brute_force(a, v):
    """
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(a)):
        for j in range(len(a)):
            if i == j:
                continue
            elif a[i] + a[j] == v :
                return True
    return False


def find_sum_of_two(a, v):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    ref = set()
    for i in range(len(a)):
        ref.add(a[i])
    for i in range(len(a)):
        if v - a[i] in ref:
            return True
    return False



if __name__ == "__main__":
    a = [5, 7, 1, 2, 8, 4, 3]
    print(brute_force(a, 10))
    print(find_sum_of_two(a, 19))