reviews-per-country
import csv

with open('winemag-data-130k-v2.csv', 'r') as csv-file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line)