import numpy as np
import matplotlib.pyplot as plt

def Fonctions_evolution(k, dt):
    E = 5
    Rg = 10
    Rm = k*Rg/(1-k)
    C = 10**-7

    t1 = Rg*C
    t2 = k*t1

    increment_uc_1 = lambda uc: E/t1*dt-uc/t1*dt

    increment_uc_2 = lambda uc: E/t1*dt-uc/t2*dt

    return(increment_uc_1, increment_uc_2)

def Variables_cachees(a=1):
    U1 = 2.7
    U2 = 1.6
    return(U1, U2)