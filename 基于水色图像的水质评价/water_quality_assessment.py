# !/usr/bin/env python

# _*_ coding: utf-8 _*_

import pandas as pd
import numpy as np

inputfile = '/Users/Mac/Desktop/moment.xls'
data = pd.read_excel(inputfile, encoding='gbk')
data = data.values
np.random.shuffle(data)

# 将数据分为训练数据和测试数据
# 由于数据较小，因此将它们放大一定倍数，提高区分度
train = data[:int(0.8*len(data)), :]*30
test = data[int(0.8*len(data)):, :]*30

x_train = train[:, 2:]
y_train = train[:, 0]

x_test = test[:, 2:]
y_test = test[:, 0]

from sklearn import svm
model = svm.SVC()
model.fit(x_train, y_train)

import pickle
pickle.dump(model, open('/Users/Mac/Desktop/svm.model', 'wb'))

from cm_plot import *
from sklearn.metrics import accuracy_score

cm_plot(y_train, model.predict(x_train)).show()
cm_plot(y_test, model.predict(x_test)).show()

train_accuracy = accuracy_score(y_train, model.predict(x_train))
test_accuracy = accuracy_score(y_test, model.predict(x_test))
print(train_accuracy)
print(test_accuracy)

# 结果
# train_accuracy=0.932098765432
# test_accuracy=0.90243902439
