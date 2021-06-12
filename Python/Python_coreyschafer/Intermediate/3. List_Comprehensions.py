
print("\n")
print("List Comprehesions:")
# List comprehension is an easier and more readable way of create a list
nums = [1,2,3,4,5,6,7,8,9,10]




# I want 'n' for each 'n' in nums
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)
# using list comprehension
my_list_listcomprehension = [n for n in nums]
print("\n")





# I want n*n for each 'n' in nums
my_list1 = []
for n in nums:
    my_list1.append(n*n)
print(my_list1)
# using list comprehension
my_list1_listcomprehension = [n*n for n in nums]
# using a map + lambda
my_list_map = map(lambda n:n*n, nums )
print(my_list_map)

print("\n")





# I want 'n' for each 'n' in nums if 'n' is even
my_list2 = []
for n in nums:
    if n%2 ==0:
        my_list2.append(n)
print(my_list2)
# using list comprehension
my_list2_listcomprehension = [n for n in nums if n%2 ==0]
print(my_list2_listcomprehension)
# using a filter + lambda
my_list2_filter = filter(lambda n: n%2 == 0, nums)
print (my_list2_filter)

print("\n")





# I want a (letter, num) pair for each letter in 'abcd' and each number in '0123'
lnpair = []
for letter in 'abcd':
    for i in range(4):
        lnpair.append((letter, i))
print(lnpair)
# using list comprehension
lnpair_lc = [(letter, num) for letter in 'abcd' for num in range(4)]
print(lnpair_lc)
print("\n")







# we can do comprihensions for dictonaries, tuples and sets also
# Dictonary Comprehensions
print("\n")
print("Dictonary Comprehesions:")

names = ['Tony Stark', 'Steve Rogers', 'Thor', 'Bruce Banner', 'Natasha Romanaof', 'Clint Barton']
heros = ['Ironman', 'Captain America', 'God of Thunder', 'Hulk', 'Black Widow', 'Hackeye']
print(zip(names, heros))
# I want a dict{'name':'hero'} for each name,hero in zip(names, heros)

avengers = {}
for name, hero in zip(names,heros):
    avengers[name] = hero
print(avengers)

avengers_lc = {name:hero for name, hero in zip(names, heros)}
print(avengers_lc)

# add conditions to the comprehesions
# if name is not equal to Clint Barton
avengers_lc_condition = {name:hero for name, hero in zip(names, heros) if name != 'Clint Barton'}
print(avengers_lc_condition)





# Set Comprehesions
print("\n")
print("Set Comprehesions:")
nums_list = [1,1,2,1,3,4,3,5,5,6,8,7,9,9,7,7,6]
nums_set = set()
for n in nums_list:
    nums_set.add(n)
print(nums_set)
# using comprehesions
nums_set_lc = {n for n in nums_list}
print(nums_set_lc)





# Generator Expressions
print('\n')
print("Generator Expressions:")
# I want to yield n*n for each n in nums
nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n

my_gen = gen_func(nums)
for i in my_gen:
    print(i)

my_gen_com = (n*n for n in nums)
for i in my_gen:
    print(i)