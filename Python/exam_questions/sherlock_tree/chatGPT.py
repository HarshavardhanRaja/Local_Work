class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def construct_tree_between(arr):
    if not arr:
        return None
    root = Node(arr[0])
    stack = [root]
    i = 1
    while i < len(arr):
        current = stack.pop(0)
        left_val = arr[i] if i < len(arr) else None
        i += 1
        right_val = arr[i] if i < len(arr) else None
        i += 1
        if left_val is not None:
            current.left = Node(left_val)
            stack.append(current.left)
        if right_val is not None:
            current.right = Node(right_val)
            stack.append(current.right)
    return root

def construct_tree_before(arr):
    if not arr:
        return None
    root = Node(arr[0])
    for val in arr[1:]:
        root.right = Node(val)
        root = root.right
    return root

def in_order_traversal(node, result):
    if node:
        in_order_traversal(node.right, result)
        result.append(node.val)
        in_order_traversal(node.left, result)

def correct_sequence_between(input1, input2, size):
    root_between = construct_tree_between(input1)
    root_before = construct_tree_before(input2)

    in_order_result_between = []
    in_order_result_before = []

    in_order_traversal(root_between, in_order_result_between)
    in_order_traversal(root_before, in_order_result_before)

    return in_order_result_between if in_order_result_between != in_order_result_before else None

# Example usage:
# input1 = [4, 2, 5, 1, 3]
# input2 = [1, 2, 4, 5, 3]
# size = 5

input1 = [2,3,5,1,6]
input2 = [1,3,2,5,6]
size = 5

result = correct_sequence_between(input1, input2, size)
print("Desired Sequence:", result)
