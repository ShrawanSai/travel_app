import code1
from prettytable import PrettyTable
t=PrettyTable(['Things to do','Website link','Cost','Details'])
sss=PrettyTable(['Things to see','Website link','Cost','Details'])
#print(t)
import fetching

s={}
d={}
see,do=code1.get_table()

for i in see:
   val=[see[i]]
   timings=fetching.timings(see[i])

   urls=fetching.links(see[i])
   if len(urls)>0:
      #print(urls)
      pass
   prices=fetching.prices(see[i])
   temp=[]
   if len(prices)>0:
      for j in prices:  
         x='$'+j
         temp.append(x)
   #print(see[i])
   val.append(temp)
   val.append(urls)
   val.append(timings)
   s.update({i:val})
   ccc=[i,urls,temp,see[i][:5:]]
   #print(ccc)
   sss.add_row(ccc)
#print(sss)
#print('\n\n\n')
   
for i in do:
   val=[do[i]]

   urls=fetching.links(do[i])
   if len(urls)>0:
      #print(urls)
      pass
   prices=fetching.prices(do[i])
   temp=[]
   if len(prices)>0:
      for j in prices:
         x='$'+j
         temp.append(x)
   #print(see[i])
   val.append(temp)
   val.append(urls)
     
   d.update({i:val})
   val.append(i)
   val.reverse()
   ccc=[i,urls,temp,do[i][:5:]]
   #print(ccc)
   t.add_row(ccc)
#print(t)
   

   
