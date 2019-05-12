def radar_chart(vars,vars2, content):
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import math

    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False

    plt.figure(figsize = (10,6), dpi = 100)
    plt.subplot(111)

    N = len(vars)  # 变量数
    alpha = [2*np.pi*i/N for i in range(N)]  # 各辐射线段的角度

    content_data = pd.DataFrame(content)
    min_data = min(content_data.min())
    max_data = max(content_data.max())
    an_distance = [min_data+(max_data-min_data)*i/6 for i in range(7)]
    R = list(range(2, 13, 2))  # 半径
    rho = 12/(max_data-min_data)

    for al in alpha:      # 绘制辐射状线段
        plt.axes(aspect = 1)
        plt.plot([0, (12 * np.cos(al))],[0, (12 * np.sin(al))], color='black', linestyle='-', alpha = 0.1)

    for an_dis, dis in zip(an_distance, list(range(0,13,2))):
        plt.annotate('%.1f'%an_dis, xy=(dis,0),xytext=(dis-0.5,-1))

    for m in R:    # 绘制网状多边形
        for k in range(N):
            if k < N-1:
                plt.plot([m * np.cos(alpha[k]), m * np.cos(alpha[k+1])],
                     [m * np.sin(alpha[k]), m * np.sin(alpha[k+1])],
                     color = 'black', alpha = 0.2)
            else:
                plt.plot([m * np.cos(alpha[k]), m * np.cos(alpha[0])],
                     [m * np.sin(alpha[k]), m * np.sin(alpha[0])],
                     color = 'black', alpha = 0.2)
    for co,ex in enumerate(content):
        color=['red', 'green', 'blue', 'yellow', 'black', 'cyan', 'magenta', 'brown', 'coral',
              'gray', 'navy', 'orchid', 'peru', 'silver']
        z = list(zip(alpha, ex))
        for c in range(N):   # 绘制雷达图
            if c < N-1:
                plt.plot([(z[c][1]-min_data)*rho*np.cos(z[c][0]), (z[c+1][1]-min_data)*rho*np.cos(z[c+1][0])],
                     [(z[c][1]-min_data)*rho*np.sin(z[c][0]), (z[c+1][1]-min_data)*rho*np.sin(z[c+1][0])],
                    color = color[co], alpha = 0.8)
            else:
                plt.plot([(z[c][1]-min_data)*rho*np.cos(z[c][0]), (z[0][1]-min_data)*rho*np.cos(z[0][0])],
                     [(z[c][1]-min_data)*rho*np.sin(z[c][0]), (z[0][1]-min_data)*rho*np.sin(z[0][0])],
                    color = color[co], alpha = 0.8, label=vars2[co])
                plt.legend()


    q = list(zip(alpha, vars))
    for k in range(N):    # 添加标注
        plt.annotate(q[k][1], xy=(R[-1] * np.cos(q[k][0]), R[-1] * np.sin(q[k][0])),
                 xytext = (R[-1] * 1.05 * np.cos(q[k][0]), R[-1] *1.05* np.sin(q[k][0])), fontsize=18)

    plt.xlim(-1.2*R[-1], 1.2*R[-1])
    plt.ylim(-1.1*R[-1], 1.1*R[-1])

    plt.xticks([])
    plt.yticks([])
    
    return plt

import matplotlib.pyplot as plt
客户群1=[-0.201529, -0.175855, -0.707957, -0.176454, -0.459047]
客户群2=[-0.132126, -0.083896,  1.132727, -0.091337, -0.318374]
客户群3 =[-0.184031, -0.583324, -0.343901, -0.543477, 1.526111]
客户群4=[2.973227, -0.016552, 0.213901, -0.001857, -0.107797]
客户群5=[0.248329, 2.331108, 0.476168, 2.253145, -0.811882]
example = [客户群1,客户群2,客户群3,客户群4,客户群5]
radar_chart(['C','F','L','M','R'], ['客户群%s'%i for i in range(1,6)], example)
plt.show()
