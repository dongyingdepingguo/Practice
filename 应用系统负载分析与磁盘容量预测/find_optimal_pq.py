import pandas as pd

change_data = pd.read_excel('/Users/Mac/Desktop/change_discdata.xls')
data = change_data.iloc[:len(change_data) - 5]
data = data.set_index('COLLECTTIME')

from statsmodels.tsa.arima_model import ARIMA

pmax = int(len(data) / 10)
qmax = int(len(data) / 10)
bic_matrix = []
for p in range(pmax):
    tmp = []
    for q in range(qmax):
        try:
            tmp.append(ARIMA(data['CWXT_DB:184:D'], (p, 1, q)).fit().bic)
        except:
            tmp.append(None)
    bic_matrix.append(tmp)
bic_matrix = pd.DataFrame(bic_matrix)
print('p, q组合的BIC信息量矩阵：')
print(bic_matrix)
p, q = bic_matrix.stack().idxmin()
print('BIC信息量最小的p, q值：')
print('p=%s, q=%s' % (p, q))
