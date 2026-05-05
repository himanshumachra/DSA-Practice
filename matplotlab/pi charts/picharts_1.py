import pandas as pd
import matplotlib.pyplot as plt 

plt.style.use('fivethirtyeight')
d=pd.read_csv('gayle-175.csv')
plt.pie(d['batsman_runs'],labels=d['batsman'],autopct='%0.2f%%',explode=[0.1,0,0,0,0,0],shadow=True)

plt.savefig('fig1.jpg')
# to save the output we usae thr plt savefig('name. extention and do not show like plt.show then the outpuit image is blank)