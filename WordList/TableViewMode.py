from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from TranslateMap import *

'''
This is a class for table mode
--------------------------------------
    Author: Runquan Ye
    Date: Sept/2020
--------------------------------------
'''

class TableViewModel(QtCore.QAbstractTableModel):
    langMap = TranslateMap().getLanguageMap()
    lIndex = 0
    tableModeHeadList = []
    def __init__(self, data, tableModeHeadList):
        super(TableViewModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]
        if role == Qt.ForegroundRole:
            if self._data[index.row()][0] == "analysis":
                return QtGui.QColor('red')

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        return 4

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return [self.langMap["WORD"][self.lIndex], self.langMap["PT"][self.lIndex], self.langMap["PASTTERM"][self.lIndex], self.langMap["MEANING"][self.lIndex]][section]

            if orientation == Qt.Vertical:
                return section + 1

    def getTableModeHeadList(self):
        return self.tableModeHeadList

    def setTableModeHeadList(self, headList):
        self.tableModeHeadList = headList

    def getLangIndex(self):
        return self.lIndex


    def setLangIndex(self, index):
        if int(index) > 0:
            self.listNum = int(index)
