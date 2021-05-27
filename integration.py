from scipy import integrate
import numpy as np
from copy import deepcopy
from scipy.constants import G
from pylab import *
from objects import *

def listoflists_to_flat(compl_list):
    flatList = []
    for elem in compl_list:
        for item in elem:
            flatList.append(item)
    return flatList

def array_tomystruct(array):
    tab = np.ndarray.tolist(array)
    corr_list = []
    for i in range(0,len(tab),6):
        corr_list.append([[tab[i],tab[i+1],tab[i+2]] , [tab[i+3],tab[i+4],tab[i+5]]])
    return corr_list

def couple_function(n):
    """
    :param n: numbers of planets (int)
    :return: couples: list of each pairs of planets to consider (list)
    """
    couples = []
    for i in range(n):
        for j in range(n):
            if i != j: # On n'ajoute pas les couples similaires ni les couples déjà présents mais permutés
                couples.append([i, j])
    return couples

def int_function(vstate, time_intervals, masses):
    n = len(masses) # Numbers of planets
    planets = array_tomystruct(vstate)

    dstate = [] #Deviendra mon énorme vecteur d'état final
    i = 0 # Compteur de tours dans la boucle
    acceleration = [0, 0, 0]
    for j in couple_function(n): # example: 3 planets ; couple = [[0,1],[0,2],[1,0],[1,2],[2,0],[2,1]]
        distance = np.linalg.norm(np.subtract(planets[j[0]][0],planets[j[1]][0]))
        direction = np.subtract(planets[j[1]][0],planets[j[0]][0])
        acceleration += (G*masses[j[1]]*direction)/pow(distance,3)
        i += 1

        if i == n-1:
            dstate = np.concatenate((dstate, planets[j[0]][1], acceleration)) # Grand vecteur d'état regroupant le vecteur d'état de la première planète puis de la seconde et ainsi de suite [dx1,dy1,dz1,ddx1,ddx1,ddx1,dx2,dy2,...]
            acceleration = [0, 0, 0]
            i = 0

    return dstate

vstate0 = np.concatenate((listoflists_to_flat(planet1), listoflists_to_flat(planet2),listoflists_to_flat(planet3),listoflists_to_flat(planet4),listoflists_to_flat(planet5),
                          listoflists_to_flat(planet6),listoflists_to_flat(planet7),listoflists_to_flat(planet8),listoflists_to_flat(planet9)))

time_intervals = np.linspace(0 , 3.154e+7 ,10000) # param1 : The starting value of the sequence. param 2 : The end value of the sequence. param 3 : Number of samples to generate, taille des espaces de temps from : https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
big_dstate = integrate.odeint(int_function, vstate0, time_intervals, args=(masses,))

"""plot
Clairement possible de modifier ici !!
Pas besoin de passer par total_obj
"""


# total_obj = [[x for planet 0 at all time],[y for planet 0 at all time],[z for planet 0 at all time],[x for planet 1 at all time],...]


