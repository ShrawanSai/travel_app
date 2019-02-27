import re
def links(text):
   urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
   return urls
def prices(text):
   p=re.findall('[\$\£\€](\d+(?:\.\d{1,2})?)', text)
   #print('______________\n')
   #print(text)
   p=re.findall('[0-9]*\sRs\s[0-9]*\/?\-?[0-9]*',text)
   #print(p)
   return p
def timings(text):
   text=text.lower()
   cc=re.findall('[1-9]{1}[0-9]*[a]{0,1}[p]{0,1}m \w [1-9]{1}[0-9]*[a]{0,1}[p]{0,1}m ', text)
   
   
   
