import csv

with open('../data/rand_people.csv', mode = 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter = ',')
    csv_writer.writerow([8,'Reese,Risman','rrisman7@google.co.jp','Agender','220.214.110.99'])

