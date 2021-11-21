import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline

files = ['algorithm1.csv', 'algorithm2.csv', 'algorithm3.csv', 'algorithm4.csv']

algorithm1 = pd.read_csv('algorithm1.csv', header=None)
x = algorithm1[0]
y = algorithm1[1]
XYSpline = make_interp_spline(x, y)
X = np.linspace(min(x), max(x), 500)
Y = XYSpline(X)
plt.plot(x, y)

algorithm2 = pd.read_csv('algorithm2.csv', header=None)
x = algorithm2[0]
y = algorithm2[1]
XYSpline = make_interp_spline(x, y)
X = np.linspace(min(x), max(x), 500)
Y = XYSpline(X)
plt.plot(x, y)

algorithm3 = pd.read_csv('algorithm3.csv', header=None)
x = algorithm3[0]
y = algorithm3[1]
XYSpline = make_interp_spline(x, y)
X = np.linspace(min(x), max(x), 500)
Y = XYSpline(X)
plt.plot(x, y)

algorithm4 = pd.read_csv('algorithm4.csv', header=None)
x = algorithm4[0]
y = algorithm4[1]
XYSpline = make_interp_spline(x, y)
X = np.linspace(min(x), max(x), 500)
Y = XYSpline(X)
plt.plot(x, y)

plt.legend(['Algorithm 1', 'Algorithm 2', 'Algorithm 3', 'Algorithm 4'])
plt.show()

# for file in files:
#     data = pd.read_csv(file, header=None)
#     x = data[0]
#     y = data[1]
#     XYSpline = make_interp_spline(x, y)
#     X = np.linspace(min(x), max(x), 500)
#     Y = XYSpline(X)
#     plt.plot(X, Y)
#     plt.title(file[:file.index('.csv')])
#     plt.xlabel('List size')
#     plt.ylabel('Average time per search (s)')
#     plt.xticks([10, 50, 100, 250, 500, 1000, 2000, 3000, 4000, 5000, 10000])
#     plt.show()