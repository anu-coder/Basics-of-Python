# implementing a context manager using class
# this class can be used with a "with statement" by mentioning the __enter__, __exit__ method
# https://book.pythontips.com/en/latest/context_managers.html



class ContextManager():
    def __init__(self, filename, modes):
        self.filename = filename
        self.modes= modes
        self.file_obj = open(filename, modes)
    def __enter__(self):
        return self.file_obj
    def __exit__(self, type, value, traceback):
        self.file_obj.close()

if __name__ == '__main__':
    with ContextManager('../data/new.txt', 'w') as f:
        f.write("hello buddies!")