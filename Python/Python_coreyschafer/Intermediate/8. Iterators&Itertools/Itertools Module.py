# Itertools are a collection of tools that allows us to work with Iterators  in a fast and memory efficient way

import itertools

# Count -> returns an Iterator that counts
# By default if we dont pass any values the count start from 0
counter = itertools.count()

"""
for num in counter:
    print(num)
"""

print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
