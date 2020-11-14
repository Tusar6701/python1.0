# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 20:55:43 2020

@author: Tusar Ranjan Mahapatra
"""

#Day 2 Code Challenge 1
import matplotlib.pyplot as plt

branch = ['Civil Engineering', 'Electrical Engineering', 'Mechanical Engineering', 'Chemical Engineering']
strength = [15000,50000,45000,10000]
plt.title("Strength of students pursuing engineering in US per year(based on branch)")
plt.pie(strength, labels=branch)
df = plt.pie(strength, labels=branch)

#Day 2 Code Challenge 2

import matplotlib.pyplot as plt

x = ['Nuclear', 'Hydro', 'Gas', 'Oil', 'Coal', 'Biofuel']
energy = [5, 6, 15, 22, 24, 8]

plt.title("ENERGY")
plt.bar(x, energy)