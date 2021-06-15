'''
Define a function that can accept two strings as input 
and concatenate them and then print it in console.
'''

def concatenate(s1, s2):
    return f'{s1}{s2}'

if __name__=='__main__':
    s1,s2 = list(map(str, input("Enter two strings seperated by comma: ").split(',')))
    print(concatenate(s1, s2))