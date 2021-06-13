'''
Question: Write a program which can compute the factorial of a given numbers. 
The results should be printed in a comma-separated sequence on a single line. 
Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

The factorial procedure used here is normal recurssion, later we shall try to also find out other ways.
'''

def factorial(n: int):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def test_factorial():
    assert factorial(8) == 40320

if __name__ == '__main__':
    test_factorial()
    # print(factorial(8))