'''
Please write a program to randomly print a integer number 
between 7 and 15 inclusive.
'''

import random


l = []
for i in range(0,100):
    l.append(random.randrange(7,16))

print(l)