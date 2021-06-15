'''
Define a function that can accept two strings as input
and print the string with maximum length in console. 
If two strings have the same length, 
then the function should print all strings line by line.
'''

def two_strings(s1,s2):
    if len(s1)>len(s2):
        print(s1)
    elif len(s2)>len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)

if __name__=='__main__':
    s1 = input("Enter first sentence: ")
    s2 = input("Enter second sentence: ")
    two_strings(s1,s2)