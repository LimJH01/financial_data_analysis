import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

df=pd.read_csv("C:\\jj.csv")

print(df.head())

print(df.tail())

# 여기서 인덱스 지정 실수해서 값이 이상하게 나옴옴
train=df[:-4]
test=df[-4:]

last_year_mean=np.mean(train.data[-4:])

print(last_year_mean)

# 과거의 평균을 예측값으로 설정한다.
test.loc[:,'pred__last_yr_mean']=last_year_mean

# 평균절대백분율오차 MAPE

test


def mape(y_true, y_pred):
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

mape_last_year_mean = mape(test['data'], test['pred__last_yr_mean'])
print(mape_last_year_mean)

fig, ax = plt.subplots()

ax.plot(train['date'], train['data'], 'g-.', label='Train')
ax.plot(test['date'], test['data'], 'b-', label='Test')
ax.plot(test['date'], test['pred__last_yr_mean'], 'r--', label='Predicted')
ax.set_xlabel('Date')
ax.set_ylabel('Earnings per share (USD)')
ax.axvspan(80, 83, color='#808080', alpha=0.2)
ax.legend(loc=2)

plt.xticks(np.arange(0, 85, 8), [1960, 1962, 1964, 1966, 1968, 1970, 1972, 1974, 1976, 1978, 1980])

fig.autofmt_xdate()
plt.tight_layout()

plt.show()