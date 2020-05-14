# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:31:00 2020

@author: 16977
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("/Users/16977/Desktop")
covid_data = pd.read_csv("full_data.csv")

print(covid_data.iloc[0:18:3,:])

def find_loc(loc):
    boolean_loc=[]
    for i in covid_data.iloc[:,1]:
        if i==loc:
            boolean_loc.append(True)
        else:
            boolean_loc.append(False)
    return boolean_loc

Afghanistan_total_cases=covid_data.loc[find_loc("Afghanistan"),"total_cases"]

world_new_cases=covid_data.loc[find_loc("World"),"new_cases"]
world_new_cases_np=np.array(world_new_cases[:])
world_new_cases_mean=np.mean(world_new_cases_np)
world_new_cases_median=np.median(world_new_cases_np)
print('\nworldwide mean',world_new_cases_mean)
print('worldwide median',world_new_cases_median)

world_new_cases_boxplot=plt.boxplot(world_new_cases_np,
                                    vert=True,
                                    whis=1.5,
                                    patch_artist=True,
                                    showmeans=True,
                                    meanline=True,
                                    showbox=True,
                                    showcaps=True,
                                    showfliers=True,
                                    notch=False)
plt.ylabel('world_new_cases')
plt.show()

world_dates=covid_data.loc[find_loc("World"),"date"]
plt.plot(world_dates,
         world_new_cases,
         'r+')
world_new_deaths=covid_data.loc[find_loc('World'),'new_deaths']
plt.plot(world_dates,
         world_new_deaths,
         'b+')
plt.xlabel("dates")
plt.ylabel("world_new_cases")
plt.xticks(world_dates.iloc[0::4],rotation=-90)
plt.legend(['world_new_cases','world_new_deaths'])
plt.show()







spain_dates=covid_data.loc[find_loc("Spain"),'date']
spain_total_cases=covid_data.loc[find_loc('Spain'),'total_cases']
spain_new_cases=covid_data.loc[find_loc('Spain'),'new_cases']
plt.plot(spain_dates,
         spain_new_cases,
         'r+')
plt.xlabel("dates")
plt.ylabel("spain_new_cases")
plt.xticks(spain_dates.iloc[0::4],rotation=-90)

plt.legend(["spain_new_cases"])
plt.show()

plt.plot(spain_dates,spain_total_cases,'b+')
plt.xlabel("dates")
plt.ylabel("spain_total_cases")
plt.xticks(spain_dates.iloc[0::4],rotation=-90)
plt.legend(["spain_total_cases"])
plt.show()
