# Question
"""
Sherlock received a strange case that had an interesting twist .
The murderer had placed the victim's body on the top of a tree.
The tree was a special one with its roots at the top and leaves at the bottom.
As any crime is not perfect, this murderer had left a series of clues in the leaves and the nodes of the tree.
The clues were a series of numbers present at the leaves and nodes starting from the bottom most leaves and moving up one by one and
Sherlock has to find them and crack them in order to solve the crime.
You have to help Sherlock crack the puzzle.
You are given the set of numbers, but in two of the following different ways:
1. Such that the root is between its children
2. Such that the root is before its children


Input Specification:
input1: The number array representing the values in the 1 st way
input2: The number array representing the values in the 2nd
way
input3: Size of the array
Note: In the case where the body is not on the tree, the tree can be empty too.

Output Specifications:
The array giving the correct sequence of numbers as desired for solving the puzzle

Example 1:
    input1 = {2,3,5,1,6}
    input2 = {1,3,2,5,6}
    input3 = 5
    output = {2,5,3,1,6}

Example2:
    input1 = {4,2,5,1,3}
    input2 = {1,2,4,5,3}
    input3 = 5
    output = {4,5,2,1,3}
"""

# Answer
