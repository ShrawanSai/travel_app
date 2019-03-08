#!/usr/bin/python3

"""
    parse_wikitable.py

    MediaWiki Action API Code Samples
    Demo of `Parse` module: Parse a section of a page, fetch its table data and save
    it to a CSV file

    MIT license
"""
import sqlite3
con=sqlite3.connect('see.db')
c=con.cursor()

import re
import requests
S = requests.Session()

URL = "http://wikitravel.org/wiki/en/api.php"

TITLE = "Banglore"

def adding_to_db(dict_see):
    place=TITLE
    #print(dict_see)
    name=dict_see['name']

    try:
        alt=dict_see['alt']
    except Exception as e:
        alt=''

    
    try:
        url=dict_see['url']
    except Exception as e:
        url=''
        
    try:
        phone=dict_see['phone']
    except Exception as e:
        phone=''
        
    try:
        email=dict_see['email']
    except Exception as e:
        email=''
        
    try:
        price=dict_see['price']
    except Exception as e:
        price=''
        
    try:
        address=dict_see['address']
    except Exception as e:
        address=''
        
    try:
        directions=dict_see['directions']
    except Exception as e:
        directions=''
        
    try:
        lat=dict_see['lat']
    except Exception as e:
        lat=''
        
    try:
        long=dict_see['long']
    except Exception as e:
        long=''
        

    try:
        hours=dict_see['hours']
    except Exception as e:
        hours=''
        

    try:
        fax=dict_see['fax']
    except Exception as e:
        fax=''

    try:
        tollfree=dict_see['tollfree']
    except Exception as e:
        tollfree=''
    
    
    return((place,name,price,hours,long,lat,address,alt,directions,url,email,phone,tollfree,fax))
    
    con.commit()
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
    for i in lineslist:
        #print(i)
        #print('_________')
        for j in find:
            if j in i:
                hhh=re.findall(r'<see name=[^>]+>', i)
                ddd=re.findall(r'<do name=[^>]+>', i)
                fff=re.findall(r'<listing name=[^>]+>', i)
                if len(fff)>0 or len(hhh)>0 or len(ddd)>0:
                    continue
                xxx=re.sub(r'\'\'\'', '', i)
                xxx=re.sub(r'\*+', '', xxx)
                
                dict1.update({j:xxx})
    
    return(dict1)


def cleaningapi(dict1):
    clean_dict={}
    for i in dict1:
        parts={}
        params=re.findall(r'[A-Za-z]+=',dict1[i])
        for j in range(len(params)):
            cur=params[j]
            end=len(params[j])
            cur=cur[:end-1]
            searchfor=r'{0}="[^"]+"'.format(cur)
            result_set=re.findall(searchfor,dict1[i])
            try:
                gg=result_set[0]
                remove=len(params[j])
                tot=len(gg)
                pp=gg[remove:tot]
            except Exception as e:
                pp=''
            parts.update({cur:pp})
        clean_dict.update({i:parts})
    return clean_dict
        
                
    
    
def extract(do,see):

    DO=''
    for line in do:
        DO+=line

        
    SEE=''
    for line in see:
        SEE+=line


    subsubdo = re.findall('\'\'\'(.+?)\'\'\'', DO)
    subsubsee = re.findall('\'\'\'(.+?)\'\'\'', SEE)

    hhh=re.findall(r'<see name=[^>]+>', SEE)
    ddd=re.findall(r'<do name=[^>]+>', DO)
    fff=re.findall(r'<listing name=[^>]+>', DO)

    
    see_places=[]
    do_places=[]

    proper_see={}#API part
    proper_do={}
    proper_list={}
    
    for i in hhh:
        temp=re.findall(r'name="[a-zA-z0-9=\.\'\(\)\-!,+:\/@#;?\[\]\{\} ]+"',i)
        for j in temp:
            
            end=len(j)
            see_places.append(j[6:end-1])

            proper_see.update({j[6:end-1]:i})
            

    for i in ddd:
        temp=re.findall(r'name="[a-zA-z0-9=\.\'\(\)\-!,+:\/@#;?\[\]\{\} ]+"',i)
        for j in temp:
            end=len(j)
            do_places.append(j[6:end-1])

            proper_do.update({j[6:end-1]:i})
            

    for i in fff:
        temp=re.findall(r'name="[a-zA-z0-9=\.\'\(\)\-!,+:\/@#;?\[\]\{\} ]+"',i)
        for j in temp:
            end=len(j)
            proper_list.update({j[6:end-1]:i})

    
    cleaned_seen=cleaningapi(proper_see)
    cleaned_do=cleaningapi(proper_do)
    cleaned_list=cleaningapi(proper_list)
    DOdict=details(subsubdo,do)
    SEEdict=details(subsubsee,see)

    
 
    for i in SEEdict:
        x=[TITLE,i,SEEdict[i]]
        c.execute("INSERT INTO NOFORMATSEE(PLACE,NAME,DESCRIPTION) VALUES(?,?,?)",x)

    for i in DOdict:
        x=[TITLE,i,DOdict[i]]
        c.execute("INSERT INTO NOFORMATDO(PLACE,NAME,DESCRIPTION) VALUES(?,?,?)",x)

        
    for i in cleaned_seen:
        x=adding_to_db(cleaned_seen[i])
        #print(x)
        x=list(x)
        c.execute("INSERT INTO SEETABLE(PLACE,NAME,PRICE,HOURS,LONG,LAT,ADDRESS,ALT,DIRECTIONS,URL,EMAIL,PHONE,TOLLFREE,FAX) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",x)
        #print('Added')
        con.commit()

    for i in cleaned_do:
        x=adding_to_db(cleaned_do[i])
        #print(x)
        x=list(x)
        c.execute("INSERT INTO DOTABLE(PLACE,NAME,PRICE,HOURS,LONG,LAT,ADDRESS,ALT,DIRECTIONS,URL,EMAIL,PHONE,TOLLFREE,FAX) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",x)
        #print('Added')
        con.commit()

    for i in cleaned_list:
        x=adding_to_db(cleaned_list[i])
        #print(x)
        x=list(x)
        c.execute("INSERT INTO SEETABLE(PLACE,NAME,PRICE,HOURS,LONG,LAT,ADDRESS,ALT,DIRECTIONS,URL,EMAIL,PHONE,TOLLFREE,FAX) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",x)
        #print('Added')
        con.commit()
    con.close()
    return SEEdict,DOdict
def get_table():
    try:
        update_to=PARAMS['section']
        while True:
            print(1)
            PARAMS.update({'section':update_to})
            update_to+=1
            print(2)
            res = S.get(url=URL, params=PARAMS)
            print(3)
            data = res.json()
            print(4)
            wikitext = data['parse']['wikitext']['*']
            print(5)
            lines = wikitext.split('|-')
            print(6)
            #print(type(lines))
            for line in lines:
                #print(line)
                if '==Do==' in line:
                    print(7)
                    do=lines
                elif '==See==' in line:
                    print(8)
                    see=lines
        #print(do)
        #print(see)
    except Exception as e:
        print(e)
        try:
           
            x,y=extract(do,see)
            return  x,y
        except Exception as e:
            print(e)
            print('Net Connection issue')
        
see,do=get_table()


