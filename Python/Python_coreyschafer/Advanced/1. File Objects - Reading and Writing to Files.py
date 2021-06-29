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
    # f_contents = f.read()
    # print(f_contents)
    # f.read()               Returns all of the content of file
    # f.readlines()          Returns all lines in a list. each line as a element of the list
    # f.readline()           Returns first line of the file. If we run it second time it will returns 2nd line likewise for other lines
    i =0
   
    for line in f:
        print(i, ":")
        i+=1
        print(line, end='')


    """
    size_to_read = 10
    f_contents = f.read()

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read()
    """

    # f.tell()                  returns current position in the file
    # f.seek(0)                  points to current position to the specified value. In this case at 0th position. i.e start of the file

"""
with open('test2.txt') as f:
    f.write('Test')
    f.write('Test')
"""

with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# Inorder to work with images we have to open them in binary mode
# That means we are gonna be reading in bytes instead of reading in text.

with open('Hierarchial clustering.jpeg', 'rb') as ri:
    with open('copy_image.jpeg', 'wb') as wi:
        for line in ri:
            print(line)
            wi.write(line)


"""
with open('Hierarchial clustering.jpeg', 'rb') as ri:
    with open('copy_image.jpeg', 'wb') as wi:
        chunk_size = 4096
        ri_chunk = ri.read(chunk_size)

        while len(ri_chunk) > 0:
            wi.write(ri_chunk)
            ri_chunk = ri.read(chunk_size)

"""