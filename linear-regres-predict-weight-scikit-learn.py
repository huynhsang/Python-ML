#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 09:09:12 2018

@author: sanghuynh
"""

from sklearn import datasets, linear_model

# height (cm), input data, each row is a data point
X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T
# weight (kg)
y = np.array([ 49, 50, 51,  54, 58, 59, 60, 62, 63, 64, 66, 67, 68])

# fit the model by Linear Regression
regr = linear_model.LinearRegression()
regr.fit(X, y) # in scikit-learn, each sample is one row
# Compare two results
print("scikit-learn’s solution  : w_1 = ", regr.coef_[0], "w_0 = ", regr.intercept_)
#print("our solution             : w_1 = ", w[1], "w_0 = ", w[0])