from Exception import *
from Word import *
from DataSourceBY import *
from DataSourceYD import *
from urllib.request import urlopen
from bs4 import BeautifulSoup
from TranslateMap import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
import WordAppUI
import sys
'''
This is a python project for me to store English Academic Word List
-------------------------------------------------------------------
    Author: Runquan Ye
    Date: Sept/2020
-------------------------------------------------------------------
'''


class WordListApplication(WordAppUI.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


def main():
    application = QApplication(sys.argv)
    app = WordListApplication()
    sys.exit(application.exec_())


# Start method trigger.
if __name__ == '__main__':
    main()
