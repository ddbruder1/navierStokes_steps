#Step 5 2D Convection
#Dmitriy Bruder
#07/02/2015

#Lib for projected 3D plots
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import matplotlib.pyplot as plt
import sympy as spy

nx = 81
ny = 81
nt = 100
c = 1.0
dx = 2.0/(nx-1)
dy = 2.0/(ny-1)
sigma = 0.2
dt = sigma*dx/c

x = np.linspace(0,2,nx)
y = np.linspace(0,2,ny)

#Create 1xn vector of ones
u = np.ones((ny,nx))
un = np.ones((ny,nx))

#I.C. u = 2 @ (0.5 <= x <= 1) and (0.5 <= y <= 1)
u[0.5/dy : 1/dy+1 , 0.5/dx : 1/dx+1]=2


#fig = plt.figure(figsize=(11,7), dpi = 100)
#ax = fig.gca(projection = '3d')
X, Y = np.meshgrid(x,y)
#surf = ax.plot_surface(X,Y,u[:])
#plt.show()


for n in range(nt+1):
    un = u.copy()
    row, col = u.shape
    for j in range(1, row):
        for i in range(1, col):
            u[j,i] = un[j, i] - (c*dt/dx*(un[j,i] - un[j,i-1])) \
                - (c*dt/dy*(un[j,i] - un[j-1,i]))
            u[0,:] = 1
            u[-1,:] = 1
            u[:,0] = 1
            u[:,-1] = 1

fig = plt.figure(figsize=(11,7), dpi = 100)
ax = fig.gca(projection = '3d')
surf2 = ax.plot_surface(X,Y,u[:])
plt.show()

