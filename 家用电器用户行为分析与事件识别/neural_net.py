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

from keras.models import Sequential
from keras.layers.core import Dense, Activation

model = Sequential()
model.add(Dense(units=17, input_dim=11))
model.add(Activation('relu'))
model.add(Dense(units=10))
model.add(Activation('relu'))
model.add(Dense(units=1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(x_train_data, y_train_data, nb_epoch=150, batch_size=1)

y_pre = model.predict_classes(x_test_data)

from cm_plot import *
cm_plot(y_test_data, y_pre).show()
