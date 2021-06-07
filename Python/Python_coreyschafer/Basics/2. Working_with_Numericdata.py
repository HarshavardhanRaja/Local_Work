print('=========================start===============================')

# Numbers are most commonly represented as INTEGERS and FLOAT
# INTEGERS -> Whole Number
# FLOAT -> Decimal

num = 3
print(type(num))        # Returns data type of object passed


# Arithemetic operators
print(3+2)          # Addition
print(3-2)          # Subtraction
print(3*2)          # Multiplication
print(3/2)          # Division
print(3//2)         # Floor Division to get quotient when divided by 2
print(3**2)         # Exponents
print(3%2)          # Modulus   to get remainder when divided by 2

# Order of operations parenthesis, multiply/division, addition/subtraction
# doing operations with the number itself
num += 1        # num = num+1
num *= 5        # num = num*5
num -= 10       # num = num-10
num /= 4        # num = num/4

# abs       removes negative sign
print(abs(-5))

# round     
print(round(3.75))         # rounds to nearest integer values
print(round(3.75, 1))      # first digit after the decimal


# Comparisions      These operators will return booleans i.e TRUE/FALSE 
print(3==2)         # Equal
print(3 != 2)       # Not Equal
print(3>2)          # Greater than
print(3<2)          # Less than
print(3 >= 2)       # Greater than or equal to 
print(3 <= 2)       # Less than or equal to



# Looks like a number but actually a string

num_1 = '100'
num_2 = '200'

print(num_1 + num_2) # This will concat as they are not numbers

num_1 = int(num_1)  # casting strings to integers
num_2 = int('200')

print(num_1 + num_2)

print('================================stop=================================')