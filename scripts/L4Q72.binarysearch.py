'''
Please write a binary search function 
which searches an item in a sorted list. 
The function should return the index of element 
to be searched in the list.
'''

'''
In a nutshell, this search algorithm takes advantage 
of a collection of elements that is already 
sorted by ignoring half of the elements after just one comparison. 

Compare x with the middle element.
> If x matches with the middle element, 
we return the mid index.
> Else if x is greater than the mid element, 
then x can only lie in the right (greater) 
half subarray after the mid element. 
Then we apply the algorithm again for the right half.
> Else if x is smaller, 
the target x must lie in the left (lower) half. 
So we apply the algorithm for the left half.
'''

import math
def binary_search(l, element):
    bottom = 0
    top = len(l)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if l[mid]==element:
            index = mid
        elif l[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

l=[2,5,7,9,11,17,222]
print(binary_search(l,11))
print(binary_search(l,12))










