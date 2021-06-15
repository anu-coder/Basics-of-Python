'''
Define a class named Rectangle which can be constructed 
by a length and width. 
The Rectangle class has a method 
which can compute the area.
'''
class Rectangle():

    def __init__(self, length, width):
        self.l = length
        self.w = width

    def area(self):
        return self.l*self.w

if __name__=='__main':
    r = Rectangle(8,2)
    print(r.area())

