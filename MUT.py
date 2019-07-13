# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 10:28:26 2019

@author: raiana
"""

#FUNÇÕES GERENCIADOR

import numpy as np
from random import randint

def GETX(XY,PAR):
  X=XY[:,0:PAR] #Extrai as primeiras colunas (valores de X)
  return X

def GETY(XY):
  Y=XY[:,-1]
  return Y

def GETBEST(mbest): # GBEST = Melhor agente entre todos os métodos
  MBEST_ST= mbest[mbest[:,-1].argsort()]
  GBEST=MBEST_ST[0]
  OTHERBEST=np.delete(MBEST_ST, np.s_[0], axis=0) # deleta GBEST
  return GBEST,OTHERBEST

def MUT1(X,GBEST,NPAR,PAR,MAX,MIN): #função Mutation que usa o best e um outro ponto qlq
    Xnew=np.zeros((NPAR,PAR))    
    for row in range(NPAR):
      rd=randint(0, (NPAR-1))
      Xj=X[rd]
      for col in range(PAR):
        MV=(X[row,col]+Xj[col])/2
        Xnew[row,col]=X[row,col]+np.random.random()*(GBEST[col]-MV)
        if Xnew[row,col]>MAX[col]:
          Xnew[row,col]=MAX[col]
        elif Xnew[row,col]<MIN[col]:
          Xnew[row,col]=MIN[col]
    #Xnew=np.clip(Xnew,MAX,MIN)
    return Xnew
  
def MUT2(X,GBEST,OTHERBEST,NPAR,PAR,MAX,MIN): #função Mutation q usa 2 entre os melhores BEST
    Xnew=np.zeros((NPAR,PAR))    
    for row in range(NPAR):
      rd=randint(0, (len(OTHERBEST)-1))
      Xj=OTHERBEST[rd]
      for col in range(PAR):
        MV=(X[row,col]+Xj[col])/2
        Xnew[row,col]=X[row,col]+np.random.random()*(GBEST[col]-MV)
        if Xnew[row,col]>MAX[col]:
          Xnew[row,col]=MAX[col]
        elif Xnew[row,col]<MIN[col]:
          Xnew[row,col]=MIN[col]
    #Xnew=np.clip(Xnew,MAX,MIN)
    return Xnew

def MUT3(X,MBEST,NPAR,PAR,MAX,MIN): #Mutation q usa um agente aleatório de MBEST
    Xnew=np.zeros((NPAR,PAR))    
    for row in range(NPAR):
      rd=randint(0, (len(MBEST)-1))
      Xj=MBEST[rd]
      for col in range(PAR):
        #MV=(X[row,col]+Xj[col])/2
        Xnew[row,col]=X[row,col]+np.random.random()*(Xj[col]-X[row,col])
        if Xnew[row,col]>MAX[col]:
          Xnew[row,col]=MAX[col]
        elif Xnew[row,col]<MIN[col]:
          Xnew[row,col]=MIN[col]
    #Xnew=np.clip(Xnew,MAX,MIN)
    return Xnew 
  
def FOBJ(X,Fun):
    rows = X.shape[0]
    fobj=np.zeros(rows)
    for i in range(rows):
        fobj[i]=Fun(X[i,])
    return fobj
  
def XYsort(X,Y): #concatena x e y e ordena por menor FO
  XY= np.c_[X,Y] #concatena X e Y
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir de Y
  return XYsorted 

def TRADE(XY,PTRADE): # Separa melhores agentes para gerenciador
  XYT=XY[0:PTRADE,]
  return XYT

def STACKSORT(XY1,XY2): # Junta e ordena um array
  XY=np.vstack((XY1,XY2))
  XYsorted = XY[XY[:,-1].argsort()] #Ordena a partir de Y
  return XYsorted
