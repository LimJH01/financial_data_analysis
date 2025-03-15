import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.api import VAR
import os
from statsmodels.tsa.stattools import grangercausalitytests, adfuller


def all_var_test():
# 파일들이 저장된 디렉토리 경로
    directory = "C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data/all_stock_data_ratio_Close_round"

    # 디렉토리 내 모든 파일에 대해 처리
    for filename in os.listdir(directory):
        # 파일이 디렉토리가 아닌 경우에만 처리
        if os.path.isfile(os.path.join(directory, filename)):
            file_path = os.path.join(directory, filename)
            name, extension = os.path.splitext(filename)

            # 파일 열기
            df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

            feature_data1 = df[['Close']]  # 'Close_Ratio' 열 선택
            feature_data2 = df[['Volume']]  # 'Volume' 열 선택
            diff = pd.Series(np.diff(df['Close'], n=1))
            feature_data2 = feature_data2.iloc[1:].reset_index(drop=True)



            # 두 열을 결합하여 VAR 모델에 사용할 DataFrame 생성
            data = pd.concat([feature_data2, feature_data1], axis=1)
            data = data.dropna()

            # VAR 모델 학습
            model = VAR(data)

            # 모델 피팅 (lags=2로 설정)
            results = model.fit(2)

            # 결과 출력
            print(results.summary())


            df['Close_diff'] = df['Close'].diff()

            # Granger 인과성 검정: Volume이 Close를 유발하는지 확인
            print('Volume Granger-causes Close?\n')
            print('------------------')
            granger_1 = grangercausalitytests(df[['Close_diff', 'Volume']].dropna(), [2])

            # Granger 인과성 검정: Close가 Volume을 유발하는지 확인
            print('\nClose Granger-causes Volume?\n')
            print('------------------')
            granger_2 = grangercausalitytests(df[['Volume', 'Close_diff']].dropna(), [2])
