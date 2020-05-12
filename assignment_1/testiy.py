# from knmi_api import knmi_api

# plt.figure(figsize=[20,7])
# sns.set_style('darkgrid')
# plt.plot(X_test.index, abs(y - y_pred), label='Prediction', color='blue')
# plt.ylim([0,200])
# plt.legend()

from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib

import seaborn as sns
import pandas as pd
import numpy as np
import mplleaflet

from sklearn.metrics import mean_squared_error
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsClassifier

from IPython.display import clear_output

import warnings
warnings.filterwarnings('ignore')
sns.set()

df = pd.read_csv('../data/bikes.csv', index_col=0)
df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d")

#Makes a copy of the dataframe so that we don't contaminate the original.
occupation_df = df.copy()

#Splits the date and the time into two different columns
occupation_df['start_date'] = pd.to_datetime(df['start_time']).dt.date
occupation_df['start_time'] = pd.to_datetime(df['start_time']).dt.time
occupation_df['end_date'] = pd.to_datetime(df['end_time']).dt.date
occupation_df['end_time'] = pd.to_datetime(df['end_time']).dt.time

#Generates a list of 30 minutes intervals starting at 0:00 ending at 23:30
lis = ['%s:%s' % (h, m) for h in ([0] + list(range(1,24))) for m in ('00', '30')]

#Checks for every time in the time list if that time is between the start and end time of a value in the dataset.
#Returns a serries with booleans representing if the time is between the start and endtime of the row.
#Right now they are all false because in the dataset the start time is equeal to the end time so no values can be inbetween them.
list_of_mask = []
for i in range(len(lis)):
    time = pd.to_datetime(lis[i], format='%H:%M').time()
    print(time)
    print(occupation_df['start_time'])
    print(occupation_df['end_time'])
    print(time >= occupation_df['start_time'])
    print(time <= occupation_df['end_time'])
    a = (time >= occupation_df['start_time']) & (time <= occupation_df['end_time'])
    list_of_mask.append(a)


#Plots the sum of all the bicycles that were occupied at a given time
oc_df = pd.concat(list_of_mask, axis=1)
oc_df.columns = lis
occupation_at_time = oc_df.sum()
occupation_at_time.plot()
occupation_at_time.plot(figsize=(50,30))
plt.xticks(range(0,len(occupation_at_time.index)), occupation_at_time.index)
plt.xticks(fontsize=40, rotation=60)
plt.yticks(fontsize=40)
plt.title("Total occupation at given time", fontsize=50)
plt.show()
