import Exception
from Word import Word
'''
This is a python project for me to store English Academic Word List
Author: Runquan Ye
Date: Sept/2020
'''

def main():
    a = Word('Subsidiary','adj, N', 'adj. 附属的, 辅助的; n. 子公司, 辅助者, 支流', '', '','', 0, 1, False)
    print("name: ", a.getWord())
    print("category: ", a.getCatergory())
    print("category list: ", a.getCatergoryList())
    print("category string: ", a.getCatergoryString())
    print("root: ", a.getRoot())
    print("derivative: ", a.getDerivativeWord())
    print("source: ", a.getSourceWord())
    print("word num: ", a.getWordNum())
    print("list num: ", a.getListNum())
    print("meaning: ", a.getMeaning())
    print("meaning list: ", a.getMeaningList())
    print("meaning dist: ", a.getMeaningDist())
    print("meaning catstring: ", a.getMeaningDistCatString())
    print("word meaning dist: ", a.getWordMeaningDist())
    print("word list dist: ", a.getWordMeaningDistList())
    print("word catstring dist: ", a.getWordMeaningDistCatString())


# Start method trigger.
if __name__ == '__main__':
    main()
