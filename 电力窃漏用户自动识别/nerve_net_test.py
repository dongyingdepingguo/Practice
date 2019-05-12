<<<<<<< HEAD

=======
>>>>>>> 9f5e4ab... 添加代码
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

# 对模型进行测试
from keras.models import Sequential
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
from keras.layers.core import Dense, Activation

net = Sequential()      # 设置网络结构，要保证跟先前训练的结构一样
net.add(Dense(units=10,input_dim=3))
net.add(Activation('relu'))
net.add(Dense(1))
net.add(Activation('sigmoid'))
net.compile(loss = 'binary_crossentropy', optimizer='adam')
net.load_weights('/Users/Mac/Desktop/net_model.h5')     # 载入之前保存的权重

predict_result = net.predict(test[:,:3]).reshape(len(test))
fpr, tpr, thresholds = roc_curve(test[:,3], predict_result, pos_label=1)
plt.plot(fpr, tpr, linewidth = 2, label = 'ROC of LM')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.xlim(0,1.05)
plt.ylim(0,1.05)
plt.legend(loc=4)
plt.show()
