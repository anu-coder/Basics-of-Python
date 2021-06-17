'''
Please write a program 
which accepts a string from 
console and print it in reverse order.
'''

def rev(s):
    return s[::-1].lower()


if __name__=='__main__':
    s = input('Enter a string ')
    print(rev(s))