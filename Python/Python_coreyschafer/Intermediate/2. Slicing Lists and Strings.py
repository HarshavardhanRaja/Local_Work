

# Slicing: it's a way for us to extract certain elements from these lists and strings


my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index    0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#-veindex -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]          end not included

print(my_list[0:8])
print(my_list[0:8:2])

print(my_list[1:])
print(my_list[:8])
print(my_list[:])


# reverse entire list
print(my_list[::-1])



sample_url = 'http://harshacs.com'
print(sample_url)

# Reverse the url
print(sample_url[::-1])

# get the top level domain
print(sample_url[-4:])


# pint the url without http://
print(sample_url[7:])

# print out the url without the http:// or the top level domain
print(sample_url[7:-4])
