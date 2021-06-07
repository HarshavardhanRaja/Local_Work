

nums = [1,2,3,4,5]

for num in nums:
    print(num)

# break: will completely break out of a loop
# continue: move on to next iteration of the loop

print('break Demonstration:')
for num in nums:
    if num == 3:
        print('Found')
        break
    print(num)
    
print('continue Demonstration:')
for num in nums:
    if num == 3:
        print('Found')
        continue
    print(num)


for num in nums:
    for letter in 'abc':
        print(num, letter)



# range
print('Demonstarate range')
for i in range(10):
    print(i)




# For loops iterated through a certain number of values
# Where as while loops itereate untill they met a stopping condition/ met break statement \

x = 0
print('===================while_loop================')
while(x<10):
    print(x)
    x += 1


print('Demonstrate break:')
x = 0
while(x<10):
    if x == 5:
        print('Found')
        break
    print(x)
    x += 1
x = 0
