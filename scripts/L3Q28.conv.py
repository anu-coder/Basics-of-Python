'''
Define a function that can receive two integral numbers
in string form and 
compute their sum and then 
print it in console.
'''

def int_to_Str(x,y):
    return (int(x)+int(y))


if __name__=='__main__':
    x, y = list(map(str, input("Entr two numbers: ").split(',')))
    print(int_to_Str(x,y))