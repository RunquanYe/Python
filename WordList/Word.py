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
    name, catergory, meaning, root, derivativeWord, sourceWord, wordNum, listNum, isHead = '', '', '', '', '', '', 0, 0, False
    def __init__(self, name, catergory, meaning, root, derivativeWord, sourceWord, wordNum, listNum, isHead):
        if bool(name and name.strip()):
            self.name = name.lower()
        else:
            raise Exception.WordNameEmpty

        if bool(catergory and catergory.strip()):
            self.catergory = catergory.lower()
        else:
            raise Exception.WordCategoryEmpty

        if bool(meaning and meaning.strip()):
            self.meaning = meaning
        else:
            raise Exception.WordMeaningEmpty

        if bool(root and root.strip()):
            self.root = root.lower()

        if bool(derivativeWord and derivativeWord.strip()):
            self.derivativeWord = derivativeWord.lower()

        if bool(sourceWord and sourceWord.strip()):
            self.sourceWord = sourceWord.lower()

        if int(wordNum) > 0:
            self.wordNum = int(wordNum)

        if int(listNum) > 0:
            self.listNum = int(listNum)

        if bool(isHead and isHead.strip()):
            self.isHead = json.loads(isHead.lower())


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

    def getWordNum(self):
        return self.wordNum

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
        if bool(catergory and catergory.strip()):
            self.catergory = catergory.lower()

    def setCatergoryInList(self, catergoryList):
        if catergoryList:
            self.catergory = ', '.join(str(i).lower() for i in sorted(catergoryList))

    def setRoot(self, root):
        if bool(root and root.strip()):
            self.root = root.lower()

    def setDerivativeWord(self, derivativeWord):
        if bool(derivativeWord and derivativeWord.strip()):
            self.derivativeWord = derivativeWord.lower()

    def setSourceWord(self, sourceWord):
        if bool(sourceWord and sourceWord.strip()):
            self.sourceWord = sourceWord.lower()

    def setListNum(self, wordNum):
        if int(wordNum) > 0:
            self.wordNum = int(wordNum)

    def setListNum(self, listNum):
        if int(listNum) > 0:
            self.wordNum = int(listNum)

    def setIsHead(self, isHead):
        if bool(isHead and isHead.strip()):
            self.isHead = json.loads(isHead.lower())

    def setMeaning(self, meaning):
        if bool(meaning and meaning.strip()):
            self.meaning = meaning