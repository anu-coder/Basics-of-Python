'''
Write a program which can 
filter even numbers in a list by using filter function. 
The list is: [1,2,3,4,5,6,7,8,9,10].
'''
def li_filter():
    l = [i for i in range(1,11)]
    even = filter(lambda x: x%2==0, l)
    return [i for i in even]

if __name__=='__main__':
    print(li_filter())