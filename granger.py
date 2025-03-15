# VAR로 방정식의 계수를 구해준다
import numpy as np
import pandas as pd
import statsmodels.api as sm
from statsmodels.tsa.api import VAR
from statsmodels.tsa.stattools import grangercausalitytests, adfuller

# 데이터 읽기
df = pd.read_csv(r"C:\Users\gud66\OneDrive\바탕 화면\시계열\stock_data\all_stock_data_ratio_Close_round\298020_ratio_Close_round.csv")

# 필요한 열만 선택하여 DataFrame 생성
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