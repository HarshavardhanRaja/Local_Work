# File Objects


# way 1 of working with files i.e is using open()
f = open('test.txt', 'r')            # provide path to the file if it is in another directory

print(f.name)
print(f.mode)                       # prints the mode of file opened i.e r, w, a, r+
# r => read only
# w => write
# a => append
# r+ => read and write


f.close()
# with open() we have to explicitly close the file
# If we don't close the file then we can end up with leaks that cause you to run over the maximum allowed file descriptors of your system
# and your applications could throw an error


# using open() with 'with' solves that problem of explicit closing
# we will be able ti use the file only when we are within that with block. if we exit the with block the file gets automatically closed

with open('test.txt', 'r') as f:
    f_readlines = f.readline()
    print(f_readlines)