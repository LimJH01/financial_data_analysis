import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
import os

def find_h():
    with open("C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/ADF_test_analysis_Close.csv",'r') as file:
        i=0
        while True:
            line=file.readline()
            if not line:
                break
            if "비정상" in line:
                pass
            else:
                line=line.strip()
                print(line)
                i=i+1
    return i

print(find_h())