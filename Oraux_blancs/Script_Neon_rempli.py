import numpy as np
import matplotlib.pyplot as plt
import sys

sys.path.append('E:\02_Thomas\ENS\Travail\Kholles_et_oraux')  # Ajouter le chemin au sys.path

from Kholle_info_centrale_4 import Fonctions_evolution # Importer le fichier .py
from Kholle_info_centrale_4 import Variables_cachees # Importer le fichier .py

t_fin = 15e-6
N_t = 1000

Temps = np.linspace(0, t_fin, N_t)  #De 0 à t_fin sec

dt = t_fin / N_t

k = 0.3


increment_uc_1, increment_uc_2 = Fonctions_evolution(k, dt)

uc = 0

Uc = [uc]

Non_Claque = True

for indice_date in range(N_t-1):
    if uc >= Variables_cachees()[0]:
        Non_Claque = False
    elif uc <= Variables_cachees()[1] and not Non_Claque:
        Non_Claque = True

    if Non_Claque:
        uc += increment_uc_1(uc)
    else:
        uc += increment_uc_2(uc)

    Uc.append(uc)

plt.plot(Temps, Uc)

plt.xlabel("date (s)")
plt.ylabel("Uc (V)")

plt.grid()

plt.show()