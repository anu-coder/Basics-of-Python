'''
Write a program which accepts a sequence of comma-separated numbers from console 
and generate a list and a tuple which contains every number. 
Suppose the following input is supplied to the program: 34,67,55,33,12,98 
Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')
'''

def tuple_list(x):
    return list(x), tuple(x)

if __name__ == '__main__':
    x = list(map(int, input('Enter comma seperated numbers').split(',')))
    print(*tuple_list(x))