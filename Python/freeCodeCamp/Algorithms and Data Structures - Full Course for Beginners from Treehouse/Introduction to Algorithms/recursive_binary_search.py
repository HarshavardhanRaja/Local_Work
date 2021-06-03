# TC--> O(logn), SC--> O(logn)

def recursive_binary_search(list, target):
    if len(list) ==0: return False
    else:
        middle = len(list)//2
        if list[middle] == target: return True
        elif list[middle] < target: return recursive_binary_search(list[middle+1:], target)
        else: return recursive_binary_search(list[:middle-1], target)
    

numbers = list(range(0,100,1))
print(numbers)
find = recursive_binary_search(numbers, 56)

if find is not False: print("Number found in the list")
else: print("number did not found")