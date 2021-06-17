'''
Please write a program which 
prints all permutations of [1,2,3]
'''
import itertools

def all_permutations(l):
    return list(itertools.permutations(l))


if __name__=='__main__':
    l = [1,2,3]
    print(all_permutations(l))