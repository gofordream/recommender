import pandas as pd
import os
from bs4 import BeautifulSoup
def run():
    files=os.listdir('E:\\data\\movie')
    #print len(files)
    titles=[]
    ids=[]
    size=[]
    for index,filename in enumerate(files):
        if index%300==0:
            print index
        #print index,filename
        myfile=open('E:\\data\\movie\\'+filename,'r')
        content=myfile.read()
        myfile.close()
        bs=BeautifulSoup(content)
        
        #print bs.title.text
        title=bs.title.text.strip()[:-5]
        movieid=filename[:-5]
        titles.append(title)
        ids.append(movieid)
        size.append(len(content))
    
    df=pd.DataFrame()
    df['name']=titles
    df['id']=ids
    df['size']=size
    df.to_csv('movie.csv',index=False)
        
#run()
def run2():
    data=pd.read_csv('E:\\data\\dataset.csv')
    user=set(data['UserID'])
    movie=set(data['MovieID'])
    #print data.shape
    #print len(user),len(movie)
    time=data['Date']
    timeset=set()
    for t in time:
        if isinstance(t,float):
            print t
            continue
        if len(t)!=10:
            print 'xx'
            continue
        timeset.add(t)
    timelist=sorted(timeset)
    print timelist[0],timelist[1],timelist[-1]
    
run2()
