'''
Please write a program 
which accepts a string from console and 
print the characters that have even indexes.
'''

def even_idx(s):
    return s[::2].lower()

if __name__=='__main__':
    s = input('Enter a string: ')
    print(even_idx(s))