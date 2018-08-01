# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 18:58:18 2018

@author: tevfik
"""


#Importing libraries
import pandas as pd 
import matplotlib

#Importing dataset
dataset = pd.read_csv("yob2017.csv")
names = dataset.iloc[:,:1].values
total_nums = dataset.iloc[:,2:3].values

matplotlib.use("Cairo")

import matplotlib.pyplot as plt

# pie chart function
def pie_chart(names,total_nums, size):     
    names = names[0:size]
    names = names[:,0]
    total_nums = total_nums[0:size]
    plt.pie(total_nums, labels=names, autopct='%1.1f%%',shadow = True,
            startangle=140)    
    plt.show()
    plt.savefig("plot1.png", dpi = 600)


pie_chart(names,total_nums,15)
