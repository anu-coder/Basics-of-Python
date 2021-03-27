# reading from a csv file

import csv

with open('../data/people.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    count = 0
    content = []
    for lines in csv_reader:
        if count == 0:
            header = lines
            count +=1
        else:
            content.append(lines)
            count+=1


if __name__=='__main__':
    print(f'Number of rows: {count}')
    print()
    print("The headers are:")
    print('\n'.join(header))
    print()
    print("First five rows: ")
    [print(content[i]) for i in range(5)]

