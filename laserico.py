import xlrd
import os
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from math import exp, e


def read_file(loc):
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    df = pd.read_excel("C:/Users/USER/Desktop/1.xlsx")
    df = df.fillna(0)
    return df

def plot2d_df(df):
    x = df.columns
    y = df.index
    X, Y = np.meshgrid(x, y)
    Z = df
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.contour(X, Y, Z)
    plt.show()



def plot3d_df(df):
    x = df.columns
    y = df.index
    X, Y = np.meshgrid(x, y)
    Z = df
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    plt.show()


def Anal(df):
    n_elements = df.count()
    temp = df.max()
    maxy = temp.max()
    total = np.count_nonzero(df)
    df_np = df.to_numpy()
    sumy_np = np.sum(df_np > 0)
    sumy_np_e = np.sum(df_np < maxy) - np.sum(df_np > 0)
    print(f'The total number of cells is: {sumy_np}\nThe only max/e number of cells is: {sumy_np_e}')



def main():
    loc = ("C:/Users/USER/Desktop/1.xlsx")
    df = read_file(loc)
    plot2d_df(df)
    plot3d_df(df)
    Anal(df)


main()



