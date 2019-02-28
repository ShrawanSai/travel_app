#!/usr/bin/python3

"""
    parse_wikitable.py

    MediaWiki Action API Code Samples
    Demo of `Parse` module: Parse a section of a page, fetch its table data and save
    it to a CSV file

    MIT license
"""
import re
import requests
S = requests.Session()

URL = "http://wikitravel.org/wiki/en/api.php"

TITLE = "Jaipur"

PARAMS = {
    'action': "parse",
    'page': TITLE,
    'prop': 'wikitext',
    'section': 0,
    'format': "json"
}
def details(find,fromhere):
    dict1={}
    lineslist=fromhere[0].split('\n')
    #print(lineslist)
    for i in lineslist:
        #print(i)
        #print('_________')
        for j in find:
            if j in i:
                dict1.update({j:i})
    return(dict1)

                
    
    
def extract(do,see):
    #print(len(x))
    DO=''
    for line in do:
        DO+=line
    SEE=''
    for line in see:
        SEE+=line
    print(SEE)
    subsubdo = re.findall('\'\'\'(.+?)\'\'\'', DO)
    print('________________________scoob___\n')
    hhh=re.findall('<see name=".+"', DO)
    print(hhh)
    print('________________________scoob___\n')
    print('________________________scoob___\n')
    
    subsubsee = re.findall('\'\'\'(.+?)\'\'\'', SEE)
    DOdict=details(subsubdo,do)
    SEEdict=details(subsubsee,see)
    
    #print(DOdict)
    #for i in DOdict:
        #print(i,end='')
        #print(DOdict[i])
        #print('\n\n\n')
    #print('_______________________________________________________________________________________________________')
    #print('\n\n\n')
    #print(SEEdict)
    #for i in SEEdict:
        #print(i,end='')
        #print(' : ',end='')
        #print(SEEdict[i])
        #print('\n\n\n')
    #print(subsubsee)
    return SEEdict,DOdict
def get_table():
    try:
        update_to=PARAMS['section']
        while True:
        
            PARAMS.update({'section':update_to})
            update_to+=1
            res = S.get(url=URL, params=PARAMS)
            data = res.json()
            wikitext = data['parse']['wikitext']['*']
            lines = wikitext.split('|-')
            #print(type(lines))
            for line in lines:
                #print(line)
                if '==Do==' in line:
                    do=lines
                elif '==See==' in line:
                    see=lines
        #print(do)
        #print(see)
    except Exception as e:
        x,y=extract(do,see)
        #print(do)
        #print(see)
        #print('------')
        #print(e)
        return  x,y
      


