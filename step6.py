#Step 6 2D Convection
#Dmitriy Bruder
#07/04/2015
#For comments see step 5

from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm #colormap
import sympy as spy

nx = 81
ny = 81
nt = 100
dx = 2.0/(nx-1)
dy = 2.0/(ny-1)
sigma = 0.2
dt = sigma*dx

x = np.linspace(0,2,nx)
y = np.linspace(0,2,ny)

u = np.ones((ny,nx))
v = np.ones((ny,nx))
un = np.ones((ny,nx))
vn = np.ones((ny,nx))

u[0.5/dx : 1/dx+1 , 0.5/dx : 1/dx+1] = 2
v[0.5/dx : 1/dx+1 , 0.5/dx : 1/dx+1] = 2

amethod = raw_input("Please select scheme evaluation method: \n" \
                    "1 -> Nested loop method \n" \
                    "2 -> Array method \n" \
                    "type 1 or 2: ")

if amethod == "1":
    print "Nested loop method selected"
    for n in range (nt+1):
        un = u.copy()
        vn = v.copy()
        urow, ucol = u.shape
        vrow, vcol = v.shape

        for j in range(1, urow):
            for i in range(1, ucol):
                u[j,i] = un[j, i] - (un[j,i]*dt/dx*(un[j,i] - un[j,i-1])) \
                        - (vn[j,i]*dt/dy*(un[j,i] - un[j-1,i]))

        for j in range(1, vrow):
            for i in range(1, vcol):
                v[j,i] = vn[j, i] - (un[j,i]*dt/dx*(vn[j,i] - vn[j,i-1])) \
                            - (vn[j,i]*dt/dy*(vn[j,i] - vn[j-1,i]))
                u[0,:]=1
                u[-1,:]=1
                u[:,0]=1
                u[:,-1]=1

                v[0,:]=1
                v[-1,:]=1
                v[:,0]=1
                v[:,-1]=1


    fig=plt.figure(figsize=(11,7), dpi=100)
    ax = fig.gca(projection = '3d')
    X,Y = np.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,u, cmap=cm.coolwarm)
    plt.show()
else:
    print "Array method selected"
    for n in range (nt+1):
            un = u.copy()
            vn = v.copy()
            u[1:,1:] = un[1:, 1:] - (un[1:,1:]*dt/dx*(un[1:,1:] - un[1:,:-1])) \
                - (vn[1:,1:]*dt/dy*(un[1:,1:] - un[:-1,1:]))

            v[1:,1:] = vn[1:, 1:] - (un[1:,1:]*dt/dx*(vn[1:,1:] - vn[1:,:-1])) \
                - (vn[1:,1:]*dt/dy*(vn[1:,1:] - vn[:-1,:1]))
            u[0,:]=1
            u[-1,:]=1
            u[:,0]=1
            u[:,-1]=1

            v[0,:]=1
            v[-1,:]=1
            v[:,0]=1
            v[:,-1]=1


    fig=plt.figure(figsize=(11,7), dpi=100)
    ax = fig.gca(projection = '3d')
    X,Y = np.meshgrid(x,y)
    surf = ax.plot_surface(X,Y,u, cmap=cm.coolwarm)
    plt.show()





