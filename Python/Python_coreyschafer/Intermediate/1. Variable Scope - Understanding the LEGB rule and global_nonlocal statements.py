
# Variable scope
"""
LEGB
Local, Enclosing, Global, Built-in



Local:          Variables defined within a function. Local variable doesnot live outside of that function.
Enclosing:      Are variables in the local scope of enclosing functions
Global:         Are variables defined at the top level of a module or explicitly declared global using global key-word
Built-in:       Are just names that are preassigned in python
"""


x = 'global x'      # here variable x is a global variable because it is at the main body of our python code

def test():
    y = 'local y'   # This y variable is local variable. Local to test function
    print('Prinitng from function:' + y)
    print('Printing from function:'+ x)        # this first checks if there's any local variable with x if not it checks enclosing if not it checks in gloabal scope


test()
# print('Prinitng from main body:' + y) This doesnot works because local variable will not live outside the function
print('Prinitng from main body:' + x)


# if same name for local and global variable
def test1():
    x = 'local x'   
    """
    This doesnot overrides global variable
    instead creates an local variable with same name

    if we actually wanted to change the global variable they we can do it using global keyword

    global x = 'local x' 
    this will change the global variables value
    """
    print('Printing from function1:'+ x)  


test1()     
print('Prinitng from main body:' + x)


"""
# built-in scopes ex: min, len, list, etc
import builtins
print(dir(builtins))
"""



# Enclosing scope has to do with nested functions
z = 'global z'
def outer():
    z = 'outer z'

    def inner():
        z = 'inner z'
        # first it checks for z in local scope
        # if not found it checks for z in enclosing function local scope
        # if not found it checks dor z in global scope
        # if not found it checks for z in buitl-in scope
        # if not found in built-in then it throws z not found/ not defined error
        print(z)
        # if we want to change global variable in a function we use global key word
        # if we want to change enclosing variable then use,
        # nonlocal z
    
    inner()
    print(z)

outer()
print(z)


