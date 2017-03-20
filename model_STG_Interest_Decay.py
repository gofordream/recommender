import pandas as pd
#from math import pow
import numpy as np
import math

def clustering(data,rate=2.0):
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
    #data=pd.read_csv('E:\\dataset\\hetrec2011-delicious-2k\\rating.csv')
    #data=pd.read_csv('E:\\data\\ratings3.csv')
    #data=pd.read_csv('E:\\data\\dataset_douban3.csv')
    #data=pd.read_csv('E:\\data\\douban_timestamp.csv')
    #data=pd.read_csv('E:\\data\\dataset_timestamp2.csv')
    #data=pd.read_csv('E:\\data\\ratings4.csv')
    #data=pd.read_csv('E:\\data\\dataset_timestamp3.csv')
    #data=pd.read_csv("E:\\data\\data_douban2.csv")
    data=pd.read_csv('E:\\data\\movielens500.csv')

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

    user_item={}
    item_session={}
    session_item={}
    session_cnt={}
    session_center={}
    
    
    for user in user_movie:
        ret=sorted(user_movie[user],key=lambda x:x[1],reverse=True)
        
        if len(ret)<=1:
            print user,ret
            return
        testset[user]=ret[0][0]
        trainset[user]=set()
        
        begin=ret[1][1]
        end=begin-window
        session_number=0
        if not user_item.has_key(user):
            user_item[user]=set()
            
        cluster=clustering(ret[1:])
        for index,(movie,time) in enumerate(ret[1:]):
            itemname='i:'+str(movie)
            user_item[user].add(itemname)
            #if time<=end:
            #    session_number+=1
            #    begin=time
            #    end=begin-window
            if index in cluster:
                session_number+=1
                
            sessionname='s:'+str(user)+'_'+str(session_number)
            if not session_center.has_key(sessionname):
                session_center[sessionname]=(time,1)
            else:
                center,size=session_center[sessionname]
                newc=(center*size+time)/(size+1)
                session_center[sessionname]=(newc,size+1)
                
        
            if not item_session.has_key(itemname):
                item_session[itemname]=set()
            item_session[itemname].add(sessionname)
            
            if not session_item.has_key(sessionname):
                session_item[sessionname]=set()
            session_item[sessionname].add(itemname)
           
        session_cnt[user]=session_number+1
                
    return testset,user_item,item_session,session_item,session_cnt,session_center

    
def IPF(items,item_session,session_item,vsnames,alpha=0.5,betas=[1.0]):
    Q=[]
    V=set()
    distance={}
    rank={}
    for index,vsname in enumerate(vsnames):
        Q.append(vsname)
        distance[vsname]=0
        rank[vsname]=betas[index]
    while len(Q)>0:
        vname=Q[0]
        Q.pop(0)
        if vname in V:
            continue
        if distance[vname]>3:
            break
        V.add(vname)
        
        if vname[0]=='i':
            for ovname in item_session[vname]:
                if not ovname in V:
                    Q.append(ovname)
                    distance[ovname]=distance[vname]+1
                decay=pow(1.0/len(item_session[vname]),alpha)
                if distance[vname]<distance[ovname]:
                    if not rank.has_key(ovname):
                        rank[ovname]=0.0
                    rank[ovname]+=rank[vname]*decay
        else:
            for ovname in session_item[vname]:
                if not ovname in V:
                    Q.append(ovname)
                    distance[ovname]=distance[vname]+1
                decay=pow(1.0/len(session_item[vname]),alpha)
                
                if distance[vname]<distance[ovname]:
                    if not rank.has_key(ovname):
                        rank[ovname]=0.0
                    rank[ovname]+=rank[vname]*decay
        
    rank=sorted(rank.iteritems(),key=lambda x:x[1],reverse=True)
    ret=[]
    for name,score in rank:
        if name[0]=='i':
            #if not name[0] in out[vuname]:
            if not name in items:
                ret.append((float(name[2:]),score))
    return ret
        
def run():
    #testset,out,item_user,item_session,session_cnt=loadData()
    testset,user_item,item_session,session_item,session_cnt,session_center=loadData()
    #ret=loadData()
    #print type(ret)
    #return
    hit_cnt=0.0
    total=0
    weights=[1,0.2,0.01]
    
    num_rec=0
    user_hit=[]
    for user in testset:
        real=testset[user]
        sessionname='s:'+str(user)+'_0'
        ret_acc={}
        session0='s:'+str(user)+'_0'
        center,size=session_center[session0]
        
        """for i in range(min(10000,session_cnt[user])):
        #for i in range(session_cnt[user]):
            sessionname='s:'+str(user)+'_'+str(i)
            time,size=session_center[sessionname]
            #print sessionname,center
            #weight=pow(0.3,i)
            #weight=weights[i]
            weight=pow(math.e,-(center-time)/(20.0*24*60*60))
            if weight<0.01:
                break
            #print -(center-time)/(1*24*60*60)
            
            ret=IPF(user_item[user],item_session,session_item,[sessionname],betas=[weight])
            for item,score in ret:
                if not ret_acc.has_key(item):
                    ret_acc[item]=0.
                ret_acc[item]+=score"""
            
        sessions=[]
        betas=[]
        for i in range(min(100000,session_cnt[user])):
            sessionname='s:'+str(user)+'_'+str(i)
            time,size=session_center[sessionname]
            weight=pow(math.e,-(center-time)/(10.0*24*60*60))
            #if weight<0.01:
            #    break
            sessions.append(sessionname)
            betas.append(weight)
            if i>0 and betas[i]==betas[i-1]:
                print user,'.....'
                return
        ret=IPF(user_item[user],item_session,session_item,sessions,betas=betas)
        for item,score in ret:
            if not ret_acc.has_key(item):
                ret_acc[item]=0.
            ret_acc[item]+=score
                
        
            
        ret=sorted(ret_acc.iteritems(),key=lambda x:x[1],reverse=True)
        if len(ret)==0:
            print '!!!!!!!!!!!!!'
            continue
        tscore=0.
        for item,score in ret:
            tscore+=score
        new_ret=[]
        for i in range(len(ret)):
            new_ret.append((ret[i][0],ret[i][1]/tscore))
        
        #for index,(item,score) in enumerate(new_ret[:10]):
        for item,score in new_ret[:10]:
            #if score<0.02:
            #    break
            num_rec+=1
            if item==real:
                hit_cnt+=1
                #if total%20==0:
                #print score,item,total
                #print new_ret,len(new_ret)
                #return
                #if score>=ret[9][1] or index <=9:
                #    hit_cnt+=1
                user_hit.append(user)
                break
            #if index>30:
            #    break
        total+=1
        #print session_cnt[user],hit_cnt,total,num_rec
        print 'alpha 0.6 hit:',hit_cnt,'total:',total,'session_cnt:',session_cnt[user],'valid_sessions:',len(sessions)
    #print hit_cnt,total
    #print user_hit


import time    
start=time.clock()
run()
end=time.clock()
print end-start

