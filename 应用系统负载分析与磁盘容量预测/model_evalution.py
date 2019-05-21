import pandas as pd
import numpy as np

change_data = pd.read_excel('/Users/Mac/Desktop/change_discdata.xls')
data = change_data.iloc[:len(change_data) - 5]
data = data.set_index('COLLECTTIME')

from statsmodels.tsa.arima_model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox

arima = ARIMA(data['CWXT_DB:184:D'], (1, 1, 1)).fit()
predict_value = arima.predict('2014-11-12', '2014-11-16', dynamic='True', typ='levels')
true_value = change_data.iloc[len(change_data) - 5:].set_index('COLLECTTIME')['CWXT_DB:184:D']
pre_data = pd.concat([true_value, predict_value], axis=1)
pre_data.columns = ['true_value_D', 'predict_value_D']
pre_data.to_excel('/Users/Mac/Desktop/pre_data.xls')
pre_data = pd.read_excel('/Users/Mac/Desktop/pre_data.xls')
pre_value = pre_data['predict_value_D']
true_value = pre_data['true_value_D']
change_value = 1024*1024

abs_ = (pre_value - true_value).abs()
mae_ = abs_.mean()
rmse_ = ((abs_**2).mean())**0.5
mape_ = (abs_/true_value).mean()

print('平均绝对误差：%0.4f.\n均方根误差：%0.4f.\n平均绝对百分误差：%0.4f.'%(mae_/change_value, rmse_/change_value, mape_*100))
