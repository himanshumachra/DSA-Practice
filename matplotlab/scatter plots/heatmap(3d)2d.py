import matplotlib.pyplot as plt
import seaborn as sas 
import random
import pandas as pd

dt = pd.read_csv('IPL_Ball_by_Ball_2008_2022.csv')
dt.head()
tdt=dt[(dt['ballnumber'].isin([1,2,3,4,5,6]))&(dt['batsman_run'])]
grid= tdt.pivot_table(index='overs',columns='ballnumber',values='batsman_run',aggfunc='count')
plt.imshow(grid)
plt.show()