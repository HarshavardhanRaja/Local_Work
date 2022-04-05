

def largestLastElement(N, arr):
    """
    Given an array of integers of size N
    Rearrange the array in any order you want before performing the operations
    operations: 1. Take sum of every consecutive pair in arr and create another array B1 of size N-1.
                2. repeat the operation till exactly one element stored in the array Bn
    Find the maximum possible value that will be stored in Bn. Since this value can be very large return it modulo 10^9+7
    """
    if N == 1:
        return arr[0]
    else:
        B1 = [0] * (N - 1)
        for i in range(N - 1):
            B1[i] = arr[i] + arr[i + 1]
        return largestLastElement(N - 1, B1)

print(largestLastElement(3, [1, 1, 2]))






