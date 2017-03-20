import matplotlib.pyplot as plt

def draw_ClusteringIPF():
    x=[0,0.001,0.1,0.5]
    y=[31,32,18,20]
    total=206.0
    for i in range(len(y)):
        x[i]=x[i]*24*60*60
        y[i]=y[i]/total
        
    ax=plt.gca()
    ax.set_xlabel('distance threshold')
    ax.set_ylabel('hit ratio')    
    plt.plot(x,y)
#draw_ClusteringIPF()

def draw_usercf():
    #x=[10,11,12,13,14,15,16,17,18,19,20]
    x=[5,6,7,8,9,10,11,12,13,14,15]
    #y1=[45,55,61,68,74,77,87,88,94,102,108]
    #y2=[7,9,11,13,14,14,15,15,16,17,18]
    y1=[24,26,32,36,38,41,42,49,50,52,55]
    y2=[2,2,2,3,4,4,5,5,5,5,5]
    for i in range(len(y1)):
        y1[i]=y1[i]/500.0
        y2[i]=y2[i]/200.0
        
    ax=plt.gca()
    ax.set_xlabel('N')
    ax.set_ylabel('hit ratio')    
    plt.plot(x,y1,label='MovieLens')
    plt.plot(x,y2,label='Douban')
    plt.legend(loc='upper left')
    
#draw_usercf()
    
def draw_ipf():
    #x=[0.0001,0.001,0.01,0.1,0.5,1,2,3]
    #y=[15,21,20,21,19,17,14,15]
    x=[0.1,1,2,3,4,5]
    y=[59,54,55,54,53,54]
    
    #douban
    #x=[3,5,7,10,11,12,13,14]
    #y=[2,5,5,11,14,17,13,13]
    total=1000.0
    for i in range(len(y)):
        x[i]=x[i]
        y[i]=y[i]/total
        
    ax=plt.gca()
    ax.set_xlabel('window (days)')
    ax.set_ylabel('hit ratio')    
    plt.plot(x,y)
#draw_ipf()
    
def draw_ipf_id_on_ml():
    #interest decay
    x1=[0.0001,0.001,0.01]
    y1=[99,99,88]
    
    #ipf
    x2=[0.0001,0.0005,0.001,0.005,0.01]
    y2=[85,95,99,79,72]
    
    plt.plot(x1,y1)
    plt.plot(x2,y2)
#draw_ipf_id_on_ml()
    

    
def draw_interestdecay():
    
    #movielens
    #x=[0.05,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]
    #y=[70,71,69,70,66,67,65,65,64,67,62]
    
    
    x1=[0.001,0.3,0.5,1,4,5,10,15,20,25,30]
    y1=[99,70,67,62,64,61,60,61,61,60,58]
    
    #douban
    #x=[1,10,20,30,40,50,60,70,80,90,100]
    #y=[16,18,19,24,22,19,22,19,18,20,18]
    x2=[1,5,10,15,20,25,30]
    y2=[70,99,115,124,119,119,120]
    for i in range(len(y1)):
        y1[i]=y1[i]/1000.0
    for i in range(len(y2)):
        y2[i]=y2[i]/1000.0
        
    ax=plt.gca()
    ax.set_xlabel('window (days)')
    ax.set_ylabel('hit ratio')    
    plt.plot(x1,y1,label='MovieLens',color='b')
    plt.plot(x2,y2,label='Douban',color='g')
    plt.legend(loc="upper left")
    
#draw_interestdecay()
    
def draw_greedyinterestdecay():
    
    ax=plt.gca()
    ax.set_xlabel('rate')
    ax.set_ylabel('hit ratio')
    total=1000.0
    #movielens
    #x=[0.1,1,2,3,4,5,6,7]
    #y=[86,86,80,85,85,83,77,77]
    #total=1000.0
    
    x=[2,3,4,5,6,7,8,9,10]
    y=[80,85,85,83,77,77,75,70,71]
    
    
    for i in range(len(y)):
        y[i]=y[i]/1000.0
    plt.plot(x,y,color='b',label='MovieLens')
    
    #douban
    #x=[0.5,1,2,3,4,5,6]
    #y=[12,17,20,25,23,20,13]
    x=[1,2,3,4]
    y=[96,102,111,113]
    
    for i in range(len(y)):
        #x[i]=x[i]*24*60*60
        y[i]=y[i]/1000.0
        
    plt.plot(x,y,color='g',label='Douban')
    plt.legend(loc='upper right')
    
#draw_greedyinterestdecay()