import os
from bs4 import BeautifulSoup
import pickle

from urllib import urlretrieve
import time
import pandas as pd
def movie_urls():
    
    movies=set()
    myfile=open('movie.pkl','r')
    movies=pickle.load(myfile)
    myfile.close()
    files=os.listdir('E:\\data\\collect3')
    cnt=0
    for name in files:
        cnt+=1
        if cnt%100==0:
            print cnt
        filename='E:\\data\\collect3\\'+name
        myfile=open(filename,'r')
        content=myfile.read()
        myfile.close()
        bs=BeautifulSoup(content)
        items=bs.select('.item-show')
        for item in items:
            movies.add(item.div.a['href'])
    myfile=open('movie.pkl','wb')
    print len(movies)
    pickle.dump(movies,myfile)
    myfile.close()
    
#movie_urls()

def run():
    myfile=open('movie.pkl','r')
    movies=pickle.load(myfile)
    myfile.close()
    print len(movies)
    return
    cnt=0
    for url in movies:
        cnt+=1
        print cnt
        mid=url[33:-1]
        filename='E:\\data\\movie\\'+mid+'.html'
        if os.path.exists(filename):
            continue
        urlretrieve(url,filename)
        time.sleep(0.7)
#run()

def run2():
    data=pd.read_csv('movie.csv')
    cnt=0
    for index,row in data.iterrows():
        name=row['name']
        mid=row['id']
        if name=='403 Forb':
            #urlretrieve()
            url='http://movie.douban.com/subject/'+str(mid)+'/'
            filename='E:\\data\\movie\\'+str(mid)+'.html'
            urlretrieve(url,filename)
            cnt+=1
            time.sleep(0.9)
            print cnt,mid
run2()
        
        