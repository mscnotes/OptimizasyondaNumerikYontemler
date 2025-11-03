# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 15:10:35 2025

@author: Spyderman
"""

import sympy


x, y = sympy.symbols('x y')

f = 5*x**2*y+ 8*x*y

f_prime_x = sympy.diff(f,x)

f_prime_y = sympy.diff(f,y)



print("x'e göre-(∂f/∂x)")
print(f_prime_x)

print("-"*10)
print("y'ye göre-(∂f/∂y)")
print(f_prime_y)