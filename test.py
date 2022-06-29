from shutil import copyfile
# import xlwings as xw

# out_xlfile = "output\\" + 'yyb_bm' + "_" + 'pz' + ".xlsx"
# copyfile("docs\\template.xlsx", out_xlfile)

# xlapp = xw.App(visible=False)
# # wb = xlapp.books.open(out_xlfile)
# wb = xw.Book(out_xlfile)
# ws = wb.sheets[0]

# # lastRow = ws.range('A' + str(wb.sheets[0].cells.last_cell.row)).end('up').row
# lastRow = ws.range('A1').end('down').row
# ws.range("A"+ str(lastRow+1)).options(index=False, header=False).value = [['','a','b','c','d','e','f'],['',1,2,3,4,5,6]]

# # lastRow = ws.range('A' + str(wb.sheets[0].cells.last_cell.row)).end('up').row
# lastRow = ws.range('A1').end('down').row
# ws.range("A"+ str(lastRow+1)).options(index=False, header=False).value = [['','a','b','c','d','e','f'],['',1,2,3,4,5,6]]

# # lastRow = ws.range('A' + str(wb.sheets[0].cells.last_cell.row)).end('up').row
# lastRow = ws.range('A1').end('down').row
# ws.range("A"+ str(lastRow+1)).options(index=False, header=False).value = [['','a','b','c','d','e','f'],['',1,2,3,4,5,6]]

# wb.save()
# xlapp.kill()


# import pyexcelerate
# import sys
# import time

#create data array
# row = range(0,10)
# i = 0
# data_array = []
# while i < 10000:
#     data_array.append(row)
#     i += 1
# data_array = [['','a','b','c','d','e','f'],['',1,2,3,4,5,6]]

# print(sys.version)

# out_xlfile = "output\\" + 'yyb_bm' + "_" + 'pz' + ".xlsx"
# copyfile("docs\\template.xlsx", out_xlfile)

# #create an excel workbook and sheet object
# out_wb = pyexcelerate.Workbook(out_xlfile)
# out_ws = out_wb.new_sheet("Sheet1")

# #single loop, writing rows
# start = time.time()

# # print("Writing with single loop using PyExcelerate")
# # out_wb.new_sheet("sheet name", data=data)
# out_ws.range("A3").value = data_array

# # print("Processing time: " + str(time.time() - start) + " seconds.")

# #close and save the file.
# out_wb.save('pyexcelerate.xlsx')
# print("Total time: " + str(time.time() - start) + " seconds.")



#!/usr/bin/env python


def case1(a,b):
    print("This is case 1")

def case2(a,b):
    print("This is case 2")

def case3(a,b):
    print("This is case 3")


token_dict = {
    "case1" : case1,
    "case2" : case2,
    "case3" : case3,
}

result = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}["c"](6)
print(result)


def main():
    cases = ("case1", "case3", "case2", "case1", "test")
    for case in cases:
        a=""
        b=""
        token_dict.get(case, lambda a,b : None)(a,b)

def test():
    None

if __name__ == '__main__':
    test()
    main()