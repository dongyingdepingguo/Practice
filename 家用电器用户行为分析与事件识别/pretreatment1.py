import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('/Users/Mac/Desktop/water_heater.xls')
data['发生时间'] = pd.to_datetime(data['发生时间'], format = '%Y%m%d%H%M%S')
data = data[data['水流量'] > 0]
plt.figure(figsize=(8,6), dpi=120)
mlist = []
tlist = np.arange(1,10,0.25)
for i in tlist:
    threshold = pd.Timedelta(minutes = i)
    d = data['发生时间'].diff() > threshold
    m = (d.cumsum()+1).max()
    mlist.append(m)
    plt.scatter([i], [m], 10, color='red')
plt.plot(tlist, mlist, color='red', linewidth=1.0, linestyle='-')
plt.show()
