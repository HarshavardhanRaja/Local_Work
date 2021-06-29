# CSV => Comma Seperated Values

# Read, Parse and Write to CSV files
import csv

with open('namess.csv', 'r+') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)
    row = []
    #next(csv_reader)    # this will not take the first row from the file

    
    with open('new_names.csv', 'w') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '\t')
        for item in csv_reader:
            csv_writer.writerow(item)


with open('new_names.csv', 'r') as new_names:
    csv_reader2 = csv.reader(new_names, delimiter = '\t') 

    for item in csv_reader2:
        print(item)


# using Dictonary reader and Dictonary writer
with open('namess.csv', 'r+') as csv_file1:
    csv_reader1 = csv.DictReader(csv_file1)
    for line in csv_reader1:
        print(line)

    # using Dictonary writer to write to a file
    """

    with open('new_names.csv', 'w') as new_file:
    field_names = ['first_name', 'last_name', 'email']
    csv_writer = csv.DictWriter(new_file, fieldnames=field_names, delimiter = '\t')
    csv_writer.writeheader()
    for item in csv_reader:
        csv_writer.writerow(item)

    """