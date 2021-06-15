'''
Question: Define a class, 
which have a class parameter 
and have a same instance parameter.
'''
'''
Hints: Define a instance parameter, 
need to add it in init method. 
You can init a object with construct parameter 
or set the value later
'''

class Student():
    
    school = "MIS"

    def __init__(self, fname, lname, std):
        self.fname = fname
        self.lname = lname
        self.std = std

    def get_name(self):
        name = f'{self.fname} {self.lname}'
        return name

    def print_details(self):
        print("NAME: ", self.get_name())
        print("Stamdard: ", self.std)
        print("School: " , self.school)

if __name__=='__main__':
    s1 = Student("Anurima", 'Dey', 10)
    s2 = Student("Abhishek", 'Bhatia', 12)
    print("Student 1:")
    s1.print_details()
    print("-"*10, '\n')
    print("Student 2: ")
    s2.print_details()
    

    





