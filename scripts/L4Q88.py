'''
By using list comprehension, 
please write a program to print the list 
after removing numbers 
which are divisible by 5 and 7 
in [12,24,35,70,88,120,155]
'''
def delete_div_5_7(l):
    return [i for i in l if (i%5!=0 and i%7!=0)]

if __name__=='__main__':
    l = list(map(int, input('Enter a list of numbers: ').split(',')))
    print(delete_div_5_7(l))

