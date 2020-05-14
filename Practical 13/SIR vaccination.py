# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:55:09 2020

@author: 16977
"""

import numpy as np
import matplotlib.pyplot as plt


population = 10000
susceptible = population-1
drugtake =  [1,2,3,4,5,6,7,8,9,10]
drugeffect1 = drugtake[0]
drugeffect2 = drugtake[1]
drugeffect3 = drugtake[2]
drugeffect4 = drugtake[3]
drugeffect5 = drugtake[4]
drugeffect6 = drugtake[5]
drugeffect7 = drugtake[6]
drugeffect8 = drugtake[7]
drugeffect9 = drugtake[8]
drugeffect10 = drugtake[9]
recovered1=0
recovered2=0
recovered3=0
recovered4=0
recovered5=0
recovered6=0
recovered7=0
recovered8=0
recovered9=0
recovered10=0
infected1 = 1
infected2 = 1
infected3 = 1
infected4 = 1
infected5 = 1
infected6 = 1
infected7 = 1
infected8 = 1
infected9 = 1
infected10 = 1
drugman1 = int(population*drugeffect1*0.1)
drugman2 = int(population*drugeffect2*0.1)
drugman3 = int(population*drugeffect3*0.1)
drugman4 = int(population*drugeffect4*0.1)
drugman5 = int(population*drugeffect5*0.1)
drugman6 = int(population*drugeffect6*0.1)
drugman7 = int(population*drugeffect7*0.1)
drugman8 = int(population*drugeffect8*0.1)
drugman9 = int(population*drugeffect9*0.1)
drugman10 = int(population*drugeffect10*0.1)
susceptible1= susceptible - drugman1
susceptible2= susceptible - drugman2
susceptible3= susceptible - drugman3
susceptible4= susceptible - drugman4
susceptible5= susceptible - drugman5
susceptible6= susceptible - drugman6
susceptible7= susceptible - drugman7
susceptible8= susceptible - drugman8
susceptible9= susceptible - drugman9
susceptible10= susceptible - drugman10
recordI1=[1]
recordI2=[1]
recordI3=[1]
recordI3=[1]
recordI4=[1]
recordI5=[1]
recordI6=[1]
recordI7=[1]
recordI8=[1]
recordI9=[1]
recordI10=[0]

beta = 0.3
gamma = 0.05

time = 0

while time <= 999:
    infectednew1 = sum(np.random.choice(range(2),susceptible1,p=[(1-beta*(infected1/population)),beta*(infected1/population)]))
    recoverednew1 = sum(np.random.choice(range(2),infected1,p=[(1-gamma),gamma]))
    infected1= infected1 + infectednew1 - recoverednew1
    susceptible1= susceptible1 - infectednew1
    recovered1= recovered1 + recoverednew1
    infectednew2 = sum(np.random.choice(range(2),susceptible2,p=[(1-beta*(infected2/population)),beta*(infected2/population)]))
    recoverednew2 = sum(np.random.choice(range(2),infected2,p=[(1-gamma),gamma])) 

    infected2= infected2 + infectednew2 - recoverednew2
    susceptible2= susceptible2 - infectednew2
    recovered2= recovered2 + recoverednew2
    infectednew3 = sum(np.random.choice(range(2),susceptible3,p=[(1-beta*(infected3/population)),beta*(infected3/population)]))
    recoverednew3 = sum(np.random.choice(range(2),infected3,p=[(1-gamma),gamma]))

    infected3= infected3 + infectednew3 - recoverednew3
    susceptible3= susceptible3 - infectednew3
    recovered3= recovered3 + recoverednew3

    infectednew4 = sum(np.random.choice(range(2),susceptible4,p=[(1-beta*(infected4/population)),beta*(infected4/population)]))
    recoverednew4 = sum(np.random.choice(range(2),infected4,p=[(1-gamma),gamma]))

    infected4= infected4 + infectednew4 - recoverednew4
    susceptible4= susceptible4 - infectednew4
    recovered4= recovered4 + recoverednew4

    infectednew5 = sum(np.random.choice(range(2),susceptible5,p=[(1-beta*(infected5/population)),beta*(infected5/population)]))
    recoverednew5 = sum(np.random.choice(range(2),infected5,p=[(1-gamma),gamma]))

    infected5= infected5 + infectednew5 - recoverednew5
    susceptible5= susceptible5 - infectednew5
    recovered5= recovered5 + recoverednew5

    infectednew6 = sum(np.random.choice(range(2),susceptible6,p=[(1-beta*(infected6/population)),beta*(infected6/population)]))
    recoverednew6 = sum(np.random.choice(range(2),infected6,p=[(1-gamma),gamma]))

    infected6= infected6 + infectednew6 - recoverednew6
    susceptible6= susceptible6 - infectednew6
    recovered6= recovered6 + recoverednew6

    infectednew7 = sum(np.random.choice(range(2),susceptible7,p=[(1-beta*(infected7/population)),beta*(infected7/population)]))
    recoverednew7 = sum(np.random.choice(range(2),infected7,p=[(1-gamma),gamma]))

    infected7= infected7 + infectednew7 - recoverednew7
    susceptible7= susceptible7 - infectednew7
    recovered7= recovered7 + recoverednew7

    infectednew8 = sum(np.random.choice(range(2),susceptible8,p=[(1-beta*(infected8/population)),beta*(infected8/population)]))
    recoverednew8 = sum(np.random.choice(range(2),infected8,p=[(1-gamma),gamma]))

    infected8= infected8 + infectednew8 - recoverednew8
    susceptible8= susceptible8 - infectednew8
    recovered8= recovered8 + recoverednew8

    infectednew9 = sum(np.random.choice(range(2),susceptible9,p=[(1-beta*(infected9/population)),beta*(infected9/population)]))
    recoverednew9 = sum(np.random.choice(range(2),infected9,p=[(1-gamma),gamma]))

    infected9= infected9 + infectednew9 - recoverednew9
    susceptible9= susceptible9 - infectednew9
    recovered9= recovered9 + recoverednew9

    '''    
    infectednew10 = sum(np.random.choice(range(2),susceptible10,p=[(1-beta*(infected10/population)),beta*(infected10/population)]))
    recoverednew10 = sum(np.random.choice(range(2),infected10,p=[(1-gamma),gamma]))

    infected10= infected10 + infectednew10 - recoverednew10
    susceptible10= susceptible10 - infectednew10
    recovered10= recovered10 + recoverednew10

    '''           
    recordI1.append(infected1)
    recordI2.append(infected2)
    recordI3.append(infected3)
    recordI4.append(infected4)
    recordI5.append(infected5)
    recordI6.append(infected6)
    recordI7.append(infected7)
    recordI8.append(infected8)
    recordI9.append(infected9)

    '''
        recordI10.append(infected10)  

    '''   
    time = time + 1


plt.xlabel("time") 
plt.ylabel("number of people") 
plt.title("SIR model with different vaccination rates")
plt.legend("susceptible")
plt.legend("recovered")
plt.legend("infected")
plt.plot(recordI1,label='10%')
plt.plot(recordI2,label='20%')
plt.plot(recordI3,label='30%')
plt.plot(recordI4,label='40%')
plt.plot(recordI5,label='50%')
plt.plot(recordI6,label='60%')
plt.plot(recordI7,label='70%')
plt.plot(recordI8,label='80%')
plt.plot(recordI9,label='90%')
plt.plot(recordI10,label='100%')

plt.legend()
plt.savefig('<vaccination>',type="png")
plt.show()

