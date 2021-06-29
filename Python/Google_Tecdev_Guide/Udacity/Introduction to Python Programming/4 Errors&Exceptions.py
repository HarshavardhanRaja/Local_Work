# https://docs.python.org/3/library/exceptions.html#bltin-exceptions


"""
Most errors can be separated into two types:

Syntax errors:
    -> occurs when Python can’t interpret our code, since we didn’t follow the correct syntax for Python. 
    -> These are errors you’re likely to get when you make a typo, or you’re first starting to learn Python.


Exceptions:
    -> occur when unexpected things happen during execution of a program, even if the code is syntactically correct. 
    -> There are different types of built-in exceptions in Python, and you can see which exception is thrown in the error message.
There are lot of exceptions some of them are,

ValueError: An object of the correct type but inappropriate value is passed as input to a built-in operation/function
AssertionError: An assert statement fails    
IndexError: A sequence subscript is out of range
KeyError: A key can't be found in a dictonary
TypeError: An object of an unsupported type is passed as input to an operation or function.

"""




# Handling errors
"""
We can use try statements to handle exceptions. 
There are four clauses you can use.

try: This is the only mandatory clause in a try statement.
     The code in this block is the first thing that Python runs in a try statement.

except: If Python runs into an exception while running the try block, 
        it will jump to the except block that handles that exception.

else: If Python runs into no exceptions while running the try block, 
      it will run the code in this block after running the try block.

finally: Before Python leaves this try statement, 
        it will run the code in this finally block under any conditions, even if it's ending the program. 
        E.g., if Python ran into an error while running code in the except or else block, this finally block will still be executed before stopping the program.

"""



"""
We can actually specify which error we want to handle in an except block like this:

try:
    # some code
except ValueError:
    # some code

Now, it catches the ValueError exception, but not other exceptions. 
If we want this handler to address more than one type of exception,
we can include a parenthesized tuple after the except with the exceptions.

try:
    # some code
except (ValueError, KeyboardInterrupt):
    # some code


Or, if we want to execute different blocks of code depending on the exception, 
you can have multiple except blocks.

try:
    # some code
except ValueError:
    # some code
except KeyboardInterrupt:
    # some code

"""



# Accessing Error Messages
"""
When you handle an exception, you can still access its error message like this:

try:
    # some code
except ZeroDivisionError as e:
   # some code
   print("ZeroDivisionError occurred: {}".format(e))

This would print something like this:

ZeroDivisionError occurred: integer division or modulo by zero


So you can still access error messages, even if you handle them to keep your program from crashing!
If you don't have a specific error you're handling, you can still access the message like this:


try:
    # some code
except Exception as e:
   # some code
   print("Exception occurred: {}".format(e))

Exception is just the base class for all built-in exceptions.

"""