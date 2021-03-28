# implementing context manager as a generator

from contextlib import contextmanager

@contextmanager
def write_file(path):
    f = open(path, 'w')
    try:
        yield f
    finally:
        f.close()


if __name__=='__main__':
    path = r"../data/c_g_gen.txt"
    with write_file(path) as f:
        f.write("Hello world? \n How have you been?")