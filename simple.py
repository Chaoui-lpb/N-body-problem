from scipy import integrate
import numpy as np
from scipy.constants import G
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

obj1 = [0,-1,0,-0.01,0,0] #[x,y,z,dx,dy,dz] #m, #m/s
m1 = 10e6 #kg
obj2 = [0,1,0,0.01,0,0]
m2 = 10e6
#obj3 = [0,0,1,0,0,0]
#m3 = 10e6
x0 = np.concatenate((obj1,obj2))
m=[m1,m2]

def f(x,t,m):
    astres = [x[6*i:6*i+6] for i in range(len(m))]
    
    astres = []
    for i in range(len(m)):
        xastre=x[6*i:6*i+6]
        astres.append(xastre)
    
    
    dstate=[]
    for source_i in range(len(astres)):
        acceleration=[0,0,0]
        for effect_i in range(len(astres)):
            if source_i!=effect_i:
                dist = np.linalg.norm(astres[source_i][0:3]-astres[effect_i][0:3]) #|[x1,y1,z1]-[x2,y2,z2]| = r
                direction = astres[effect_i][0:3]-astres[source_i][0:3] #[x2,y2,z2]-[x1,y1,z1] = r21
                acceleration+=G*m[effect_i]*direction/pow(dist,3) #a = G*m2*r21/r³
        dstate = np.concatenate((dstate,astres[source_i][3:6],acceleration))
    return(dstate)

t = np.linspace(0, 1000, 10000)
x=integrate.odeint(f,x0,t,args=(m,)) #ODEINT, algo LSODA

#Display sur graphique
astres=[]
for i in range(len(m)):
    astrex=[]
    astrey=[]
    astrez=[]
    for xt in x:
        astrex.append(xt[i*6])
        astrey.append(xt[i*6+1])
        astrez.append(xt[i*6+2])
    astres.append([astrex,astrey,astrez])
    
fig = figure()
ax = fig.add_subplot(111, projection='3d')
ax.autoscale(enable=False,axis='both')
ax.set_xbound(-1,1)
ax.set_ybound(-1,1)
ax.set_zbound(-1,1)
for i in astres:
    plot(i[0],i[1],i[2],'-',linewidth=1)
legend(['une planète','une autre planète','un autre machin'])


show()
