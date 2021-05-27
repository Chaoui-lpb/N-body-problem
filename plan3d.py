from objects import *
from integration import *
from pylab import *

total_obj = []
for i in range(0,len(masses)*6,6): # len(masses)*6 car 1 planète = x,y,z,dx,dy,dz donc 6 infos par planètes
    total_obj.append(big_dstate[:,i])
    total_obj.append(big_dstate[:,i+1])
    total_obj.append(big_dstate[:,i+2])

fig = figure()
ax = fig.add_subplot(111,projection="3d")
ax.autoscale(enable=False,axis='both')

#TODO : Terminer le plot
#TODO : Faire un algo qui otpimise le code et qui trouve tout seul la position la plus lointaine dans big_dstate
#ax.set_xbound(big_dstate.min(),big_dstate.max())
#ax.set_ybound(big_dstate.min(),big_dstate.max())
#ax.set_zbound(big_dstate.min(),big_dstate.max())

ax.set_xbound(-2e12,2e12)
ax.set_ybound(-2e12,2e12)
ax.set_zbound(-2e12,2e12)

for i in range(0, len(masses)*3, 3):
    x = total_obj[i]
    y = total_obj[i+1]
    z = total_obj[i+2]
    plot(x,y,z)
legend(["Soleil","Mercure","Vénus","Terre","Mars","Jupiter","Saturne","Uranus","Neptune"])
title('Système solaire sur 1 an', fontsize=10)
show()
