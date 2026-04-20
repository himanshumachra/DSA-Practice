import matplotlib.pyplot as plt
import seaborn as sas 
import random
import pandas as pd

# use this loop to put the actual data name to the point and see it in the graph 
plt.figure(figsize=(18,8))
dt = pd.read_csv('batter.csv')
plt.scatter(dt['strike_rate'],dt['avg'],color='black',marker='o')
plt.xlabel('strike rate')
plt.ylabel('average runs')
plt.title('avg player buying info')
plt.axhline(45,color='red')
plt.axvline(178,color='green')

for i in range(dt.shape[0]):
    plt.text(dt['strike_rate'].values[i],dt['avg'].values[i],dt['batter'].values[i])
plt.show()






# use this for manual pointing the name of the batter or the elements

"""x = [54, 41, 69, 76, 93, 36, 99, 64, 95, 66, 96, 52, 42, 62]
y = [4, 12, 3, 21, 16, 6, 22, 15, 13, 19, 14, 7, 10, 5]

plt.scatter(x,y)
plt.text(54,4,'point1')

plt.show()
"""