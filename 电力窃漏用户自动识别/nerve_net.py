# !/usr/bin/env python

# _*_ coding: utf-8 _*_

import pandas as pd
from random import shuffle  # 导入随机函数shuffle，打乱数据

inputfile = '/Users/Mac/Desktop/model.xls'
data = pd.read_excel(inputfile)
data = data.as_matrix()
shuffle(data)   # 将数据打乱


# 将文件分割为训练部分和测试部分
p=0.8
train = data[:int(len(data)*p),:]   # 前80%为训练部分
test = data[int(len(data)*p):,:]    # 后20%为测试部分

# 构建神经网络模型
from keras.models import Sequential
from keras.layers.core import Dense, Activation


netfile = '/Users/Mac/Desktop/net_model.h5'     # 创建保存模型的文件
net = Sequential()
net.add(Dense(units=10,input_dim=3))    # input_dim表示输入层节点数量，unit表示隐含层节点数量
net.add(Activation('relu'))     # 设置隐含层激活函数
net.add(Dense(1))       # 设置输入层节点
net.add(Activation('sigmoid'))      # 设置输入层激活函数
net.compile(loss = 'binary_crossentropy', optimizer='adam')

net.fit(train[:,:3], train[:,3], epochs=1000, batch_size=1)

predict_result = net.predict_classes(train[:,:3]).reshape(len(train))
net.save_weights(netfile)   # 保存模型权重

from cm_plot import *
cm_plot(train[:,3],predict_result).show()
