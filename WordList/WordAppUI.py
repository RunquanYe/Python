# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QFont, QColor, QStandardItem
from PyQt5.QtWidgets import QSplitter, QHBoxLayout, QTableWidget, QAbstractItemView, QLabel
from TranslateMap import *
from TableViewMode import *
import sys
'''
This is a GUI for the word application
--------------------------------------
    Author: Runquan Ye
    Date: Sept/2020
--------------------------------------
'''

class Ui_MainWindow(object):
    _langMap = TranslateMap().getLanguageMap()
    _lIndex = 0
    _onlineSource = "Bing"
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 12, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)

        # tabWidget and wordListTab
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.wordListTab = QtWidgets.QWidget()
        self.wordListTab.setObjectName("wordListTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.wordListTab)
        self.gridLayout_2.setContentsMargins(8, 5, 8, 8)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # wordListTable
        self.wordListTable = QtWidgets.QTableView(self.wordListTab)
        self.wordListTable.setObjectName("wordListTable")
        self.wordListTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.wordListTable.horizontalHeader().setStretchLastSection(True);
        self.wordListTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.gridLayout_2.addWidget(self.wordListTable, 0, 0, 1, 1)
        self.tabWidget.addTab(self.wordListTab, "")

        # headListSpanTab
        self.headListSpanTab = QtWidgets.QWidget()
        self.headListSpanTab.setObjectName("headListSpanTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.headListSpanTab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        # self.gridLayout_3.setContentsMargins(8, 5, 8, 8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.container = QtWidgets.QFrame(self.headListSpanTab)
        self.container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.container.setObjectName("container")

        # headSpanTable
        self.headSpanTable = QtWidgets.QTableView(self.container)
        self.headSpanTable.setMinimumWidth(35 * MainWindow.width() / 50)
        self.headSpanTable.setGeometry(QtCore.QRect(170, 0, 541, 501))
        self.headSpanTable.setObjectName("headSpanTable")
        self.headSpanTable.setColumnWidth(3, MainWindow.width() / 3)
        self.headSpanTable.horizontalHeader().setStretchLastSection(True);
        self.headSpanTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.headSpanTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        # headSpanTree
        self.headSpanTree = QtWidgets.QTreeView(self.container)
        self.headSpanTree.setObjectName("headSpanTree")
        self.headSpanTree.setGeometry(QtCore.QRect(0, 0, 90, 501))
        self.headSpanTree.setMinimumWidth(50)
        self.treeModel = QStandardItemModel()
        self.rootNode = self.treeModel.invisibleRootItem()
        self.headSpanTree.setHeaderHidden(True)
        self.headSpanTree.setModel(self.treeModel)
        self.headSpanTree.expandAll()

        #add the splitter
        hbox = QHBoxLayout()
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(self.headSpanTree)
        splitter.addWidget(self.headSpanTable)
        splitter.setSizes([75, 250])
        splitter.setCollapsible(0, False)
        splitter.setCollapsible(1, False)
        hbox.addWidget(splitter)
        hbox.setContentsMargins(7, 0, 7, 5)
        self.container.setLayout(hbox)

        self.gridLayout_3.addWidget(self.container, 0, 0, 1, 1)
        self.tabWidget.addTab(self.headListSpanTab, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        self.tabWidget.setCurrentIndex(0)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuOperation = QtWidgets.QMenu(self.menubar)
        self.menuOperation.setObjectName("menuOperation")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionUpdate = QtWidgets.QAction(MainWindow)
        self.actionUpdate.setObjectName("actionUpdate")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAbout_Programmer = QtWidgets.QAction(MainWindow)
        self.actionAbout_Programmer.setObjectName("actionAbout_Programmer")
        self.actionAbout_Application = QtWidgets.QAction(MainWindow)
        self.actionAbout_Application.setObjectName("actionAbout_Application")
        self.actionAdd = QtWidgets.QAction(MainWindow)
        self.actionAdd.setObjectName("actionAdd")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionModify = QtWidgets.QAction(MainWindow)
        self.actionModify.setObjectName("actionModify")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionReset = QtWidgets.QAction(MainWindow)
        self.actionReset.setObjectName("actionReset")
        self.actionSelect_Dictionary = QtWidgets.QAction(MainWindow)
        self.actionSelect_Dictionary.setObjectName("actionSelect_Dictionary")
        self.actionSelect_Languary = QtWidgets.QAction(MainWindow)
        self.actionSelect_Languary.setObjectName("actionSelect_Languary")

        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionUpdate)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionHelp)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionAdd)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addAction(self.actionModify)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionReset)
        self.menuOperation.addAction(self.actionSelect_Dictionary)
        self.menuOperation.addAction(self.actionSelect_Languary)
        self.menuAbout.addAction(self.actionAbout_Application)
        self.menuAbout.addAction(self.actionAbout_Programmer)
        self.menuAbout.addSeparator()

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOperation.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        # add button listener
        # self.actionOpen.triggered.connect(lambda pass)

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.status_Internet = QLabel('Wifi Connection: ' + 'on')
        self.status_Lang = QLabel('Language: ' + ('中文' if self._lIndex == 1 else 'English'))
        self.status_Dictionary = QLabel('Dictionary Source: ' + ('YD' if self._onlineSource == "YouDao" else 'BY'))

        self.status_Lang.setAlignment(QtCore.Qt.AlignCenter)
        self.status_Dictionary.setAlignment(QtCore.Qt.AlignRight)

        self.statusbar.addPermanentWidget(self.status_Internet, stretch=1)
        self.statusbar.addPermanentWidget(self.status_Lang, stretch=1)
        self.statusbar.addPermanentWidget(self.status_Dictionary, stretch=1)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", self._langMap["TITLE"][self._lIndex]))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.wordListTab), _translate("MainWindow", self._langMap["WORDLIST"][self._lIndex]))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.headListSpanTab), _translate("MainWindow", self._langMap["HEADLIST"][self._lIndex]))
        self.menuFile.setTitle(_translate("MainWindow", self._langMap["FILE"][self._lIndex]))
        self.menuEdit.setTitle(_translate("MainWindow", self._langMap["EDIT"][self._lIndex]))
        self.menuOperation.setTitle(_translate("MainWindow", self._langMap["SETTING"][self._lIndex]))
        self.menuAbout.setTitle(_translate("MainWindow", self._langMap["ABOUT"][self._lIndex]))
        self.actionOpen.setText(_translate("MainWindow", self._langMap["OPEN"][self._lIndex]))
        self.actionOpen.setToolTip(_translate("MainWindow", self._langMap["OPEN_TIP"][self._lIndex]))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", self._langMap["SAVE"][self._lIndex]))
        self.actionSave.setToolTip(_translate("MainWindow", self._langMap["SAVE_TIP"][self._lIndex]))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionUpdate.setText(_translate("MainWindow", self._langMap["UPDATE"][self._lIndex]))
        self.actionUpdate.setToolTip(_translate("MainWindow", self._langMap["UPDATE_TIP"][self._lIndex]))
        self.actionUpdate.setShortcut(_translate("MainWindow", "Ctrl+U"))
        self.actionHelp.setText(_translate("MainWindow", self._langMap["HELP"][self._lIndex]))
        self.actionHelp.setToolTip(_translate("MainWindow", self._langMap["HELP_TIP"][self._lIndex]))
        self.actionHelp.setShortcut(_translate("MainWindow", "Ctrl+H"))
        self.actionExit.setText(_translate("MainWindow", self._langMap["EXIT"][self._lIndex]))
        self.actionExit.setToolTip(_translate("MainWindow", self._langMap["EXIT_TIP"][self._lIndex]))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Alt+F4"))

        self.actionAbout_Application.setShortcut(_translate("MainWindow", "Ctrl+Shift+P"))
        self.actionAdd.setText(_translate("MainWindow", self._langMap["ADD"][self._lIndex]))
        self.actionAdd.setToolTip(_translate("MainWindow", self._langMap["ADD_TIP"][self._lIndex]))
        self.actionAdd.setShortcut(_translate("MainWindow", "Ctrl+Alt+A"))
        self.actionDelete.setText(_translate("MainWindow", self._langMap["DELETE"][self._lIndex]))
        self.actionDelete.setToolTip(_translate("MainWindow", self._langMap["DELETE_TIP"][self._lIndex]))
        self.actionDelete.setShortcut(_translate("MainWindow", "Ctrl+Alt+D"))
        self.actionModify.setText(_translate("MainWindow", self._langMap["MODIFY"][self._lIndex]))
        self.actionModify.setToolTip(_translate("MainWindow", self._langMap["MODIFY_TIP"][self._lIndex]))
        self.actionModify.setShortcut(_translate("MainWindow", "Ctrl+Alt+M"))
        self.actionUndo.setText(_translate("MainWindow", self._langMap["UNDO"][self._lIndex]))
        self.actionUndo.setToolTip(_translate("MainWindow", self._langMap["UNDO_TIP"][self._lIndex]))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Alt+U"))
        self.actionReset.setText(_translate("MainWindow", self._langMap["REST"][self._lIndex]))
        self.actionReset.setToolTip(_translate("MainWindow", self._langMap["REST_TIP"][self._lIndex]))
        self.actionReset.setShortcut(_translate("MainWindow", "Ctrl+Alt+R"))
        self.actionSelect_Dictionary.setText(_translate("MainWindow", self._langMap["SELECT_DICT"][self._lIndex]))
        self.actionSelect_Dictionary.setToolTip(_translate("MainWindow", self._langMap["SELECT_DICT_TIP"][self._lIndex]))
        self.actionSelect_Dictionary.setShortcut(_translate("MainWindow", "Ctrl+Alt+E"))
        self.actionSelect_Languary.setText(_translate("MainWindow", self._langMap["SELECT_LANG"][self._lIndex]))
        self.actionSelect_Languary.setToolTip(_translate("MainWindow", self._langMap["SELECT_LANG_TIP"][self._lIndex]))
        self.actionSelect_Languary.setShortcut(_translate("MainWindow", "Ctrl+Alt+L"))
        self.actionAbout_Programmer.setText(_translate("MainWindow", self._langMap["ABOUT_PROGRAMMER"][self._lIndex]))
        self.actionAbout_Programmer.setToolTip(_translate("MainWindow", self._langMap["ABOUT_PROGRAMMER_TIP"][self._lIndex]))
        self.actionAbout_Programmer.setShortcut(_translate("MainWindow", "Ctrl+Shift+C"))
        self.actionAbout_Application.setText(_translate("MainWindow", self._langMap["ABOUT_PROJECT"][self._lIndex]))
        self.actionAbout_Application.setToolTip(_translate("MainWindow", self._langMap["ABOUT_PROJECT_TIP"][self._lIndex]))


    def CustomTreedItem(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        fnt = QFont('Arial', font_size)
        fnt.setBold(set_bold)

        node = QStandardItem()
        node.setEditable(False)
        node.setForeground(color)
        node.setFont(fnt)
        node.setText(txt)
        node.setCheckable(True)
        return node


    def getLangIndex(self):
        return self._lIndex


    def setLangIndex(self, index):
        if int(index) > 0:
            self._lIndex = int(index)


    def getOnlineSource(self):
        return self._onlineSource


    def setOnlineSource(self, onlineSource):
        if bool(onlineSource and onlineSource.strip()):
            self._onlineSource = onlineSource


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
