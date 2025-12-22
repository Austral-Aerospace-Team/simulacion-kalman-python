import pandas as pan
import numpy as np
import matplotlib.pyplot as plt
from sensors.barometro import Barometro
from sensors.acelerometro import Acelerometro

# Leer CSV (ignora comentarios)
datos = pan.read_csv("resources/prueba_simu.csv", comment="#", decimal=',')

# Pasar a numpy
tiempos = datos["Tiempo (s)"][305:365]
altitudes = datos["Altitud (m)"][305:365]
velocities = datos["Velocidad total (m/s)"][305:365]
acelerations = datos["AceleraciÃ³n total (m/sÂ²)"][305:365]


#Sensores
barometro = Barometro()
acelerometro = Acelerometro()





# Crear subplots compartiendo eje X
fig, axs = plt.subplots(2, 2, sharex=True, figsize=(10, 8))

bar_prueba = []
acel_prueba = []
for s,v,a in zip(altitudes,velocities,acelerations):
    bar_prueba.append(barometro.lectura(s, v, a))
    acel_prueba.append(acelerometro.lectura(a))




# Altura
axs[0,0].plot(tiempos, altitudes)
axs[0,0].plot(tiempos, bar_prueba, color ="red", linestyle ="dotted")
axs[0,0].set_title("Tiempo vs Altura")
axs[0,0].set_ylabel("Altura [m]")

errores = np.array(bar_prueba) - np.array(altitudes)

axs[0,1].plot(tiempos,errores)
axs[0,1].set_title("Errores barometro")
axs[0,1].set_ylabel("Error de medicion [m]")


"""# Velocidad
axs[1,0].plot(tiempos, velocities)
axs[1,0].set_title("Tiempo vs Velocidad")
axs[1,0].set_ylabel("Velocidad [m/s]")"""

# Aceleración
axs[1,0].plot(tiempos, acelerations)
axs[1,0].plot(tiempos, acel_prueba, color ="red", linestyle ="dotted")
axs[1,0].set_title("Tiempo vs Aceleración")
axs[1,0].set_ylabel("Aceleración [m/s²]")
axs[1,0].set_xlabel("Tiempo [s]")

errores_acel = np.array(acel_prueba) -np.array(acelerations)
axs[1,1].plot(tiempos, errores_acel)
axs[1,1].set_title("Errores aceleracion")
axs[1,1].set_ylabel("Aceleracion [m/s²")

# Ajuste automático de espacios
plt.tight_layout()
plt.show()
