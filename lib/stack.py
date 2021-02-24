import os
import csv

with open('input.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    header = readCSV.next()
    for row in readCSV:
        dirname = "/".join((row[2]))
        if not os.path.exists(dirname):
            os.makedir(dirname)