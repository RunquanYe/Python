import re
import json
import Exception
from DataSourceBY import *
from DataSourceYD import *
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
    _name, _catergory, _meaning, _us_pt, _uk_pt, _root, _passTerm, _derivativeWord, _sourceWord, _wordNum, _listNum, _isHead = '', '', '', '', '', '', '', '', '', 0, 0, False
    _onlineSource = None

    def __init__(self, _name, _catergory="", _meaning="", _us_pt="", _uk_pt="", _root="", _passTerm="", _derivativeWord="", _sourceWord="", _wordNum=0, _listNum=1, _isHead=False):

        if bool(_name and _name.strip()):
            self._name = _name.lower()
            self._onlineSource = DataSourceBY(self._name)
        else:
            raise Exception.WordNameEmpty

        if bool(_meaning and _meaning.strip()):
            self._meaning = _meaning
        else:
            self._meaning = self._onlineSource.getWordMeaning()

        if bool(_catergory and _catergory.strip()):
            self._catergory = _catergory.lower()
        else:
            if bool(self._meaning and self._meaning.strip()):
                self._catergory = ', '.join(str(e) for e in [i[0] for i in self.getMeaningList()]).lower()
            else:
                self._catergory = self._onlineSource.getWordCategory()

        if bool(_us_pt and _us_pt.strip()):
            self._us_pt = _us_pt
        else:
            self._us_pt = self._onlineSource.getWordDataUSPT()

        if bool(_uk_pt and _uk_pt.strip()):
            self._uk_pt = _uk_pt
        else:
            self._uk_pt = self._onlineSource.getWordDataUKPT()

        if bool(_root and _root.strip()):
            self._root = _root.lower()

        if bool(_passTerm and _passTerm.strip()):
            self._passTerm = _passTerm
        else:
            self._passTerm = DataSourceYD(self._name).getWordPastTerm()

        if type(_derivativeWord) is list:
            if _derivativeWord != None:
                self._derivativeWord = ', '.join(str(e) for e in _derivativeWord).lower()
        if type(_derivativeWord) is str:
            if bool(_derivativeWord and _derivativeWord.strip()):
                self._derivativeWord = _derivativeWord.lower()

        if bool(_sourceWord and _sourceWord.strip()):
            self._sourceWord = _sourceWord.lower()

        if int(_wordNum) > 0:
            self._wordNum = int(_wordNum)

        if int(_listNum) > 0:
            self._listNum = int(_listNum)

        if type(_isHead) == bool:
            self._isHead = _isHead
        elif bool(_isHead and _isHead.strip()):
            self._isHead = json.loads(_isHead.lower())


# methods
    def soureModeSwitchUpdate(self):
        self.setMeaning(self._onlineSource.getWordMeaning())
        self.setCatergoryInList(self.getMeaningList())
        self.setUKPT(self._onlineSource.getWordDataUKPT())
        self.setUSPT(self._onlineSource.getWordDataUSPT())


#getters
    def getWord(self):
        return self._name.lower()

    def getCatergory(self):
        return self._catergory.lower()

    def getCatergoryList(self):
        #'n., Adj. ,vt., v' => ['adj', 'n', 'v', 'vt']
        return sorted(list(filter(None, list(re.split('[,.;，； ]', self._catergory.lower())))))

    def getCatergoryString(self):
        #'n., Adj. ,vt., v' => 'adj, n, v, vt'
        sortList = self.getCatergoryList()
        return ', '.join([str(e) for e in sortList]).lower()

    def getOnlineSourceMode(self):
        return self._onlineSource.getModeName()

    def getUSPT(self):
        if not bool(self._us_pt and self._us_pt.strip()):
            self._us_pt = self._onlineSource.getWordDataUSPT()
        return self._us_pt

    def getUKPT(self):
        if not bool(self._uk_pt and self._uk_pt.strip()):
            self._uk_pt = self._onlineSource.getWordDataUKPT()
        return self._uk_pt

    def getRoot(self):
        return self._root.lower()

    def getDerivativeWordString(self):
        return self._derivativeWord.lower()

    def getDerivativeWordList(self):
        return sorted(list(filter(None, list(re.split('[,.;，； ]', self.getDerivativeWordString())))))

    def getSourceWord(self):
        return self._sourceWord.lower()

    def getSourceWordString(self):
        return self._sourceWord.lower()

    def getWordNum(self):
        return self._wordNum

    def getListNum(self):
        return self._listNum

    def getMeaning(self):
        return self._meaning.lower()

    def getIsHead(self):
        return self._isHead

    def getPassTerm(self):
        if not bool(self._passTerm and self._passTerm.strip()):
            self._passTerm = DataSourceYD(self._name).getWordPastTerm()
        return self._passTerm

    def getMeaningToString(self):
        return str('; '.join(str(e) for e in re.split('[;；]', self.getMeaning())))

    def getMeaningList(self):
        #adj. 附属的, 辅助的; n. 子公司, 辅助者, 支流' => ['adj. 附属的, 辅助的', ' n. 子公司, 辅助者, 支流']
        temp = re.split('[;；]', self._meaning.lower())
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
        return {self._name.lower() : self._meaning.lower()}

    def getWordMeaningDistList(self):
        #{'subsidiary': [['adj', '附属的', '辅助的'], ['n', '子公司', '辅助者', '支流']]}
        return {self._name.lower() : self.getMeaningList()}

    def getWordMeaningDistCatString(self):
        #{'subsidiary': {'adj': '附属的, 辅助的', 'n': '子公司, 辅助者, 支流'}}
        return {self._name.lower() : self.getMeaningDistCatString()}

    # def getWordToString(self, sperator='|'):
    #     return f"{self._wordNum}{sperator}{self._name}{sperator}{self.getUSPTwTitle()}{sperator}{self.getMeaning()}{sperator}{self._derivativeWord}{sperator}{self._sourceWord}{sperator}{self._listNum}"

    def getWordDataToString(self, sperator=' | '):
            return f"{self._name}{sperator}{self._catergory}{sperator}{self._meaning}{sperator}{self._us_pt}{sperator}{self._uk_pt}{sperator}{self._root}{sperator}{self._passTerm}{sperator}{self._derivativeWord}{sperator}{self._sourceWord}{sperator}{str(self._wordNum)}{sperator}{str(self._listNum)}{sperator}{str(self._isHead)}"

    def getWordDocToString(self, sep='|'):
        return '{0:{gap}^5}{sep}{1:{gap}<13}{sep}{2:{gap}<21}{sep}{3:{gap}<50}{sep}{4:{gap}^5}\n'.format(self.getWordNum(), self.getWord(), self.getUSPTwTitle(), self.getMeaningToString(), self.getListNum(), gap=' ', sep=sep)

    def getWordDictData(self):
        return [self._catergory, self._meaning, self._us_pt, self._uk_pt, self._root, self._passTerm, self._derivativeWord, self._sourceWord, str(self._wordNum), str(self._listNum), str(self._isHead)]


# setters
    def setCatergory(self, _catergory):
        if bool(_catergory and _catergory.strip()):
            self._catergory = _catergory.lower()

    def setCatergoryInList(self, catergoryList):
        if catergoryList:
            self._catergory = ', '.join(str(i).lower() for i in sorted(catergoryList))

    def setOnlineSourceMode(self, modeString):
        if modeString.strip().lower() == "yd" or "youdao" in modeString.strip().lower():
            self._onlineSource = DataSourceYD(self._name)
        else:
            self._onlineSource = DataSourceBY(self._name)

    def setUSPT(self, _us_pt):
        if bool(_us_pt and _us_pt.strip()):
            self._us_pt = _us_pt

    def setUKPT(self, _uk_pt):
        if bool(_uk_pt and _uk_pt.strip()):
            self._uk_pt = _uk_pt

    def setRoot(self, _root):
        if bool(_root and _root.strip()):
            self._root = _root.lower()

    def setDerivativeWord(self, _derivativeWord):
        if bool(_derivativeWord and _derivativeWord.strip()):
            self._derivativeWord = _derivativeWord.lower()

    def setSourceWord(self, _sourceWord):
        if bool(_sourceWord and _sourceWord.strip()):
            self._sourceWord = _sourceWord.lower()

    def setListNum(self, _wordNum):
        if int(_wordNum) > 0:
            self._wordNum = int(_wordNum)

    def setListNum(self, _listNum):
        if int(_listNum) > 0:
            self._wordNum = int(_listNum)

    def setIsHead(self, _isHead):
        if bool(_isHead and _isHead.strip()):
            self._isHead = json.loads(_isHead.lower())

    def setMeaning(self, _meaning):
        if bool(_meaning and _meaning.strip()):
            self._meaning = _meaning

    def setPassTerm(self, _passTerm):
        if bool(_passTerm and _passTerm.strip()):
            self._passTerm = _passTerm