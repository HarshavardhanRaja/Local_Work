
# if we want to write code for a function later after creating it we hace to use 'pass' argument
def hello():
    pass


print(hello)
print(hello())


def hello_function():
    print('hello function')

hello_function()

# functions are used so that they are DRY compliant i.e Dont Repear Yourself
# Return is used to get output from a function
def hello_function_return():
    return 'Hello Function!'

print(hello_function_return())


# Passing arguments
def hello_input_parameters(greeting):
    return f'{greeting} Function.'

print(hello_input_parameters('Hi'))

# setting default value
def hello_deafault_value(greeting, name = 'you'):
    return f'{greeting}, {name}'

print(hello_deafault_value('hi'))
print(hello_deafault_value('hello', 'tony'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info('Math', 'Art', name = 'john', age = 25 )


courses = ['math', 'art', 'CS']
info = {'name':'john', 'age':25}

student_info(courses, info)
student_info(*courses, **info)






month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

def is_leap(year):
    """Return true for leap year, False for non-leap year"""
    return year%4 ==0 and (year%100 != 0 or year%400 ==0)

def days_inmonth(year, month):
    """Return number of days in the month in that year """

    if not 1 <=month <=12:
        return 'Invalid Month'
    if month ==2 and is_leap(year):
        return 29
    
    return month_days[month]

print(is_leap(2017))
print(days_inmonth(2017, 6))