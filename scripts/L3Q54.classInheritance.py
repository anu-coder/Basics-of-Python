'''
Define a class named Shape
 and its subclass Square. 
 The Square class has an init function 
 which takes a length as argument. 
 Both classes have a area function 
 which can print the area of the shape 
 where Shape's area is 0 by default.
'''

class Shape():
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.l = l

    def area(self):
        return self.l**2

if __name__=='__main__':
    a = Square(3)
    print(a.area())




