'''
Please write a program to 
print some Python built-in functions documents, 
such as abs(), int(), raw_input()
'''


def square(n):
    '''
    Returns the square of any given numbers:
    parameters
    ----------
    n : Any number
    '''
    return n**2

if __name__=='__main__':
    print(abs.__doc__)
    print(int.__doc__)
    print(input.__doc__)
    # func = input("Enter any function name: ")
    # print(f'{func}.__doc__')
    print(square.__doc__)
    n = int(input('Enter any number: '))
    print(f"The square is: {square(n)}")