# -*- coding: utf-8 -*-
"""
Created on Thu May 14 23:05:56 2020

@author: 16977
"""

import numpy as np
import matplotlib.pyplot as plt
population = np.zeros((100,100)) 
beta = 0.3
gamma = 0.05
time = 0 
outbreak = np.random.choice(range(100),2) 
population[outbreak[0],outbreak[1]] = 1 

plt.figure(figsize=(6,4),dpi=150) 
plt.imshow(population,cmap='viridis',interpolation='nearest')

while time <= 99:        
    infectedIndex = np.where(population==1) 
    for i in range(len(infectedIndex[0])): 
        x = infectedIndex[0][i]
        y = infectedIndex[1][i] 
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                if (xNeighbour,yNeighbour) != (x,y): 
                    if xNeighbour not in [-1,100] and yNeighbour not in [-1,100]: 
                        if population[xNeighbour,yNeighbour] == 0: 
                            population[xNeighbour,yNeighbour] = np.random.choice(range(2),1,p=[1-beta,beta])[0]
                else: 
                    population[xNeighbour,yNeighbour] = np.random.choice(range(2),1,p=[1-gamma,gamma])[0] + 1

    time = time + 1

    if time==10 or time==50 or time==100:
        plt.figure(figsize=(6,4),dpi=150)
        plt.imshow(population,cmap='viridis',interpolation='nearest')