import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
import os
import re



def get_Close_ADF():
# 파일들이 저장된 디렉토리 경로
    directory = "C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data_ratio_Close"

    # 디렉토리 내 모든 파일에 대해 처리
    for filename in os.listdir(directory):
        # 파일이 디렉토리가 아닌 경우에만 처리
        if os.path.isfile(os.path.join(directory, filename)):
            file_path = os.path.join(directory, filename)
            name, extension = os.path.splitext(filename)
            numbers = re.findall(r'\d+', name)
            numbers = ''.join(numbers)

            # 파일 열기
            df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')




            save_path="C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data_ratio_Close_round/"+ numbers+"_ratio_Close_round.csv"

            df['Open'] = df['Open'].apply(int)
            df['High'] = df['High'].apply(int)
            df['Low'] = df['Low'].apply(int)
            df['Close'] = df['Close'].apply(int)
            df['Close_Ratio'] = df['Close_Ratio'].round(5)

            df.dropna().to_csv(save_path, index=True)




get_Close_ADF()