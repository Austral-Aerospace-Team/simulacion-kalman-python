import pandas as pan
import numpy as np
import matplotlib.pyplot as plt
from sensors.barometro import Barometro
from sensors.acelerometro import Acelerometro

# Leer CSV (ignora comentarios)
datos = pan.read_csv("resources/prueba_simu.csv", comment="#", decimal=',')

# Pasar a numpy
tiempos = datos["Tiempo (s)"][310:365]
altitudes = datos["Altitud (m)"][310:365]
velocities = datos["Velocidad total (m/s)"][310:365]
acelerations = datos["AceleraciÃ³n total (m/sÂ²)"][310:365]


#Sensores
barometro = Barometro()





# Crear subplots compartiendo eje X
fig, axs = plt.subplots(1, 2, sharex=True, figsize=(10, 8))

lec_prueba = []
for s,v,a in zip(altitudes,velocities,acelerations):
    lec_prueba.append(barometro.lectura(s,v,a))




# Altura
axs[0].plot(tiempos, altitudes)
axs[0].plot(tiempos,lec_prueba, color = "red", linestyle = "dotted")
axs[0].set_title("Tiempo vs Altura")
axs[0].set_ylabel("Altura [m]")

errores = np.array(lec_prueba) - np.array(altitudes)

axs[1].plot(tiempos,errores)
axs[1].set_title("Errores barometro")
axs[1].set_ylabel("Error de medicion [m]")


"""# Velocidad
axs[1,0].plot(tiempos, velocities)
axs[1,0].set_title("Tiempo vs Velocidad")
axs[1,0].set_ylabel("Velocidad [m/s]")

# Aceleración
axs[1,1].plot(tiempos, acelerations)
axs[1,1].set_title("Tiempo vs Aceleración")
axs[1,1].set_ylabel("Aceleración [m/s²]")
axs[1,1].set_xlabel("Tiempo [s]")"""

# Ajuste automático de espacios
plt.tight_layout()
plt.show()
