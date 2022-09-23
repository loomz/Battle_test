import xlrd
import json
import csv

class CommonReadFile(object):
    def get_data_excel(filename, sheet=0):
        wb = xlrd.open_workbook((filename))
        # wb.sheet_by_index(0) 通过索引获得工作薄
        sheet = wb.sheet_by_index(sheet)
        rows = sheet.nrows  # 获取总行数
        cols = sheet.ncols  # 获取总列数
        lit = []
        for row in range(rows):  # 遍历行
            for col in range(cols):  # 遍历列
                col_data = sheet.cell_value(row, col)  # 获取单元格的值
                lit.append(col_data)
        return lit

    def get_data_cvs(file_cvs):
        #with opn 打开某文件 定义别名 f
        with open(file_cvs) as f:
            #读取里面值
            lst =csv.reader(f)
            my_data = []
            for row in lst:
                my_data.extend(row)
            return my_data

    def get_data_json(file_json,key_name):
        with open(file_json) as f:
            lit = []
            data = json.load(f)
            # extend 追加
            lit.extend(data[key_name])
            return lit