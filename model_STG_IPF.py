import pandas as pd
import numpy as np


def clustering(data,rate=0.5):
    gaps=[(0,0)]
    for i in range(1,len(data)):
        gaps.append((i,data[i-1][1]-data[i][1]))
    
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

def loadData():
    #data=pd.read_csv('E:\\data\\ratings4.csv')
    #data=pd.read_csv('E:\\data\\dataset_douban3.csv')
    #data=pd.read_csv('E:\\dataset\\hetrec2011-delicious-2K\\rating.csv')
    data=pd.read_csv('E:\\data\\data_douban2.csv')
    #data=pd.read_csv('E:\\data\\movielens500.csv')
    user_movie={}
    for index,row in data.iterrows():
        user=row['userId']
        movie=row['movieId']
        time=row['timestamp']
        if not isinstance(time,(float,np.int64)):
            print type(time)
            return
        if not user_movie.has_key(user):
            user_movie[user]=set()
        user_movie[user].add((movie,time))
    
    trainset={}
    testset={}
    window=10*24*60*60
    
    
    item_user={}
    item_session={}
    out={}
    
    session_cnt={}
    
    for user in user_movie:
        ret=sorted(user_movie[user],key=lambda x:x[1],reverse=True)
        testset[user]=ret[0][0]
        trainset[user]=set()
        begin=ret[1][1]
        end=begin-window
        session_number=0
        username='u:'+str(user)
        #cluster=clustering(ret[1:])
        for index,(movie,time) in enumerate(ret[1:]):
            itemname='i:'+str(movie)
            if time<=end:
                session_number+=1
                begin=time
                end=begin-window
            #if index in cluster:
            #    session_number+=1
            
            sessionname='s:'+str(user)+'_'+str(session_number)
            
            if not item_user.has_key(itemname):
                item_user[itemname]=set()
            item_user[itemname].add(username)

            if not item_session.has_key(itemname):
                item_session[itemname]=set()
            item_session[itemname].add(sessionname)
            
            if not out.has_key(username):
                out[username]=set()
            out[username].add(itemname)
            
            if not out.has_key(itemname):
                out[itemname]=set()
            out[itemname].add(username)
            out[itemname].add(sessionname)
            
            if not out.has_key(sessionname):
                out[sessionname]=set()
            out[sessionname].add(itemname)
        session_cnt[user]=session_number+1
                
    return testset,out,item_user,item_session,session_cnt
#loadData()
    
def IPF(out,item_user,item_session,vuname,vsname,alpha=0.5,beta=0.1,gamma=0.5):
    
    Q=[]
    V=set()
    distance={}
    rank={}
    Q.append(vuname)
    Q.append(vsname)
    distance[vuname]=0
    distance[vsname]=0
    rank[vuname]=beta
    rank[vsname]=1-beta
    while len(Q)>0:
        vname=Q[0]
        Q.pop(0)
        if vname in V:
            continue
        if distance[vname]>3:
            break
        V.add(vname)
        
        
        for ovname in out[vname]:
            
            if not ovname in V:
                Q.append(ovname)
                distance[ovname]=distance[vname]+1
            
            if vname[0]=='i':
                if ovname[0]=='u':
                    #decay=pow(float(gamma)/(gamma*len(item_user[vname])+len(item_user[vname])),alpha)#bug... 2016.12.16 0:41 find
                    decay=pow(float(gamma)/(gamma*len(item_user[vname])+len(item_session[vname])),alpha)
                elif ovname[0]=='s':
                    #decay=pow(1.0/(gamma*len(item_user[vname])+len(item_user[vname])),alpha)#bug...
                    decay=pow(1.0/(gamma*len(item_user[vname])+len(item_session[vname])),alpha)
                else:
                    print '!!!'
                    return
            elif vname[0]=='u' or vname[0]=='s':
                if ovname[0]=='i':
                    decay=pow(1.0/len(out[vname]),alpha)
                else:
                    print '!!!!'
                    return
            else:
                print '!!!!!'
                return
                
            if distance[vname]<distance[ovname]:
                if not rank.has_key(ovname):
                    rank[ovname]=0.0
                rank[ovname]+=rank[vname]*decay
    rank=sorted(rank.iteritems(),key=lambda x:x[1],reverse=True)
    ret=[]
    for name,score in rank:
        if name[0]=='i':
            if not name in out[vuname]:
                ret.append((float(name[2:]),score))
    return ret
"""def search(testset,out,item_user,item_session,alpha,beta,gamma):
    hit_cnt=0.0
    
    for user in testset:
        #print user
        real=testset[user]
        username='u:'+str(user)
        sessionname='s:'+str(user)+'_0'
        ret=IPF(out,item_user,item_session,username,sessionname,alpha,beta,gamma)
        for index,(item,score) in enumerate(ret):
            if item==real:
                if score>=ret[9][1]:
                    hit_cnt+=1
                break
            if index>30:
                break
    return hit_cnt
    
def grid_search():
    testset,out,item_user,item_session,session_cnt=loadData()
    alphas=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]
    betas=[0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
    gammas=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0]
    print 'searching...'
    for alpha in alphas:
        for beta in betas:
            for gamma in gammas:
                hit_cnt=search(testset,out,item_user,item_session,alpha,beta,gamma)
                print 'hit count:',hit_cnt,alpha,beta,gamma
"""    
        
def run():
    testset,out,item_user,item_session,session_cnt=loadData()
    hit_cnt=0.0
    total=0
    
    for user in testset:
        #print user
        real=testset[user]
        username='u:'+str(user)
        sessionname='s:'+str(user)+'_0'
        ret=IPF(out,item_user,item_session,username,sessionname)
        #for index,(item,score) in enumerate(ret):
        for item,score in ret[:10]:
            #if item==real:
            if item==real:
                hit_cnt+=1
                
                #break
        total+=1
        print 'index:',hit_cnt,total,session_cnt[user],'window 3'

#run()
def runtime():
    import time    
    start=time.clock()
    run()
    end=time.clock()
    print end-start
runtime()
        
def datatest():
    data=pd.read_csv('E:\\data\\data_douban2.csv')
    print data
#datatest()