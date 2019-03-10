# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 00:01:34 2017

@author: raiana
"""
import numpy as np
from math import *
   

################################### Funções unimodais
    
'''Rosembrock Function'''
def Rosenbrock(x):
    fun=0
    a=1.0
    b=100.0
    for i in range(len(x)):
        fun = ((a-x[i])**2 + b*(x[i+1]-x[i]**2)**2) 
    return fun 

#Rosembrock_domain=[-30,30]
# Global Minimum: 0

def sphere_function(x):
    return sum([i**2 for i in x])

def sum_of_different_powers_function(x):
    return sum([abs(x[i])**(i+2) for i in range(len(x))])

def six_hump_camel_function(x): #parece sum_of_different_powers_function mas inclinação mto maior
    return (4 - 2.1*x[0]**2 + x[0]**4/3)*x[0]**2 + x[0]*x[1]\
           + (-4 + 4*x[1]**2)*x[1]**2

def easom_function(x):
    return -cos(x[0])*cos(x[1])*exp(-(x[0] - pi)**2 - (x[1] - pi)**2)

def booth_function(x):
    return (x[0] + 2*x[1] - 7)**2 + (2*x[0] + x[1] - 5)**2

def beale_function(x):
    return (1.5 - x[0] + x[0]*x[1])**2 + (2.25 - x[0] + x[0]*x[1]**2)**2 + \
           (2.625 - x[0] + x[0]*x[1]**3)**2

### Unimodais parecidas

def bohachevsky_function(x): #gráfico parecido c a espera
    return x[0]**2 + 2*x[1]**2 - 0.3*cos(3*pi*x[0]) - 0.4*cos(4*pi*x[1]) + 0.7

def sum_squares_function(x): #gráfico parecido c a espera
    return sum([(i+1)*x[i]**2 for i in range(len(x))])

def matyas_function(x): #parece booth (papel)
    return 0.26*sphere_function(x) - 0.48*x[0]*x[1]

def mccormick_function(x): #parece booth (papel)
    return sin(x[0] + x[1]) + (x[0] - x[1])**2 - 1.5*x[0] + 2.5*x[1] + 1

def dixon_price_function(x): #sum_of_different_powers_function
    return (x[0] - 1)**2 + sum([(i+1)*(2*x[i]**2 - x[i-1])**2
                                for i in range(1, len(x))])

def three_hump_camel_function(x):  #sum_of_different_powers_function
    return 2*x[0]**2 - 1.05*x[0]**4 + x[0]**6/6 + x[0]*x[1] + x[1]**2
############################################################################

###################################Funções multimodais
    
'''Schubert Function'''

def Shubert(x):
    n=1
    sum1=0
    sum2=0
    for n in range(1,6):
        new1=(n*np.cos((n+1)*x[0]+n))
        new2=(n*np.cos((n+1)*x[1]+n))
        sum1=sum1+new1
        sum2=sum2+new2
    return (sum1*sum2)

# Domain: xi ∈ [-5.12, 5.12] ou [-10,10]
# Global Minimum: -186.7309
 
'''Schwefel Function'''

def Schwefel(x):
    
    summ=0
    for i in range(len(x)):
        new=x[i]*np.sin((abs(x[i]))**0.5)
        summ=summ+new
#        print(summ)
    return (418.9829*len(x)-summ)    

# Global optimum: f(xi)= 0 for xi = 420.968746 for i=1,...,n  ;  xi in [-500,500] 
    
def ackley_function(x):
    return -exp(-sqrt(0.5*sum([i**2 for i in x]))) - \
           exp(0.5*sum([cos(i) for i in x])) + 1 + exp(1)

def bukin_function(x):
    return 100*sqrt(abs(x[1]-0.01*x[0]**2)) + 0.01*abs(x[0] + 10)


def cross_in_tray_function(x):
    return round(-0.0001*(abs(sin(x[0])*sin(x[1])*exp(abs(100 -
                            sqrt(sum([i**2 for i in x]))/pi))) + 1)**0.1, 7)

def michalewicz_function(x):
    return -sum([sin(x[i])*sin((i+1)*x[i]**2/pi)**20 for i in range(len(x))])


def drop_wave_function(x):
    return -(1 + cos(12*sqrt(sphere_function(x))))/(0.5*sphere_function(x) + 2)