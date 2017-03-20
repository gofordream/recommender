from bs4 import BeautifulSoup
import os
import pickle
from urllib import urlretrieve
import time


def run():
    files=os.listdir('E:\\data\\movie')
    reviewurl=set()
    for index,name in enumerate(files):
        filename='E:\\data\\movie\\'+name
        myfile=open(filename,'r')
        content=myfile.read()
        bs=BeautifulSoup(content)
        myfile.close()
        reviews=bs.select('.review-hd-expand')
        #print 'index',index,len(reviews),name
        for tag in reviews:
            #print tag.a['href']
            reviewurl.add(tag.a['href'])
        if index%20==0:
            print index
    myfile=open('reviewurl.pkl','w')
    pickle.dump(reviewurl,myfile)
    myfile.close()


def request():
    myfile=open('reviewurl.pkl','r')
    reviewurl=pickle.load(myfile)
    myfile.close()
    print len(reviewurl)
    
    for index,url in enumerate(reviewurl):
        rid=url[32:-1]
        filename='E:\\data\\review\\'+rid+'.html'
        print index,rid
        if os.path.exists(filename):
            continue
        urlretrieve(url,filename)
        time.sleep(0.9)
        
request()
    