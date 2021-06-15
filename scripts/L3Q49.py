'''
Write a program which can map() 
to make a list whose elements are square of numbers 
between 1 and 20 (both included).
'''

sq = map(lambda x: x**2, range(1,21))
print([i for i in sq])
