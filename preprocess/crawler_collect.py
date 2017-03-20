import requests

from bs4 import BeautifulSoup

from urllib import urlretrieve

import pickle
import time

import os
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')

def login():
    loginurl='https://accounts.douban.com/login'
    s=requests.Session()
    r=s.get(loginurl)
    soup=BeautifulSoup(r.text)
    
    data={}
    data['form_email']='***'
    data['form_password']='***'

    if len(soup.select('#captcha_image'))>0:
        imgurl=soup.select('#captcha_image')[0]['src']
        urlretrieve(imgurl,'captcha.jpg')
        code=raw_input('captcha:')
        data['captcha-solution']=code
        start=imgurl.find('=')
        end=imgurl.find('&')
        data['captcha-id']=imgurl[start+1:end]
    r=s.post(loginurl,data)
    return s
        
def user_friend(session,url):
    r=session.get(url)
    soup=BeautifulSoup(r.text)
    friends=soup.select('.obu')
    ret=[]
    for f in friends:
        url=f.dt.a['href']
        #name=f.dt.a.img['alt']
        #ret.append((name,url))
        ret.append(url)
    return ret

def user_urls():
    #start='https://www.douban.com/people/60592551/'
    start='https://www.douban.com/people/Femmetatale/'
    mylist=[start]
    users=set()
    mydict={}
    session=login()
    cnt=0
    while len(mylist)>0:
        user=mylist[0]
        mylist=mylist[1:]
        if mydict.has_key(user):
            continue
        mydict[user]=1
        users.add(user)
        time.sleep(1)
        friends=user_friend(session,user+'contacts')
        for f in friends:
            users.add(f)
            if not mydict.has_key(f):
                mylist.append(f)
        cnt+=1
        print 'count:',cnt
        print len(users)
        if len(users)>44000:
            break
    myfile=open('user.pkl','wb')
    pickle.dump(users,myfile)
    myfile.close()
#user_urls()

def savefile(data,filename):
    myfile=open(filename,'w')
    myfile.write(data)
    myfile.close()
def run():
    print 'start'
    myfile=open('user.pkl','r')
    users=list(pickle.load(myfile))
    myfile.close()
    session=login()
    cnt=0
    filter_out=['https://www.douban.com/people/rakumm/','https://www.douban.com/people/luzhiyu/','https://www.douban.com/people/xzyzsk7/','https://www.douban.com/people/chenchangxing/','https://www.douban.com/people/chunsue/','https://www.douban.com/people/hitchitsch/']
    #for url in users[4800:]:
    print '...'
    for url in users[8000:]:
        userid=url[30:-1]
        page=0
        cnt+=1
        print url,cnt
        if url in filter_out:
            print 'ignore...'
            continue
        while True:
            myurl=url.replace('www','movie')+'collect?mode=list&start='+str(page*30)
            page+=1
            try:
                #filename='E:\\data\\collect3\\'+str(userid)+'_'+str(page)+'.html'
                #if os.path.exists(filename):
                #    break
                exist=0
                paths=['E:\\data\\collect\\','E:\\data\\collect2\\','E:\\data\\collect3\\','E:\\data\\collect4\\','E:\\data\\collect5\\']
                for path in paths:
                    filename=path+str(userid)+'_'+str(page)+'.html'
                    if os.path.exists(filename):
                        exist=1
                        break
                if exist>0:
                    break
                filename='E:\\data\\collect5\\'+str(userid)+'_'+str(page)+'.html'
                time.sleep(1.0)
                r=session.get(myurl)
                #urlretrieve(myurl,filename)
                savefile(r.text,filename)
                
                if len(r.text)<=19593:
                    print '...'
                    return
                if r.text.find('>后页')<0:
                    break
            except:
                print 'exception...'
                break
run()
            
def remove():
    #os.remove('E:\\data\\collect\\janewoo_1.html')
    #print os.path.getsize('E:\\data\\collect\\lff121_1.html')
    myfile=open('user.pkl','r')
    users=list(pickle.load(myfile))
    myfile.close()
    for url in users[0:5000]:
        userid=url[30:-1]
        filename='E:\\data\\collect\\'+str(userid)+'_1.html'
        if os.path.exists(filename):
            size=os.path.getsize(filename)
            if size<=19593:
                os.remove(filename)
