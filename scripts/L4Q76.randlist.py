'''
Please write a program to output 
a random even number between 
0 and 10 inclusive using random module and 
list comprehension.
'''

import random
def randlist(n):
    return [random.choice([i for i in range(n+1) if i%2==0])]

if __name__=='__main__':
    n = int(input('Enter a number n for [0, n]: '))
    print(*randlist(n))



