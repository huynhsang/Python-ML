#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:54:16 2018

@author: sanghuynh
"""
# Applying Gradient Descent for f(x) = x^2 + 5sin(x)

import numpy as np

def grad(x):
    return 2*x + 5*np.cos(x)

def cost(x):
    return x**2 + 5*np.sin(x)

def myGradDes(x0, eta):
    x = [x0]
    for it in range(100):
        x_new = x[-1] - eta*grad(x[-1])
        if abs(grad(x_new)) < 1e-3:
            break;
        x.append(x_new)
    return (x, it)

(x1, it1) = myGradDes(-5, .1)
(x2, it2) = myGradDes(5, .1)
print('Solution x1 = %f, cost = %f, after %d iterations' %(x1[-1], cost(x1[-1]), it1))
print('Solution x2 = %f, cost = %f, after %d iterations' %(x2[-1], cost(x2[-1]), it2))
