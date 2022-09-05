# known as Word Break Problem
# https://leetcode.com/problems/word-break/
# https://leetcode.com/problems/word-break-ii/

# https://www.geeksforgeeks.org/word-break-problem-dp-32/
# https://www.techiedelight.com/word-break-problem/
# https://www.interviewkickstart.com/problems/word-break

"""
You are given a dictionary of words and a large input string. 
You have to find out whether the input string can be completely segmented into 
the words of a given dictionary. 

The following two examples elaborate on the problem further.
Given dictonary of words:

{'pie', 'pear', 'peach', 'apple'}
applepie
applepeer

{'now', 'hello', 'hell', 'on'}
hellonow


"""


def brute_force(a, s):
    #Recursive Approach
    """
    Time Complexity: O(2^n)
    Space Complexity: O(n)

    """
    # base cases
    if not s:
        return True
    elif s in a:
        return True   

    for i in range(1, len(s)+1):
        firts_seg = s[0:i]
        second_seg = s[i:]
        if firts_seg in a and brute_force(a, second_seg):
            return True
    return False




def memoization(a, s):
    # memoization
    # Top Down Memoization
    """
    Time Complexity: O(2^n)
    Space Complexity: O(n)

    """
    # base cases
    if not s:
        return True
    elif s in a:
        return True   

    for i in range(1, len(s)+1):
        firts_seg = s[0:i]
        second_seg = s[i:]
        if second_seg not in mem_cache:
            mem_cache[second_seg] =  brute_force(a, second_seg)
        if firts_seg in a and mem_cache[second_seg]: 
            return True
    return False


def dp(a, s):
    # Bootom Up Tabulation
    # Tabulation is the process of storing results of sub-problems from a 
    # bottom up approach sequentially
    """
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    dp = [False for i in range(len(s) +1)]
    dp[0] = True

    for i in range(len(s) +1):
        for j in range(i):
            if dp[j] and s[j:i] in a:
                dp[i] = True

    return dp[len(s)]


if __name__ == "__main__":
    a = {'pie', 'pear', 'peach', 'apple'}
    b = {'now', 'hello', 'hell', 'on'}
    s1 = 'applepiepear'
    s2 = 'applepeer'
    s3 = 'hellonow'
    mem_cache = {}
    # print(brute_force(b, s3))
    print(dp(b, s3))


# take a look at this as well if time permits
#https://leetcode.com/problems/word-break-ii/