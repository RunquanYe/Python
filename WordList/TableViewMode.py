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
    _langMap = TranslateMap().getLanguageMap()
    _lIndex = 0
    _tableModeHeadList = []
    _headWordColor = QtGui.QColor('red')
    _subWordColor = QtGui.QColor('black')
    def __init__(self, data, tableModeHeadList):
        super(TableViewModel, self).__init__()
        self._data = data
        self._tableModeHeadList = tableModeHeadList

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]
        if role == Qt.ForegroundRole:
            if self._data[index.row()][0] in self._tableModeHeadList:
                return self._headWordColor
            else:
                return self._subWordColor

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        return 4

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return [self._langMap["WORD"][self._lIndex], self._langMap["PT"][self._lIndex], self._langMap["PASTTERM"][self._lIndex], self._langMap["MEANING"][self._lIndex]][section]

            if orientation == Qt.Vertical:
                return section + 1


    def getTableModeHeadList(self):
        return self._tableModeHeadList


    def setTableModeHeadList(self, headList):
        self._tableModeHeadList = headList


    def getLangIndex(self):
        return self._lIndex


    def setLangIndex(self, index):
        if int(index) > 0:
            self._listNum = int(index)


    def setHeadWordColor(self, headColor):
        if QtGui.QColor(headColor) and QtGui.QColor(headColor).getRgb() != self._headWordColor.getRgb():
            self._headWordColor = QtGui.QColor(headColor)


    def setSubWordColor(self, subColor):
        if QtGui.QColor(subColor) and QtGui.QColor(subColor).getRgb() != self._subWordColor.getRgb():
            self._subWordColor = QtGui.QColor(subColor)