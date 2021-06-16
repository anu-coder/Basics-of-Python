'''
Please write assert statements 
to verify that every number in the list [2,4,6,8] is even.
'''
l = [2,4,6,8]
even = [i for i in l if i%2==0]
assert l==even 