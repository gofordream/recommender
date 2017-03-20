import pandas as pd
import random

def run():
    raw_data=pd.read_csv('E:\\dataset\\ml-1m\\ratings.dat',sep='::',names=['user','movie','rating','time'])
    print len(set(raw_data['user'])),len(set(raw_data['movie']))
    return
    mindict={}
    maxdict={}
    usercntdict={}
    rmset=set()
    users =list(raw_data['user'])
    movies=list(raw_data['movie'])
    times =list(raw_data['time'])
    userinx=random.sample(range(raw_data.shape[0]),1000)
    for i in range(raw_data.shape[0]):
        user=users[i]
        movie=movies[i]
        time=times[i]
        
        if not mindict.has_key(user) or time<mindict[user]:
            mindict[user]=time
        if not maxdict.has_key(user) or time>maxdict[user]:
            maxdict[user]=time
        if not usercntdict.has_key(user):
            usercntdict[user]=0
        usercntdict[user]+=1
        
    
    addset=set()
    for user in mindict:
        gap=maxdict[user]-mindict[user]
        if gap<100*24*60*60 or gap>600*24*60*60:
            rmset.add(user)
        if usercntdict[user]>600:
            rmset.add(user)
            
        
    print len(rmset)
    
    
    new_user=[]
    new_movie=[]
    new_time=[]
    
    for i in range(raw_data.shape[0]):
        user=users[i]
        movie=movies[i]
        time=times[i]
        #if user in rmset:
        if not user in addset:
            continue
        new_user.append(user)
        new_movie.append(movie)
        new_time.append(time)
    df=pd.DataFrame()
    df['userId']=new_user
    df['movieId']=new_movie
    df['timestamp']=new_time
    df.to_csv('E:\\data\\ratings3.csv',index=False)
#run()
def sampling():
    
    raw_data=pd.read_csv('E:\\dataset\\ml-1m\\ratings.dat',sep='::',names=['user','movie','rating','time'])
    print len(set(raw_data['user'])),len(set(raw_data['movie']))
    
    
    users=list(raw_data['user'])    
    times=list(raw_data['time'])
    mintime={}
    maxtime={}
    
    for i in range(raw_data.shape[0]):
        user=users[i]
        timestamp=times[i]
        if not mintime.has_key(user):
            mintime[user]=timestamp
        if not maxtime.has_key(user):
            maxtime[user]=timestamp
        if timestamp<mintime[user]:
            mintime[user]=timestamp
        if timestamp>maxtime[user]:
            maxtime[user]=timestamp
        
    userlist=[]
    for user in mintime:
        gap=maxtime[user]-mintime[user]
        #if gap>=0.01*24*60*60:
        #    userlist.append(user)
        userlist.append(user)
    print len(userlist)
    #return
        
    
    #userlist=list(set(raw_data['user']))
    userinx=random.sample(range(len(userlist)),500)
    userset=set()
    for i in userinx:
        userset.add(userlist[i])
    
    
    users=list(raw_data['user'])
    movies=list(raw_data['movie'])
    times=list(raw_data['time'])
    new_user=[]
    new_movie=[]
    new_time=[]
    for i in range(raw_data.shape[0]):
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
    df.to_csv('E:\\data\\movielens500.csv',index=False)
    
    print df.shape
    print len(set(new_user)),len(set(new_movie))

sampling()  
def process():
    data=pd.read_csv('E:\\data\\ratings4.csv')
    userset1=set([4109, 16, 27, 2086, 4189, 2185, 171, 2226, 4300, 231, 2287, 2295, 2302, 744, 2438, 395, 4509, 418, 2513, 2469, 522, 558, 2651, 4721, 640, 4741, 2711, 674, 2763, 2770, 766, 2833, 2853, 811, 833, 917, 2126, 2984, 5036, 3018, 5116, 3161, 2575, 1135, 1157, 1165, 1822, 5339, 5352, 1368, 3460, 3465, 5541, 3496, 1457, 1534, 5641, 1599, 3669, 1639, 5754, 3718, 3767, 5902, 5911, 1817, 3870, 4562, 5962, 6003, 1929])
    userset2=set([4097, 4109, 27, 2086, 2096, 4184, 4189, 4230, 2185, 4259, 171, 4300, 231, 1849, 2287, 2295, 2302, 2333, 361, 2438, 395, 4509, 414, 418, 4519, 4174, 1719, 4534, 441, 2513, 2469, 4638, 558, 573, 583, 4686, 782, 2651, 4721, 640, 4741, 2711, 674, 2770, 761, 766, 2833, 811, 833, 900, 2954, 917, 2126, 2984, 5036, 1864, 3018, 847, 5116, 3161, 5877, 1157, 1165, 3269, 5281, 1822, 5339, 3302, 1270, 5437, 5456, 3460, 1439, 5541, 1457, 5602, 1534, 5641, 3623, 3654, 1623, 5646, 1639, 5754, 3718, 3767, 5902, 3870, 3894, 5962, 3946, 1906, 6003, 1919, 6020, 1929, 6034, 1986, 2722])
    userset3=set([4109, 16, 27, 2086, 4189, 2185, 171, 4300, 231, 2287, 2295, 2302, 744, 2438, 395, 4509, 418, 4519, 441, 2513, 2469, 522, 558, 573, 2651, 4721, 640, 4741, 2711, 674, 2763, 2770, 761, 766, 2833, 811, 833, 2954, 917, 2126, 2984, 5036, 1864, 3018, 847, 5116, 3161, 2575, 1157, 1165, 3269, 1822, 5339, 3302, 5352, 5437, 5456, 3460, 3465, 5541, 3496, 1457, 1534, 5641, 3623, 1599, 3654, 3669, 5646, 1639, 5754, 3718, 3767, 3834, 5902, 5911, 1817, 3870, 4562, 3894, 5962, 3946, 6003, 6020, 1929, 2722])
    rmuser=userset2.difference(userset3)
    print len(rmuser)
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
        if user in rmuser:
            continue
        new_user.append(user)
        new_movie.append(movie)
        new_time.append(timestamp)
    df=pd.DataFrame()
    df['userId']=new_user
    df['movieId']=new_movie
    df['timestamp']=new_time
    df.to_csv('E:\\data\\ratings5.csv',index=False)
#process()
#print set([1,2,3]).difference(set([1,5,6]))
    
    
def test():
    data=pd.read_csv('E:\\data\\ratings3.csv')
    userset=set()    
    movieset=set()
    for index,row in data.iterrows():
        user=row['userId']
        movie=row['movieId']
        userset.add(user)
        movieset.add(movie)
    print len(userset),len(movieset)
    print data.shape
    print 1-float(index)/len(userset)/len(movieset)
#test()
   
