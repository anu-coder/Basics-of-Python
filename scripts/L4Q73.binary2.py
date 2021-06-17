'''
Please write a binary search function 
which searches an item in a sorted list. 
The function should return the 
index of element to be searched in the list.
'''

import math
def binary_search(l, ele):
    bottom = 0 
    top = len(l) - 1
    index = -1
    while top>=bottom and index == -1:
        mid = int(math.floor((top+bottom)/2))
        if l[mid]==ele: 
            index = mid
        elif l[mid]> ele:
            top = mid-1
        else:
            bottom = mid +1

    return index

l = [2,5,7,9,11,17,222]
print(binary_search(l, 11))
print(binary_search(l, 12))