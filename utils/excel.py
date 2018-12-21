#-*-coding:utf-8-*-
#__author__='maxiaohui'

from win32com.client import Dispatch
import time

class easyExcel:  # 用于excel处理

    def __init__(self, filename=None):  # 打开文件或者新建文件（如果不存在的话）
        self.xlApp = Dispatch('Excel.Application')
        self.xlApp.Visible = True
        if filename:
            self.filename = filename
            self.xlBook = self.xlApp.Workbooks.Open(filename)
        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = ''

    def addSheet(self, sheetname):  # 加入一个指定名称的sheet
        self.xlApp.Worksheets.Add().Name = sheetname
        xlSheet = self.xlApp.Worksheets(sheetname)
        return xlSheet

    def getSheet(self, sheetname):  # 根据名称获得某个sheet
        xlSheet = self.xlApp.Worksheets(sheetname)
        return xlSheet

    def removeFloat(self, v):  # 处理excel读出的数字变成了浮点类型
        if str(v).find(".0") >= 0:
            b = str(v)
            c = b.replace(".0", "")
        else:
            c = str(v)
        return c

    def writeCellwithBeforeValue(self, xlSheet, r, c, v):  # 写cell,处理原有item叠加
        vBefore = xlSheet.Cells(r, c).Value
        if vBefore == None:
            time.sleep(0.01)
            xlSheet.Cells(r, c).Value = v
        else:
            time.sleep(0.005)
            vBefore = self.removeFloat(vBefore)
            xlSheet.Cells(r, c).Value = str(vBefore) + ';' + v

    def writeCell(self, xlSheet, r, c, v):  # 写cell
        # time.sleep(0.02)
        xlSheet.Cells(r, c).Value = v

    def getCell(self,xlSheet,r,c):
        return xlSheet.Cells(r,c).Value

    def writeRow(self, xlSheet, list, rowID, startColumn=1):  # 把列表写入指定行,可指定起始列
        for i in range(startColumn, startColumn + len(list)):
            self.writeCell(xlSheet, rowID, i, list[i - startColumn])

    def filterColumnTextContains(self, xlSheet, rowNumbers, columnNumber, filterChar):  # 筛选出某一列包含某字符串的条目的个数
        count = 0
        for i in range(2, rowNumbers + 1):
            if xlSheet.Cells(i, columnNumber).find(filterChar) >= 0:
                count += 1
        return count

    def findTxtInColumn(self, sheet, column, startRow, endRow, txt):
        rowNum = 0
        for i in range(startRow, endRow + 1):
            if sheet.Cells(i, column).Value == txt:
                rowNum = i
                break
        # print(rowNum)
        return rowNum

    def get_cell_cols(self, sheet):  # 获得总得列数
        return sheet.UsedRange.Columns.Count

    def getRange(self,sht,row1,col1,row2,col2):  #获得某一个范围的值
        return sht.Range(sht.Cells(row1, col1), sht.Cells(row2, col2)).Value

    def save(self):
        self.xlBook.Save()

    def getTestCase(self,xlSheet,row):  # 获得相关case的数据 -- fiddler中
        testModule=xlSheet.Cells(row,2).Value
        testName=xlSheet.Cells(row,3).Value
        testMethod=xlSheet.Cells(row,4).Value
        testUrl=xlSheet.Cells(row,5).Value
        runOrNot=xlSheet.Cells(row,7).Value
        testAccount=xlSheet.Cells(row,6).Value
        data1=xlSheet.Cells(row,11).Value
        expectedResult1=xlSheet.Cells(row,12).Value
        dict={'module':testModule,'name':testName,'method':testMethod,'url':testUrl,'run':runOrNot,'account':testAccount,'test_data':data1,'expected':expectedResult1}
        return dict

    def getSwaggerTestCase(self,xlSheet,row): #获得相关case数据
        testName = xlSheet.Cells(row, 2).Value
        testMethod = xlSheet.Cells(row, 3).Value
        testUrl = xlSheet.Cells(row, 4).Value
        testHeaders = xlSheet.Cells(row, 5).Value
        testData = xlSheet.Cells(row, 6).Value
        testRole = xlSheet.Cells(row, 8).Value
        dict = { 'name': testName, 'method': testMethod, 'url': testUrl,'header':testHeaders,'test_data':testData,'role':testRole}
        return dict

    def getSwaggerTestCaseUpdate(self,xlSheet,row): #获得相关case数据
        testName = xlSheet.Cells(row, 4).Value
        testMethod = xlSheet.Cells(row, 6).Value
        testUrl = xlSheet.Cells(row, 5).Value
        testHeaders = xlSheet.Cells(row, 7).Value
        testData = xlSheet.Cells(row, 8).Value
        testRole = xlSheet.Cells(row, 10).Value
        dict = { 'name': testName, 'method': testMethod, 'url': testUrl,'header':testHeaders,'test_data':testData,'role':testRole}
        return dict


if __name__ == "__main__":
    pass