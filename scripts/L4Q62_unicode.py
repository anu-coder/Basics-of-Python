'''
Write a program to read an ASCII string 
and to convert it to a unicode string encoded by utf-8.
'''

def use_utf(s):
    return s.encode('utf-8')

if __name__=='__main__':
    s = input("Enter a string: ")
    print(use_utf(s))