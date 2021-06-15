'''
Define a class named American and its subclass NewYorker.
'''
class American():
    country = 'America'

class NewYorker(American):
    state = 'NewYork'

    def get_values(self):
        print(self.country)
        print(self.state)

if __name__== '__main__':
    A = American()
    NY = NewYorker()
    # print(A.__init__)
    NY.get_values()