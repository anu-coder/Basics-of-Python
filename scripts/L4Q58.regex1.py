'''
Assuming that we have some email addresses in 
the "username@companyname.com" format, 
please write program to print the 
user name of a given email address. 
Both user names and company names are composed of letters only.

Example: If the following email address is 
given as input to the program:
john@google.com
Then, the output of the program should be:
john
'''

'''
I feel it will only take up more of my time and space, 
I will only end up entangling myself more into this karmic account. 
I just want to be done with this man, Prantik for life. 
This is just one thing that is keeping me away from taking a 
legal step after all that I am going through. 
'''

# import re
def extract_usernames(l):
    '''Simple split for extracting usernames from emial ids'''
    usernames = []
    for elems in l:
        usernames.append(elems.split('@')[0])
        # usernames.append(re.findall('[A-Za-Z]', elems)[0])
    
    return usernames



if __name__=='__main__':
    l = list(map(str, input("Enter list of email ids in comma seperated format: ").split(',')))
    print(*extract_usernames(l), sep = ',')