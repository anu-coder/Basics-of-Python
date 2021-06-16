'''
Write a program which accepts a sequence of words 
separated by whitespace as input to print the words 
composed of digits only.
Example: If the following words is given as input to the program:
2 cats and 3 dogs.
Then, the output of the program should be:
['2', '3']
'''



import re
def only_digits(l):
    return re.findall('[\d]+', l)

if __name__=='__main__':
    l = input('Enter a digit: ')
    print(only_digits(l))