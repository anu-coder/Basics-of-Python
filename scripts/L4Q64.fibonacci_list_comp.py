'''
The Fibonacci Sequence is computed 
based on the following formula:
f(n)=0 if n=0 f(n)=1 if n=1 f(n)=f(n-1)+f(n-2) if n>1
Please write a program using list comprehension 
to print the Fibonacci Sequence in comma separated form 
with a given n input by console.
Example: 
If the following n is given as input to the program:
7
Then, the output of the program should be:
0,1,1,2,3,5,8,13
'''

# def fibo_list(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         [(i-1)+ (i-2) for i in range(2,n+1)]

# def fibo_list(n):
#     s = [0, 1]
#     s += [(s := [s[1], s[0] + s[1]]) and s[1] for k in range(n)]
#     return s

def fibo_list(n):
    series=[]
    series.append(1)
    series.append(1)
    [series.append(series[k-1]+series[k-2]) for k in range(2,n)]
    return series

if __name__=='__main__':
    n = int(input("Enter a number: "))
    print(fibo_list(n))

