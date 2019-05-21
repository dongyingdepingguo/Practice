import pandas as pd
import numpy as np

change_data = pd.read_excel('/Users/Mac/Desktop/change_discdata.xls')
data = change_data.iloc[:len(change_data)-5]

from statsmodels.stats.diagnostic import acorr_ljungbox
[lb, p] = acorr_ljungbox(data['CWXT_DB:184:D'], lags=int(np.log(len(data))))
h = (p < 0.05).sum()
if h > 0:
    print('原始序列为非白噪声序列')
else:
    print('原始序列为白噪声序列')

[ld1, p1] = acorr_ljungbox(data['CWXT_DB:184:C'].diff().dropna(), lags=int(np.log(len(data))))
h1 = (p1 < 0.05).sum()
if h1 > 0:
    print('一阶差分序列为非白噪声序列')
else:
    print('一阶差分序列为白噪声序列')
