#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 17:38:00 2018

@author: sanghuynh
Genetic Algorithm
"""

import numpy as np
import matplotlib.pyplot as plt
import random

class MyQuickSort:
    # Python program for implementation of Quicksort Sort

    secondArr, thirdArr = [], []
    def __init__(self, secondArr, thirdArr):
        self.secondArr = secondArr
        self.thirdArr = thirdArr
    # This function takes last element as pivot, places
    # the pivot element at its correct position in sorted
    # array, and places all smaller (smaller than pivot)
    # to left of pivot and all greater elements to right
    # of pivot
    
    def partition(self, arr, low, high):
        i = (low -1)            # index of smaller element
        pivot = arr[high]       # pivot
    
        for j in range(low, high):
    
            # If current element is smaller than or equal to pivot
            if arr[j] <= pivot:
                
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
                self.secondArr[i], self.secondArr[j] = self.secondArr[j], self.secondArr[i]
                self.thirdArr[i], self.thirdArr[j] = self.thirdArr[j], self.thirdArr[i]
                
        arr[i+1], arr[high] = arr[high], arr[i+1]
        self.secondArr[i+1], self.secondArr[high] = self.secondArr[high], self.secondArr[i+1]
        self.thirdArr[i+1], self.thirdArr[high] = self.thirdArr[high], self.thirdArr[i+1]
        return (i + 1)
    
    # The main function that implements QuickSort
    # arr[] --> Array to be sorted,
    # low --> Starting index,
    # high --> Ending index
    
    # Function to do Quick sort
    def sort(self, arr, low, high):
    	if low < high:
    
    		# pi is partitioning index, arr[p] is now
    		# at right place
    		pi = self.partition(arr,low,high)
    
    		# Separately sort elements before
    		# partition and after partition
    		self.sort(arr, low, pi-1)
    		self.sort(arr, pi+1, high)

class GA:
    target = [30, 25, 30]
    N = 250
    data = []
    
    amount = 1000 # amount of gene in a generator
    genes, bestGenes = [], []
    losses, lossDetail = [], []
    bestIndex = 0
    
    @property
    def myQuickSort(self):
        return MyQuickSort(self.genes, self.lossDetail)
    
    def __init__(self, target=[800, 950, 800], N=1000):
        self.target = target
        self.N = N
        for i in range(self.N):
            self.data.append([random.randint(0, 5), random.randint(0, 5), random.randint(0, 5)])
        print("data", self.data)

    def initFirstGenerator(self):
        for i in range(self.amount):
            gen = []
            for j in range(self.N):
                gen.append(random.randint(0, 3))
            
            self.genes.append(gen)
        print("genes", self.genes)
        
    def calculateLostfunction(self):
        self.losses, self.lossDetail = [], []
        for gen in self.genes:
            total = [0, 0, 0]
            for count, element in enumerate(gen):
                if (element != 3):
                    print
                    total[element] += self.data[count][element]
            self.losses.append(self.calculateFitness(total))
            self.lossDetail.append(total)
            
        #print("losses", self.losses)
        #print("lossDetail", self.lossDetail)
        self.myQuickSort.sort(self.losses, 0, self.N - 1)
        print("losses", self.losses[0:10])
        print("lossDetail", self.lossDetail[0:10])
    def validation(self):
        for index in range(10):
            if (self.losses[index] <= 0.00001) and self.isPassTargetValidation(index):
                self.bestIndex = index
                return True
        return False
 
    def evolution(self):
        self.bestGenes = self.genes[0:10]
        newGenes = []
        for count in range(self.N//2):
            index = self.getAGoodRandomValue(count, len(self.bestGenes) - 1)
            newGenes += self.breed(self.genes[count], self.bestGenes[index])
        
        self.genes = newGenes
    def mutate(self):
        for gen in self.genes:
            number = random.randint(1, 100)
            if number == 1:
                temp = random.randint(0, self.N - 1)
                gen[temp] = self.getAGoodRandomValue(gen[temp], 3)
        return
    def calculateFitness(self, total):
        fitness = 0
        for index, value in enumerate(total):
            fitness += pow(1 - value/self.target[index], 2)
        return fitness
    
    def isPassTargetValidation(self, position):
        count = 0
        while count < 3:
            if self.target[count] < self.lossDetail[position][count]:
                return False
            count += 1;
        return True 
    
    def breed(self, parent1, parent2):

        geneA = int(random.random() * len(parent1))
        geneB = int(random.random() * len(parent1))
        
        startGene = min(geneA, geneB)
        endGene = max(geneA, geneB)
        
        child1 = parent1[0:startGene] + parent2[startGene:endGene] + parent1[endGene:len(parent1)]
        child2 = parent2[0:startGene] + parent1[startGene:endGene] + parent2[endGene:len(parent2)]
        
        return [child1, child2]
    
    def getAGoodRandomValue(self, rejectNumber, inRange):
        goodNumber = random.randint(0, inRange)
        if (goodNumber == rejectNumber):
            self.getAGoodRandomValue(rejectNumber, inRange)
        return goodNumber
    
    def run(self):
        self.initFirstGenerator() 
        self.calculateLostfunction()
        while self.validation() != True:
            print("Next Generatoion...")
            self.evolution()
            self.mutate()
            self.calculateLostfunction()
        print("The best ", self.bestIndex, self.bestGenes[self.bestIndex])
        
ga = GA()
ga.run()





