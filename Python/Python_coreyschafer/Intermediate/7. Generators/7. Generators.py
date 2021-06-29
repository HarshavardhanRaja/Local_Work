# Generators: How to use them and benifits you receive

# creating generator objects
"""
# the below function will return generator object
def square_numbers(nums):
    result = []
    yield (i*i)


# creating generator object using list comprehensions
my_nums = (x*x for x in [1,2,3,4,5])

# printing values from generator object
for num in my_nums:
    print(num)


# converting generator object into list

my_nums = list(my_nums)
"""





# Generators are better with performance
# As  It's not holding all the values in memory 


# What are Generators?
"""
Are functions that returns traversable objects
Produce items one at a time and only when required
Are run along with for loops
"""

#Advantages of Generators
"""
Generators Don't hold the entire result in memory. It Yields one result at a time

"""

# normal Function
def square_nums(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


# Function to create Generator
def square_nums_gen(nums):
    for num in nums:
        yield num*num

# creating generators using list comprehensions
my_nums_gen_comp = (x*x for x in [1,2,3,4,5])   # this will create a generator. we have to use ()


my_nums = square_nums([1,2,3,4,5])
my_nums_gen = square_nums_gen([1,2,3,4,5])

print(my_nums)  # returns [1,4,9,16,25]
print(my_nums_gen) # returns generator object

# Convert generator object to list
my_nums_gen_list = list(my_nums_gen) # this will compute the generator and returns values to a list
# if we convert it into list then we'll lose the advantage that we get from generators


