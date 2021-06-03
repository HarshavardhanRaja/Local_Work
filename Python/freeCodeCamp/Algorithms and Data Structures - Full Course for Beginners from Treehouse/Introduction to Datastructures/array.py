"""
Array/list:
    => A common DS built into every programming language.
    => Fundamental DS
    => used to represent collection of values.
    => Are building blocks for creating custom DS.
    => Contigous DS i.e, stored in continious blocks of memory with no gaps.
"""

new_list = list(range(0,100,1))

#Access/Read values from list using index
print(new_list[5]) #read from a particular index '5'
print(new_list[:]) #read full list
print(new_list[5:]) #read list starting from index '5' to end of list
print(new_list[:8]) #read list from starting to index '8'
print(new_list[3:80]) #read list from index '3' to index '80'



# Search for a value in list 

# method 1: using in operator
#  in operator calls a "Contains" method that is defined on the list type which runs a linear search operation.
if 56 in new_list: print(True) 

#method 2: directly implementing linear search algo 
for i in new_list:
    if i == 103:
        print(True)
        break





# Inserting values in list: 3 types of insert operations

# Type1: True insert i.e, using index we insert value anywhere in the list as we want. TC=O(n)
print(new_list[0], len(new_list))
new_list.insert(0, -1)
print(new_list[0], len(new_list))

# Type2: Appending i.e, Add element at the end of the list. TC = O(1)
new_list.append(101)

# Type3: Add one list to another. TC = O(K) where k = number of elements in the added second list
new_list.extend([102,103,104,105])
test = [106, 107, 108, 109, 110]
new_list.extend(test)
print(new_list)




# Deleting values from the list
# Inserting shifts every element to right after the inserted index
# Deleting shifts every element to left after the deleted index

test.clear()   #Remove all items: clear()
new_list.pop(10)    #Remove an item by index and get its value: pop()
new_list.remove(56) #Remove an item by value: remove()
del new_list[80] #Remove items by index or slice: del


# Python list uses "List_resize" operation incase the size of the list is to be modifed for above operations
# List_resize operation uses Growth pattern as, 0,4,8,16,25,35,46......










# Other important list functions and operations

# “in” operator :- This operator is used to check if an element is present in the list or not. Returns true if element is present in list else returns false.
if 1 in new_list: print("1 is present in the list")

# “not in” operator :- This operator is used to check if an element is not present in the list or not. Returns true if element is not present in list else returns false.
if 245 not in new_list: print("245 not in list")

# len() :- This function returns the length of list.
print(len(new_list))

# min() :- This function returns the minimum element of list.
print(min(new_list))

# max() :- This function returns the maximum element of list.
print(max(new_list))

# “+” operator :- This operator is used to concatenate two lists into a single list.
print(new_list + test)

# “*” operator :- This operator is used to multiply the list “n” times and return the single list.
print(test * 5)

# index(ele, beg, end) :- This function returns the index of first occurrence of element after beg and before end.
print(new_list.index(5, 0, 10))

# count() :- This function counts the number of occurrences of elements in list.
print(new_list.count(10))

# reverse() :- This function reverses the elements of list.
new_list.reverse()
print(new_list)

# sort() :- This function sorts the list in increasing order.
new_list.sort()
print(new_list)

 # sum() : Calculates sum of all the elements of List.
print(sum(new_list))


