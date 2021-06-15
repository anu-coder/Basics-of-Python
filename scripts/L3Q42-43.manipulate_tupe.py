'''
With a given tuple (1,2,3,4,5,6,7,8,9,10), 
write a program to print 
the first half values in one line and 
the last half values in one line.
'''

def tup_mani():
    tup = tuple(range(1,11))
    evn = [i for i in tup if i%2 == 0]
    print(tup[:5])
    print(tup[5:])
    print(tuple(evn))
    
if __name__=='__main__':
    tup_mani()
