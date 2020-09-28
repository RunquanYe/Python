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


def loadFile(inputFile):
    # open file in the read mode
    wordnum = 0
    infile = open(inputFile, "r")

    # read the file content lines by lines
    lines = infile.readlines()

    try:
        for l in lines:
            wordlist = l.split(' ')
            for vocably in wordlist:
                wordnum += 1
                word = Word(vocably, '', '', '', wordlist[1:] if wordlist.index(vocably) == 0 else '', wordlist[0] if wordlist.index(vocably) != 1 else '', wordnum, 1, True if wordlist.index(vocably) == 0 else False)
                print(word.getWordToString())

    except OSError as err:
        print("OS error: {0}".format(err))
        pass
    except WordNameEmpty:
        print("Error! Empty word name!")
        pass

    # close files
    infile.close()


def saveFile(outputFile):
    # create file in the write mode
    outfile = open(outputFile, "w+")

    title = 'Academic Words List Application'
    programmer = 'Programmer: Runquan Ye        Date: September 2020        GitHub: https://github.com/RunquanYe'
    header = '\n{0:{gap}^4}{sep}{1:{gap}^12}{sep}{2:{gap}^20}{sep}{3:{gap}^80}\n'.format('编号', '单词', '音标', '词意', gap='-', sep='|')
    outfile.writelines(f"{title.title()}".center(len(header) + 8, " "))
    outfile.writelines('\n')
    outfile.writelines(f"{programmer.title()}".center(len(header) + 8, " "))
    outfile.writelines(f"{'=' * (len(header) + 8)}")
    outfile.writelines(header)

    try:
        pass

    except OSError as err:
        print("OS error: {0}".format(err))
        pass
    except WordNameEmpty:
        print("Error! Empty word name!")
        pass

    # close files
    outfile.close()


def main():
    loadFile("inputFile.txt")
    saveFile("outputFile.txt")
    # application = QApplication(sys.argv)
    # app = WordListApplication()
    # sys.exit(application.exec_())


# Start method trigger.
if __name__ == '__main__':
    main()
