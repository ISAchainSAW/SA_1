import openpyxl as oxl

wb = oxl.load_workbook('SBER.xlsx')
sheet = wb.sheetnames[0]
ws = wb.active
pay = []
for i in ws.values:
    if i == 0:
        break
    else:
        pay.append(i[1])
# for i in range(len(pay)):
#     print(pay[i*3],pay[i*3]+1,pay[i*3]+2)
