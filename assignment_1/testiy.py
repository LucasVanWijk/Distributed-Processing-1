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

occupation_df = df.copy()

#Splits the date and the time into two different columns
occupation_df['start_date'] = pd.to_datetime(df['start_time']).dt.date
occupation_df['start_time'] = pd.to_datetime(df['start_time']).dt.time
occupation_df['end_date'] = pd.to_datetime(df['end_time']).dt.date
occupation_df['end_time'] = pd.to_datetime(df['end_time']).dt.time

def seconds_converter(list_of_times):
    l = []
    for i in list_of_times:
        seconds = int(i[0]) * 36000 + int(i[1]) * 3600 + int(i[3]) * 600 + int(i[4]) * 60 + int(i[6]) * 10 + int(i[7]) 
        l.append(seconds)

    return np.array(l) 

start_in_seconds = seconds_converter(occupation_df['start_time'].astype('str'))
end_in_seconds = seconds_converter(occupation_df['end_time'].astype('str'))
differance = end_in_seconds - start_in_seconds

print("Aantal huren onder de 1 uur {} van de {} dat is {} % van totaal".format(str(np.count_nonzero(differance < 3600)), str(len(differance)), str(np.count_nonzero(differance < 3600) / len(differance) * 100 )))
print("Aantal huren onder de 30 minuten {} van de {} dat is {} % van totaal".format(str(np.count_nonzero(differance < 1800)), str(len(differance)), str(np.count_nonzero(differance < 1800) / len(differance) * 100 )))
print("Aantal huren onder de 15 minuten {} van de {} dat is {} % van totaal".format(str(np.count_nonzero(differance < 900)), str(len(differance)), str(np.count_nonzero(differance < 900) / len(differance) * 100 )))
print("Aantal huren onder de 5 minuten {} van de {} dat is {} % van totaal".format(str(np.count_nonzero(differance < 300)), str(len(differance)), str(np.count_nonzero(differance < 300) / len(differance) * 100 )))
print("Aantal huren onder de 2 minuten {} van de {} dat is {} % van totaal".format(str(np.count_nonzero(differance < 120)), str(len(differance)), str(np.count_nonzero(differance < 120) / len(differance) * 100 )))

print(str(pd.Timedelta(pd.to_datetime(df['end_time']) - pd.to_datetime(df['start_time'])).seconds))

def calculate_occupation(start_in_seconds, end_in_seconds):

    list_of_mask = []
    for time in range(0, 86400,60):
        occupied_at_current_time = (time >= start_in_seconds) & (time <= end_in_seconds)
        list_of_mask.append(pd.Series(occupied_at_current_time))

        presentage_done =  round(time / 864,1)
        if presentage_done % 10 == 0:
            print(str(presentage_done) + "%")

    collum_names = []
    for i in range (0,1440,1):
            minutes = i % 60
            hours = i // 60
            string = "{}:{}".format(hours,minutes)
            collum_names.append(string)



    oc_df = pd.concat(list_of_mask, axis=1)
    oc_df.columns = collum_names
    occupation_at_time = oc_df.sum()

    occupation_at_time.plot()
    occupation_at_time.plot(figsize=(50,30))
    plt.title("Total occupation at given time", fontsize=50)
    plt.show()

#calculate_occupation(start_in_seconds, end_in_seconds)