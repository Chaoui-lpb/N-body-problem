from plan3d import *
from matplotlib import animation
from pylab import *
import numpy as np

#TODO : CLAIREMENT A FINR ET BIEN COMPRENDRE
def animate(i, total_obj, all_lines,fig):
    k = 0
    for j in range(len(all_lines)):
        all_lines[j].set_data(np.array(total_obj[k]),np.array(total_obj[k+1]))
        all_lines[j].set_3d_propreties(np.array(total_obj[k+2]))
        ax.set_xbound(big_dstate.min(), big_dstate.max())
        ax.set_ybound(big_dstate.min(), big_dstate.max())
        ax.set_zbound(big_dstate.min(), big_dstate.max())
        k+=3

    fig.canvas.draw()
    return all_lines

def my_animation(big_dstate, total_obj, masses):

    #Plan 3d
    fig = figure()
    ax = fig.add_subplot(111, projection="3d")
    ax.autoscale(enable=False, axis='both')
    ax.set_xbound(big_dstate.min(), big_dstate.max())
    ax.set_ybound(big_dstate.min(), big_dstate.max())
    ax.set_zbound(big_dstate.min(), big_dstate.max())
    for i in range(0, len(masses)*3, 3):
        x = total_obj[i]
        y = total_obj[i+1]
        z = total_obj[i+2]
        plot(x,y,z)

    #Initialiser les variables de position
    plt.gca().set_prop_cycle(None)
    all_lines = []
    for i in range(0,len(masses)*3, 3):
        line ,= plot(0,0,0,'o')
        all_lines.append(line)

    anim = animation.FuncAnimation(fig, animate, time_intervals, interval=10, fargs=[total_obj,all_lines,fig])

    show()

total_obj = []
for i in range(0, len(masses)*6, 6):  # len(masses)*6 car 1 planète = x,y,z,dx,dy,dz donc 6 infos par planètes
    total_obj.append(big_dstate[:,i])
    total_obj.append(big_dstate[:,i+1])
    total_obj.append(big_dstate[:,i+2])

my_animation(big_dstate, total_obj, masses)