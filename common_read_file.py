
import xlrd

def get_data_excel():
    filename = 'data.xlsx'
    wb = xlrd.open_workbook((filename))
    # wb.sheet_by_index(0) 通过索引获得工作薄
    sheet = wb.sheet_by_index(0)
    rows = sheet.nrows  # 获取总行数
    cols = sheet.ncols  # 获取总列数
    lit = []
    for row in range(rows):  # 遍历行
        for col in range(cols):  # 遍历 列
            col_data = sheet.cell_value(row, col)  # 获取单元格的值
            lit.append(col_data)
    return lit