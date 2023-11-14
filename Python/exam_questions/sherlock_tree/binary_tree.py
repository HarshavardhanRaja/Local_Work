"""
A Tree Data Structure can be traversed in following ways:
1. Depth First Search or DFS
    a. Inorder Traversal
    b. Preorder Traversal
    c. Postorder Traversal
2. Level Order Traversal or Breadth First Search or BFS
3. Boundary Traversal
4. Diagonal Traversal





Algorithm Preorder(tree)
Approach:
    1. Visit the root.
    2. Traverse the left subtree, i.e., call Preorder(left->subtree)
    3. Traverse the right subtree, i.e., call Preorder(right->subtree)
Uses:
    Preorder traversal is used to create a copy of the tree. Preorder traversal is also used to get prefix expressions on an expression tree.
KPIs:
    1. Time Complexity: O(N)
    2. Auxiliary Space: If we don’t consider the size of the stack for function calls then O(1) otherwise O(h) where h is the height of the tree.


Algorithm Postorder(tree)
Approach:
    1. Traverse the left subtree, i.e., call Postorder(left->subtree)
    2. Traverse the right subtree, i.e., call Postorder(right->subtree)
    3. Visit the root
Uses:
    Postorder traversal is used to delete the tree.
    Postorder traversal is also useful to get the postfix expression of an expression tree
KPIs:




"""


class Node:
    def __int__(self, key):
        self.left = None
        self.right =None
        self.val = key

def inorder_traversal(root):
    """
    Algorithm Inorder(tree)
    Approach:
        1. Traverse the left subtree, i.e., call Inorder(left->subtree)
        2. Visit the root.
        3. Traverse the right subtree, i.e., call Inorder(right->subtree)
    Uses:
        In the case of binary search trees (BST), Inorder traversal gives nodes in non-decreasing order.
        To get nodes of BST in non-increasing order, a variation of Inorder traversal where Inorder traversal is reversed can be used.
    KPIs:
        1. Time Complexity: O(N)
        2. Auxiliary Space: If we don’t consider the size of the stack for function calls then O(1) otherwise O(h) where h is the height of the tree.
    """
    if root:
        inorder_traversal(root.left)
        print(root.val)
        inorder_traversal(root.right)

def preorder_traversal(root):
    if root:
        print(root.val)
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val)

