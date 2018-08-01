# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:43:14 2018

@author: tevfik
"""

#Importing libraries
import pandas as pd 
import matplotlib.pyplot as plt

# Importing and Parsing dataset
dataset = pd.read_csv("student-por.csv")
age_health = dataset[['age','health']]
all_data = age_health.iloc[:].values

# Creating unique ages list
unique_ages = []
for x in all_data[:,0]:
    if x not in unique_ages:
        unique_ages.append(x)
unique_ages.sort()

# Calculating average health rates of ages(18-22)
avg_healths = []
for age in unique_ages:
    total = 0.0
    counter = 0
    avg = 0.0
    for num in all_data:
        if num[0] == age:
            counter +=1
            total += num[1]
    avg = (total / counter)
    avg_healths.append(avg)
    
# Plotting the average health and ages
width = 1/1.7
plt.xlabel("Ages")
plt.ylabel("Average Health Rates")
plt.bar(unique_ages,avg_healths, width, color="blue")
plt.show()