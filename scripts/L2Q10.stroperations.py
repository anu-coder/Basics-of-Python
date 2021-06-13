'''
Question: Write a program that accepts a sequence of whitespace separated words as input
and prints the words after removing all duplicate words and sorting them alphanumerically. 
Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again 
Then, the output should be: again and hello makes perfect practice world
'''

def list_sort_arrange(sent):
    words = sent.split(' ')
    check = []
    for word in words:
        if word not in check:
            check.append(word.lower())
    check.sort()
    return check

if __name__=='__main__':
    sent = input('Enter a sentence: ')
    print(' '.join(list_sort_arrange(sent)))
