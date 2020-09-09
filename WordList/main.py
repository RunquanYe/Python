from Exception import *
from Word import *
from DataSource import *

from urllib.request import urlopen
from bs4 import BeautifulSoup
'''
This is a python project for me to store English Academic Word List
Author: Runquan Ye
Date: Sept/2020
'''

def main():
    '''
     b = DataSource("boxy")
     print("name: ", b.getWordName())
     print("category string: ", b.getWordCategory())
     print("category list: ", b.getWordCategoryList())
     print("meaning string: ", b.getWordMeaning())
     print("meaning list: ", b.getWordMeaningList())
     print("USPT: ", b.getWordDataUSPT())
     print("UKPT: ", b.getWordDataUKPT())
     '''
    try:
        a = Word('Subsidiary','n. adj', 'adj. 附属的, 辅助的; n. 子公司, 辅助者, 支流', '', '','', 0, 1, False)
        print("name: ", a.getWord())
        print("category: ", a.getCatergory())
        print("category list: ", a.getCatergoryList())
        print("category string: ", a.getCatergoryString())
        print("USPT: ", a.getUSPT(), "; ", a.getUSPTwTitle(), "; ", a.getUSPTwETitle())
        print("UKPT: ", a.getUKPT(), "; ", a.getUKPTwTitle(), "; ", a.getUKPTwETitle())
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
        
    except OSError as err:
        print("OS error: {0}".format(err))
        pass
    except WordNameEmpty:
        print("Error! Empty word name!")
        pass
'''   
    except WordCategoryEmpty:
        print("Error! Empty word category!")
        pass
    except WordMeaningEmpty:
        print("Error! Empty word meaning!")
        pass
'''

# Start method trigger.
if __name__ == '__main__':
    main()
