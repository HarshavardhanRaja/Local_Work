

def merge_sort(list):
    
    """
    Sorts a list in ascending order
    returns a new sorted list
    DIVIDE: find the mid point of the list and divide into sub lists 
    CONQUER: Recursively sort the sublists created in previous steps
    COMBINE: Merge the sorted sub lists  create in previous steps
    
    Recursive function has a basic pattern, 
        First we starts with a base case that includes stopping condition
        After that we have some logic that breaks down the problem and recursively calls itself


    Stopping condition: is end goal i.e sorted array
    Base Case: (simplest condition that satisfies the end result) i.e.,  single element list or empty list
    """

    # Stoping condition
    if len(list) <=1 :
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge (left, right)

def split(list):
    """
    Divide a unsorted list at mid point into sublists
    Returns two sub-lists - left & right
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Mergers two lists(arrays), sorting them in the process 
    Returns a new merge list 
    """
    l = []
    i = 0
    j = 0 

    while i<len(left) and j <len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j+=1

    while i<len(left):
        l.append(left[i])
        i += 1

    while j<len(right):
        l.append(right[j])
        j += 1

    return l 





alist = [23, 45, 67, 78, 89,34, 65, 123, 456, 875, -65, 0, -45, 0, 1, 1]
l = merge_sort(alist)
print(l)