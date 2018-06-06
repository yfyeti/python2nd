import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# mpl.rcParams['font.sans-serif'] = 'SimHei'

a = 1
t = np.linspace(0, 2*np.pi, 1024)
x = a*(2*np.cos(t)-np.cos(2*t))
y = a*(2*np.sin(t)-np.sin(2*t))
plt.subplot(111)
plt.plot(y, x, 'r--')
plt.figtext(0.5, 0.9, '笛卡尔心脏线', ha='center')
plt.axis('off')
plt.show()
