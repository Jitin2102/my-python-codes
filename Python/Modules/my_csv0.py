import csv
with open('pdt.csv','w',newline='') as file:
    csvWriter = csv.writer(file,delimiter='\t', lineterminator='\n\n')
    fileWriter=csv.writer(file)
    fileWriter.writerow(['Name','Age','City'])
    fileWriter.writerow(['Arjit',21,'Lucknow'])
    fileWriter.writerow(['Kisan',22,'Raibareli'])
file.close() 