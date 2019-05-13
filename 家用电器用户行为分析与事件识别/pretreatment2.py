import pandas as pd
import numpy as np

data = pd.read_excel('/Users/Mac/Desktop/water_heater.xls')
data['发生时间'] = pd.to_datetime(data['发生时间'], format = '%Y%m%d%H%M%S')
data = data[data['水流量'] > 0]
mlist = []
tlist = np.arange(1,10,0.25)
for i in tlist:
    threshold = pd.Timedelta(minutes = i)
    d = data['发生时间'].diff() > threshold
    m = (d.cumsum()+1).max()
    mlist.append(m)

K = 100
th = 0
for j in range(len(mlist)-4):
    k=0
    for h in range(4):
        k += abs((mlist[j+h]-mlist[j+h+1])/(tlist[j+h]-tlist[j+h+1]))
    K1 = k/4
    if K1 < K:
        K = K1
        th = tlist[j]
    #print(K, th)
if K >= 5:
    th = 4
print(th)
