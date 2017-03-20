import pandas as pd
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def draw_horizontal_cluster():
    data=pd.read_csv('E:\\data\\ratings2.csv')
    user_movie={}
    #plt.figure(1)
    #plt.subplot(211)
    #plt.scatter([1,2,3],[1,1,2])
    for index,row in data.iterrows():
        user=row['userId']
        movie=row['movieId']
        time=row['timestamp']
        if not isinstance(time,float):
            print type(time)
            return
        if not user_movie.has_key(user):
            user_movie[user]=set()
        user_movie[user].add((movie,time))
        #if abs(time-986242886)<=24*60*60*3:
        #    print user
    for user in user_movie:
        print user,len(user_movie[user])
        
    
    x=[]
    y=[]
        
    ret=sorted(user_movie[452],key=lambda x:x[1],reverse=True)
    for movie,time in ret:
        x.append(time)
        y.append(2)
    plt.figure(figsize=(8,4))
    ax=plt.gca()
    ax.set_xlabel('time')
    ax.set_xticklabels([])
    ax.set_yticks([])
    
    plt.scatter(x,y,s=30,marker='+',color='b',label='user 452')
    x=[]
    y=[]
    #print user_movie[656]
    ret=sorted(user_movie[472],key=lambda x:x[1],reverse=True)
    for movie,time in ret:
        x.append(time)
        y.append(2.5)
    plt.scatter(x,y,s=30,marker='+',color='g',label='user 472')
    
    x=[]
    y=[]
    
        
    ret=sorted(user_movie[509],key=lambda x:x[1],reverse=True)
    for movie,time in ret:
        x.append(time)
        y.append(3)
    #plt.plot(x,y)
    plt.scatter(x,y,s=30,marker='+',color='r',label='user 509')
    plt.legend(loc='upper right')
    return
    
    x=[]
    y=[]
    ret=sorted(user_movie[480],key=lambda x:x[1],reverse=True)
    for movie,time in ret:
        x.append(time)
        y.append(4)
    #plt.plot(x,y)
    plt.scatter(x,y,s=30,marker='+',color='y')
    
draw_horizontal_cluster()