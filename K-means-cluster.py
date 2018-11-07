#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:29:20 2018

@author: sanghuynh
"""

from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import random

np.random.seed(18)
means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500

X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)
X = np.concatenate((X0, X1, X2), axis = 0)
K = 3 # 3 clusters
original_label = np.asarray([0]*N + [1]*N + [2]*N).T

def kmeans_init_centroids(X, k):
    # randomly pick k rows of X as initial centroids
    return X[np.random.choice(X.shape[0], k, replace=False)]

def kmeans_assign_labels(X, centroids):
    # calculate pairwise distances btw data and centroids
    D = cdist(X, centroids)
    # return index of the closest centroid axis = 1 (Ox) axis = 0 (Oy) no axis (index of minimum value)
    return np.argmin(D, axis = 1)

def has_converged(centroids, new_centroids):
    # return True if two sets of centroids are the same
    print(centroids)
    print(new_centroids)
    print("=======")
    return (set([tuple(a) for a in centroids]) ==
        set([tuple(a) for a in new_centroids]))
    
def kmeans_update_centroids(X, labels, K):
    centroids = np.zeros((K, X.shape[1]))
    for k in range(K):
        # collect all points that are assigned to the k-th cluster
        Xk = X[labels == k, :]
        centroids[k,:] = np.mean(Xk, axis = 0) # then take average
    return centroids

def kmeans_display(X, label, centroids):
    X0 = X[label == 0, :]
    X1 = X[label == 1, :]
    X2 = X[label == 2, :]
    
    plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize = 4, alpha = .8)
    plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 4, alpha = .8)
    plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize = 4, alpha = .8)
    plt.plot(centroids[:, 0], centroids[:, 1], 'y*', markersize = 14, alpha = .8)

    plt.axis('equal')
    plt.plot()
    plt.show()

def kmeans_cluster(X, K):
    labels = []
    centroids = [kmeans_init_centroids(X, K)]
    it = 0
    while True:
        labels.append(kmeans_assign_labels(X, centroids[-1]))
        newCentroids = kmeans_update_centroids(X, labels[-1], K)
        if has_converged(centroids[-1], newCentroids):
            break
        centroids.append(newCentroids)
        it += 1
    return (centroids, labels, it)

(centroids, labels, it) = kmeans_cluster(X, K)
print("Centers found by our algorithm:\n", centroids[-1], it)
kmeans_display(X, labels[-1], centroids[-1])