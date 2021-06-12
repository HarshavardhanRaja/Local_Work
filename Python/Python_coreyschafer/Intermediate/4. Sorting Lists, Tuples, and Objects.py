

# sort vs sorted
"""
Sorted() takes a list as input and returns newly created sorted list as output
Whereas sort() is used to sort the list inplace and returns none

And for a tuple we cannot do an inplace sort as it is immutable
so we can sort it using sorted() function 
"""



li = [9,1,8,2,7,3,6,4,5]

s_li = sorted(li)

print('sorted list using sorted():', s_li)
print('original list:', li)
li.sort()
print('sorted using sort() :', li)

"""
By default both sorted() and sort() functions sorts in Ascending order 
If you want to change the order use 'reverse = True'

sorted(li, reverse=True)
li.sort(reverse=True)
"""



# Sorting tuples
# for a tuple we cannot do an inplace sort as it is immutable
# so we can sort it using sorted() function but it returns a list as output even we are passing tuple
print('\n')
print('Sorting tuple:')
tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)

print('sorted tuple using sorted():', s_tup)




# sorting Dictonary
# by default it sorts based on keys and returns sorted list of keys
# we cannot use sort() for dictonaries as well
print('\n')
print('Sorting Dictonary:')
names = ['Tony Stark', 'Steve Rogers', 'Thor', 'Bruce Banner', 'Natasha Romanaof', 'Clint Barton']
heros = ['Ironman', 'Captain America', 'God of Thunder', 'Hulk', 'Black Widow', 'Hackeye']
avengers_dict = {name:hero for name,hero in zip(names,heros)}

s_di = sorted(avengers_dict)
print('Sorted Dictonary', s_di)


# what if we want to sort based on absolute values 
lis = [-5, -8, -2, 1,3,7,9]
s_lis = sorted(lis)
print('Default sort:', s_lis)
sa_lis = sorted(lis, key = abs)
print('ABS sorted:', sa_lis)


class employee:
    def __init__(self, name, age, salary ):
        self.name = name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return f'{self.name}, {self.age}, ${self.salary}'

e1 = employee('tony', 35, 70000)
e2 = employee('nat', 28, 50000)
e3 = employee('clint', 39, 40000)

employees = [e1, e2, e3]

def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key=e_sort)
# s_employees = sorted(employees, key = lambda e : e.name)
# s_employees = sorted(employees, key = attrgetter('name')) for this we need to add, from operator import attergetter

