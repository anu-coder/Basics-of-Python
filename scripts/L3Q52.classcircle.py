'''
Define a class named Circle 
which can be constructed by a radius. 
The Circle class has a method which can compute the area.
'''

class Circle():
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2
    
if __name__=='__main__':
    c1 = Circle(6)
    print("The area of the circle is: ", c1.area())
