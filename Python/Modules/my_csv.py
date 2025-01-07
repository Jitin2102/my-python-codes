import csv
with open('new.csv', newline='') as file:
    fileReader=csv.reader(file)
    fileData=list(fileReader)
    for row in fileData:
        print(row)
#FIRST INSTALL CSV MODULE
