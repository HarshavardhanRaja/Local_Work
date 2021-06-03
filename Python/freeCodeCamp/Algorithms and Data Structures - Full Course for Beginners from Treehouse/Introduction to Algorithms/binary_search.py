def binary_search(list, target):
    first = 0
    last = len(list) -1

    while first <= last:
        middle = (first+last)//2
        if list[middle] == target: return middle
        elif list[middle] < target: first = middle+1
        else: last = middle-1
    return None


def verify(index):
    if index is not None: print("Value found at index:", index)
    else: print("value did not found")

numbers = list(range(0,100))
print(numbers)
verify(binary_search(numbers, 46))
