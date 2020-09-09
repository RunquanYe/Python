from Exception import *
from Word import *

from urllib.request import urlopen
from bs4 import BeautifulSoup
'''
This is a python project for me to store English Academic Word List
Author: Runquan Ye
Date: Sept/2020
'''

def main():

    get_data()
    '''
    try:
        a = Word('Subsidiary','adj, n', 'adj. 附属的, 辅助的; n. 子公司, 辅助者, 支流', '', '','', 0, 1, False)
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
        
    except OSError as err:
        print("OS error: {0}".format(err))
        pass
    except WordNameEmpty:
        print("Error! Empty word name!")
        pass
    except WordCategoryEmpty:
        print("Error! Empty word category!")
        pass
    except WordMeaningEmpty:
        print("Error! Empty word meaning!")
        pass
    '''

def get_data():
    webpage = urlopen('https://cn.bing.com/dict/search?q=hail&mkt=zh-cn').read()

    soup = BeautifulSoup(webpage, 'html.parser')

    target = soup.find_all('meta')
    for i in target:
        if "name" in i.attrs:
            if i["name"] == "description":
                rawData = str(i["content"])

    hindex = rawData.find("释义，美")
    tindex = rawData.find("网络释义")
    #data => 美[səbˈsɪdiˌeri]，英[səbˈsɪdiəri]，n.子公司；附属公司； adj.辅助的；附带的；次要的；附属的；
    data = rawData[(hindex+3) : tindex]

    t1 = re.split('[，]', data)

    uspt = str(t1[0][1:])
    ukpt = str(t1[1][1:])
    wRawMean = str(t1[2])[:-2]

    wTempMean = re.sub('\；\s+([a-z,A-Z]+\.)', '|\\1', wRawMean)
    print(wTempMean)
    wMean = wTempMean.replace('；', ', ').replace('|', '; ')

    t3 = re.split('[;；]', wMean.lower())
    t4 = [i[0] for i in sorted([list(filter(None, re.split('[.,， ]',i))) for i in t3])]
    print(wMean)
    print(t3)
    print(t4)

# Start method trigger.
if __name__ == '__main__':
    main()
