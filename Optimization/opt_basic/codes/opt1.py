import numpy as np
import mpmath as mp
import matplotlib.pyplot as plt
from numpy import linalg as LA
import cvxpy  as cp

import sys                                          #for path to external scripts
#sys.path.insert(0,'/storage/emulated/0/github/cbse-papers/CoordGeo')         #path to my scripts
sys.path.insert(0,'/home/dell/opt/CoordGeo')

#local imports
from line.funcs import *
from triangle.funcs import *
from conics.funcs import *

#if using termux
import subprocess
import shlex
#end if

# ax+by+cz >= d
A = np.array([[4,1],[2,1],[1,0],[0,1]])
A_b = np.array([80,60,0,0]).reshape(4,1)
# objective function coeffs
c = np.array([10, 4])
x = cp.Variable((2,1),nonneg=True)
#Cost function
f = c@x
obj = cp.Minimize(f)
#Constraints
constraint = [ A@x >= A_b]

#solution
prob = cp.Problem(obj, constraint)
prob.solve()
#print("status:", prob.status)
print("optimal value:", np.round(f.value))
print("optimal var:", np.round(x.value.T))

x1=np.linspace(-10,80,200)
#print(len(x1))
y1=(80-4*x1)
y2=(60-2*x1)
plt.plot(x1,y1,label='4x+y=80')
plt.plot(x1,y2,label='2x+y=60')
#y4=np.zeros(len(x1))
#plt.plot(x1,y4,label='y=0')
#plt.plot(y4,x1,label='x=0')
plt.title('')
#plt.ylim([-2,8])
# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=1,linestyle='--')
plt.legend()
plt.savefig('/home/dell/opt/optfig.pdf')
#subprocess.run(shlex.split("termux-open /sdcard/Download/anusha1/python1/opt1.pdf"))
plt.show()
