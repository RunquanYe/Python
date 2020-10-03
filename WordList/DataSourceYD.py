from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
'''
This is a class for finding online data from YouDao Dictionary for the missing data
-----------------------------------------------------------------------------------
    Author: Runquan Ye
    Date: Sept/2020
-----------------------------------------------------------------------------------
'''

class DataSourceYD():
    # constructor
    # 词名，词类，词意，美音标，英音标, 词类list，词意list
    _dName, _dCatergory, _dMeaning, _dUS_pt, _dUK_pt, _dCatergoryList, _dMeaningList = '', '', '', '', '', [], []
    # 过去式，过去分词，现在分词，复数，第三人称单数
    _pastTerm, _pastParticipleTerm, _presentParticipleTerm, _pluralTerm, _singularTerm = '', '', '', '', ''

    _modeName = "YouDao"

    def __init__(self, word):
        if bool(word and word.strip()):
            self._dName = word.lower()

        #get word's data from the web
            webpage = urlopen('http://dict.youdao.com/w/eng/' + self._dName + '/#keyfrom=dict2.index').read()

        #transfer opening url to html document
            soup = BeautifulSoup(webpage, 'html.parser')
            target = soup.find_all("div", class_="trans-container", limit=1)[0]

            if all(e == "trans-container" for e in target["class"]) and target.contents[1].name == "ul":
                for i in target.ul.find_all('li'):
                    self._dMeaningList.append(i.string.lower())
                    sorted(self._dMeaningList)
                subList = target.ul.find_next_sibling('p')
                if subList:
                    termList = list(filter(None, subList.string.split(' ')))[1: -1]
                    termList = [str(i).rstrip() for i in termList]
                    if '过去式' in termList:
                        self._pastTerm = termList[termList.index('过去式') + 1].lower()
                    if '过去分词' in termList:
                        self._pastParticipleTerm = termList[termList.index('过去分词') + 1].lower()
                    if '现在分词' in termList:
                        self._presentParticipleTerm = termList[termList.index('现在分词') + 1].lower()
                    if '复数' in termList:
                        self._pluralTerm = termList[termList.index('复数') + 1].lower()
                    if '第三人称单数' in termList:
                        self._singularTerm = termList[termList.index('第三人称单数') + 1].lower()

            if len(self._dMeaningList):
                self._dMeaning = ' || '.join(str(e) for e in self._dMeaningList)
            self._dCatergoryList = list(dict.fromkeys([i[0] for i in sorted([list(filter(None, re.split('[.,，;； ]', i))) for i in self._dMeaningList])]))
            self._dCatergory = ', '.join(str(i) for i in self._dCatergoryList)

            ptList = target.find_previous_sibling().find_all("span", class_="pronounce", limit=2)

            for pt in ptList:
                if pt.contents[0].rstrip() == "英":
                    self._dUK_pt = pt.contents[1].string
                else:
                    self._dUS_pt = pt.contents[1].string


    def getWordName(self):
        return self._dName.lower()

    def getWordPresentParticipleTerm(self):
        return self._presentParticipleTerm.lower()

    def getWordDataUSPT(self):
        return self._dUS_pt

    def getWordDataUKPT(self):
        return self._dUK_pt

    def getWordMeaning(self):
        return self._dMeaning.lower()

    def getWordCategory(self):
        return self._dCatergory.lower()

    def getWordCategoryList(self):
        return self._dCatergoryList

    def getWordMeaningList(self):
        return self._dMeaningList
        
    def getWordPastTerm(self):
        return self._pastTerm.lower()
        
    def getWordPastParticipleTerm(self):
        return self._pastParticipleTerm.lower()

    def getWordPresentParticipleTerm(self):
        return self._presentParticipleTerm.lower()
        
    def getWordPluralTerm(self):
        return self._pluralTerm.lower()
    
    def getWordSingularTerm(self):
        return self._singularTerm.lower()

    def getModeName(self):
        return self._modeName

    # YD online word audio:
    # UK: http://dict.youdao.com/dictvoice?audio=job&type=1
    # US: http://dict.youdao.com/dictvoice?audio=job&type=2