'''
Question: A website requires the users to 
input username and password to register. 
Write a program to check the validity of password 
input by users. 
Following are the criteria for 
checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12 
Your program should accept a sequence of 
comma separated passwords 
and will check them according 
to the above criteria. 
Passwords that match the criteria 
are to be printed, 
each separated by a comma. 
Example If the following passwords are given 
as input to the program: 
ABd1234@1,a F1#,2w3E*,2We3345 
Then, the output of the program should be: 
ABd1234@1
'''
import re
def password_validator(password):
    '''validate passwords'''
    lower = len(re.findall(r'[a-z]', password))
    number = len(re.findall(r'[0-9]', password))
    upper = len(re.findall(r'[A-Z]', password))
    charac = len(re.findall(r'[$#@]', password))
    length = lower + number + upper + charac
    
    if (lower>=1 and number>=1 and upper>=1 and charac>=1) and length>= 6 and length<=12 and length == len(password):
        return password

if __name__=='__main__':
    passwords = list(map(str, input('Enter passwords in comma seperated format: ').split(',')))
    output = [password_validator(password) for password in passwords if password_validator(password)]
    print(*output, sep = ',')