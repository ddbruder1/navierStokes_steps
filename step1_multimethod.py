# -*- coding: utf-8 -*-
# this is a test:;
"""
Created on Mon Jun 29 13:29:45 2015

@author: MGhost
"""


import numpy as np
import matplotlib.pyplot as plt
#matplotlib.use('TkAgg')
import pylab
#UI variables
#init variables

print "Please select scheme to use: \n" \
      "1  B.D. in space\n" \
      "2  C.D. in space\n" \
      "2  F.D. in space\n" \

userInput = raw_input("Type 1, 2 or 3: ")

nx = 41 #number of points in the grid
dx = 2.0/(nx-1) #distance between adjacent grid points (dx) 0.05 * 40 steps
dt = 0.025 #lenght of time step
nt = 25 #number of time steps
c = 1.0 #transport velocity
sigma = c*dt/dx

print sigma
# array index
u = np.ones(nx) #define an array which with nx elements in lenght
un = np.ones(nx) #init temporary array to store the values of u @ time n

u[0.5/dx : 1/dx+1]=2 # initial condition u = 2 at 0.5 <= x <= 1

plt.plot(np.linspace(0,2,nx),u)

def BDScheme():
    for n in range(1,nt): #run the loop nt times (0 to nt)
        un = u.copy() #copy the value of u(array) into un(array)
        for i in range(1,nx):
            u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])
    plt.plot(np.linspace(0,2,nx),u)
def CDScheme():
    for n in range(1,nt): #run the loop nt times (0 to nt)
        un = u.copy() #copy the value of u(array) into un(array)
        for i in range(1,nx):
            u[i] = un[i]-c*dt/2*dx*(un[i+1]-un[i-1])
    plt.plot(np.linspace(0,2,nx),u)
def FDScheme():
    for n in range(1,nt): #run the loop nt times (0 to nt)
        un = u.copy() #copy the value of u(array) into un(array)
        for i in range(1,nx):
            u[i] = un[i]-c*dt/2*dx*(un[i+1]-un[i])
    plt.plot(np.linspace(0,2,nx),u)

def test():
    print "test"

message = "You have selected option "
if userInput == "1":
    print message + "%s -> BD" % (userInput)
    BDScheme()
elif userInput == "2":
    print message + "%s -> CD" % (userInput)
    CDScheme()
elif userInput == "3":
    print message + "%s -> FD" % (userInput)
    FDScheme()
else:
    print "Invalid"
plt.show()
#raw_input()
