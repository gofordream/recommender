import os
from bs4 import BeautifulSoup

def etl():
    etlfile=open('E:\\data\\dataset.csv','a')
    #etlfile.write('UserID,MovieID,Date\n')
    files=os.listdir('E:\\data\\collect3')
    cnt=0
    lines=[]
    for name in files:
        if cnt%50==0:
            print cnt
        cnt+=1
        filename='E:\\data\\collect3\\'+name
        myfile=open(filename,'r')
        content=myfile.read()
        myfile.close()
        bs=BeautifulSoup(content)
        items=bs.select('.item-show')
        sta=filename.rfind('\\')
        end=filename.rfind('_')
        uid=filename[sta+1:end]
        for item in items:
            murl=item.div.a['href']
            mid=murl[33:-1]
            if len(item.select('.date'))<=0:
                print filename
                print item
                etlfile.close()
                return
            
            date=item.select('.date')[0].text
            date=date.replace('\n','').replace(' ','').strip()
            line=uid+','+mid+','+date+'\n'
            lines.append(line)
            #etlfile.write(line)
            
    for line in lines:
        etlfile.write(line)
    etlfile.close()
        

etl()

