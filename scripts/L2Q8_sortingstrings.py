'''
Question: Write a program that accepts a comma separated sequence of words as input 
and prints the words in a comma-separated sequence after sorting them alphabetically. 
Suppose the following input is supplied to the program: without,hello,bag,world 
Then, the output should be: bag,hello,without,world
'''

import pandas as pd

def sortlist(l):
    '''Just sorting a list'''
    l.sort()
    return l

if __name__ == '__main__':
    l = list(map(str, input("Enter some words: ").split(',')))
    print(','.join(sortlist(l)))