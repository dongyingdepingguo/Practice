# 数据前处理的代码重复部分略去
# 构建CART决策树模型
from sklearn.tree import DecisionTreeClassifier

treefile = '/Users/Mac/Desktop/tree.pkl'
tree = DecisionTreeClassifier()
tree.fit(train[:,:3],train[:,3])

from sklearn.externals import joblib
joblib.dump(tree, treefile)     # 这里使用joblib模块来保存模型数据

from cm_plot import *
cm_plot(train[:,3], tree.predict(train[:,:3])).show()


# 数据前处理部分略去
#模型测试
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
from sklearn.externals import joblib

tree = joblib.load('/Users/Mac/Desktop/tree.pkl')

fpr, tpr, thresholds = roc_curve(test[:,3], tree.predict_proba(test[:,:3])[:,1],pos_label=1)
plt.plot(fpr, tpr, linewidth = 2, label = 'ROC of CART')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.ylim(0, 1.05)
plt.xlim(0, 1.05)
plt.legend(loc=4)
plt.show()
