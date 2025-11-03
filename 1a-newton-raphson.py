# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 14:15:55 2025
DOLAYLI YÖNTEM : AMAÇ türevin 0 a eşit noktasını bulmak.
Newton Raphson : Dolaylı yoldan fonksiyon minimumlarını bulmaya yarayan işlem.


INPUT : Bir x0​ başlangıç noktası gereklidir.
- Karesel olarak yakınsar.
- İteratiftir.
- Taylor serisini kullanır.
- Geometrik temele sahiptir.
f′′(x∗)>0 ise yerel minimum
f′′(x∗)<0 ise yerel maksimumdur
@author: Spyderman
"""

def f(x):
    return (x-1)**2*(x-2)*(x-3)


def f1(x):
    return (x - 3)*(x - 2)*(2*x - 2) + (x - 3)*(x - 1)**2 + (x - 2)*(x - 1)**2

def f2(x):
    return 2*(x - 3)*(x - 2) + 2*(x - 3)*(2*x - 2) + 2*(x - 2)*(2*x - 2) + 2*(x - 1)**2
    
x = -18
iteration = 0 
while abs(f1(x))>1e-10 and iteration<1000:
    iteration+=1
    deltax = -f1(x)/f2(x)
    x =x + deltax
    print(f"{iteration+1}.adım,f1(x):{f1(x)}, x:{x}")
    
    