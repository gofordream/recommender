import pandas as pd
import matplotlib.pyplot as plt
def clustering():
    data=pd.read_csv('E:\\data\\ratings.csv')
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
    trainset={}
    testset={}
    
    x=[0]
    y=[0]
        
    gap=[]
    userid=131
    userid=333
    userid=350
    ret=sorted(user_movie[userid],key=lambda x:x[1],reverse=True)
    for i in range(1,len(ret)-1):
        g=ret[i-1][1]-ret[i][1]
        #g2=ret[i]-ret[i+1][1]
        x.append(i)
        y.append(g)

    ax=plt.gca()
    ax.set_xlabel('i')
    ax.set_ylabel('gap')
    plt.plot(x,y,label='user 350')
    
    x=[0]
    y=[0]
    #userid=341
    userid=348
    ret=sorted(user_movie[userid],key=lambda x:x[1],reverse=True)
    for i in range(1,len(ret)-1):
        g=ret[i-1][1]-ret[i][1]
        x.append(i)
        y.append(g)
    #plt.plot(x,y,label='user 348')
    plt.legend(loc='upper right')
    #for movie,time in ret:
    #    x.append(time)
    #    y.append(1)
    
    #plt.scatter(x,y,s=20,marker='.',color='r')
       
    return
    for index,user in enumerate(user_movie):
        ret=sorted(user_movie[user],key=lambda x:x[1],reverse=True)
        gap=[]
        #print ret
        for i in range(1,len(ret)):
            gap.append(ret[i-1][1]-ret[i][1])
            x.append(i)
            y.append(ret[i-1][1]-ret[i][1])
        #plt.scatter(x,y,s=20,marker='.',color='r')
        plt.plot(x,y)
        print gap
        if index>3:
            return
        return
        testset[user]=ret[0][0]
        trainset[user]=set()
clustering()