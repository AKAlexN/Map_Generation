import numpy as np
from matplotlib import pyplot as plt

f = open(".\examp4.txt", 'r')
data_raw = f.readlines()
f.close()
n = len(data_raw)
data = np.zeros((n, 684))
for i in range(n):
    line = data_raw[i]
    a = line.replace(',', '')
    a = a.replace(';', '')
    a = a.split()
    new_line = list(map(float,a))
    data[i,:] = new_line

x, y, angle = data[:,0], data[:,1], data[:,2]

theta = np.radians(np.linspace(-120, 121, 681))
a, b, = [], []

plt.figure(1)
for i in range(n):
    for j in range(3,684):
        if 2.0 < data[i,j] < 5.6:
            a.append(np.cos(angle[i]-theta[j])*(data[i,j])+x[i]+0.3*np.cos(angle[i]))
            b.append(np.sin(angle[i]-theta[j])*(data[i,j])+y[i]+0.3*np.sin(angle[i]))

plt.plot(x,y)
plt.scatter(a,b, color="red");       
plt.xlabel('x')
plt.ylabel('y')

plt.show()
