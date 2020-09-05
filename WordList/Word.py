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
        if(bool(self.name and self.name.strip())):
            self.name = name.lower()
        else:
            raise Exception.WordNameEmpty

        if (bool(self.catergory and self.catergory.strip())):
            self.catergory = catergory.lower()
        else:
            raise Exception.WordCategoryEmpty

        if (bool(self.meaning and self.meaning.strip())):
            self.meaning = meaning
        else:
            raise Exception.WordMeaningEmpty

        if (bool(self.root and self.root.strip())):
            self.root = root.lower()
        else:
            self.root = ''

        if (bool(self.derivativeWord and self.derivativeWord.strip())):
            self.derivativeWord = derivativeWord.lower()
        else:
            self.derivativeWord = ''

        if (bool(self.sourceWord and self.sourceWord.strip())):
            self.sourceWord = sourceWord.lower()
        else:
            self.sourceWord = ''

        if (bool(self.listNum and self.listNum.strip())):
            self.listNum = int(listNum)
        else:
            self.listNum = 0

        if (bool(self.isHead and self.isHead.strip())):
            self.isHead = json.loads(isHead.lower())
        else:
            self.isHead = False


#getters
    def getWord(self):
        return self.name

    def getCatergory(self):
        return self.catergory

    def getCatergoryList(self):
        return list(filter(None, list(re.split('[,.; ]', self.catergory))))

    def getCatergoryString(self):
        sortList = list(filter(None, list(re.split('[,.; ]', self.catergory)))).sort()
        return ', '.join([str(e) for e in sortList])

    def getRoot(self):
        return self.root

    def getDerivativeWord(self):
        return self.derivativeWord

    def getSourceWord(self):
        return self.sourceWord

    def getListNum(self):
        return self.listNum

    def getMeaningString(self):
        return self.meaning


# setters
    def setCatergory(self, catergory):
        if (bool(self.catergory and self.catergory.strip())):
            self.catergory = catergory.lower()

    def setRoot(self, root):
        if (bool(self.root and self.root.strip())):
            self.root = root.lower()

    def setDerivativeWord(self, derivativeWord):
        if (bool(self.derivativeWord and self.derivativeWord.strip())):
            self.derivativeWord = derivativeWord.lower()

    def setSourceWord(self, sourceWord):
        if (bool(self.sourceWord and self.sourceWord.strip())):
            self.sourceWord = sourceWord.lower()

    def setListNum(self, listNum):
        if (bool(self.listNum and self.listNum.strip())):
            self.listNum = int(listNum)

    def setIsHead(self, isHead):
        if (bool(self.isHead and self.isHead.strip())):
            self.isHead = json.loads(isHead.lower())

    def setMeaning(self, meaning):
        if (bool(self.meaning and self.meaning.strip())):
            self.meaning = meaning


