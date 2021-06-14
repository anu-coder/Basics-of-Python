''' 
Question: Write a program that computes 
the value of a+aa+aaa+aaaa 
with a given digit as the value of a. 
Suppose the following input is supplied to the program: 
9 
Then, the output should be: 
11106
'''

def mathstring(a):
    s = 0
    for i in range(1, 5):
        s = s + int(a*i)
    return s

if __name__=='__main__':
    a = input('Enter any number: ')
    print(mathstring(a))