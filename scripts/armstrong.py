# armstrong number: sum of the cubes of the digits equals number: eg: 153 = 1^3+5^3+3^3

def is_armstrong(n):
    sum_of_cubes=0
    a = n
    while(n>0):
        p = n %10
        sum_of_cubes = sum_of_cubes + (p**3)
        n = int(n/10)
    if sum_of_cubes == a:
        return True
    else:
        return False


if __name__ == '__main__':
    n = int(input("Enter any number: "))
    print(is_armstrong(n))
