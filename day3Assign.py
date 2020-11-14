# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 15:31:19 2020
Day 3
@author: Tushar


Code Challenge
  Name: 
    Food Truck Profit Prediction Tool
  Filename: 
    Foodtruck.py
  Dataset:
    Foodtruck.csv
  Problem Statement:
    Suppose you are the CEO of a restaurant franchise and are considering 
    different cities for opening a new outlet. 
    
    The chain already has food-trucks in various cities and you have data for profits 
    and populations from the cities. 
    
    You would like to use this data to help you select which city to expand to next.
    
    Perform Simple Linear regression to predict the profit based on the 
    population observed and visualize the result.
    
    Based on the above trained results, what will be your estimated profit, 
    
    If you set up your outlet in Jaipur? 
    (Current population in Jaipur is 3.073 million)
        
  Hint: 
    You will implement linear regression to predict the profits for a 
    food chain company.
    Foodtruck.csv contains the dataset for our linear regression problem. 
    The first column is the population of a city and the second column is the 
    profit of a food truck in that city. 
    A negative value for profit indicates a loss.
"""

#day3 task
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv("Foodtruck.csv")

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


from sklearn.linear_model import LinearRegression
rg = LinearRegression()
rg.fit(X_train, y_train)


y_pred = rg.predict(X_test)
print (y_pred)


plt.scatter(X_train, y_train)
plt.plot(X_train, rg.predict(X_train), color = 'blue')
plt.title('Profit chart')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()

plt.scatter(X_test, y_test)
plt.plot(X_train, rg.predict(X_train))
plt.title('Profit chart')
plt.xlabel('Population')
plt.ylabel('Profit')
plt.show()
