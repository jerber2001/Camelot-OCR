import pandas as pd
import numpy as np
import sys
import os

data_path = '/Users/jycai/OneDrive - PennO365/Python Projects/Data/'

df = pd.read_csv(data_path+'Selected_Tennis_Data.csv')
print(df.head())

first_name = []
last_name = []

#Go down the list with iterative from n [0,64] and find 