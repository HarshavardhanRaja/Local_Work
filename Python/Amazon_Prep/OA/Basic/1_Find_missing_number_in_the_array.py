"""
You are given an array of positive numbers from 1 to n, 
such that all numbers from 1 to n are present except one number x. 
You have to find x. 
The input array is not sorted. 
Look at the below array and give it a try before checking the solution.

[3, 7, 1, 2, 8, 4, 5]
n =8 and missing number =6

"""

def brute_force(a):
    """
    Time Complexity: O(n^2)
    Space Comlexity: O(1)
    """
    n = len(a) + 1
    for i in range(1,n):
        if i not in a:
            return i


def find_missing(a):
    """
    Time Complexity : O(n)
    Space Complexity : O(c)
    """
    n = len(a)+1
    expected_sum = n*(n+1)/2
    actual_sum = sum(a)
    return int(expected_sum - actual_sum)

    

if __name__ == '__main__':
    a = [3, 7, 1, 2, 8, 4, 5]
    print(find_missing(a))
    print(brute_force(a))