'''
Define a function which can generate a list 
where the values are square of numbers between 1 and 20 
(both included). 
Then the function needs to print 
the first 5 
and last 5 elements 
and all except first five in the list.
'''

def first_last():
    l = [i**2 for i in range(1,21)]
    print("Full list", *l, sep = ' ')
    print("First five:", *l[:5], sep = ' ')
    print("Last five:", *l[15:], sep = ' ')
    print("Except first five:", *l[5:])

if __name__=='__main__':
    first_last()

