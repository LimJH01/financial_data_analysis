import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
import os




def get_ratio():
# 파일들이 저장된 디렉토리 경로
    directory = "C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data"

    # 디렉토리 내 모든 파일에 대해 처리
    for filename in os.listdir(directory):
        # 파일이 디렉토리가 아닌 경우에만 처리
        if os.path.isfile(os.path.join(directory, filename)):
            file_path = os.path.join(directory, filename)
            name, extension = os.path.splitext(filename)

            # 파일 열기
            df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

            #--------------------------------------ADF검정-------------------------------------------#
            

            # 전날 Close 값을 저장하는 열 생성 (shift 함수 사용)
            df['Previous_Close'] = df['Close'].shift(1)

            # 전날 Close와 당일 Close의 비율 계산
            df['Close_Ratio'] = df['Close'] / df['Previous_Close']

            # 새로운 파일로 저장 (NaN 행 제거)
            save_path="C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data_ratio_Close/"+ name+"ratio_Close.csv"
            df.dropna().to_csv(save_path, index=True)

            



            #fig, ax = plt.subplots(figsize=(20, 10)) 
            #ax.plot(df['Close_Ratio'])  
            #ax.set_xlabel('Time')
            #ax.set_ylabel('Price')

            # 날짜 포맷 조정
            #fig.autofmt_xdate()

#            그래프 간격 자동 조정
            #plt.tight_layout()

            # 그래프 저장
            #graph_path = "C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data_ratio_plot_Close/"+name+"ratio_plot_Close.png"
            #plt.tight_layout()
            #plt.savefig(graph_path, dpi=300)

            #plt._pyplot.close()




                
get_ratio()