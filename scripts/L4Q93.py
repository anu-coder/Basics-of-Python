'''
Q 93: With two given lists 
[1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
write a program to make a list whose elements 
are intersection of the above given lists.
'''

l1 = [1,3,6,78,35,55]
l2 = [12,24,35,24,88,120,155]
l1 = set(l1)
print(list(l1.intersection(set(l2))))
print(list(l1 & set(l2)))

'''
Q 94: With a given list 
[12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing 
all duplicate values with original order reserved.
'''

l = [12,24,35,24,88,120,155,88,120,155]


def deduplicate(l):
    out_list = []
    for i in l:
        if i not in out_list:
            out_list.append(i)

    return out_list

print(deduplicate(l))