"""
Reverse the order of words in a given sentence (an array of characters).

"Hello World" ----> "World Hello"

"""

def reverse_sentence(s):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    s = s.split(' ')
    n = len(s)
    for i in range(int(n/2)):
        temp = s[i]
        s[i] = s[-(i+1)]
        s[-(i+1)] = temp
    return ' '.join(map(str, s))


if __name__ == '__main__':

    s1 = "Hello World"
    s2 = "I have army we have a hulk"
    s3 = "I am Inevitable"
    s4 = "I am Ironman"

    print(reverse_sentence(s2))