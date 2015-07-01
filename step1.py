'''
CFD ME702 Step 1 // 1D linear convection //

eq: u[i]@ n+1 = u[i] @ n -c*(dt/dx)*(u[i] @n - u[i-1] @n)
in this eq:  transporting some initial profile "u" with velocity "c"
solution: u(x,t)=u_sub_0(x-ct)
Using: Forward Diff in time from n to n+1
       Backward Diff in space from i to i-1
Initial conditions: u=2 at 0.5<= x <=1
                    u=1 everywhere else in (0,2)
Boundary conditions: u=1 at x=0, x=2
'''

import numpy as np
import matplotlib.pyplot as plt
import time as sys

#%matplotlib inline #dispay results in line in ipython notebook
"""init variables"""
nx = 41 #number of points in the grid
dx = 2.0/(nx-1) #distance between adjacent grid points (dx) 0.05 * 40 steps
dt = 0.025 #lenght of time step
nt = 25 #number of time steps
c = 1.0 #transport velocity
#c = 0.5 #will decrease the rate at which u is beeing displaced
#c = 0.00001 #will be the same as the t = 0
"""establish initial conditions"""
u = np.ones(nx) #define an array which with nx elements in lenght
u[0.5/dx : 1/dx+1]=2 # initial condition u = 2 at 0.5 <= x <= 1
print u

plt.plot(np.linspace(0,2,nx),u)

un = np.ones(nx) #init temporary array to store the values of u @ time n
for n in range(1,nt): #run the loop nt times (0 to nt)
    un = u.copy() #copy the value of u(array) into un(array)
    for i in range(1,nx):
    #for i in range(nx): #same for loop, diff syntax
       """the main eq"""       
       u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])
        
plt.plot(np.linspace(0,2,nx),u);
