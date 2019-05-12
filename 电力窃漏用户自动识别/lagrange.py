# !/usr/bin/env python

# _*_ coding: utf-8 _*_

# 使用拉格朗日插值法填入空缺值

import pandas as pd
from scipy.interpolate import lagrange

inputfile = '/Users/Mac/Desktop/missing_data.xls'
outputfile = '/Users/Mac/Desktop/processes_missing_data.xls'

data = pd.read_excel(inputfile, header=None)    # 读入文件

def ployinterp_column(s, n, k=5):       # 定义插值函数
    y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))]    # k为插值前后距离
    y = y[y.notnull()]
    return lagrange(y.index, list(y))(n)

# 检查每列中的每个值是否为空值，并对空值进行插值

for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j] = ployinterp_column(data[i], j)

data.to_excel(outputfile, header=None, index = False)
