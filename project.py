import pandas as pd
import matplotlib.pyplot as plt
import csv
import shutils

def fileCopie():
    shutils.copyfile('main.csv', 'data.csv')

def changeData():
    df = pd.read_csv('data.csv')

    df['Time'] = df['Time'].str.split().str[1]

    df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S')

    df['Time'] = df['Time'].dt.round('10min')

    df.to_csv('data.csv', index=False)

    df = pd.read_csv('data.csv')

    df.iloc[:, 0] = df.iloc[:, 0].apply(lambda x: x.split()[-1])

    df.to_csv('data.csv', index=False)

def getId():
    try:
        user_input = input("Enter an ID: ")
        return user_input
    except:
        print("Something went terribly wrong")

def main():
    fileCopie()
    getId()
    changeData()
    