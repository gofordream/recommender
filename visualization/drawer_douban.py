import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def draw_genres_evolution():
    dataset=pd.read_csv('E:\\data\\dataset.csv')
    
    userlist=dataset['UserID']
    movielist=dataset['MovieID']
    timelist=dataset['Date']

    user_dict={}
    for i in range(100000):
        user=userlist[i]
        movie=movielist[i]
        time=timelist[i]
        if not user_dict.has_key(user):
            user_dict[user]=[]
        user_dict[user].append((movie,time))
    
    
    #for user in user_dict:
    #    print len(user_dict[user]),user
    userid=1641214
    #userid=1563045
    hist=sorted(user_dict[userid],key=lambda x:x[1])
    type_cnt={}
    #daydict={}
    yeardict={}
    for movie,time in hist:
        filename='E:\\data\\movie\\'+str(int(movie))+'.html'
        myfile=open(filename,'r')
        content=myfile.read()
        myfile.close()
        bs=BeautifulSoup(content)
        #tags=bs.select('#info')
        #if len(tags)<=0:
        #    continue
        #yearmon=time[:7]
        year=time[:4]
        if not yeardict.has_key(year):
            yeardict[year]=[]
        tags=bs.select('span[property="v:genre"]')
        for tag in tags:
            if not type_cnt.has_key(tag.text):
                type_cnt[tag.text]=0
            type_cnt[tag.text]+=1
            
            yeardict[year].append(tag.text)
    df=pd.DataFrame()
    df['type']=type_cnt.keys()
    columns={}
    for time in yeardict:
        mylist=[]
        for mtype in type_cnt:
            count=yeardict[time].count(mtype)
            #ratio=float(daydict[time].count(mtype))/len(daydict[time])
            #print mtype,count
            #mylist.append(str(ratio)[:4])
            mylist.append(count)
        total=sum(mylist)
        
        columns[time]=[str(float(i)/total)[:4] for i in mylist]
        #df[year]=yearlist
    for time in sorted(columns.keys()):
        df[time]=columns[time]
    #df.to_csv('E:\\data\\douban.csv',index=False)
#draw_genres_evolution()
def draw_genres_evolution_from_file():
    data=pd.read_csv('E:\\data\\douban.csv',encoding="gb2312")
    x1=[]
    y1=[]
    x2=[]
    y2=[]
    for index,row in data.iterrows():
        genres=row['type']
        year2007=row['2007']
        year2008=row['2008']
        year2009=row['2009']
        year2010=row['2010']
        year2011=row['2011']
        year2012=row['2012']
        year2013=row['2013']
        year2014=row['2014']
        year2015=row['2015']
        year2016=row['2016']
        
        #print genres
        if genres=='爱情':
            print 'YES'
            y1.append(year2007)
            y1.append(year2008)
            y1.append(year2009)
            y1.append(year2010)
            y1.append(year2011)
            y1.append(year2012)
            y1.append(year2013)
            y1.append(year2014)
            y1.append(year2015)
            y1.append(year2016)
        
        if genres=='惊悚':
            print 'No'
            y2.append(year2007)
            y2.append(year2008)
            y2.append(year2009)
            y2.append(year2010)
            y2.append(year2011)
            y2.append(year2012)
            y2.append(year2013)
            y2.append(year2014)
            y2.append(year2015)
            y2.append(year2016)
    
    x=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016]
    
    ax=plt.gca()
    ax.set_xlabel('year')
    ax.set_ylabel('interest')
    ax.set_xticklabels([2007,2008,2009,2010,2011,2012,2013,2014,2015,2016])
    
    plt.plot(x,y1,label='Romance ')
    plt.plot(x,y2,label='Thriller ')
    plt.legend(loc='upper right')
#draw_genres_evolution_from_file()
def draw_rating_evolution():
    dataset=pd.read_csv('E:\\data\\dataset.csv')
    
    userlist=dataset['UserID']
    movielist=dataset['MovieID']
    timelist=dataset['Date']
    

    user_dict={}
    for i in range(100000):
        user=userlist[i]
        movie=movielist[i]
        time=timelist[i]
        if not user_dict.has_key(user):
            user_dict[user]=[]
        user_dict[user].append((movie,time))
    
    print len(user_dict)
    
    for user in user_dict:
        print len(user_dict[user]),user
    userid=1641214
    userid=10241572
    userid=1729609
    hist=sorted(user_dict[userid],key=lambda x:x[1])
    year_rating={}
    month_rating={}
    for movie,time in hist:
        filename='E:\\data\\movie\\'+str(int(movie))+'.html'
        myfile=open(filename,'r')
        content=myfile.read()
        myfile.close()
        bs=BeautifulSoup(content)
        year=time[:4]
        tags=bs.select('strong[property="v:average"]')
        if len(tags)<=0:
            continue
        tag=tags[0]
        if len(tag.text)<3:
            continue
        rating=float(tag.text)
        if not year_rating.has_key(year):
            year_rating[year]=[]
        year_rating[year].append(rating)
        month=time[:7]
        if not month_rating.has_key(month):
            month_rating[month]=[]
        month_rating[month].append(rating)
        
    
    
    y=[]
    for year in sorted(year_rating.keys()):
    #for month in sorted(month_rating.keys()):
        #print year,len(year_rating),sum(year_rating)/len(year_rating)
        #print year,len(year_rating[year]),sum(year_rating[year])/len(year_rating[year])
        #x.append(int(year))
        rating=sum(year_rating[year])/len(year_rating[year])
        #rating=sum(month_rating[month])/len(month_rating[month])
        y.append(rating)
        #y.append(sum(year_rating[year])/len(year_rating[year]))
    #plt.scatter(x,y,s=20,marker='.',color='r')
    ax=plt.gca()
    ax.set_xlabel('year')
    ax.set_ylabel('mean rating')
    #ax.set_xticks(np.linspace(0,len(year_rating)-1,len(year_rating)))
    ax.set_xticks(np.linspace(0,len(y)-1,len(year_rating)))
    tl=sorted(year_rating.keys())
    #print tl,type(tl)
    ax.set_xticklabels(tl)
    
    #ax.set_xticklabels([2001,2001])
    #plt.plot(x,y)
    #print y
    plt.plot(y)

draw_rating_evolution()

    