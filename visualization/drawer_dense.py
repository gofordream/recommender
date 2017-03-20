import pandas as pd
import matplotlib.pyplot as plt



def clustering(data,rate=2.0):
    gaps=[(0,0)]
    for i in range(1,len(data)):
        #gaps.append((i,data[i-1][1]-data[i][1]))
        gaps.append((i,data[i-1]-data[i]))
    
    gaps=sorted(gaps,key=lambda x:x[1],reverse=True)
    
    if gaps[0][1]==0:
        print '!!!!'
        return []
        
    sessions=[gaps[0][0]]
    
    acc=0.
    for movie,time in gaps:
        acc+=time
    mean=float(acc)/(len(gaps)-1)
    
    
    
    for i in range(1,len(gaps)):
        if gaps[i][1]<mean*rate:
        #if gaps[i][1]<gaps[0][1]*0.05:
        #if gaps[i][1]<3*24*60*60:
            break
        
        if gaps[i][1]==0:
            print '!!!!!!!!!!!'
            print gaps[i][1],gaps[0][1]
            return
        sessions.append(gaps[i][0])
    return sessions

def draw():
    plt.figure(figsize=(8,4))
    ax=plt.gca()
    ax.set_xlabel('time')
    #ax.set_xticks([])
    ax.set_xticklabels([])
    ax.set_yticks([])
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
    
    x=[]
    y=[]
        
    ret=sorted(user_movie[452],key=lambda x:x[1],reverse=True)
    for movie,time in ret:
        x.append(time)
        y.append(1)
    #plt.plot(x,y)
    plt.scatter(x,y,s=20,marker='+',color='b',label='user 452')
    clus=clustering(x,50)
    #print len(clus),len(x)
    
    for inx in clus:
        plt.scatter(x[inx],1,marker='|',s=1000,color='r')
        #break
    
    
    x=[]
    y=[]
        
    ret=sorted(user_movie[472],key=lambda x:x[1],reverse=True)
    for movie,time in ret:
        x.append(time)
        y.append(2)
    #plt.plot(x,y)
    plt.scatter(x,y,s=20,marker='+',color='g',label='user 472')
    clus=clustering(x,50)
    for inx in clus:
        plt.scatter(x[inx],2,marker='|',s=1000,color='r')
    
    x=[]
    y=[]
        
    ret=sorted(user_movie[509],key=lambda x:x[1],reverse=True)
    for movie,time in ret:
        x.append(time)
        y.append(3)
    #plt.plot(x,y)
    plt.scatter(x,y,s=20,marker='+',color='r',label='user 509')
    clus=clustering(x,50)
    for inx in clus:
        plt.scatter(x[inx],3,marker='|',s=1000,color='r')
    plt.legend(loc='upper right')
draw()