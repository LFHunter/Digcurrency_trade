# -*- coding: utf-8 -*-
import  requests
import   os
import  time
from bs4 import BeautifulSoup
import  time
import  json
import re
import  os
import threading
import os
import brotli
def  sendCommand(output):
    os.system(output)


class  Bigbon_Crawler():
    def __init__(self,config):
        self.request =   requests.Session()
        self.cookie = ''
        # self.dataDic = dataDic
        # self.accountid = self.dataDic['accountid']
        self.logfileName =  'a.log'
        self.auth = config['auth']
        # self.login()
        # print(os.getcwd())
        # self.print_byType(os.getcwd())
       # self.save_folder = 'data'
        #self.mk_dir(self.save_folder)

    def  print_byType(self,message,fileName=''):
        fileName  =self.logfileName
        if not os.path.isdir('log'):
            os.mkdir('log')
        path =  os.path.join('log', fileName)
        #print(path)
        with open(path,'a') as f:
            print(message)
            f.write(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )  + ' | ' + str(message) + '\n')

    def  get_HoldContract(self):
        #https://www.mochanji.com/index/index.php
        url = f'https://api-app.cmlucky.com/api/v1/contract/order/hold?fundType=1&pagingSize=15&pageId=0&marginCoinName=VST&marginType=0'
        headers = {"accept" : "application/json, text/plain, */*" ,
                    "accept-encoding" : "gzip, deflate, br" ,
                    "accept-language" : "en-US,en;q=0.9" ,
                    "app_version" : "2.5.7" ,
                    "appid" : "30004" ,
                    "authorization" :  self.auth,
                    "ccn" : "official" ,
                    "channel" : "official" ,
                    "content-type" : "application/json" ,
                    "device_id" : "788008a0-15b6-11eb-b0f6-f5bc3a848591" ,
                    "lang" : "zh-HK" ,
                    "mainappid" : "10009" ,
                    "origin" : "https" ,
                    "platformid" : "30" ,
                    "referer" : "https" ,
                    "sec-fetch-dest" : "empty" ,
                    "sec-fetch-mode" : "cors" ,
                    "sec-fetch-site" : "cross-site" ,
                    #"sign" : "D5835177DBDD41D6805A09132055964BCDF45BC4D9F91C1F692DCCCEB245BD84" ,
                    "timestamp" : "1603554768610" ,
                    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"

                   }
        self.print_byType(f'url:{url}')
        data = {'account_id': self.cookie}

        resp = self.request.get(url=url, allow_redirects=False, headers=headers, timeout=10, data=data)
        # self.print_byType(resp.status_code)
        # self.print_byType(resp.text)
        data = brotli.decompress(resp.content)
        data1 = data.decode('utf-8')
        print(data1)
        print(resp.status_code)
        print(resp.encoding)
        print("--------------------------------")
        return {'webText': resp.text, 'webContent': resp.content}

from  config import bigbon_config

bi = Bigbon_Crawler(bigbon_config)
bi.get_HoldContract()
a = ''' accept: application/json, text/plain, */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
app_version: 2.5.7
appid: 30004
authorization: QQQQ
ccn: official
channel: official
content-type: application/json
device_id: 788008a0-15b6-11eb-b0f6-f5bc3a848591
lang: zh-HK
mainappid: 10009
origin: https://www.bingbon.com
platformid: 30
referer: https://www.bingbon.com/
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: cross-site
sign: 268305A9D67475163E16C4FB4F12032A7FCBD439B0E33540EAFBBC448ABE239E
timestamp: 1603554768610
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36
'''
rowList =  a.split("\n")
for  row  in rowList:
    dataList = row.split(":")
    #dic ={dataList[0]: dataList[1]}
    try:
        print('"'+dataList[0].strip()+'"',":",'"'+dataList[1].strip()+'"',",")
    except :
        pass
