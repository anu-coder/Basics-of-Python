'''
Question: Write a method which can calculate square value of number
'''

def square(n):
    return n**2


if __name__=='__main__':
    n = int(input("enter a number: "))
    print(square(n))