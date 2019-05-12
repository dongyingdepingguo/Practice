import pandas as pd
import numpy as np

filename = '/Users/Mac/Desktop/air_data.xls'
data = pd.read_excel(filename)
result = data.describe().T[['max', 'min']]
result['null'] = len(data) - data.describe().T['count']
result = result[['null', 'min', 'max']]
result.columns = ['空值数', '最小值', '最大值']
result.to_excel('/Users/Mac/Desktop/result_data.xls')

data = data[data['SUM_YR_1'].notnull() & data['SUM_YR_2'].notnull()]  # 丢弃标价为空的记录

index = ((data['SUM_YR_1'] != 0) & (data['SUM_YR_2'] != 0)) | ((data['avg_discount'] == 0) & (data['SEG_KM_SUM'] == 0))  # 丢弃标价为0，平均折扣率不为0，总飞行公里数大于0的记录
data = data[index]
data.to_excel('/Users/Mac/Desktop/data_clean.xls')

data = data[['FFP_DATE','LOAD_TIME','FLIGHT_COUNT','avg_discount','SEG_KM_SUM','LAST_TO_END']]

L = [int(i.days/1) for i in data['LOAD_TIME'] - data['FFP_DATE']]
R = data['LAST_TO_END']
F = data['FLIGHT_COUNT']
M = data['SEG_KM_SUM']
C = data['avg_discount']

change_data = pd.DataFrame(dict((('L',L), ('R', R), ('F', F), ('M', M), ('C', C))))
zscore_data = (change_data - change_data.mean())/change_data.std()
zscore_data.to_excel('/Users/Mac/Desktop/zscore_data.xls')
