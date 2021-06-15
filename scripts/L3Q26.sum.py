'''
Define a function which can compute the sum of two numbers.
'''

def sum_func(x, y):
    '''returns the sum of two numbers'''
    return x+y

if __name__=='__main__':
    x, y = list(map(int, input("Enter two numbers: ").split(',')))
    print(sum_func(x,y))