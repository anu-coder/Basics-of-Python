'''
Define a custom exception class which takes a string message 
as attribute.
'''


class RaiseCustomException(Exception):
    '''
    '''
    def __init__(self, msg):
        self.msg = msg


def dodone():
    return print(RaiseCustomException("Exception: No such functions defined"))

if __name__=='__main__':
    dodone()
    
