import pandas as pd

change_data = pd.read_excel('/Users/Mac/Desktop/change_discdata.xls')
data = change_data.iloc[:len(change_data) - 5]

from statsmodels.tsa.stattools import adfuller as ADF

d = 0
adf = ADF(data['CWXT_DB:184:D'])
print('原始序列单位根检验结果：')
print(adf)
while adf[1] >= 0.05:
    d += 1
    adf = ADF(data['CWXT_DB:184:C'].diff(d).dropna())
print('%s阶差分后序列单位根检验结果：' % d)
print(adf)
