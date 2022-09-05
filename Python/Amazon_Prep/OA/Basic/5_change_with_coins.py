"""
Suppose we have coin denominations of [1, 2, 5] and the total amount is 7. 
We can make changes in the following 6 ways:
1,1,1,1,1,1,1
1,1,1,1,1,2
1,1,1,2,2
1,2,2,2
1,1,5
2,5

"""

def make_change(denominations, amount):
    count = 0
    for d in denominations:
        


if __name__ == 'main':
    denominations = [1, 2, 5]
    amount = 7
    print(make_change(denominations, amount))