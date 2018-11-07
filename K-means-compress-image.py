#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 17:43:26 2018

@author: sanghuynh
"""

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

img = mpimg.imread('./data/girl3.jpg')
plt.imshow(img)
imgplot = plt.imshow(img)
plt.axis('off')
plt.show() 

print(img.shape)
X = img.reshape((img.shape[0]*img.shape[1], img.shape[2]))
print(X)
K = 5

def kmeans_init_centroids(X, k):
    # randomly pick k rows of X as initial centroids
    return X[np.random.choice(X.shape[0], k, replace=False)]

def assign_label(X, centroids):
    D = cdist(X, centroids)
    return np.argmin(D, axis = 1)

def kmeans_update_centroids(X, labels, K):
    centroids = np.zeros((K, X.shape[1]))
    for k in range(K):
        # collect all points that are assigned to the k-th cluster
        Xk = X[labels == k, :]
        centroids[k,:] = np.mean(Xk, axis = 0) # then take average
    return centroids

def has_converged(centroids, new_centroids):
    # return True if two sets of centroids are the same
    return (set([tuple(a) for a in centroids]) ==
        set([tuple(a) for a in new_centroids]))
    
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

img1 = np.zeros_like(X)
temp = centroids[-1]
print(temp)
print(labels[-1])
for k in range(K):
    img1[labels[-1] == k] = temp[k]
    
img2 = img1.reshape((img.shape[0], img.shape[1], img.shape[2]))
plt.imshow(img2, interpolation='nearest')
plt.axis('off')
plt.show()   


for K in [5]:
    kmeans = KMeans(n_clusters=K).fit(X)
    label = kmeans.predict(X)
    print(kmeans.cluster_centers_)
    print(label)
    img4 = np.zeros_like(X)
    # replace each pixel by its center
    for k in range(K):
        img4[label == k] = kmeans.cluster_centers_[k]
    # reshape and display output image
    img5 = img4.reshape((img.shape[0], img.shape[1], img.shape[2]))
    plt.imshow(img5, interpolation='nearest')
    plt.axis('off')
    plt.show() 