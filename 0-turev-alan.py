# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 15:05:30 2025

@author: Spyderman
"""

import sympy

x = sympy.symbols('x')

f = (x-1)**2*(x-2)*(x-3)


f_prime = sympy.diff(f, x)

print(f"Turev: {f_prime}")




