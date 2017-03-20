import pandas as pd
import matplotlib.pyplot as plt
def run():
    data=pd.read_csv('E:\\data\\ratings.csv')
    #print data
    movieset=pd.read_csv('E:\\data\\movies.csv')
    #print movie['genres']
    #print data
    userdict={}
    for index,row in data.iterrows():
        user=row['userId']
        movie=row['movieId']
        rating=row['rating']
        time=row['timestamp']
        if not userdict.has_key(user):
            userdict[user]=[]
        userdict[user].append((movie,rating,time))
    
    maxsize=0
    maxuser=0
    for user in userdict:
        userdict[user]=sorted(userdict[user],key=lambda x:x[2])
        if len(userdict[user])>maxsize:
            maxsize=len(userdict[user])
            maxuser=user
    print maxuser,maxsize
    
    moviedict={}
    for index,row in movieset.iterrows():
        movie=row['movieId']
        genres=row['genres'].split('|')
        if not moviedict.has_key(movie):
            moviedict[movie]=set()
        for gen in genres:
            moviedict[movie].add(gen)
    
    
    y=[]
    x=[]
    genresdict={}
    for movie,rating,time in userdict[maxuser]:
        for genres in moviedict[movie]:
            if not genresdict.has_key(genres):
                genresdict[genres]=0
            genresdict[genres]+=1
        if 'IMAX' in moviedict[movie]:
            y.append(1)
        else:
            y.append(0)
        x.append(time)
    
    for genres in genresdict:
        print genres,genresdict[genres]
        
        
    plt.plot(x,y)
            
    
        
        
    
run()