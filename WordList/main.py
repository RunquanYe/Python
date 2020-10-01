import sys
from os import path, stat
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTableWidgetItem
from Exception import *
from Word import *
from TranslateMap import *
import WordAppUI
'''
This is a python project for me to store English Academic Word List
-------------------------------------------------------------------
    Author: Runquan Ye
    Date: Sept/2020
-------------------------------------------------------------------
'''


class WordListApplication(WordAppUI.Ui_MainWindow, QtWidgets.QMainWindow):
    appWordList = []
    appWordDict = {}
    appWordHeadList = []
    appWordFilterList = []
    langIndex = 0
    ptIndex = 0
    innerWordListExist = False
    innerWordDataExist = False
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.langIndex = self.lIndex


    def loadInnerData(self):
        if path.exists("WordListData.txt") and stat("WordListData.txt").st_size > 0:
            self.innerWordListExist = True

        if path.exists("WordDictData.txt") and stat("WordDictData.txt").st_size > 0:
            self.innerWordListExist = True

        if not self.appWordList:
            if self.innerWordDataExist:
                self.loadInnerData("WordDictData.txt", "dict")
            else:
                self.loadInnerData("WordListData.txt", "list")


    def updateAllTable(self):
        # self.loadDataWLTable()
        self.loadDataTreeLis()
        # self.loadDataHLTable(self.appWordHeadList, 0)

    def updateHeadListTab(self):
        self.loadDataTreeLis()
        self.loadDataHLTable(self.appWordHeadList, 0)


    # def loadDataWLTable(self):
    #     num = 0
    #     for w in self.appWordList:
    #         self.wordListTable.setItem(num, 0, QTableWidgetItem(str(w.getWord())))
    #         self.wordListTable.setItem(num, 1, QTableWidgetItem(str(self.langMap["USPT_Title"][self.langIndex] if self.ptIndex == 0 else self.langMap["UKPT_Title"][self.langIndex])+ str(" " + w.getUSPT())))
    #         self.wordListTable.setItem(num, 2, QTableWidgetItem(str(DataSourceYD(w.getWord()).getWordPastTerm())))
    #         self.wordListTable.setItem(num, 3, QTableWidgetItem(str(w.getMeaningToString())))
    #         num += 1


    # def loadDataHLTable(self, targetList, method):
    #     if method == 0:
    #         displayList = targetList
    #         num = 0
    #         for w in displayList:
    #             self.headSpanTable.setItem(num, 0, QTableWidgetItem(str(w.getWord())))
    #             self.headSpanTable.setItem(num, 1, QTableWidgetItem(str(self.langMap["USPT_Title"][self.langIndex] + " " + w.getUSPT()) if self.ptIndex == 0 else str(self.langMap["UKPT_Title"][self.langIndex] + " " + w.getUKPT())))
    #             self.headSpanTable.setItem(num, 2, QTableWidgetItem(str(DataSourceYD(w.getWord()).getWordPastTerm())))
    #             self.headSpanTable.setItem(num, 3, QTableWidgetItem(str(w.getMeaningToString())))
    #             num += 1
    #     elif method == 1:
    #         displayList = targetList
    #         num = 0
    #         for wname in displayList:
    #             self.headSpanTable.setItem(num, 0, QTableWidgetItem(str(wname)))
    #             self.headSpanTable.setItem(num, 1, QTableWidgetItem(str(self.langMap["USPT_Title"][self.langIndex]  + " " + self.appWordDict[wname][2]) if self.ptIndex == 0 else str(self.langMap["UKPT_Title"][self.langIndex] + " " + self.appWordDict[wname][3])))
    #             self.headSpanTable.setItem(num, 2, QTableWidgetItem(self.appWordDict[wname][5]))
    #             self.headSpanTable.setItem(num, 3, QTableWidgetItem(self.appWordDict[wname][1]))
    #             num += 1


    def loadDataTreeLis(self):
        for w in self.appWordList:
            if w.getIsHead():
                tempHead = self.StandardItem(w.getWord(), 16, set_bold=True, color=QColor(155, 0, 0))
                # tempHead.mousePressEvent(self, self.loadDataHLTable(list(str(w.getWord() + ", " + w.getDerivativeWordString()).split(', ')), 1))
                self.rootNode.appendRow(tempHead)
            else:
                tempNode = self.StandardItem(w.getWord(), 14)
                tempHead.appendRow(tempNode)


    def loadInnerData(self, inputFile, method):
        # open file in the read mode
        infile = open(inputFile, "r")

        if stat(inputFile).st_size > 0:
            # read the file content lines by lines
            lines = infile.readlines()

            try:
                wordnum = 1
                for l in lines:
                    word = None
                    re.sub(r"^\s+|\s+$", "", str(l))
                    if "list" in str(method).lower():
                        rawData = l.split(' ')
                        listNum = rawData[0]
                        wordlist = rawData[1:]
                        for vocably in wordlist:
                            print(wordnum, ": ",vocably)
                            word = Word(str(vocably).rstrip(), '', '', '', '', '', '', wordlist[1:] if wordlist.index(vocably) == 0 else '', wordlist[0] if wordlist.index(vocably) != 0 else '', wordnum, listNum, True if wordlist.index(vocably) == 0 else False)
                            self.appWordList.append(word)
                            self.appWordDict.update({word.getWord(): word.getWordDictData()})
                            if wordlist.index(vocably) == 0:
                                self.appWordHeadList.append(word)
                            wordnum += 1
                    elif "dict" in str(method).lower():
                        # re.sub(r"^\s+|\s+$", "", s) ==> remove leading and trailing spaces and ending newline mark
                        data = list(re.sub(r"^\s+|\s+$", "", str(i)) for i in l.split('|'))
                        word = Word(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11])
                        self.appWordList.append(word)
                        self.appWordDict.update({word.getWord():word.getWordDictData()})
                        if data[10]:
                            self.appWordHeadList.append(word)
                # print([i.getWord() for i in self.appWordList])
                # print(self.appWordDict)
                self.updateAllTable()
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
    app.loadInnerData("WordListData.txt", "list")
    sys.exit(application.exec_())


# Start method trigger.
if __name__ == '__main__':
    main()
