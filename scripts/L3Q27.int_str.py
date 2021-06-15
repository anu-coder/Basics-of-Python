'''
Define a function that can convert 
a integer into a string and print it in console.
'''

def int_str_conv(n: int):
    print(str(n))


if __name__=='__main__':
    n = int(input("Enter a number: "))
    int_str_conv(n)