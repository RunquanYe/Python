import re
'''
This is a class for Word and its attributes
Author: Runquan Ye
Date: Sept/2020
'''

class Word():
#constructor
    def __init__(self, name, catergory, meaning, root, derivativeWord, sourceWord, listNum):
        if(bool(self.name and self.name.strip())):
            self.name = name
        else:
            pass

        if (bool(self.catergory and self.catergory.strip())):
            self.catergory = catergory
        else:
            pass

        if (bool(self.meaning and self.meaning.strip())):
            self.meaning = meaning
        else:
            pass

        if (bool(self.root and self.root.strip())):
            self.root = root
        else:
            self.root = ''

        if (bool(self.derivativeWord and self.derivativeWord.strip())):
            self.derivativeWord = derivativeWord
        else:
            self.derivativeWord = ''

        if (bool(self.sourceWord and self.sourceWord.strip())):
            self.sourceWord = sourceWord
        else:
            self.sourceWord = ''

        if (bool(self.listNum and self.listNum.strip())):
            self.listNum = int(listNum)
        else:
            self.listNum = 0


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
            self.catergory = catergory
        else:
            pass

    def setRoot(self, root):
        if (bool(self.root and self.root.strip())):
            self.root = root
        else:
            self.root = ''

    def setDerivativeWord(self, derivativeWord):
        if (bool(self.derivativeWord and self.derivativeWord.strip())):
            self.derivativeWord = derivativeWord
        else:
            self.derivativeWord = ''

    def setSourceWord(self, sourceWord):
        if (bool(self.sourceWord and self.sourceWord.strip())):
            self.sourceWord = sourceWord
        else:
            self.sourceWord = ''

    def setListNum(self, listNum):
        if (bool(self.listNum and self.listNum.strip())):
            self.listNum = int(listNum)
        else:
            self.listNum = 0

    def setMeaning(self, meaning):
        if (bool(self.meaning and self.meaning.strip())):
            self.meaning = meaning
        else:
            pass


