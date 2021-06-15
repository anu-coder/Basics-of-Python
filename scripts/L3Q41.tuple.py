'''
Define a function which can generate and print a tuple 
where the value are square of numbers between 1 and 20 
(both included).
'''

def print_tup():
    l = [i**2 for i in range(1,21)]
    print(tuple(l))

if __name__=='__main__':
    print_tup()