import pandas as pd
import time
import random


def dataset_sampling():
    data=pd.read_csv('E:\\data\\dataset_timestamp.csv')
    userlist=list(data['userId'])
    usercnt={}
    for i in range(len(userlist)):
        user=userlist[i]
        if not usercnt.has_key(user):
            usercnt[user]=0
        usercnt[user]+=1
    userlist=[]
    for user in usercnt:
        if usercnt[user]>=10 and usercnt[user]<=800:
            userlist.append(user)
    print len(userlist),len(usercnt)
    userset=set()
    userinx=random.sample(range(len(userlist)),200)
    for i in userinx:
        userset.add(userlist[i])
    users=list(data['userId'])
    movies=list(data['movieId'])
    times=list(data['timestamp'])
    new_user=[]
    new_movie=[]
    new_time=[]
    for i in range(data.shape[0]):
        user=users[i]
        movie=movies[i]
        timestamp=times[i]
        if not user in userset:
            continue
        new_user.append(user)
        new_movie.append(movie)
        new_time.append(timestamp)
    df=pd.DataFrame()
    df['userId']=new_user
    df['movieId']=new_movie
    df['timestamp']=new_time
    #df.to_csv('E:\\data\\dataset_timestamp3.csv',index=False)
    df.to_csv('E:\\data\\douban_200.csv',index=False)
    print df.shape
    print len(set(new_user)),len(set(new_movie))
    
#dataset_sampling()

def run0():
    data=pd.read_csv('E:\\data\dataset.csv')
    users=data['UserID']
    movies=data['MovieID']
    times=data['Date']
    new_users=[]
    new_movies=[]
    new_times=[]
    for i in range(data.shape[0]):
        user=users[i]
        movie=movies[i]
        timestamp=times[i]
        if not isinstance(timestamp,str):
            continue
        timestamp=time.strptime(times[i],"%Y-%m-%d")
        timestamp=time.mktime(timestamp)
        new_users.append(user)
        new_movies.append(movie)
        new_times.append(timestamp)
        if i%100==0:
            print i
    df=pd.DataFrame()
    df['userId']=new_users
    df['movieId']=new_movies
    df['timestamp']=new_times
    df.to_csv('E:\\data\\dataset_timestamp.csv',index=False)
#run0()
def run1():
    data=pd.read_csv('E:\\data\\dataset_timestamp.csv')
    users=list(data['userId'])
    movies=list(data['movieId'])
    times=list(data['timestamp'])
    usertime={}
    usercnt={}
    for i in range(data.shape[0]):
        user=users[i]
        movie=movies[i]
        timestamp=times[i]
        if not usertime.has_key(user):
            usertime[user]=set()
        usertime[user].add(timestamp)
        if not usercnt.has_key(user):
            usercnt[user]=0
        usercnt[user]+=1
        if i%1000000==0:
            print i
    print len(usertime)
    #for user in usertime:
    #    print len(usertime[user])
    
    moviecnt={}
    rmuser=set()
    for i in range(data.shape[0]):
        user=users[i]
        movie=movies[i]
        #timestamp=times[i]
        if len(usertime[user])<30 or len(usertime[user])>500 or usercnt[user]>500:
            rmuser.add(user)
            continue
        #new_user.append(user)
        #new_movie.append(movie)
        #new_time.append(timestamp)
        if not moviecnt.has_key(movie):
            moviecnt[movie]=0
        moviecnt[movie]+=1
    
    
    for i in range(data.shape[0]):
        user=users[i]
        movie=movies[i]
        if not moviecnt.has_key(movie):
            continue
        if moviecnt[movie]<=1:
            rmuser.add(user)
    new_user=[]
    new_movie=[]
    new_time=[]
    for i in range(data.shape[0]):
        user=users[i]
        movie=movies[i]
        timestamp=times[i]
        if user in rmuser:
            continue
        new_user.append(user)
        new_movie.append(movie)
        new_time.append(timestamp)
    print len(set(new_user)),len(set(new_movie)),len(new_user)
        
            
            
    df=pd.DataFrame()
    df['userId']=new_user
    df['movieId']=new_movie
    df['timestamp']=new_time
    df.to_csv('E:\\data\\dataset_timestamp2.csv',index=False)
    
#run1()
def run2():
    data=pd.read_csv('E:\\data\\dataset_timestamp3.csv')
    #print data
    print data.shape
    print len(set(data['userId'])),len(set(data['movieId']))
#run2()
        
def run():
    t=time.strptime("2015-01-01","%Y-%m-%d")
    print type(time.mktime(t))
    
    data=pd.read_csv('E:\\data\\dataset.csv')
    
    

    
    users=data['UserID']
    movies=data['MovieID']
    times=data['Date']
    
    
    mintime={}
    maxtime={}
    usercnt={}
    rmuser=set()
    
    minusertime={}
    maxusertime={}
    
    userdate={}
    for i in range(data.shape[0]):
        user=users[i]
        movie=movies[i]
        timestamp=times[i]
        #timestamp=time.strptime(times[i],"%Y-%m-%d")
        #timestamp=time.mktime(timestamp)
        #times[i]=timestamp
        
        """if not mintime.has_key(user):
            mintime[user]=timestamp
        if not maxtime.has_key(user):
            maxtime[user]=timestamp"""
            
        
        if not usercnt.has_key(user):
            usercnt[user]=0
        usercnt[user]+=1
        
        if not minusertime.has_key(user):
            minusertime[user]=timestamp
        if not maxusertime.has_key(user):
            maxusertime[user]=timestamp
        if time<minusertime[user]:
            minusertime[user]=timestamp
        if time>maxusertime[user]:
            maxusertime[user]=timestamp
        if not userdate.has_key(user):
            userdate[user]=set()
        userdate[user].add(timestamp)
        
        #if usercnt[user]>1000:
            #rmuser.add(user)
            #continue
    rmuser=set()
    for user in minusertime:
        maxtime=maxusertime[user]
        mintime=minusertime[user]
        #print maxtime
        if not isinstance(maxtime,str) or not isinstance(mintime,str):
            rmuser.add(user)
            continue
        
        
        maxstamp=time.strptime(maxtime,"%Y-%m-%d")
        maxstamp=time.mktime(maxstamp)
        minstamp=time.strptime(mintime,"%Y-%m-%d")
        minstamp=time.mktime(minstamp)
        
        gap=maxstamp-minstamp
        if gap<100*24*60*60:
            rmuser.add(user)
        if gap>1000*24*60*60:
            rmuser.add(user)
        if len(userdate[user])<20:
            rmuser.add(user)
        
        
    print len(rmuser)
    
    new_user=[]
    new_movie=[]
    new_time=[]
    for i in range(data.shape[0]):
        user=users[i]
        movie=movies[i]
        timestamp=times[i]
        if usercnt[user]>800 or usercnt[user]<100:
            continue
        if user in rmuser:
            continue
        new_user.append(user)
        new_movie.append(movie)
        new_time.append(timestamp)
    df=pd.DataFrame()
    df['userId']=new_user
    df['movieId']=new_movie
    df['timestamp']=new_time
    df.to_csv('E:\\data\\dataset_douban.csv',index=False)
        
#run()
def sampling():
    #print np.random.randint(0,10,5)
    #return
    #print np.random.randint(0,10,10)
    #print random.sample(range(200),10)
    #return
    
    data=pd.read_csv('E:\\data\\dataset_douban.csv')
    
    userset=set(data['userId'])
    movieset=set(data['movieId'])
    print len(userset),len(movieset)
    print data.shape
    
    userlist=list(set(data['userId']))
    
    #userinx=np.random.randint(0,len(userlist),200)
    userinx=random.sample(range(len(userlist)),200)
    
    userset=set()
    for inx in userinx:
        userset.add(userlist[inx])
    
    
    users=data['userId']
    movies=data['movieId']
    times=data['timestamp']
    
    new_user=[]
    new_movie=[]
    new_time=[]
    
    for i in range(data.shape[0]):
        user=users[i]
        movie=movies[i]
        timestamp=times[i]
        
        if i%10000==0:
            print i
            
        
        if not user in userset:
            continue
    
        new_user.append(user)
        new_movie.append(movie)
        new_time.append(timestamp)
        
    df=pd.DataFrame()
    df['userId']=new_user
    df['movieId']=new_movie
    df['timestamp']=new_time
    df.to_csv('E:\\data\\dataset_douban2.csv',index=False)    
#sampling()
def timeprocess():
    #data=pd.read_csv('E:\\data\\dataset_douban2.csv')
    data=pd.read_csv('E:\\data\\dataset_douban.csv')
    
    print data
    users=data['userId']
    movies=data['movieId']
    times=data['timestamp']
    
    new_user=[]
    new_movie=[]
    new_time=[]
    for i in range(data.shape[0]):
        user=users[i]
        movie=movies[i]
        timestamp=time.strptime(times[i],"%Y-%m-%d")
        timestamp=time.mktime(timestamp)
        times[i]=timestamp
        new_user.append(user)
        new_movie.append(movie)
        new_time.append(timestamp)
        if i%100==0:
            print i
    df=pd.DataFrame()
    df['userId']=new_user
    df['movieId']=new_movie
    df['timestamp']=new_time
    #df.to_csv('E:\\data\\dataset_douban3.csv',index=False)
    df.to_csv('E:\\data\\dataset_douban_timestamp.csv',index=False)

#timeprocess()

def test():
    data=pd.read_csv('E:\\data\\dataset_douban3.csv')
    mintime={}
    maxtime={}
    for index,row in data.iterrows():
        user=row['userId']
        movie=row['movieId']
        timestamp=float(row['timestamp'])
        if not mintime.has_key(user):
            mintime[user]=timestamp
        if not maxtime.has_key(user):
            maxtime[user]=timestamp
        if timestamp<mintime[user]:
            mintime[user]=timestamp
        if timestamp>maxtime[user]:
            maxtime[user]=timestamp
    for user in mintime:
        gap=maxtime[user]-mintime[user]
        print user,gap/(24*60*60)
        
        
#test()
def run3():
    data=pd.read_csv('E:\\data\\dataset_douban3.csv')
    print data.shape
    print len(set(data['movieId'])),len(set(data['userId']))
    
#run3()
    
