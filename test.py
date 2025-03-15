import statsmodels.api as sm
from statsmodels.tsa.api import VAR
import pandas as pd
import statsmodels.tsa.stattools as sts 



# 데이터 읽기
df = pd.read_csv(r"C:\Users\gud66\OneDrive\바탕 화면\시계열\stock_data\all_stock_data_ratio_Close_round\005380_ratio_Close_round.csv")

# 필요한 열만 선택하여 DataFrame 생성
feature_data1 = df[['Volume']]  # 'Close_Ratio' 열 선택
feature_data2 = df[['Close']]  # 'Volume' 열 선택

# 두 열을 결합하여 VAR 모델에 사용할 DataFrame 생성
data = pd.concat([feature_data1, feature_data2], axis=1)
# 정상성 검사
# 두번째줄이 p-value p-value가 0.05 이하일때 정상성을 가지고 있다고 봄 

maxlag = 100
VAR_model = VAR(data) 
lag_order =VAR_model.select_order(maxlag)
print(lag_order.summary())