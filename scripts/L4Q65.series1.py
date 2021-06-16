'''
Write a program to compute 
1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
'''

def series(n):
    s = 0
    for i in range(1,n+1):
        s = s + i/(i+1)

    return round(s, 2)

if __name__=='__main__':
    n = int(input("Enter an integer: "))
    print(series(n))
