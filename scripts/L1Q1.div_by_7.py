'''
Question 1: Write a program which will find all such numbers which are divisible by 7
but are not a multiple of 5, between 2000 and 3200 (both included). 
The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
def div_by_7_not_5():
    '''
    Displays numbers divisible by 7 but not by 5
    '''
    output_list = []
    for i in range(2000,3200+1):
        if i%7 == 0 and i%5 != 0:
            output_list.append(i)
    return output_list

def test_div_by_7_not_5():
    assert len(div_by_7_not_5()) == 138

if __name__ == '__main__':
    print(div_by_7_not_5())








