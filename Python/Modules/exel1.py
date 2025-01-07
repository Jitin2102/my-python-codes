import openpyxl

print('opening Workbook...')
wb=openpyxl.load_workbook('exel3.xlsx')
sheet=wb.active
countryData={}
print('Reading rows...')
for row in range(2,sheet.max_row + 1):
    state=sheet['B'+str(row)].value
    country=sheet['C'+str(row)].value
    pop=sheet['D' +str(row)].value
print("Done!")    