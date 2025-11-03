# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 15:39:59 2025
DOLAYLI YÖNTEM AMAÇ f1(x) = 0 olduğunu bulmak
MANTIK: Kök bulma algoritmasıdır. fonks türevine uygalnır minimumunu bulmaya yönelik...
1 i poziitif diğeri negatifini bulmaya yönelik
Bi Section - İkiye Bölme Yöntemi

f′(a) ve f′(b) zıt işaretli olmalı
@author: Spyderman
"""

def f(x):
    return (x-1)**2*(x-2)*(x-3)

def f1(x):
    return (x - 3)*(x - 2)*(2*x - 2) + (x - 3)*(x - 1)**2 + (x - 2)*(x - 1)**2

xa = -2
xb = 5
iter = 0

if f1(xa)*f1(xb)<0:
    while abs(xb-xa) > 1e-10:
        xk = (xa + xb) / 2
        if f1(xk)*f1(xa)>0:
            xa = xk
        else:
            xb = xk
            
        iter+=1
        print(f"{iter}.adım, xa:{xa}, xb:{xb},abs: {abs(xa-xb)}")



else:
    print("noktalar yanlış biri pozitif biri negatif olmalı")
    