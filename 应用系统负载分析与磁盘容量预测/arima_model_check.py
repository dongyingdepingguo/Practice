import pandas as pd
import numpy as np

change_data = pd.read_excel('/Users/Mac/Desktop/change_discdata.xls')
data = change_data.iloc[:len(change_data) - 5] #最后5行数据不用于训练
data = data.set_index('COLLECTTIME')

from statsmodels.tsa.arima_model import ARIMA
from statsmodels.stats.diagnostic import acorr_ljungbox

arima = ARIMA(data['CWXT_DB:184:D'], (1, 1, 1)).fit() #训练已经确定的模型
x_predict = arima.predict(typ='levels')
pred_error = (x_predict - data['CWXT_DB:184:D']).dropna() #残差
lb, p = acorr_ljungbox(pred_error, lags=int(np.log(len(pred_error)))) #对残差进行白噪声检验
h = (p < 0.05).sum()
if h > 0:
    print('模型ARIMA(1, 1, 1)的残差不符合白噪声检验')
else:
    print('模型ARIMA(1, 1, 1)的残差符合白噪声检验')
