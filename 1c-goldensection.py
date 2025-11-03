# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 16:07:12 2025
ARALIK DARALTMA YÖNTEMLERİNİN ŞAHI
türev gerekmezzzz.
INPUT = xalt , xust, deltax
daralta ve karşılaştırarak minimumu bulur.
@author: Spyderman
"""
import numpy as np

def f(x):
    return (x-1)**2*(x-2)*(x-3)


xalt = 0
xust = 4
deltax = 1e-4
tau=0.38197
eps = (deltax/(xust-xalt))

#iterasyon sayisi
N = int(-2.078*np.log(eps))


for iteration in range(0,N):
    x1 = xalt + tau* (xust - xalt ) ; f1 = f(x1) 
    x2 = xust - tau*(xust - xalt) ; f2 = f(x2)
    
    if f1 > f2:
        xalt = x1
        x1 = x2
        f1 = f2
        x2 = xust - tau*(xust - xalt) ; f2 = f(x2)
    else :
        xust = x2
        x2 = x1
        f2 = f1 
        x1 = xalt + tau* (xust - xalt ) ; f1 = f(x1) 
    x = xalt + (xust -xalt)/2
    print('iteration',iteration+1,'f(x):',f(x),'x:',x)

        
        
    
    