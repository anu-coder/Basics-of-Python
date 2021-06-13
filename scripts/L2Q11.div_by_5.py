'''
Question: Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence. 
Example: 0100,0011,1010,1001 
Then the output should be: 1010 
Notes: Assume the data is input by console.
'''

def div_by_5(l: list):
    out = []
    for i in l:
        if i%5==0:
            out.append(i)
    return out

if __name__=='__main__':
    l = list(map(int, input('Enter four digit numbers: ').split(',')))
    print(*div_by_5(l), sep = ',')
