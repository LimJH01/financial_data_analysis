import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
import os

def stat_analysis(feature):

    directory = "C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data"

    for filename in os.listdir(directory):
        # 파일이 디렉토리가 아닌 경우에만 처리
        if os.path.isfile(os.path.join(directory, filename)):
            file_path = os.path.join(directory, filename)
            name, extension = os.path.splitext(filename)

            save_path="C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/ADF_test_analysis_Close.csv"
            # 파일 열기
            df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

            #--------------------------------------ADF검정-------------------------------------------#

            data_length = len(df) - 1

            ADF_result = adfuller(df[feature])


            (f'ADF Statistic: {ADF_result[0]}\n')
            (f'p-value: {ADF_result[1]}')
                
            with open(save_path, 'w') as file:
                if ADF_result[1] < 0.05:
                    file.write(name+" " +ADF_result[0].tostring()+" 귀무가설을 기각 시계열이 정상적이다\n")
                else:
                    file.write(name+" "+ ADF_result[0].tostring() +" 귀무가설을 채택 시계열이 비정상적이다\n")



def ADF_analysis(feature):
    directory = "C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data_ADF_"+feature

    for filename in os.listdir(directory):
        # 파일이 디렉토리가 아닌 경우에만 처리
        if os.path.isfile(os.path.join(directory, filename)):
            file_path = os.path.join(directory, filename)
            #name, extension = os.path.splitext(filename)

            save_path="C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/ADF_test_analysis_"+feature+".csv"
            # 파일 열기
            #df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

            #--------------------------------------ADF검정-------------------------------------------#
            with open(file_path,'r') as r_file:
                name_space = r_file.readline()  # 첫 번째 줄 읽기
                name = name_space.strip()
                ADF_result = r_file.readline()
                line = r_file.readline()  # p-value: 0.3973055601355675
                # 'p-value: ' 부분을 제거하고 숫자만 남기기
                p_value_str = line.replace("p-value: ", "").strip()  # '0.3973055601355675'
                p = float(p_value_str)  # 실수로 변환
            
            with open(save_path, 'a') as file:
                if p < 0.05:
                    file.write(name+" 귀무가설을 기각: 시계열이 정상적이다\n")
                else:
                    file.write(name+"  귀무가설을 채택: 시계열이 비정상적이다\n")

feature='Close'
ADF_analysis(feature)
