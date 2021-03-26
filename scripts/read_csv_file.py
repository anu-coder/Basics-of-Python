import csv

def read_csv_file(path):
    with open(path, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        colnames = next(csv_reader)
        content = []
        for lines in csv_reader:
            content.append(lines)
    return colnames, content

def display_columns(col_choice, max_rows, content):
    for lines in content[0:max_rows]:
        print(lines[col_choice-1])

if __name__ == '__main__':
    path = r"..\data\Favorite TV Shows - Form Responses 1.csv"
    colnames = read_csv_file(path)[0]
    content = read_csv_file(path)[1]
    print('The headers of the file are: ')
    for i, col in enumerate(colnames):
        print(f'{i+1}. {col}')
    col_choice = int(input("Choose a header: "))
    max_rows = int(input("Max rows to display: "))
    print()
    print(colnames[col_choice-1])
    print('-'*len(colnames[col_choice-1]))
    display_columns(col_choice, max_rows, content)

