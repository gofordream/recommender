
import pandas as pd

def split():
    data=pd.read_csv('E:\\data\\dataset.csv')
    user=list(data['UserID'])
    #movie=list(data['MovieID'])
    date=list(data['Date'])
    
    lasttime={}
    flag=[]
    #print data.loc[5931180:5931197]
    #print data.shape
    for i in range(data.shape[0]):
        u=str(user[i])
        d=str(date[i])
        if len(d)<10:
            print d,'yyy',u,i
            flag.append(2)
            continue
        if not lasttime.has_key(u):
            lasttime[u]=d
            flag.append(1)
        else:
            flag.append(0)
        if d>lasttime[u]:
            print  'xxx'
            return
    data['flag']=flag
    trainset=data[data['flag']==0]
    testset=data[data['flag']==1]
    
    trainset=trainset.drop(['flag'],axis=1)
    testset=testset.drop(['flag'],axis=1)
            
    trainset.to_csv('E:\\data\\trainset.csv',index=False)
    testset.to_csv('E:\\data\\testset.csv',index=False)
        
#split()
