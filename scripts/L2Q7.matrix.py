'''
Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j. 
Note: i=0,1.., X-1; j=0,1,¡­Y-1. 
Example Suppose the following inputs are given to the program: 3,5 
Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''

import numpy as np

def matrix(x,y):
    ''' 
    Returns a matrix with the entries as i*j where i = 0,1,..,x-1, and j = 0,1,2,...,y-1
    '''
    mat = np.empty([x,y], dtype = int)
    for i in range(x):
        for j in range(y):
            mat[i][j] = i*j
    return mat

if __name__ == '__main__':
    x,y = list(map(int, input('Enter the dimensions: ').split(' ')))
    print(matrix(x,y))

