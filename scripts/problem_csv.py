import csv

def read_csv_file(path):
    with open(path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        colnames = next(csv_reader)
                
    i = 1
    for col in colnames:
        print(f'{i}. {col}')
        i+=1

if __name__ == '__main__':
    path = 'data\Favorite TV Shows - Form Responses 1.csv'
    print(read_csv_file(path))
    choice = input("Choose a header: ")
    max_rows = input("Max rows to display: ")
