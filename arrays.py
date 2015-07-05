#Test in implamenting the array function using numpy


import numpy as np

nx = 3
ny = 3
nt = 2
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
u = np.ones((ny,nx))


numpoints = 6
v = np.ones(numpoints)

print v
print "\n"
#print u
#print "\n"
"""
for n in range(nt):
    un = u.copy()
    u[:,:] = un[:,:] #u[row,col] = u[ny,nx]
    print u
"""
for n in range(nt):
    #move 1 index up from the start and 1 index back from the end, then add 2
    v[1:-1] = v[1:-1]+2  
    v[:] = v[:]+v[:-1]
    print v
    print "\n"
    