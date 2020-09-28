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
from os import path, stat
'''
This is a python project for me to store English Academic Word List
-------------------------------------------------------------------
    Author: Runquan Ye
    Date: Sept/2020
-------------------------------------------------------------------
'''


class WordListApplication(WordAppUI.Ui_MainWindow, QtWidgets.QMainWindow):
    appWordlist = []
    appWordDict = {}
    wordnum = 0
    innerWordListExist = False
    innerWordDataExist = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()


    def loadData(self):
        if path.exists("WordListData.txt") and stat("WordListData.txt").st_size > 0:
            self.innerWordListExist = True

        if path.exists("WordDistData.txt") and stat("WordDistData.txt").st_size > 0:
            self.innerWordListExist = True

        if not self.appWordlist:
            if self.innerWordDataExist:
                self.loadFile("WordDistData.txt", "dict")
            if self.innerWordListExist:
                self.loadFile("WordListData.txt", "list")



    def loadFile(self, inputFile, method):
        # open file in the read mode
        infile = open(inputFile, "r")

        if stat(inputFile).st_size > 0:
            # read the file content lines by lines
            lines = infile.readlines()

            try:
                for l in lines:
                    if "list" in str(method).lower():
                        rawData = l.split(' ')
                        listNum = rawData[0]
                        wordlist = rawData[1:]
                        for vocably in wordlist:
                            self.wordnum += 1
                            a = Word(vocably, '', '', '', wordlist[1:] if wordlist.index(vocably) == 0 else '', wordlist[0] if wordlist.index(vocably) != 0 else '', self.wordnum, listNum, True if wordlist.index(vocably) == 0 else False)
                            print(a.getWordDataToString())
                    elif "dict" in str(method).lower():
                        rawData = l.split('|')

                        word = Word(vocably, '', '', '', wordlist[1:] if wordlist.index(vocably) == 0 else '',
                                    wordlist[0] if wordlist.index(vocably) != 1 else '', self.wordnum, listNum,
                                    True if wordlist.index(vocably) == 0 else False)
                        print(word.getWordToString())


            except OSError as err:
                print("OS error: {0}".format(err))
                pass
            except WordNameEmptyException:
                print("Error! Empty word name!")
                pass
        else:
            raise EmptyFileException

        # close files
        infile.close()


    def saveFile(self, outputFile):
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
        except WordNameEmptyException:
            print("Error! Empty word name!")
            pass

        # close files
        outfile.close()


def main():
    application = QApplication(sys.argv)
    app = WordListApplication()
    app.loadFile("WordListData.txt", "list")
    app.saveFile("outputFile.txt")
    sys.exit(application.exec_())


# Start method trigger.
if __name__ == '__main__':
    main()
