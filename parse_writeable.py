#!/usr/bin/python3

"""
    parse_wikitable.py

    MediaWiki Action API Code Samples
    Demo of `Parse` module: Parse a section of a page, fetch its table data and save
    it to a CSV file

    MIT license
"""
import nltk
import re
import csv
import requests

S = requests.Session()

URL = "http://wikitravel.org/wiki/en/api.php"

TITLE = "Bangalore"


PARAMS = {
    'action': "parse",
    'page': TITLE,
    'prop': 'wikitext',
    'format': "json"
}
def details(x):
    pass
    
def extract(x,pos):
    #print(len(x))
    subsub = re.findall('\'\'\'(.+?)\'\'\'', x)
    sub = re.findall('\=\=\=(.+?)\=\=\=', x)

    dopart=x[pos[0]::]
    see=[]
    do=[]
    for i in subsub:
        if i in dopart:
            do.append(i)
        else:
            see.append(i)
    print(see)
    print(do)

def sax(text):
    a=''
    for i in range(len(text)):
        a+=text[i]
        #print(a)
   
    z=[m.start() for m in re.finditer('==See',a)]
    print(z)


    xxx=[m.start() for m in re.finditer('[==[A-Za-z]==',a)]
    ff=re.findall('[^=]==[A-Za-z][^=]==',a)
    print(ff)
    #print(a)
    #print(a)
    print(xxx)
    for i in range(len(xxx)):
        if xxx[i]==z[0]:
            c=xxx[i+2]
            break
    #print('--------------------')
    print(c)
    x=a[z[0]-1:c:]
    print(x)
    y=[m.start() for m in re.finditer('==Do',x)]
    extract(x,y)
    #print(xxx)
def get_table():
    final={}
    p=[]
    """ Parse a section of a page, fetch its table data and save it to a CSV file
    """
    res = S.get(url=URL, params=PARAMS)
    data = res.json()
    wikitext = data['parse']['wikitext']['*']
    lines = wikitext.split('|-')
    entries = []
    #print(lines)
    #print(len(lines))
    sax(lines)
      
    '''c=''
    for i in x:
        c+=i
        if len(c)>15:
            if c[::-8]=='==Cope==':
                break
    print('------------------------------------')
    print(c)
    print('------------------------------------')'''


if __name__ == '__main__':
    get_table()
