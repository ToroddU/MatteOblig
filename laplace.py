import numpy as np
import matplotlib.pyplot as plt



L_x = np.pi
L_y = np.pi
n = 100
h = L_x/n

x = np.linspace(0, L_x, n+1)
y = np.linspace(0, L_y, n+1)



a=0
def f(x):
    return a*x+1


r = np.zeros((n+1, n+1))
#randkrav:

r[0, :] = f(x) 
r[:, 1] = 0 
r[1, :] = 0 
r[:, -1] = 0 



iter = 1000
for i in range(iter):
    for j in range(1, n):  
        for k in range(1, n):
            r[k, j] = (r[k+1, j] + r[k-1, j] + r[k, j+1] + r[k, j-1]) / 4


plt.xlabel("x")
plt.ylabel("y")
plt.contourf(x, y, r, 100, cmap = "viridis")
plt.title("Laplaces likning i 2D, numerisk")
plt.show()