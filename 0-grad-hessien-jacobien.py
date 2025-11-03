# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 16:47:49 2025
Verilen bir fonksiyonun gradient vektörü ve hessian matrisini veren kod.
@author: Spyderman
"""


import numpy as np
import math
import sympy
from sympy import symbols, Matrix, hessian


x1, x2,x3 = symbols('x1 x2 x3')

f = (x1-2*x2 + x3 + 1)**2 + (x1 + x2 -x3 + 3 )**2 + (-2*x1+x2-x3)**2
grad_f_sembolik = [f.diff(x1),f.diff(x2), f.diff(x3)]

H_sembolik = hessian(f,[x1, x2, x3])

print(f"Gradyan (\u2207f):")
print(f"df/dx1 = {grad_f_sembolik[0]}")
print(f"df/dx2 = {grad_f_sembolik[1]}")
print(f"df/dx2 = {grad_f_sembolik[2]}")
print("\n---")


print(f"Hessian (\u2207\u00b2f):\n{H_sembolik}\n")
print("---")

