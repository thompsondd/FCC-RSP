# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
import random
from math import *
def g(a):
    if a>0:
        return a
    return 1
            
def player(prev_play, opponent_history=[]):
    opponent_history.append(prev_play)
    temp=opponent_history.copy()
    p={"R":"P","P":"S","S":"R"}
    n=len(opponent_history)-1
    if n==0:
        n=1
    dt={
        "P":(opponent_history.count('P')+2*int(prev_play=="P"))/n,
        "R":(opponent_history.count('R')+2*int(prev_play=="R"))/n,
        "S":(opponent_history.count('S')+2*int(prev_play=="S"))/n
    }
    db={
        "PS":0,
        "PP":0,
        "PR":0,
        "SS":0,
        "SP":0,
        "SR":0,
        "RR":0,
        "RS":0,
        "RP":0
    }
    while True:
        try:
            temp.pop(temp.index(""))
        except:
            break
       
    for i in range(len(temp)-1):
        a=1
        if i==len(temp)-2:
            a=2
        db[temp[i]+temp[i+1]]+=a
    
    keys=list(db.keys())
    values=list(db.values())
    for i in keys:
        db[i]/=g(sum(values))
        
    newD1={"P":0,"R":0,"S":0}
    for i in db:
        if i[0] in temp[-1:]:
            newD1[i[1]]+=(db[i]*(dt[i[0]]*dt[i[1]]))/g(dt[i[0]]+dt[i[1]])
        #newD[i[1]]+=(db[i]+dt[i[0]]*dt[i[1]])/max(1,(dt[i[0]]*dt[i[1]]))
    #print(newD)
    newD={"P":0,"R":0,"S":0}
    b=0.8
    for i in newD:
        newD[i]=(newD1[i]*g(dt[i]))*(newD1[i]*g(dt[i]))/g(2*newD1[i]+2*g(dt[i]))
    keys=list(newD.keys())
    values=list(newD.values())
    mv=max(values)
    mk=keys[values.index(mv)]
    guess=mk
    
    '''
    Max=0
    guess = ""
    for i in distribution:
        if Max<distribution[i]:
            guess=i
            Max=distribution[i]
    if guess=="":
        guess=list(p.keys())[random.randint(0,2)]'''
    return p[guess]
