

# ways of importing a file
"""
importing all the contents of module:
    -> import my_module
    -> from my_module import *
    -> import mymodule as mm

Importing a particular function
    -> import my_module.find_index
    -> import my_module.find_index as fi
    -> from my_module import find_index
    -> from my_module import find_index as fi
"""

import my_module as mm


courses = ['maths', 'physics', 'chemistry', 'CS']

index = mm.find_index(courses, 'chemistry')
print(index)



# How does python know where to find the module??
# when we import a module it checks multiple locations 
# we can find those location in sys.path

import sys
print(sys.path)

"""
These were the paths that it searches for module to import in my computer
[
    '/Users/harsha/Desktop/Coding/Python/Python_coreyschafer/Basics/8. Import Modules and Exploring The Standard Library', 
    '/opt/homebrew/Cellar/python@3.9/3.9.4/Frameworks/Python.framework/Versions/3.9/lib/python39.zip', 
    '/opt/homebrew/Cellar/python@3.9/3.9.4/Frameworks/Python.framework/Versions/3.9/lib/python3.9', 
    '/opt/homebrew/Cellar/python@3.9/3.9.4/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload', 
    '/opt/homebrew/lib/python3.9/site-packages', 
    '/opt/homebrew/Cellar/protobuf/3.15.8/libexec/lib/python3.9/site-packages'
]

order of searching for the module:
[
    current working directory
    python path environment variable
    standard library directories
    site packages directory for 3rd party packages
]
"""


# if the module code is not in the directory of the running script follow this
"""
Manually add that directory where module code is present to sys.path

import sys
sys.path.append('directory address')

this will add the path to the sys.path list at the end 

But this isn't the best looking approach because we are appending this directory before other imports and 
also if we were to import our module and we had this manually hard coded in multiple locations then
we have to change all of those

So instead we can make this change in the next place sys.path looks i.e is the "python path environment variable"

changing python path environment variable in mac:

    => Open Terminal
    => nano ~/.bash_profile
    => go to end of the file
    => export PYTHONPATH= 'the directory path that module is ' 
    => contro+x and y

"""

import os

# To get the path of the module stored in our computer, use
print(os.__file__)
#/opt/homebrew/Cellar/python@3.9/3.9.4/Frameworks/Python.framework/Versions/3.9/lib/python3.9/os.py

import datetime
print(datetime.__file__)
#/opt/homebrew/Cellar/python@3.9/3.9.4/Frameworks/Python.framework/Versions/3.9/lib/python3.9/datetime.py