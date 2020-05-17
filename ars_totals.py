import xlrd

book = xlrd.open_workbook("dummy_ar.xlsx")
sheet = book.sheet_by_index(0)

print(sheet.ncols)
print(sheet.nrows)

ars_list = list(set(sheet.col_values(2)))
ars_list.remove("ARS")

print(ars_list)

ars_totals = []

for n in ars_list:
    ars_totals.append(0.0)

for row_idx in range(1, sheet.nrows):
    ars = sheet.cell_value(row_idx, 2)
    ars_totals[ars_list.index(ars)] += (sheet.cell_value(row_idx, 3))

for t in range(len(ars_totals)):
    print(ars_list[t] + ": " + str(ars_totals[t]))