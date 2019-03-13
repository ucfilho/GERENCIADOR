import numpy as np

import Fun

''' 
FOBJ gera vetorialmente os valores com a funcao objetivo escalar
em outras palavras gera para populacao o valor da funcao 
a ser otimizada
'''
def FOBJ(X):
    rows = X.shape[0]
    fobj=np.zeros(rows)
    for i in range(rows):
        fobj[i]=Fun.Fun(X[i,])
    return fobj
