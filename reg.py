import csv
filename1=input("enter the csv filename(with .csv extension):")
with open(filename1,'r')as csvfile:
    csvreader=csv.reader(csvfile)
    for row in csvreader:
        print(row)
