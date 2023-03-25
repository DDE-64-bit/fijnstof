import pandas as pd

df = pd.read_csv('data.csv')

df['Time'] = pd.to_datetime(df['Time'])

df['Hour'] = df['Time'].dt.hour
df['Minute'] = df['Time'].dt.minute
df['Second'] = df['Time'].dt.second

print(df)
