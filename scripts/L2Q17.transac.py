'''
Question: Write a program that 
computes the net amount of a bank account 
based a transaction log from console input. 
The transaction log format is shown as following: 
D 100 W 200

D means deposit while 
W means withdrawal. 
Suppose the following input is supplied to the program: 
D 300 D 300 W 200 D 100 
Then, the output should be: 500
'''

def transactions(l):
    dic = {'D': [], 'W': []}
    for i, ele in enumerate(l):
        if ele == 'D':
            dic['D'].append(int(l[i+1]))
        elif ele == 'W':
            dic['W'].append(int(l[i+1]))
    
    return sum(dic['D']) - sum(dic['W'])


if __name__=='__main__':
    l = list(map(str, input("Enter the string of transactions: ").split(' ')))
    print(transactions(l))