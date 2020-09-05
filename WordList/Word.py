'''
This is a class for Word and its attributes
Author: Runquan Ye
Date: Sept/2020
'''

class Word():
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


    def getWord(self):
        return self.name

    def getCatergoryString(self):
        return self.catergory


