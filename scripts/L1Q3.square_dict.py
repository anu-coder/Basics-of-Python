'''
Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) 
such that is an integral number between 1 and n (both included). 
and then the program should print the dictionary. 
Suppose the following input is supplied to the program: 8 
Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''


def generate_dict(n: int):
    out_dict = {}
    for i in range(1,n+1):
        out_dict[i] = i*i
    return out_dict

# def test_generate_dict():
#     generate_dict(8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

if '__name__' == '__main__':
    # test_generate_dict()
    print(generate_dict(8))

