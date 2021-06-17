'''
Please write a program which count 
and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:
abcdefgabc
Then, the output of the program should be:
a,2 c,2 b,2 e,1 d,1 g,1 f,1
'''

def letter_count(s):
    count = {}
    for i in s:
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1
    
    return count

if __name__ == '__main__':
    s = input('Enter the string: ')
    print(letter_count(s))