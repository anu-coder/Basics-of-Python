'''
Write a function to 
compute 5/0 and 
use try/except to catch the exceptions.
'''

def exception():
    return 5/0


if __name__=='__main__':
    try:
        exception()
    except ZeroDivisionError:
        print('Error: Divided by zero')
    except Exception:
        print("Found an exception")
    finally:
        print("This is the finally step")




