from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
'''
This is a class for finding online data from Bing Dictionary for the missing data
---------------------------------------------------------------------------------
    Author: Runquan Ye
    Date: Sept/2020
---------------------------------------------------------------------------------
'''

class DataSourceBY():
    # constructor
    # 词名，词类，词意，美音标，英音标, 词类list，词意list
    _dName, _dCatergory, _dMeaning, _dUS_pt, _dUK_pt, _dCatergoryList, _dMeaningList = '', '', '', '', '', [], []

    _modeName = "Bing"

    def __init__(self, word):
        if bool(word and word.strip()):
            self._dName = word.lower()

        #get word's data from the web
            # webpage = urlopen('https://cn.bing.com/dict/search?q=' + self._dName + '&FORM=BDVSP6&mkt=zh-cn').read()
            webpage = urlopen('https://cn.bing.com/dict/search?q=' + self._dName + '&mkt=zh-cn').read()

        #transfer opening url to html document
            soup = BeautifulSoup(webpage, 'html.parser')

        #find the html element tag
            target = soup.find_all('meta')

            for i in target:
                if "name" in i.attrs:
                    if i["name"] == "description":
                        rawData = str(i["content"])

        #modify the raw data content
            hindex = rawData.find("释义，美")
            tindex = rawData.find("网络释义")
            #data => 美[heɪl]，英[heɪl]，n. 冰雹；雹子；【气】雹；像雹子般落下的东西； v. 招呼；〈正式〉喊；捧；歌颂； int. 万岁；
            data = rawData[(hindex+3) : tindex]

            #temp => ['美[heɪl]', '英[heɪl]', 'n. 冰雹；雹子；【气】雹；像雹子般落下的东西； v. 招呼；〈正式〉喊；捧；歌颂； int. 万岁； ']
            temp = re.split('[,，]', data)

            if len(temp) == 3:
                #uspt => '[heɪl]'
                uspt = str(temp[0][1:])
                #ukpt => '[heɪl]'
                ukpt = str(temp[1][1:])
                #wRawMean => 'n. 冰雹；雹子；【气】雹；像雹子般落下的东西； v. 招呼；〈正式〉喊；捧；歌颂； int. 万岁'
                wRawMean = str(temp[2])[:-2]

                #wTempMean => n. 冰雹；雹子；【气】雹；像雹子般落下的东西｜v. 招呼；〈正式〉喊；捧；歌颂｜int. 万岁
                wTempMean = re.sub('\；\s+([a-z,A-Z]+\.)', '|\\1', wRawMean)
                # wMean => n. 冰雹, 雹子, 【气】雹, 像雹子般落下的东西; v. 招呼, 〈正式〉喊, 捧, 歌颂; int. 万岁
                wMean = wTempMean.replace('；', ', ').replace('|', '; ')

                # wMean => ['n. 冰雹, 雹子, 【气】雹, 像雹子般落下的东西', ' v. 招呼, 〈正式〉喊, 捧, 歌颂', ' int. 万岁']
                self._dMeaningList = re.split('[;；]', wMean.lower())
                #_dMeaningList => ['int', 'n', 'v']
                self._dCatergoryList = [i[0] for i in sorted([list(filter(None, re.split('[.,， ]', i))) for i in self._dMeaningList])]

                self._dUS_pt = uspt
                self._dUK_pt = ukpt
                self._dCatergory = ', '.join(str(i) for i in self._dCatergoryList)
                self._dMeaning = wMean


    def getWordName(self):
        return self._dName.lower()

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

    def getModeName(self):
        return self._modeName

    # Bing online word audio:
    '''
    UK
    <div class="client_daily_word_pn_audio">
                      <div class="client_icon_container">
                        <a
                          class="client_aud_o"
                          title="Click to listen"
                          onmouseover="BilingualDict.Click(this,'https://dictionary.blob.core.chinacloudapi.cn/media/audio/george/fe/b9/FEB9E4F442858E3672BC4580843B9915.mp3','akicon.png',false,'dictionaryvoiceid')"
                          onClick="BilingualDict.Click(this,'https://dictionary.blob.core.chinacloudapi.cn/media/audio/george/fe/b9/FEB9E4F442858E3672BC4580843B9915.mp3','akicon.png',false,'dictionaryvoiceid')"
                          href="javascript:void(0)"
                          h="ID=Dictionary,5094.1"
                        ></a>
                      </div>
                    </div>
    '''

    '''
    US 
                        <div class="client_daily_word_pn_audio">
                      <div class="client_icon_container">
                        <a
                          class="client_aud_o"
                          onmouseout="this.className='client_aud_o'"
                          title="Click to listen"
                          onmouseover="BilingualDict.Click(this,'https://dictionary.blob.core.chinacloudapi.cn/media/audio/tom/fe/b9/FEB9E4F442858E3672BC4580843B9915.mp3','akicon.png',false,'dictionaryvoiceid')"
                          onClick="BilingualDict.Click(this,'https://dictionary.blob.core.chinacloudapi.cn/media/audio/tom/fe/b9/FEB9E4F442858E3672BC4580843B9915.mp3','akicon.png',false,'dictionaryvoiceid')"
                          href="javascript:void(0)"
                          h="ID=Dictionary,5093.1"
                        ></a>
                      </div>
                    </div>
    '''