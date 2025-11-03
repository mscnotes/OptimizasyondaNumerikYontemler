# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 18:52:22 2025

@author: Spyderman
"""

import numpy as np

#fonk değişicek
from ornekFonksiyon2 import f,gradient



#en iyisi
def goldensection(x,p):
    salt = 0
    sust = 1
    deltas = 1e-6
    tau = 0.38197
    eps = deltas/(sust-salt)
    N = int(-2.078*np.log(eps))
    for iteration in range(0,N):
        s1 = salt + tau*(sust-salt); f1 = f(x+s1*p)
        s2 = sust - tau*(sust-salt); f2 = f(x+s2*p)
        if f1>f2:
            salt = s1
            s1 = s2
            f1 = f2
            s2 = sust - tau*(sust-salt); f2 = f(x+s2*p)
        else:
            sust = s2
            s2 = s1
            f2 = f1
            s1 = salt + tau*(sust-salt); f1 = f(x+s1*p)
        s = salt + (sust -salt)/2
    return s

# verdiği yerde belirlicez

x = np.array([0.5, 0.5])
x1 = [x[0]]
x2 = [x[1]]

eps = 1e-10

N = 100000

k = 0

C1 = k<N
C2 = True
C3 = True
C4 = np.linalg.norm(gradient(x))>eps

while all([C1,C2,C3,C4]):
    k += 1
    if k==1:
        p = -gradient(x)
        prevp = p.copy()
        prevg = gradient(x).copy()
    else:
        beta = np.dot(gradient(x),gradient(x))/np.dot(prevg,prevg)
        p = -gradient(x) + beta*prevp
        prevp = p.copy()
        prevg = gradient(x).copy()
    
    # s = 0.25
    s = goldensection(x,p)
    prevF = f(x)
    prevX = x
    x = x + s*p
    x1.append(x[0])
    x2.append(x[1])
    
    
    print('k:',k,'s:',s,'x1',x[0],'x2',x[1],'f(x):',f(x),'||gradient(x)||',np.linalg.norm(gradient(x)))
    C1 = k<N
    C2 = abs(f(x) - prevF)>eps
    C3 = np.linalg.norm(x - prevX)>eps
    C4 = np.linalg.norm(gradient(x))>eps
    
    if not C1:
        print('maksimum iterasyona ulaşıldı...')
    if not C2:
        print('fonksiyon değişmiyor...')
    if not C3:
        print('değişkenler değişmiyor...')
    if not C4:
        print('durağan noktaya gelindi...')

#------------------------------------------------------------------------------     
#------------------------------------------------------------------------------    
import matplotlib.pyplot as plt    
# plotting the points 
plt.plot(x1, x2, color='darkred', linestyle='solid', linewidth = 0.5, marker='o', markerfacecolor='black', markersize=1)
plt.xlabel('x1')
plt.ylabel('x2')
plt.title('Conjugate Gradient Algoritması',fontstyle='italic')
plt.grid(color = 'green', linestyle = '--', linewidth = 0.1)
plt.show()    
#------------------------------------------------------------------------------     
