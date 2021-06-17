'''
Please write a program 
to print the list after 
removing delete even numbers 
in [5,6,77,45,22,12,24].
'''

def delete_even(l):
    return [i for i in l if i%2!=0]

if __name__=='__main__':
    l = list(map(int, input('Enter a list of numbers: ').split(',')))
    print(delete_even(l))