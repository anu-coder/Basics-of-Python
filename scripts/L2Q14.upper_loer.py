'''
Question: Write a program that accepts a sentence 
and calculate the number of upper case letters and lower case letters. 
Suppose the following input is supplied to the program: 
Hello world! 
Then, the output should be: 
UPPER CASE 1 LOWER CASE 9
'''

import re
def upper_lower(s):
    upper = re.findall(r'[A-Z]', s)
    lower = re.findall(r'[a-z]', s)
    return f'UPPER CASE {len(upper)} LOWER CASE {len(lower)}'

if __name__=='__main__':
    s=input('Enter a sentence: ')
    print(upper_lower(s))