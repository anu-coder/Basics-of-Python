'''
Question: Write a program that accepts a sentence and calculate the number of letters and digits. 
Suppose the following input is supplied to the program: hello world! 123 
Then, the output should be: LETTERS 10 DIGITS 3
'''
import re

def letters_numbers(sent):
    letters = re.findall(r'[a-zA-Z]', sent)
    numbers = re.findall(r'[0-9]', sent)
    return f'LETTERS {len(letters)} DIGITS {len(numbers)}'

if __name__=='__main__':
    sent = input("Enter a sentence: ")
    print(letters_numbers(sent))