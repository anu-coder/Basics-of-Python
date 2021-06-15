'''
Define a function which can 
print a dictionary where the keys are numbers 
between 1 and 20 (both included) and 
the values are square of keys.
'''

def print_dict():
    dict = {}
    for i in range(1,21):
        dict[i] = i**2
    
    print(*dict.values(), sep = ',')

if __name__=='__main__':
    print_dict()
