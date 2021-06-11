# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 13:35:15 2021


@author: bradley.jones
"""

import pandas as pd 
import numpy as np 

path = "C:\\Users\\bradley.jones\\Documents\\Data Analysis Training\\"
CarData = pd.read_csv(path + "Car.csv")

Carsample = CarData.sample(n = 50, replace = False)
print(Carsample)

Carsample['Car Make'].value_counts()

#We are setting up the cluster at random and selecting two teams.
clusters = np.random.choice(np.arange(1,4), size=5)

#We want the conditions to be based off team number
cluster_sample = CarData[CarData['Team Number'].isin(clusters)]

#view first six rows of sample
cluster_sample.head()

#We then run this in the column to validate that it has worked.
cluster_sample['Team Number'].value_counts()