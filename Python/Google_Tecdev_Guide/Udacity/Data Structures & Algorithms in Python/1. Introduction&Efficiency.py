"""
1. Introduction and Efficiency
    Course Introduction
    Syntax
    Efficiency
    Notation of Efficiency

2. List-Based Collections
    Lists/Arrays
    Linked Lists
    Stacks
    Queues

3. Searching and Sorting
    Binary Search
    Recursion
    Bubble Sort
    Merge Sort
    Quick Sort

4. Maps and Hashing
    Maps
    Hashing
    Collisions
    Hashing Conventions

5. Trees
    Trees
    Tree Traversal
    Binary Trees
    Binary Search Trees
    Heaps
    Self-Balancing Trees

6. Graphs
    Graphs
    Graph Properties
    Graph Representation
    Graph Traversal
    Graph Paths

7. Case Studies in Algorithms
    Shortest Path Problem
    Knapsack Problem
    Traveling Salesman Problem

8. Technical Interview Tips
    Mock Interview Breakdown
    Additional Tips
    Practice with Pramp
    Next Steps
"""


# Comments
# This is a one-line Python comment - code blocks are so useful!
"""This type of comment is used to document the purpose of functions and classes."""

# Declaration/Initialization
"""
# Remember values, not variables, have data types.
# A variable can be reassigned to contain a different data type.
answer = 42
answer = "The answer is 42."
"""

# Data Types
"""
boolean = True
number = 1.1
string = "Strings can be declared with single or double quotes."
list = ["Lists can have", 1, 2, 3, 4, "or more types together!"]
tuple = ("Tuples", "can have", "more than", 2, "elements!")
dictionary = {'one': 1, 'two': 2, 'three': 3}
variable_with_zero_data = None
"""


# Simple Logging
"""
print("Printed!")
"""


# Conditionals
"""
if cake == "delicious":
    return "Yes please!"
elif cake == "okay":
    return "I'll have a small piece."
else:
    return "No, thank you."
"""



# Loops
"""
for item in list:
    print item

while (total < max_val):
    total += values[i]
    i += 2
"""


# Functions
"""
def divide(dividend, divisor):
    quotient = dividend / divisor
    remainder = dividend % divisor
    return quotient, remainder

def calculate_stuff(x, y):
    (q, r) = divide(x,y)
    print q, r
"""


# Classes
"""
class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def birthday(self):
        self.age += 1
"""




# Efficiancy or Complexity
"""
Two types of omplexities:
    Time complexity:    How long does your code taka to run?
    Space complexity    How much storage space does your code needs?

"""


# Notation
"""
Efficiancy is often represented by Big O Notation. O(n)
n -> lenght of the input

Best Case, Average Case, Worst Case

Most often worst case is considered.

"""



# Efficiancy Practice
#Below are some examples of functions in Python. Look at each and take note of the time efficiency. Then, in the quiz, enter those values using the correct notation. Use approximations wherever possible!
"""
input manatees: a list of "manatees", where one manatee is represented by a dictionary
a single manatee has properties like "name", "age", et cetera
n = the number of elements in "manatees"
m = the number of properties per "manatee" (i.e. the number of keys in a manatee dictionary)

def example1(manatees):
    for manatee in manatees:
        print manatee['name']

def example2(manatees):
    print manatees[0]['name']
    print manatees[0]['age']

def example3(manatees):
    for manatee in manatees:
        for manatee_property in manatee:
            print manatee_property, ": ", manatee[manatee_property]

def example4(manatees):
    oldest_manatee = "No manatees here!"
    for manatee1 in manatees:
        for manatee2 in manatees:
            if manatee1['age'] < manatee2['age']:
                oldest_manatee = manatee2['name']
            else:
                oldest_manatee = manatee1['name']
    print oldest_manatee


"""

# Answers
"""
Here are the answers and explanations:

Example 1
We iterate over every manatee in the manatees list with the for loop. 
Since we're given that manatees has n elements, our code will take approximately O(n) time to run.

Example 2
We look at two specific properties of a specific manatee.
We aren't iterating over anything - just doing constant-time lookups on lists and dictionaries. 
Thus the code will complete in constant, or O(1), time.

Example 3
There are two for loops, and nested for loops are a good sign that you need to multiply two runtimes. 
Here, for every manatee, we check every property. 
If we had 4 manatees, each with 5 properties, then we would need 5+5+5+5 steps. 
This logic simplifies to the number of manatees times the number of properties, or O(nm).


Example 4
Again we have nested for loops. 
This time we're iterating over the manatees list twice - every time we see a manatee, 
we compare it to every other manatee's age. 
We end up with O(nn), or O(n^2) (which is read as "n squared").



https://www.bigocheatsheet.com/
"""