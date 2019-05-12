import pandas as pd
from sklearn.cluster import KMeans

inputfile = '/Users/Mac/Desktop/zscore_data.xls'
k = 5
iteration = 500

data = pd.read_excel(inputfile)
kmodel = KMeans(n_clusters = k, n_jobs=2, max_iter = iteration)
kmodel.fit(data)

r1 = pd.DataFrame(kmodel.cluster_centers_ )
r2 = pd.Series(kmodel.labels_).value_counts()
r3 = pd.Series(['%0.2f%%'%(i*100/r2.sum()) for i in r2], index = r2.index)
r = pd.concat([r2, r3, r1], axis = 1)
r.columns = ['类别数目']+['样本个数占比'] + list(data.columns)
r.index = ['客户群%s'%i for i in range(1,1+k)]
print(r)

#结果
"""
       类别数目  样本个数占比   C        F         L         M        R
客户群1  15869  38.22% -0.201529 -0.175855 -0.707957 -0.176454 -0.459047
客户群2  10735  25.86% -0.132126 -0.083896  1.132727 -0.091337 -0.318374
客户群3   9214  22.19% -0.184031 -0.583324 -0.343901 -0.543477  1.526111
客户群4   1796   4.33%  2.973227 -0.016552  0.213901 -0.001857 -0.107797
客户群5   3902   9.40%  0.248329  2.331108  0.476168  2.253145 -0.811882
"""
