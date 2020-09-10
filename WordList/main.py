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
    header = '\n{0:{gap}^4}{sep}{1:{gap}^12}{sep}{2:{gap}^20}{sep}{3:{gap}^50}{sep}{4:{gap}^8}{sep}{5:{gap}^30}{sep}{6:{gap}^12}{sep}{7:{gap}^4}\n'.format('编号', '单词', '音标', '词意', '词根', '派生词', '源生词', '词表', gap='-', sep='|')
    # outfile.writelines('{0:50}'.format('Academic Words List Application\n'))
    outfile.writelines(f"{title.title()}".center(len(header) + 8, " "))
    outfile.writelines('\n')
    outfile.writelines(f"{programmer.title()}".center(len(header) + 8, " "))
    outfile.writelines(f"{'=' * (len(header) + 8)}")
    outfile.writelines(header)

    for l in lines:
        wordlist = l.split(' ')
        firstWord = wordlist[0]
        wordnum += 1
        fw = Word(firstWord,'', '', '', ', '.join(str(u) for u in wordlist[1:]),'', wordnum, 1, True)
        print(type(wordlist[1:]))
        print(type(', '.join(str(u) for u in wordlist[1:])) != 'str')
        print(fw.getDerivativeWord())
        outfile.writelines('{0:{gap}^5}{sep}{1:{gap}<13}{sep}{2:{gap}<21}{sep}{3:{gap}<50}{sep}{4:{gap}^9}{sep}{5:{gap}<32}{sep}{6:{gap}<14}{sep}{7:{gap}^5}\n'.format(fw.getWordNum(), fw.getWord(), fw.getUSPTwTitle(), fw.getMeaning(), fw.getRoot(), fw.getDerivativeWord(), fw.getSourceWord(), fw.getListNum(), gap=' ',sep='|'))
        # for vocabulary in wordlist[1:]:
        #     print(vocabulary)

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
        a = Word('analyse','', '', '', '','', 0, 1, False)
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
    # close files
    infile.close()
    outfile.close()



# Start method trigger.
if __name__ == '__main__':
    main("inputFile.txt")
