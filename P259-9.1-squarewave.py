import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

mpl.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# mpl.rcParams['font.sans-serif'] = 'SimHei'

def fourier(x, y, n):
    x1 = []
    for i in range(n):
        x1.append(np.sin(x * i + x))
        x1.append(np.cos(x * i + x))
    m = np.mat(x1).T
    y.shape = (y.shape[0], 1)
    p = m * np.linalg.inv(m.T * m) * m.T * y
    ym = np.array(p)
    ym.shape = (ym.shape[0],)
    return ym


x = np.linspace(-10, 10, 300)
y = []
for i in x:
    if np.sin(i) > 0:
        y.append(-1)
    else:
        y.append(1)
y = np.array(y)
plt.figure(figsize=(16, 9))
# plt.plot(x, y, color='g', label=u'方波')
plt.plot(x, fourier(x, y, 3), color='r', label=u'3')
plt.plot(x, fourier(x, y, 8), color='b', label=u'8')
plt.plot(x, fourier(x, y, 50), color='k', label=u'50')
plt.legend()
plt.axis('equal')
plt.show()
