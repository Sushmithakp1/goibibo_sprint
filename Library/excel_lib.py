import xlrd
from Library import config


def read_locators():
    workbook = xlrd.open_workbook(config.Config.LOCATOR_PATH)
    worksheet = workbook.sheet_by_name('locators_sheet')
    rows = worksheet.nrows
    d = {}

    for i in range(rows):
        row = worksheet.row_values(i)
        d[row[0]] = (row[1], row[2])
    return d


print(read_locators())



def read_data():
    workbook = xlrd.open_workbook(config.Config.TEST_DATA_PATH)
    worksheet = workbook.sheet_by_name('Test_data')
    rows = worksheet.get_rows()
    header = next(rows)
    columns = worksheet.ncols
    list1 = []
    for i in rows:
        values = ()
        for j in range(columns):
            values += (i[j].value,)
        list1.append(values)
    return list1
print(read_data())





# import xlrd
# from Library.config import Config
#
# class ReadExcel:
#
#     def read_testdata(self, sheetname):
#
#         wb = xlrd.open_workbook(Config.TEST_DATA_PATH)
#         ws = wb.sheet_by_name(sheetname)
#         columns = ws.ncols
#         rows = ws.get_rows()
#         header = next(rows)
#         data = []
#
#         for row in rows:
#             if columns == 1:
#                 data.append(row[0].value)
#             else:
#
#                 values = ()
#                 for j in range(columns):
#                     values += (row[j].value,)
#                 data.append(values)
#         return data
#
#     def read_locators(self, sheetname):
#         wb = xlrd.open_workbook(Config.LOCATOR_PATH)
#         ws = wb.sheet_by_name(sheetname)
#         rows = ws.get_rows()
#         header = next(rows)
#
#         d = {}
#         for row in rows:
#             d[row[0].value] = (row[1].value, row[2].value)
#         return d
#         print(d)

# import xlrd
# from Library import config
#
# def read_locators():
#     workbook = xlrd.open_workbook(config.Config.LOCATOR_PATH)
#     worksheet = workbook.sheet_by_name('locators_sheet')
#     rows = worksheet.nrows
#     d = {}
#
#     for i in range(rows):
#         row = worksheet.row_values(i)
#         d[row[0]] = (row[1], row[2])
#     return d
#
# print(read_locators())
#
#
# #
# def read_data():
#     workbook = xlrd.open_workbook(config.Config.TEST_DATA_PATH)
#     worksheet = workbook.sheet_by_name('Test_data')
#     rows = worksheet.get_rows()
#     header = next(rows)
#     columns = worksheet.ncols
#     list1 = []
#     for i in rows:
#         values = ()
#         for j in range(columns):
#             values +=(i[j].value,)
#         list1.append(values)
#     return list1
#
# print(read_data())
