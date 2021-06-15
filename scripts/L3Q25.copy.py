'''
Rewriting class for practise
'''
class Student():
    
    school = "MIS"

    def __init__(self, fname, lname, std):
        self.fname = fname
        self.lname = lname
        self.std = std

    def get_name(self):
        return f'{self.fname} {self.lname}'

    def get_details(self):
        print("Full name: ", self.get_name())
        print("Standard: ", self.std)
        print("School: " , self.school)

if __name__ == '__main__':
    s1 = Student('Anurima', 'Dey', 10)
    s2 = Student('Abhishek', 'Bhatia', 12)
    s3 = Student('Dinesh Uncle', 'Bhatia', 'Inf')
    print('Student 1: ')
    s1.get_details()
    print('-'*10 , '\n')
    print('Student 2: ')
    s2.get_details()
    print('-'*10, '\n')
    print('Student 3: ')
    s3.get_details()