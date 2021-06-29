# https://www.programiz.com/python-programming/exceptions
# error/exception handeling using try&except blocks


"""
try:
    pass
except Exception:
    pass
else:
    pass
finally:
    pass
"""

# below piece of code throws file not found error
"""
f= open('testfile.txt')
"""
"""
Generalised error/exception
Exception: catches all exceptions or errors


FilenotfoundError

"""

"""
try:
    f = open('testfile.txt')
except Exception:
    print('Sorry this file does not exsists')
"""


# To print error/exception
"""
try:
    f = open('testfile.txt')
except Exception as e:
    print(e)

"""

# except clause runs only when exception happens
# else clause runs when try clause doenot raises any exceptions
# Finally clause runs no matter what happens in try/exception/else clause


try:
    f = open('testfile.txt')
except FileNotFoundError:
    print('Sorry this file does not exsists')
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally.........")

# we can raise an exception manually by using raise
"""
try:
    f = open('testfile.txt')
    if somecondition:
        raise Exception
except FileNotFoundError:
    print('Sorry this file does not exsists')
else:
    print(f.read())
    f.close()
finally:
    print("Executing finally.........")
"""