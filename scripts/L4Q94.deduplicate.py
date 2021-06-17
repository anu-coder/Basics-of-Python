'''
Q 94: With a given list 
[12,24,35,24,88,120,155,88,120,155], 
write a program to print this list after removing 
all duplicate values with original order reserved.
'''


def deduplicate(l):
    out_list = []
    for i in l:
        if i not in out_list:
            out_list.append(i)

    return out_list


if __name__=='__main__':
    l = [12,24,35,24,88,120,155,88,120,155]
    print(deduplicate(l))