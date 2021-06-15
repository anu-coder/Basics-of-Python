'''
Write a program which can map() 
to make a list whose elements are square of 
even elements in [1,2,3,4,5,6,7,8,9,10].
'''
def list_map():
    l = [i for i in range(1,11)]
    even = map(lambda x: x**2, filter(lambda x: x%2==0, l))
    evens = [i for i in even]
    print(evens)

if __name__=='__main__':
    list_map()