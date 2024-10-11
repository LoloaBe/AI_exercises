
from promptflow import tool
import numpy as np
import pandas as pd




@tool
def my_python_tool():
    df = pd.read_csv('data_files/Social_Network_Ads.csv')
    print ('*****FILE LOADED******')
    #X = df.iloc[:, :-1].values
    #y = df.iloc[:, -1].values
    return df
