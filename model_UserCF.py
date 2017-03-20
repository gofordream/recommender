
import pandas as pd
from math import sqrt
import numpy as np
#def Item_CF():

def sim_cos(set1,set2):
    common=set1.intersection(set2)
    return len(common)/sqrt(len(set1)*len(set2))
def sim_jaccard(set1,set2):
    common=set1.intersection(set2)
    union=set1.union(set2)
    return float(len(common))/len(union)
    
    
def loadData():
    #data=pd.read_csv('E:\\data\\ratings4.csv')
    #data=pd.read_csv('E:\\data\\dataset_douban3.csv')
    #data=pd.read_csv('E:\\data\\data_douban2.csv')
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
    
    trainmovie=set()
    testmovie=set()
    for user in user_movie:
        ret=sorted(user_movie[user],key=lambda x:x[1],reverse=True)
        testset[user]=ret[0][0]
        trainset[user]=set()
        testmovie.add(ret[0][0])
        for movie,time in ret[1:]:
            trainmovie.add(movie)
            trainset[user].add(movie)
            
    print len(trainmovie),len(testmovie)
    
    
    return trainset,testset
    
#loadData()
    
def User_CF(K,N=14):
    trainset,testset=loadData()
    hit_cnt=0
    for user in testset:
        sim_user=[]
        for other in trainset:
            if user==other:
                continue
            mset_user =trainset[user]
            mset_other=trainset[other]
            sim=sim_cos(mset_user,mset_other)
            #sim=sim_jaccard(mset_user,mset_other)
            sim_user.append((other,sim))
        sim_user=sorted(sim_user,key=lambda x:x[1],reverse=True)[:K]
        rec_list={}
        for other,sim in sim_user:
            for movie in trainset[other]:
                if movie in trainset[user]:
                    continue
                if not rec_list.has_key(movie):
                    rec_list[movie]=0.
                rec_list[movie]+=sim
        rec_list=sorted(rec_list.iteritems(),key=lambda x:x[1],reverse=True)[:N]
        real=testset[user]
        for movie,score in rec_list:
            if real==movie:
                hit_cnt+=1
    print hit_cnt,len(testset),float(hit_cnt)/len(testset)
    
#User_CF(10)
    
import time    
start=time.clock()
User_CF(10)
end=time.clock()
print end-start
    
#for i in range(50):
#    print 10+i*10
#    User_CF(10+i*10)
