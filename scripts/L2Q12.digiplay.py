'''
Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) 
such that each digit of the number is an even number. 
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''

def even_digits(n: int):
    n1 = str(n)
    c = 0 
    for i in n1:
        if int(i)%2==0:
            c+=1
    if c == len(n1):
        return n

def even_range():
    even_digit = []
    for i in range(1000,3001):
        if even_digits(i):
            even_digit.append(i)
    return even_digit

if __name__=='__main__':
    print(*even_range(), sep = ',')

