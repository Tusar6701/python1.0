import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv("Bahubali2_vs_Dangal.csv")


x1 = dataset.iloc[:, 0:1].values
y1 = dataset.iloc[:, 1:2].values  
y2 = dataset.iloc[:, 2:3].values   

from sklearn.linear_model import LinearRegression
rg = LinearRegression()
rg.fit(x1, y1)

regressor2 = LinearRegression()
regressor2.fit(x1, y2) 

day = input("Enter Day to Check Collection: ")

y1_pred = rg.predict(day)
print ("Bahubali 2 earns".format(day))
print (y1_pred)
y2_pred = regressor2.predict(day)
print ("Dangal earns ".format(day))
print (y2_pred)

plt.plot(x1, y1, color = 'red',label="Bahubali 2")
plt.plot(x1, y2, color = 'green', label="Dangal")
plt.scatter(day, rg.predict(day), color = 'red',s=300)
plt.scatter(day, regressor2.predict(day), color = 'green',s=300)
plt.title('Bahubali 2 vs Dangal')
plt.xlabel('Day')
plt.ylabel('Collection')
plt.legend()
plt.show()

if y1_pred > y2_pred:
 print ("Bahubali 2 will earn more".format(day))
else:
 print ("Dangal will earn more".format(day))