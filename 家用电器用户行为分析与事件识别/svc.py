# !/usr/bin/env python

# _*_ coding: utf-8 _*_

import pandas as pd

train_filename = '/Users/Mac/Desktop/train_neural_network_data.xls'
test_filename = '/Users/Mac/Desktop/test_neural_network_data.xls'
train_data = pd.read_excel(train_filename)
test_data = pd.read_excel(test_filename)
y_train_data = train_data.iloc[:, 4].as_matrix()
x_train_data = train_data.iloc[:, 5:16].as_matrix()
y_test_data = test_data.iloc[:, 4].as_matrix()
x_test_data = test_data.iloc[:, 5:16].as_matrix()

from sklearn import svm
model = svm.SVC()
model.fit(x_train_data, y_train_data)

from cm_plot import *
cm_plot(y_test_data, model.predict(x_test_data)).show()
