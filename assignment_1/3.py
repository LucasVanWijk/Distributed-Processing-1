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

occupation_df['start_time'] = pd.to_datetime(occupation_df['start_time'], format="%Y-%m-%d")
occupation_df['end_time'] = pd.to_datetime(occupation_df['end_time'], format="%Y-%m-%d")

occupation_df['diff'] = occupation_df['end_time'] - occupation_df['start_time']
print(occupation_df['diff'])

occupation_df['diff']

def temp(x):
    return np.count_nonzero(occupation_df['diff'].dt.total_seconds() < x)

print("Aantal huren onder de 1 uur      {} van de {} dat is {} % van totaal".format(temp(3600), len(occupation_df['diff']), round(temp(3600) / len(occupation_df['diff']) * 100, 2)))
print("Aantal huren onder de 30 minuten {} van de {} dat is {} % van totaal".format(temp(1800), len(occupation_df['diff']), round(temp(1800) / len(occupation_df['diff']) * 100, 2)))
print("Aantal huren onder de 15 munten  {} van de {} dat is {} % van totaal".format(temp(900), len(occupation_df['diff']), round(temp(900) / len(occupation_df['diff']) * 100, 2)))
print("Aantal huren onder de 1 minuut   {} van de {} dat is {} % van totaal".format(temp(300), len(occupation_df['diff']), round(temp(300) / len(occupation_df['diff']) * 100, 2)))