import matplotlib.pyplot as plt
#import seaborn as sns
import numpy as np
import math
    
def draw_interestdecay():
    x=[1,5,10,15,20,25,30,35,40,45]
    y1=[37,37,38,37,35,33,35,35,34,34]
    y2=[9,15,16,18,16,15,18,20,21,20]
    for i in range(len(y1)):
        y1[i]=y1[i]/500.0
    for i in range(len(y2)):
        y2[i]=y2[i]/200.0
    ax=plt.gca()
    ax.set_xlabel('window (days)')
    ax.set_ylabel('hit ratio')    
    plt.plot(x,y1,label='MovieLens',color='b')
    plt.plot(x,y2,label='Douban',color='g')
    plt.legend(loc="upper left")
    #plt.plot(0,0.02)
    #plt.plot(0,0.13)
#draw_interestdecay()
    
def draw_greedy():
    x=[1,2,3,4,5,6,7,8,9,10]
    y2=[15,18,16,16,15,14,13,13,10,9]
    y1=[45,46,44,43,41,39,38,37,35,36]
    for i in range(len(y1)):
        y1[i]=y1[i]/500.0
    for i in range(len(y2)):
        y2[i]=y2[i]/200.0
    ax=plt.gca()
    ax.set_xlabel(r'$\alpha$')
    #plt.plot(x,y,label='$\lambda=10$')
    ax.set_ylabel('hit ratio')    
    plt.plot(x,y1,label='MovieLens',color='b')
    plt.plot(x,y2,label='Douban',color='g')
    plt.legend(loc="upper right")
    #plt.plot([1],[0.03])
    
#draw_greedy()
        

def draw_parameter():
    x=[0.1,0.2,0.5,0.6,0.8,0.9,1.0,1.2,1.5,]
    y1=[38,38,38,47,49,54,48,46,35]
    y2=[19,19,20,20,20,19,17,16,13]
    for i in range(len(y1)):
        y1[i]=y1[i]/500.0
    for i in range(len(y2)):
        y2[i]=y2[i]/200.0
    ax=plt.gca()
    #ax.set_xlabel('p')
    ax.set_xlabel(r'$\rho$')
    ax.set_ylabel('hit ratio')    
    plt.plot(x,y1,label='MovieLens',color='b')
    plt.plot(x,y2,label='Douban',color='g')
    plt.legend(loc="upper right")
#draw_parameter()
    
def draw_final():
    #fig=plt.figure(figsize=(6,4))
    ax=plt.gca()
    ax.set_xlabel('algorithms')
    ax.set_ylabel('hit ratio')
    ax.set_xticks(np.linspace(1.2,4.2,4))
    ax.set_xticklabels(['UserCF','IPF','IDSSTG','GIDSSTG'])
    hit_ml=[0.082,0.072,0.076,0.092]
    hit_db=[0.02,0.065,0.105,0.09]
    plt.bar([1,2,3,4],hit_db,width=0.4,color='#aaaadd',alpha=0.7)
    plt.plot([0.5,5],[0,0])
#draw_final()
def draw_final2():
    ax=plt.gca()
    ax.set_xlabel('algorithms')
    ax.set_ylabel('hit ratio')
    ax.set_xticks(np.linspace(0.3,3.3,4))
    ax.set_xticklabels(['UserCF','IPF','IDSSTG','GIDSSTG'])
    hit_ml=[0.082,0.072,0.076,0.092]
    hit_db=[0.02,0.065,0.105,0.09]
    #plt.bar([1,2,3,4],hit_db,width=0.4,color='#aaaadd',alpha=0.7)
    #plt.plot([0.5,5],[0,0])
    plt.bar(0,hit_db[0],width=0.5,color='r',alpha=0.7)
    plt.bar(1,hit_db[1],width=0.5,color='g',alpha=0.7)
    plt.bar(2,hit_db[2],width=0.5,color='b',alpha=0.7)
    plt.bar(3,hit_db[3],width=0.5,color='y',alpha=0.7)
    plt.plot([-0.2,3.7],[0,0])
#draw_final2()
def draw_final3():
    ax=plt.gca()
    ax.set_xlabel('algorithms')
    ax.set_ylabel('hit ratio')
    ax.set_xticks(np.linspace(1.3,4.3,4))
    ax.set_xticklabels(['UserCF','IPF','IDSSTG','GIDSSTG'])
    hit_ml=[0.082,0.072,0.076,0.092]
    hit_db=[0.02,0.065,0.105,0.09]
    plt.bar([1,2,3,4],hit_db,width=0.3,color='#aaaadd',alpha=0.6,label='Douban')
    plt.bar([1.3,2.3,3.3,4.3],hit_ml,width=0.3,color='#aaddaa',alpha=0.6,hatch='//',label='MovieLens')
    plt.plot([0.8,4.8],[0,0])
    plt.legend(loc="upper left")
#draw_final3()   
def draw_timefunction():

    x=[]
    y=[]
    y2=[]
    y3=[]
    y4=[]
    y5=[]
    for i in range(100):
        x.append(i)
        e=math.e
        value=pow(e,-i/10.0)
        y.append(value)
        y2.append(pow(e,-i/20.0))
        y3.append(pow(e,-i/30.0))
        y4.append(pow(e,-i/40.0))
        y5.append(pow(e,-i/50.0))
    
    ax=plt.gca()
    ax.set_xlabel('t (days)')
    ax.set_ylabel('f(t)')    
    plt.plot(x,y,label='$\lambda=10$')
    plt.plot(x,y2,label='$\lambda=20$')
    plt.plot(x,y3,label='$\lambda=30$')
    plt.plot(x,y4,label='$\lambda=40$')
    plt.plot(x,y5,label='$\lambda=50$')
    plt.legend(loc='upper right')
#draw_timefunction()

def draw_function2():
    x=[]
    y=[]
    y2=[]
    y3=[]
    y4=[]
    y5=[]
    i=0.0
    while i<=2:
        x.append(i)
        y.append(1/pow(3,i))
        y2.append(1/pow(4,i))
        y3.append(1/pow(5,i))
        y4.append(1/pow(6,i))
        y5.append(1/pow(7,i))
        
        i+=0.1
        
   
    
    ax=plt.gca()
    ax.set_xlabel(r'$\rho$')
    ax.set_ylabel(r'$\phi(v,V)$')    
    plt.plot(x,y,label='out(v)=3')
    plt.plot(x,y2,label='out(v)=4')
    plt.plot(x,y3,label='out(v)=5')
    plt.plot(x,y4,label='out(v)=6')
    plt.plot(x,y5,label='out(v)=7')
    plt.legend(loc='upper right')
    
draw_function2()
    
    
    
def testlatex():
    x=np.arange(0.01,1,0.01)
    y=0.5*np.log((1-x)/x)
   
    plt.grid()    
    plt.subplots_adjust(top=0.9)
    plt.scatter(x,y,label=r'$\alpha =\frac{1}{2}\ln(\frac{1-\varepsilon}{\varepsilon })$')
    
    plt.legend()
    plt.xlabel(r'$\varepsilon$',fontsize=20)
    plt.ylabel(r'$\alpha$',fontsize=20)
    plt.xlim(0,1)    

    plt.show()
#testlatex()
