import openpyxl
wb=openpyxl.load_workbook('example1.xlsx')
# sheet = wb['Sheet1']
# tuple(sheet['A1':'C3'])
# for row in sheet['A1':'C3']:
#     for cell in row:
#         print(cell.coordinate, cell.value)
#     print('----END OF ROW----')    
sheet = wb.active
for cell in sheet.iter_cols(min_col=1, max_col=1, min_row=1):
    for c in cell:
        print(c.value)