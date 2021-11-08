#TP Proba
import random
from math import *
from matplotlib import pyplot
import numpy


def miseajourMABA(p,A,k):
    l=k
    if (l!=A) and (l!=0):
        pas=2*(random.random()<p)-1
        l=k+pas
    return l

def trajMABA(p,A,k,n):
    traj=[k]
    for i in range(n):
        traj.append(miseajourMABA(p,A,traj[-1]))
    pyplot.plot(range(n+1),traj,color='blue')
    pyplot.show()

def tempsabsMABA(p,A,k):
    traj=[k]
    compteur=0
    while traj[-1] not in [0,A]:
        traj.append(miseajourMABA(p,A,traj[-1]))
        compteur=compteur+1
    absorbeur=traj[-1]
    return absorbeur,compteur

def tempsabsMABA1(p,A,k):
    traj=[k]
    compteur=0
    while traj[-1] not in [0,A]:
        traj.append(miseajourMABA(p,A,traj[-1]))
        compteur=compteur+1
    absorbeur=traj[-1]
    return compteur


def estimMABA(p,A,k,n):#où n est la taille de l'échantillon
    absorb=[]
    temps=[]
    for i in range(n):
        [abs,tps]=tempsabsMABA(p,A,k)
        absorb.append(abs)
        temps.append(tps)
    tpsmoy=sum(temps)/n
    pAapprox=sum(absorb)/(A*n)
    return(pAapprox,tpsmoy)

#ex2
def miseajourMA2BR(p,A,k):
    l=k
    if l==0:
        if(random.random()<p):
            pas=1
        else:
            pas=0
    elif l==A:
        if (random.random()>p):
            pas=-1
        else:
            pas=0
    else:
        pas=2*(random.random()<p)-1
    l=k+pas
    return l











