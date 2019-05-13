# !/usr/bin/env python

# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np

filename = '/Users/Mac/Desktop/拓展思考样本数据.xls'
dataframe = pd.read_excel(filename)
data = dataframe
rank = {'I':1, 'II':2, 'III':3, 'V':4, 'IV':5, 'VI':6, 'VII':7}
for i in rank:
    data.iloc[:, 6].replace(i, rank[i], inplace = True)

data = data.values
np.random.shuffle(data)

# 分割文件成测试文件和训练文件
x_train = data[:int(0.8*len(data)), :6]
y_train = data[:int(0.8*len(data)), 6]

x_test = data[int(0.8*len(data)):, :6]
y_test = data[int(0.8*len(data)):, 6]

from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.metrics import accuracy_score
import pydotplus
from cm_plot import *

model = DecisionTreeClassifier()
model.fit(x_train, y_train.astype('int'))

# 使用accuracy_score函数计算正确率
train_accuracy = accuracy_score(y_train, model.predict(x_train))
test_accuracy = accuracy_score(y_test, model.predict(x_test))

# 绘制混淆矩阵
cm_plot(y_train, model.predict(x_train)).show()
cm_plot(y_test, model.predict(x_test)).show()

# 输出决策树可视化文件
dot_data = export_graphviz(model, out_file=None, feature_names=list(dataframe.columns)[:6])
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_pdf('/Users/Mac/Desktop/tree.pdf')
print(train_accuracy, test_accuracy)

# 结果
# train_accuracy=1.0
# test_accuracy=0.953125
