'''
Use a list comprehension to square each odd number in a list. 
The list is input by a sequence of comma-separated numbers. 
Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9 
Then, the output should be: 
1,9,25,49,81
'''

def list_sq(l: list):
    return [i*i for i in l if i%2!=0]


if __name__=='__main__':
    l = list(map(int, input('Enter comma seperated numbers: ').split(',')))
    print(*list_sq(l), sep = ',')