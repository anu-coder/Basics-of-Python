'''
Define a function that can accept an integer number as input
and print the "It is an even number" if the number is even, 
otherwise print "It is an odd number".
'''

def even_old(n: int):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is a odd number")


if __name__=='__main__':
    n = int(input('Enter a number: '))
    even_old(n)
