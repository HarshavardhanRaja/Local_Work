"""
given a string S consisting of N letters 'a' and/or 'b'

Returns True when all occurrences of letter 'a' are before all occurrences of letter 'b'
and returns False otherwise


S = 'aabbb' True
S = 'ba'    False
S = 'aaa'   True
S = 'b'     True
S = 'abba'  False


"""

def solve(s):

    temp = False
    for i in s:
        if i == 'b':
            temp = True
        if i == 'a' and temp:
            return False
    return True



if __name__ == '__main__':
    S1 = 'aabbb' 
    S2 = 'ba'    
    S3 = 'aaa'   
    S4 = 'b'     
    S5 = 'abba' 

    print(solve(S5))