#时序图
import matplotlib.pyplot as plt
import pandas as pd

change_data = pd.read_excel('/Users/Mac/Desktop/change_discdata.xls')
change_data = change_data.set_index('COLLECTTIME')
c_data = change_data['CWXT_DB:184:C']
d_data = change_data['CWXT_DB:184:D']
x = change_data.index
plt.figure(dpi=1024)
plt.plot(x, c_data, 'r', label='C disk usage')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.scatter(x, c_data, 10, color='red')
plt.figure(dpi=1024)
plt.plot(x, d_data, 'b', label='D disk usage')
plt.xticks(rotation=45)
plt.legend(loc='upper left')
plt.scatter(x, d_data, 10, color='blue')
plt.show()
