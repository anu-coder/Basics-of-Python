# armstrong number: 153 = 1^3+5^3+3^3

def is_armstrong(n):
    s=0
    a = n
    while(n>0):
        p = n %10
        s = s + (p*p*p)
        n = int(n/10)
    if s == a:
        return True
    else:
        return False

n = int(input("Enter any number: "))
print(is_armstrong(n))
