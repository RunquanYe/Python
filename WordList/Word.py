import re
import json
import Exception
'''
This is a class for Word and its attributes
Author: Runquan Ye
Date: Sept/2020
'''

class Word():
#constructor
    def __init__(self, name, catergory, meaning, root, derivativeWord, sourceWord, listNum, isHead):
        if bool(self.name and self.name.strip()):
            self.name = name.lower()
        else:
            raise Exception.WordNameEmpty

        if bool(self.catergory and self.catergory.strip()):
            self.catergory = catergory.lower()
        else:
            raise Exception.WordCategoryEmpty

        if bool(self.meaning and self.meaning.strip()):
            self.meaning = meaning
        else:
            raise Exception.WordMeaningEmpty

        if bool(self.root and self.root.strip()):
            self.root = root.lower()
        else:
            self.root = ''

        if bool(self.derivativeWord and self.derivativeWord.strip()):
            self.derivativeWord = derivativeWord.lower()
        else:
            self.derivativeWord = ''

        if bool(self.sourceWord and self.sourceWord.strip()):
            self.sourceWord = sourceWord.lower()
        else:
            self.sourceWord = ''

        if bool(self.listNum and self.listNum.strip()):
            self.listNum = int(listNum)
        else:
            self.listNum = 0

        if bool(self.isHead and self.isHead.strip()):
            self.isHead = json.loads(isHead.lower())
        else:
            self.isHead = False


#getters
    def getWord(self):
        return self.name.lower()

    def getCatergory(self):
        return self.catergory.lower()

    def getCatergoryList(self):
        #'n., Adj. ,vt., v' => ['adj', 'n', 'v', 'vt']
        return sorted(list(filter(None, list(re.split('[,.; ]', self.catergory.lower())))))

    def getCatergoryString(self):
        #'n., Adj. ,vt., v' => 'adj, n, v, vt'
        sortList = self.getCatergoryList()
        return ', '.join([str(e) for e in sortList]).lower()

    def getRoot(self):
        return self.root.lower()

    def getDerivativeWord(self):
        return self.derivativeWord.lower()

    def getSourceWord(self):
        return self.sourceWord.lower()

    def getListNum(self):
        return self.listNum

    def getMeaning(self):
        return self.meaning.lower()

    def getMeaningList(self):
        #adj. 附属的, 辅助的; n. 子公司, 辅助者, 支流' => ['adj. 附属的, 辅助的', ' n. 子公司, 辅助者, 支流']
        temp = re.split('[;]', self.meaning.lower())
        #['adj. 附属的, 辅助的', ' n. 子公司, 辅助者, 支流'] => [['adj', '附属的', '辅助的'], ['n', '子公司', '辅助者', '支流']]
        return sorted([list(filter(None, re.split('[., ]',i))) for i in temp])

    def getMeaningDist(self):
        #temp => [['adj', '附属的', '辅助的'], ['n', '子公司', '辅助者', '支流']]
        temp = self.getMeaningList()
        #temp => {'adj': ['附属的', '辅助的'], 'n': ['子公司', '辅助者', '支流']}
        return {i[0]:i[1:] for i in temp}

    def getMeaningDistCatString(self):
        #temp => ['adj', '附属的', '辅助的'], ['n', '子公司', '辅助者', '支流']]
        temp = self.getMeaningList()
        #temp => {'adj': '附属的, 辅助的', 'n': '子公司, 辅助者, 支流'}
        return {i[0]:', '.join(str(e) for e in i[1:]) for i in temp}

    def getWordMeaningDist(self):
        #{'Subsidiary': 'adj. 附属的, 辅助的; n. 子公司, 辅助者, 支流'}
        return {self.name.lower() : self.meaning.lower()}

    def getWordMeaningDistList(self):
        #{'subsidiary': [['adj', '附属的', '辅助的'], ['n', '子公司', '辅助者', '支流']]}
        return {self.name.lower() : self.getMeaningList()}

    def getWordMeaningDistCatString(self):
        #{'subsidiary': {'adj': '附属的, 辅助的', 'n': '子公司, 辅助者, 支流'}}
        return {self.name.lower() : self.getMeaningDistCatString()}

# setters
    def setCatergory(self, catergory):
        if bool(self.catergory and self.catergory.strip()):
            self.catergory = catergory.lower()

    def setCatergoryInList(self, catergoryList):
        if catergoryList:
            self.catergory = ', '.join(str(i).lower() for i in sorted(catergoryList))

    def setRoot(self, root):
        if bool(self.root and self.root.strip()):
            self.root = root.lower()

    def setDerivativeWord(self, derivativeWord):
        if bool(self.derivativeWord and self.derivativeWord.strip()):
            self.derivativeWord = derivativeWord.lower()

    def setSourceWord(self, sourceWord):
        if bool(self.sourceWord and self.sourceWord.strip()):
            self.sourceWord = sourceWord.lower()

    def setListNum(self, listNum):
        if bool(self.listNum and self.listNum.strip()):
            self.listNum = int(listNum)

    def setIsHead(self, isHead):
        if bool(self.isHead and self.isHead.strip()):
            self.isHead = json.loads(isHead.lower())

    def setMeaning(self, meaning):
        if bool(self.meaning and self.meaning.strip()):
            self.meaning = meaning