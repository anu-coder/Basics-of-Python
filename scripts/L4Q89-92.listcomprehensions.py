'''
By using list comprehension, 
please write a program to print the list 
after removing the 

Q 89:
0th, 2nd, 4th,6th 
numbers in [12,24,35,70,88,120,155],

Q 91:
0th,4th,5th numbers in 
[12,24,35,70,88,120,155]..

Q 92
removing the value 24 in 
[12,24,35,24,88,120,155]
'''

l = [12,24,35,70,88,120,155]

# using enumerate
print([ele for i, ele in enumerate(l) if i%2!=0])

# using index of a list
print([i for i in l if l.index(i)%2!=0])

#remove 0, 4, 5th element
print([i for i in l if l.index(i) not in [0,4,5]])

# remove 24 from the list
l.remove(24)
print(l)

'''
By using list comprehension, 
please write a program generate a 
358 3D array whose each element is 0.
'''

array = [[ [0 for col in range(8)] for col in range(5)] for row in range(3)]
print(array)

