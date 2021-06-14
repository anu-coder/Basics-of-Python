'''
Question: Define a class with a generator 
which can iterate the numbers, 
which are divisible by 7, 
between a given range 0 and n.

Hints: Consider use yield
'''

def div_by_7(n):
    for i in range(0, n, 7):
        print(i)

if __name__=='__main__':
    n = int(input('Enter a number: '))
    div_by_7(n)

