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
amethod = 0

x = np.linspace(0,2,nx)
y = np.linspace(0,2,ny)

#Create 1xn vector of ones
#'ones' function fills the array with float 1.0
u = np.ones((ny,nx))
un = np.ones((ny,nx))

#I.C. u = 2 @ (0.5 <= x <= 1) and (0.5 <= y <= 1)
u[0.5/dy : 1/dy+1 , 0.5/dx : 1/dx+1]=2


#fig = plt.figure(figsize=(11,7), dpi = 100)
#ax = fig.gca(projection = '3d')

#generate a grid of x and y values for the 3d plot
X, Y = np.meshgrid(x,y)

#surf = ax.plot_surface(X,Y,u[:])
#plt.show()
amethod = raw_input("Please select scheme evaluation method: \n" \
                    "1 -> Nested loop method \n" \
                    "2 -> Array method \n" \
                    "type 1 or 2: ")

if amethod == "1":
    print "Nested loop method selected"
    for n in range(nt+1):
        un = u.copy()
        row, col = u.shape #assign row and col to the array shape
        for j in range(1, row):
            for i in range(1, col):
                u[j,i] = un[j, i] - (c*dt/dx*(un[j,i] - un[j,i-1])) \
                    - (c*dt/dy*(un[j,i] - un[j-1,i]))
                u[0,:] = 1
                u[-1,:] = 1
                u[:,0] = 1
                u[:,-1] = 1
    #initialize the figure window, figsize and dpi are optional
    fig = plt.figure(figsize=(11,7), dpi = 100)
    #assigns axes label ax, and specifyes a 3d projection plot type
    ax = fig.gca(projection = '3d')
    #same as regular plot command, but takes X,Y grid values to plot u
    surf2 = ax.plot_surface(X,Y,u[:])
    plt.show()

else:
    print "Array method selected"
    for n in range(nt+1):
        un = u.copy()
        #u[1:,1:] everything in j,i starting from 1 ????
        u[1:,1:]=un[1:,1:]-(c*dt/dx*(un[1:,1:]-un[1:,:-1])) \
            - (c*dt/dy*(un[1:,1:]-un[:-1,1:]))
        u[0,:] = 1 #everything in the 0th row = 1
        u[-1,:] = 1 #everything in the 0th row -1 = 1
        u[:,0] = 1 #everuthing in the 0th col = 1
        u[:,-1] = 1 #everything in the 0th col -1 = 1

    fig = plt.figure(figsize=(11,7), dpi = 100)
    ax = fig.gca(projection = '3d')
    surf2 = ax.plot_surface(X,Y,u[:])
    plt.show()


