#Python libraries for math and graphics
import numpy as np
import mpmath as mp
import math as m
import random as r
import matplotlib.pyplot as plt
from numpy import linalg as LA
import sympy as sym
import math
import sympy
import sys                                          #for path to external scripts
#sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts
sys.path.insert(0,'/home/dell/matrix/CoordGeo')


#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import circ_gen
from sympy import Poly,roots,simplify
from sympy import*
#if using termux
import subprocess
import shlex
#end if

#Defining f(x)
def f(x):
	return 2*(2*(np.cos(x/2)/np.sin(x/2))+(np.sin(x)/np.cos(x))) 
label_str = "$cot+tan$"

#For minima using gradient ascent
cur_x = 0.1
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 2*(-1/(np.sin(x/2)**2)+1/(np.cos(x)**2))            

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x -= alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

min_val = f(cur_x)
print("Minimum value of f(x) is ", min_val, "at","x =",cur_x)

#Plotting f(x)
x=np.linspace(0,2,10)
y=f(x)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,min_val,'o')
plt.text(cur_x, min_val,f'P({cur_x:.4f},{min_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()
plt.savefig('/home/dell/opt/opt2.pdf')
plt.show()
