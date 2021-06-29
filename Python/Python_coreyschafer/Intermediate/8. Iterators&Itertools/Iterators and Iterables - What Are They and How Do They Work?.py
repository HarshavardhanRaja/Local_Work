

# List is Iterable but it is not an Iterator

# What is it something means Iterable?
"""
Iterable:
    => On higher level it simply means something that can be looped over.
    ex:- List is iterable
    tuples, dictonaries, strings, files, generators, other different objects
"""

nums = [1,2,3,4,5]
for num in nums:
    print(num)


# How can we tell something is Iterable?
"""
If something is Iterable it should have special method called " __iter__() "

To look at methods and attributes available for a particular object use dir(object)
"""

print(dir(nums))




# What makes something an Iterator?
"""
calling __iter--() for an object return Iterator.


An Iterator is an object with a state so that it remembers it's state during an Iteration.
Iterators can only go forward. they cannot go backward

"""

i_nums = nums.__iter__()        # or iter(nums)
print(i_nums)
print(dir(i_nums))


# This is exactly like for loop that we used above
while True:
    try: 
        item = next(i_nums)
        print(item)
    except StopIteration:
        break


