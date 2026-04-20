import matplotlib.pyplot as plt
import seaborn as sas 
import random
import pandas as pd


# use this loop to put the actual data name to the point and see it in the graph 
dt=pd.read_csv('batter.csv')

fig = plt.figure()
ax= plt.subplot(projection='3d')
ax.scatter3D(dt['runs'],dt['avg'],dt['strike_rate'],color='red')

#for pointing the names 
for i in range(dt.shape[0]):
    ax.text(dt['runs'].values[i],dt['avg'].values[i],dt['strike_rate'].values[i],dt['batter'].values[i])
plt.show()