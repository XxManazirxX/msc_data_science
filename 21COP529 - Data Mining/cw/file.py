import matplotlib.pyplot as plt
import numpy as np
import pandas as pd



df = pd.read_csv('Data.csv')
print(df.head())

df1 = df.dropna()
print(df1.head())


df1.to_csv('respiratory_data.csv',index = False)