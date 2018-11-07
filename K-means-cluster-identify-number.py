#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 16:46:58 2018

@author: sanghuynh
"""

from __future__ import print_function
import numpy as np
from sklearn.datasets import fetch_mldata
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors

data_dir = './data' # path to your data folder
mnist = fetch_mldata('MNIST original', data_home=data_dir)
print("Shape of minst data:", mnist.data.shape)


K = 10 # number of clusters
N = 10000
X = mnist.data[np.random.choice(mnist.data.shape[0], N)]
kmeans = KMeans(n_clusters=K).fit(X)  
pred_label = kmeans.predict(X)
print(pred_label)