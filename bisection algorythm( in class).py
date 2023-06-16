# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 17:24:59 2023

@author: kpenaalvarez
"""
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    """
    np.exp(x)  gives you whatever you put in to the (_) to raise as an exponent of e^x
    f(x) = exp(x) - x**2

    Parameters
    ----------
    x : TYPE float
        DESCRIPTION. input to the function f(x)

    Returns
    -------
    y : output of f(x)

    """
    y = np.exp(x) - x**2
    return y 

#find x so that f(x) = 0

xAxis = np.linspace(-3, 1)
y = f(xAxis)
    
plt.plot(xAxis, y)
plt.axhline(y=0, color='red', ls=':')
    
xLow = -1
xHigh = 2

for i in range(15):
    xTry = (xLow+xHigh)/2
    if f(xTry) > 0:
        xHigh = xTry
    else:
        xLow = xTry
    print(f"x = {xTry}, f(x) = {f(xTry)}")
    
print(f"Final answer = {xTry}, f = {f(xTry): 0.5f}")