import re
import json
import Exception
from DataSource import *
'''
This is a class for Word and its attributes
-------------------------------------------
    Author: Runquan Ye
    Date: Sept/2020
------------------------------------------- 
'''

class Word():
#constructor
    #词名，词类，词意，美音标，英音标，词根，派生词，源生词，词号，词表号，是否源生词
    name, catergory, meaning, us_pt, uk_pt, root, derivativeWord, sourceWord, wordNum, listNum, isHead = '', '', '', '', '', '', '', '', 0, 0, False
    onlineSource = None

    def __init__(self, name, catergory, meaning, root, derivativeWord, sourceWord, wordNum, listNum, isHead):

        if bool(name and name.strip()):
            self.name = name.lower()
            self.onlineSource = DataSource(self.name)
        else:
            raise Exception.WordNameEmpty

        if bool(meaning and meaning.strip()):
            self.meaning = meaning
        else:
            self.meaning = DataSource(self.name).getWordMeaning()

        if bool(catergory and catergory.strip()):
            self.catergory = catergory.lower()
        else:
            if bool(self.meaning and self.meaning.strip()):
                self.catergory = ', '.join(str(e) for e in [i[0] for i in self.getMeaningList()]).lower()
            else:
                self.catergory = self.onlineSource.getWordCategory()

        if bool(root and root.strip()):
            self.root = root.lower()


        if type(derivativeWord) == 'list':
            if derivativeWord != None:
                self.derivativeWord = ', '.join(str(e) for e in derivativeWord).lower()
        if type(derivativeWord) == 'str':
            if bool(derivativeWord and derivativeWord.strip()):
                self.derivativeWord = derivativeWord.lower()

        if bool(sourceWord and sourceWord.strip()):
            self.sourceWord = sourceWord.lower()

        if int(wordNum) > 0:
            self.wordNum = int(wordNum)

        if int(listNum) > 0:
            self.listNum = int(listNum)

        if type(isHead) == bool:
            self.isHead = isHead
        elif bool(isHead and isHead.strip()):
            self.isHead = json.loads(isHead.lower())


#getters
    def getWord(self):
        return self.name.lower()

    def getCatergory(self):
        return self.catergory.lower()

    def getCatergoryList(self):
        #'n., Adj. ,vt., v' => ['adj', 'n', 'v', 'vt']
        return sorted(list(filter(None, list(re.split('[,.;，； ]', self.catergory.lower())))))

    def getCatergoryString(self):
        #'n., Adj. ,vt., v' => 'adj, n, v, vt'
        sortList = self.getCatergoryList()
        return ', '.join([str(e) for e in sortList]).lower()

    def getUSPT(self):
        if not bool(self.us_pt and self.us_pt.strip()):
            self.us_pt = self.onlineSource.getWordDataUSPT()
        return self.us_pt

    def getUKPT(self):
        if not bool(self.uk_pt and self.uk_pt.strip()):
            self.uk_pt = self.onlineSource.getWordDataUKPT()
        return self.uk_pt

    def getUSPTwTitle(self):
        if not bool(self.us_pt and self.us_pt.strip()):
            self.us_pt = self.onlineSource.getWordDataUSPT()
        return  '美' + self.us_pt if bool(self.us_pt and self.us_pt.strip()) else ''

    def getUSPTwETitle(self):
        if not bool(self.us_pt and self.us_pt.strip()):
            self.us_pt = self.onlineSource.getWordDataUSPT()
        return 'US ' + self.us_pt if bool(self.us_pt and self.us_pt.strip()) else ''

    def getUKPTwTitle(self):
        if not bool(self.uk_pt and self.uk_pt.strip()):
            self.uk_pt = self.onlineSource.getWordDataUKPT()
        return '英' + self.uk_pt if bool(self.uk_pt and self.uk_pt.strip()) else ''

    def getUKPTwETitle(self):
        if not bool(self.uk_pt and self.uk_pt.strip()):
            self.uk_pt = self.onlineSource.getWordDataUKPT()
        return 'UK ' + self.uk_pt if bool(self.uk_pt and self.uk_pt.strip()) else ''

    def getRoot(self):
        return self.root.lower()

    def getDerivativeWord(self):
        return self.derivativeWord.lower()

    def getSourceWord(self):
        return self.sourceWord.lower()

    def getSourceWordString(self):
        return self.sourceWord.lower()

    def getWordNum(self):
        return self.wordNum

    def getListNum(self):
        return self.listNum

    def getMeaning(self):
        return self.meaning.lower()

    def getMeaningList(self):
        #adj. 附属的, 辅助的; n. 子公司, 辅助者, 支流' => ['adj. 附属的, 辅助的', ' n. 子公司, 辅助者, 支流']
        temp = re.split('[;；]', self.meaning.lower())
        #['adj. 附属的, 辅助的', ' n. 子公司, 辅助者, 支流'] => [['adj', '附属的', '辅助的'], ['n', '子公司', '辅助者', '支流']]
        return sorted([list(filter(None, re.split('[.,， ]',i))) for i in temp])

    def getMeaningDist(self):
        #[['adj', '附属的', '辅助的'], ['n', '子公司', '辅助者', '支流']] => {'adj': ['附属的', '辅助的'], 'n': ['子公司', '辅助者', '支流']}
        return {i[0]:i[1:] for i in self.getMeaningList()}

    def getMeaningDistCatString(self):
        #[['adj', '附属的', '辅助的'], ['n', '子公司', '辅助者', '支流']] => {'adj': '附属的, 辅助的', 'n': '子公司, 辅助者, 支流'}
        return {i[0]:', '.join(str(e) for e in i[1:]) for i in self.getMeaningList()}

    def getWordMeaningDist(self):
        #{'Subsidiary': 'adj. 附属的, 辅助的; n. 子公司, 辅助者, 支流'}
        return {self.name.lower() : self.meaning.lower()}

    def getWordMeaningDistList(self):
        #{'subsidiary': [['adj', '附属的', '辅助的'], ['n', '子公司', '辅助者', '支流']]}
        return {self.name.lower() : self.getMeaningList()}

    def getWordMeaningDistCatString(self):
        #{'subsidiary': {'adj': '附属的, 辅助的', 'n': '子公司, 辅助者, 支流'}}
        return {self.name.lower() : self.getMeaningDistCatString()}

    # def getWordToString(self, sperator=' '):
    #     return f"{self.wordNum}{sperator}{self.name}{sperator}{self.getUSPTwTitle()}{sperator}{self.getMeaning()}{sperator}{self.derivativeWord}{sperator}{self.sourceWord}{sperator}{self.listNum}"

    def getWordToString(self, sperator=' '):
        return (''.format(self.wordNum, self.name, self.getUSPTwTitle(), self.getMeaning(), self.derivativeWord, self.sourceWord, self.listNum))

# setters
    def setCatergory(self, catergory):
        if bool(catergory and catergory.strip()):
            self.catergory = catergory.lower()

    def setCatergoryInList(self, catergoryList):
        if catergoryList:
            self.catergory = ', '.join(str(i).lower() for i in sorted(catergoryList))

    def setUSPT(self, us_pt):
        if bool(us_pt and us_pt.strip()):
            self.us_pt = us_pt

    def setUKPT(self, uk_pt):
        if bool(uk_pt and uk_pt.strip()):
            self.uk_pt = uk_pt

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