'''
Example: If the following email address is given as input to the program:
john@google.com
Then, the output of the program should be:
google
'''


import re
def extract_cnames(l):
    '''Simple split for extracting usernames from emial ids'''
    cnames = []
    for elems in l:
        cnames.append(re.split('[@|.]', elems)[1])
    
    return cnames



if __name__=='__main__':
    l = list(map(str, input("Enter list of email ids in comma seperated format: ").split(',')))
    print(*extract_cnames(l), sep = ',')