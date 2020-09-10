from Exception import *
from Word import *
from DataSource import *

from urllib.request import urlopen
from bs4 import BeautifulSoup
'''
This is a python project for me to store English Academic Word List
-------------------------------------------------------------------
    Author: Runquan Ye
    Date: Sept/2020
-------------------------------------------------------------------
'''


def main(inputFile):
    # open file in the read mode
    wordnum = 0
    infile = open(inputFile, "r")
    outfile = open('outputFile.txt', "w+")

    # read the file content lines by lines
    lines = infile.readlines()

    title = 'Academic Words List Application'
    programmer = 'Programmer: Runquan Ye        Date: September 2020        GitHub: https://github.com/RunquanYe'
    # header = '\n{0:{gap}^4}{sep}{1:{gap}^12}{sep}{2:{gap}^20}{sep}{3:{gap}^50}{sep}{4:{gap}^8}{sep}{5:{gap}^30}{sep}{6:{gap}^12}{sep}{7:{gap}^4}\n'.format('编号', '单词', '音标', '词意', '词根', '派生词', '源生词', '词表', gap='-', sep='|')
    header = '\n{0:{gap}^4}{sep}{1:{gap}^12}{sep}{2:{gap}^20}{sep}{3:{gap}^50}{sep}{4:{gap}^4}\n'.format('编号', '单词', '音标', '词意', '词表', gap='-', sep='|')
    outfile.writelines(f"{title.title()}".center(len(header) + 8, " "))
    outfile.writelines('\n')
    outfile.writelines(f"{programmer.title()}".center(len(header) + 8, " "))
    outfile.writelines(f"{'=' * (len(header) + 8)}")
    outfile.writelines(header)

    for l in lines:
        wordlist = l.split(' ')
        '''
        firstWord = wordlist[0]
        wordnum += 1
        fw = Word(firstWord,'', '', '', wordlist[1:],'', wordnum, 1, True)
        outfile.writelines('{0:{gap}^5}{sep}{1:{gap}<13}{sep}{2:{gap}<21}{sep}{3:{gap}<50}{sep}{4:{gap}^5}\n'.format(fw.getWordNum(), fw.getWord(), fw.getUSPTwTitle(), fw.getMeaning(), fw.getListNum(), gap=' ',sep='|'))
        '''
        for vocably in wordlist:
            wordnum += 1
            word = Word(vocably, '', '', '', wordlist[1:] if wordlist.index(vocably) == 0 else '', wordlist[0] if wordlist.index(vocably) != 1 else '', wordnum, 1, True if wordlist.index(vocably) == 0 else False)
            outfile.writelines('{0:{gap}^5}{sep}{1:{gap}<13}{sep}{2:{gap}<21}{sep}{3:{gap}<50}{sep}{4:{gap}^5}\n'.format(word.getWordNum(), word.getWord(), word.getUSPTwTitle(), word.getMeaningToString(), word.getListNum(), gap=' ',sep='|'))

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
        a = Word('analytical','', '', '', '','', 0, 1, False)
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
        print("word meaning toString: ", a.getWordToString())
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
    # close files
    infile.close()
    outfile.close()



# Start method trigger.
if __name__ == '__main__':
    main("inputFile.txt")
