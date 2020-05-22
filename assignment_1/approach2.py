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

day_count = df.date.groupby(df.date.dt.floor('d')).count()
df_day = pd.DataFrame([day_count.index,day_count.values]).T
df_day.columns = ['date', 'count']
df_day.date = pd.to_datetime(df_day.date)
df_day['month'] = df_day.date.dt.month.astype('category')
df_day['weekday'] = df_day.date.dt.weekday.astype('category')
df_day['day'] = df_day.date.dt.dayofyear.astype('int')
df_day['count'] = df_day['count'].astype('int')
df_day.count = df_day['count'].astype('int')

# ten_most_rentals = df_day.sort_values('count',ascending=False)
# ten_most_rentals = ten_most_rentals.head(100)
# dates_of_ten_most_rentals = list(ten_most_rentals['date'])


#Makes a copy of the dataframe so that we don't contaminate the original.
occupation_df = df.copy()

#Splits the date and the time into two different columns
occupation_df['start_date'] = pd.to_datetime(df['start_time']).dt.date
occupation_df['start_time'] = pd.to_datetime(df['start_time']).dt.time
occupation_df['end_date'] = pd.to_datetime(df['end_time']).dt.date
occupation_df['end_time'] = pd.to_datetime(df['end_time']).dt.time

#occupation_df = occupation_df.loc[occupation_df['start_date'].isin(dates_of_ten_most_rentals)]

#Generates a list of 30 minutes intervals starting at 0:00 ending at 23:30
#lis = ['%s:%s' % (h, m) for h in ([0] + list(range(1,288))) for m in ('00', '05')]

#Checks for every time in the time list if that time is between the start and end time of a value in the dataset.
#Returns a serries with booleans representing if the time is between the start and endtime of the row.
#Right now they are all false because in the dataset the start time is equeal to the end time so no values can be inbetween them.

def seconds_converter(list_of_times):
    l = []
    for i in list_of_times:
        seconds = int(i[0]) * 36000 + int(i[1]) * 3600 + int(i[3]) * 600 + int(i[4]) * 60 + int(i[6]) * 10 + int(i[7]) 
        l.append(seconds)

    return np.array(l) 

start_in_seconds = seconds_converter(occupation_df['start_time'].astype('str'))
end_in_seconds = seconds_converter(occupation_df['end_time'].astype('str'))
differance = end_in_seconds - start_in_seconds

def calc_ussage_between_interval(interval,start_in_seconds,end_in_seconds):
    """Calculates how many bikes are in use between the given interval. So if given a interval hour it will
    calcultate how many bike where in use at 01:00,02:00,etc 

    :param interval: How many seconds need te be inbetween intervals
    :type interval: int
    :param start_in_seconds: a np array of the ammount of seconds every start time is from start of the day
    :type start_in_seconds: Np array
    :param end_in_seconds: a np array of the ammount of seconds every end time is from start of the day
    :type end_in_seconds: Np array
    """
    collum_names = []
    for i in range (0,86400 - interval,interval):
        interval_minutes = (i % 3600) / 60
        interval_hours = i // 3600
        string = "{}:{}".format(interval_hours,interval_minutes)
        collum_names.append(string)

    list_of_mask = []
    for start_time_inteval in range(0, 86400 - interval, interval):
        end_time_interval = start_time_inteval + interval
        occupied_at_current_time = (start_in_seconds >= start_time_inteval) & (end_in_seconds <= end_time_interval)
        list_of_mask.append(pd.Series(occupied_at_current_time))

    presentage_done =  round(end_time_interval / 864,1)
    if presentage_done % 10 == 0:
        print(str(presentage_done) + "%")

    oc_df = pd.concat(list_of_mask, axis=1)
    oc_df.columns = collum_names
    return oc_df

# Plots the sum of all the bicycles that were occupied at a given time
occupation_at_time = calc_ussage_between_interval(3600,start_in_seconds,end_in_seconds).sum()
occupation_at_time.plot()
occupation_at_time.plot(figsize=(50,30))
plt.xticks(fontsize=40, rotation=60)
plt.yticks(fontsize=40)
plt.title("Total occupation at given time", fontsize=50)
plt.show()


print("values under 5 minutes " + str(np.count_nonzero(differance < 300)) + "\n \n" + "total records  " + str(len(differance)))


    
