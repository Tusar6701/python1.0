# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 22:21:37 2020

@author: Tushar
"""


import numpy as np
import matplotlib as mpl
import pandas as pd
import matplotlib.pyplot as plt
#TO CHECK FOR SIGNIFICANCE:-
dataset = pd.read_csv("C:/Users/KIIT/Desktop/Python Class Assignments/ML/Female_Stats.csv")
features = dataset.iloc[:, 1:].values
labels = dataset.iloc[:, 0:1].values
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.2, random_state = 0)
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train, labels_train)
prdctn = regressor.predict(features_test)
x=pd.DataFrame(list(zip(prdctn, labels_test)))
x.ndim
x=np.array(x)
s=0
for i in range (0,len(x)):
    s=s+(x[i][0]-x[i][1])
avg=s/len(x)
if avg<1:
    print("Both Predictors Are Significant For A Students’ Height")
else:
    print("Both Predictors Are NOT Significant For A Students’ Height")


#Keeping Father's height constant, check the change in the student's height with the Mother's height:-
#Using dummy values to get a random prediction
features1=[60,70] #constant height of dad kept at 70 inches
features1=np.array(features1)
features1=features1.reshape(1,2)
label1=regressor.predict(features1)
#Increasing the mother's height in the dummy values to get the increase in the student's height
features2=[61,70]
features2=np.array(features2)
features2=features2.reshape(1,2)
label2=regressor.predict(features2)
diff=float(label2-label1)
print("Increase in the height of the daughter with Father's ht constant and increase in mother's height by 1 inch will be ",diff, " inches.")

#Keeping Mother's height constant, check the change in the student's height with the Father's height:-
#Using dummy values to get a random prediction
features1=[60,70] #constant height of mom kept at 60 inches
features1=np.array(features1)
features1=features1.reshape(1,2)
label1=regressor.predict(features1)
#Increasing the father's height in the dummy values to get the increase in the student's height
features2=[60,71]
features2=np.array(features2)
features2=features2.reshape(1,2)
label2=regressor.predict(features2)
diff=float(label2-label1)
print("Increase in the height of the daughter with Mother's ht constant and increase in father's height by 1 inch will be ",diff, " inches.")
