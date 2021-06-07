

# Lists: used to store list of values. These values can be int/str/float/ lists itself.
courses = ['Maths', 'Physics', 'Chemistry', 'C.S']
print(courses)
print(len(courses))

print(courses[0])
print(courses[3])
print(courses[-1])

# printing range of values /slicing
print(courses[0:2])         # [start:end]     excluding end
print(courses[:2])
print(courses[2:])

# Important list methods
courses.append('economics')
courses.insert(0, 'Art')
temp = ['nat', 'cap', 'banner']
courses.extend(temp)
print(courses)


courses.remove('Art')
courses.pop()       # Removes last value


courses.reverse()
print(courses, ':Reverse_order')
courses.sort()
print(courses, ':Sorted_lexicographical_order')
courses.sort(reverse=True)
print('Reverse Sorted order:', courses)

# Sort is used if you want the sort to happen inplace
# Sorted function returns the sorted list instead of sorting it inplace
sorted_courses = sorted(courses)
print(sorted_courses)

# min(list), max(list), sum(list)

# To find the index of a particular value
print(courses.index('Maths'))
print('Art' in courses)


for item in courses:
    print(item)


for index, item in enumerate(courses):
    print(index, item)


for index, item in enumerate(courses, start=1):
    print(item, index)




course_str1 = ', '.join(courses)
print('str1:', course_str1)
print(type(course_str1))
course_str2 = ':'.join(courses)
print('str2-', course_str2)

new_courses =  course_str2.split(':')
print(new_courses)



# Tuples
# Tuples are very similar to lists with one major difference
# we cannot modify tupels i.e these are immutable
# Tupels --> Immutable
# Lists --> Mutable

list_1 = ['nat', 'cap', 'tony', 'Thor', 'Banner']
list_2 = list_1

print(list_1)
print(list_2)

list_1[1] = 'steve'

print(list_1)
print(list_2)




tuple_1 = ('nat', 'cap', 'tony', 'thor', 'banner' )
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple_1[1] = 'steve'  this step doesnot supports in tuple, AS it is immutable







# Sets are values that are unordered and also have no duplicates
# Sets ---> unordered, No duplicates.

cs_courses = {'maths', 'physics', 'CS'}

print(cs_courses) # every time we print sets we get different order of courses as it is unorderd

print('maths' in cs_courses) # Although both lists and tuples can perform this step but sets are optimised for this step

art_courses = {'maths', 'art', 'physics'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


# Creating emplty lists, tupels, sets
empty_list = [] # or we can use empty_list = list()
empty_tuple = () # or we can use empty_tuple = tuple()
empty_set = set() # we cannot use empty_set = {}, As brackets are reserved for dictonaries




