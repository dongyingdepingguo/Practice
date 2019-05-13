# !/usr/bin/env python

# _*_ coding: utf-8 _*_

import pandas as pd

datafile = '/Users/Mac/Desktop/data.xls'
dataframe_all = pd.read_excel(datafile)
dataframe = dataframe_all.iloc[:, 0:6]

k = 4
iteration = 500
pre = []

for i in range(6):
    from sklearn.cluster import KMeans

    data = dataframe.iloc[:,i]
    model = KMeans(n_clusters=k, n_jobs=2, max_iter=iteration)
    model.fit(data.values.reshape(-1, 1))
    r1 = pd.Series(model.labels_)


    data2 = pd.concat([data, r1], axis = 1)
    data2.columns = ['系数',dataframe.columns[i]]
    r2 = data2.groupby(dataframe.columns[i]).max().sort_values(by='系数')['系数']
    r3 = pd.Series(model.labels_).value_counts()
    r = pd.concat([r3, r2], axis=1)
    r.columns = ['聚类个数', dataframe.columns[i]+'范围']
    r.sort_values(by=r.columns[1], inplace = True)

    print(r.T)

    range_symbol = ['A', 'B', 'C', 'D', 'E', 'F']
    for j in range(len(r)):
        data2[dataframe.columns[i]].replace(list(r.index)[j], '%s%s'%(range_symbol[i],j+1), inplace = True)
    # print(data2)

    pre.append(data2.iloc[:,1])

pre.append(dataframe_all.iloc[:, 7])
pre_data = pd.concat(pre, axis=1)

pre_data.to_excel('/Users/Mac/Desktop/pre_data.xls')
