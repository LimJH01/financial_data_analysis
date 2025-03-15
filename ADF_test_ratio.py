import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.stattools import adfuller
import os



def get_Close_ADF(feature):
# 파일들이 저장된 디렉토리 경로
    directory = "C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data_ratio_Close"

    # 디렉토리 내 모든 파일에 대해 처리
    for filename in os.listdir(directory):
        # 파일이 디렉토리가 아닌 경우에만 처리
        if os.path.isfile(os.path.join(directory, filename)):
            file_path = os.path.join(directory, filename)
            name, extension = os.path.splitext(filename)

            # 파일 열기
            df = pd.read_csv(file_path, parse_dates=['Date'], index_col='Date')

            #--------------------------------------ADF검정-------------------------------------------#
            feature_data=df[feature]

            if feature_data.isna().any():
                print(name+'\n')
                pass
            else:
                ADF_result = adfuller(df[feature])

                ADF_save_path="C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data_ADF_ratio_Close/"+ name+"_adf_"+feature+".csv"


                with open(ADF_save_path, 'w') as ADF_file:
                    # 파일에 ADF 검정결과를 저장
                    ADF_file.write(name+'\n')
                    ADF_file.write(f'ADF Statistic: {ADF_result[0]}\n')
                    ADF_file.write(f'p-value: {ADF_result[1]}')
        
                #----------------------------------------ACF----------------------------------------------#
                ACF_save_path="C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data_ACF_ratio_Close/"+name+"_acf_plot"+feature+".png"

                # 자기상관(ACF) 플롯

                data_length = len(df) - 1
                # 데이터의 길이가 100 보다 작을때의 예외 처리리
                lags = min(100, max(1, data_length // 3))

                plot_acf(df[feature], lags=lags)

                # 플롯을 저장 (출력하지 않음)
                plt.savefig(ACF_save_path)
                plt.close()
                ACF_describe_save_path="C:/Users/gud66/OneDrive/바탕 화면/시계열/stock_data/all_stock_data_ratio_ADF_describe_Close/"+name+"_acf_describe"+feature+".csv"
                # describe 저장

                with open(ACF_describe_save_path,'w')as ACF_file:
                    ACF_file.write(name+'\n')
                    ACF_file.write(df[feature].describe().to_string())



feature='Close_Ratio'
get_Close_ADF(feature)