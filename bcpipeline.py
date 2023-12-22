#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

#Importing csv file using pandas
df = pd.read_csv('BreastCancer.csv',skiprows=1)
df.head()

#Cleaning data
# Removing the last row from the DataFrame
last_row_index = df.index[-1]
df = df.drop(last_row_index)

#Creating an 'average' column
df['average'] = df[['2020', '2021', '2022']].mean(axis=1).round(2)

#Loading the data into a database in sqlite3 
conn = sqlite3.connect('BreastCancer_Database.db')

#Loading the data
df.to_sql('BreastCancerAnalysis',conn,if_exists='replace',index=False)

#Closing the connection
conn.close()

print("Completed")