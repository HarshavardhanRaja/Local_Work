def linear_search(list, target):

    for i in range(0, len(list)):
        if list[i] == target: return i
    return None

def verify(index):
    if index is not None: print("number found at index", index)
    else: print("number is not in the list")


numbers = list(range(0,100))
print(numbers)
find = linear_search(numbers, 12)
verify(find)