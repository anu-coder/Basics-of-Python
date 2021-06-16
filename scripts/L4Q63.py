'''
Count the number of blankspaces in a string
'''

import re
def spcl_chars(s):
    return len(re.findall('[\s]+', s))

if __name__=='__main__':
    s = input('Enter a string: ')
    print(spcl_chars(s))