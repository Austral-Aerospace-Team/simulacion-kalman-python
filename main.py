import pandas as pan
import numpy as np
import matplotlib.pyplot as plt
from sensors.barometro import Barometro
from sensors.acelerometro import Acelerometro
from kalman import Kalman

# Leer CSV (ignora comentarios)
datos = pan.read_csv("resources/prueba_simu.csv", comment="#", decimal=',')


#Defino que analizo
apogeo = True
activar_kalman = True


tiempos = []
altitudes = []
velocities = []
accelerations = []
iniciales = []

if apogeo:
    tiempos = datos["Tiempo (s)"][290:380]
    altitudes = datos["Altitud (m)"][290:380]
    velocities = datos["Velocidad total (m/s)"][290:380]
    acelerations = datos["AceleraciÃ³n total (m/sÂ²)"][290:380]
    iniciales.append(datos["Altitud (m)"][289])
    iniciales.append(datos["Velocidad total (m/s)"][289])
    iniciales.append(datos["AceleraciÃ³n total (m/sÂ²)"][289])

else:
    tiempos = datos["Tiempo (s)"]
    altitudes = datos["Altitud (m)"]
    velocities = datos["Velocidad total (m/s)"]
    acelerations = datos["AceleraciÃ³n total (m/sÂ²)"]
    iniciales = [0,0,0]


#Defino desvios
desvio_baro = 2
desvio_acel = 1
desvio_modelo = 1


#Sensores
barometro = Barometro(desvio_baro)
acelerometro = Acelerometro(desvio_acel)

#Modelo
kalman = Kalman(desvio_modelo, desvio_baro, desvio_acel, iniciales)




"""if not activar_kalman:

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
else:
    # Crear subplots compartiendo eje X
    fig, axs = plt.subplots(2, 2, sharex=True, figsize=(10, 8))

    kalman_altitud = []
    kalman_aceleración =[]
    for s,v,a in zip(altitudes, velocities, acelerations):
        ks,kv,ka = kalman.iterate(s,v,a,barometro.lectura(s,v,a), acelerometro.lectura(a))
        kalman_altitud.append(ks)
        kalman_aceleración.append(ka)
    # Altura
    axs[0, 0].plot(tiempos, altitudes)
    axs[0, 0].plot(tiempos, kalman_altitud, color="red", linestyle="dotted")
    axs[0, 0].set_title("Tiempo vs Altura")
    axs[0, 0].set_ylabel("Altura [m]")

    errores = np.array(kalman_altitud) - np.array(altitudes)

    axs[0, 1].plot(tiempos, errores)
    axs[0, 1].set_title("Errores barometro")
    axs[0, 1].set_ylabel("Error de medicion [m]")

    # Aceleración
    axs[1, 0].plot(tiempos, acelerations)
    axs[1, 0].plot(tiempos, kalman_aceleración, color="red", linestyle="dotted")
    axs[1, 0].set_title("Tiempo vs Aceleración")
    axs[1, 0].set_ylabel("Aceleración [m/s²]")
    axs[1, 0].set_xlabel("Tiempo [s]")

    errores_acel = np.array(kalman_aceleración) - np.array(acelerations)
    axs[1, 1].plot(tiempos, errores_acel)
    axs[1, 1].set_title("Errores aceleracion")
    axs[1, 1].set_ylabel("Aceleracion [m/s²")

    # Ajuste automático de espacios
    plt.tight_layout()
    plt.show()"""




#debug
fig, axs = plt.subplots(2, 2, sharex=True, figsize=(10, 8))

kalman_altitud = []
kalman_aceleración =[]
kalman_predicción = []
kalman_medicion = []
for s,v,a in zip(altitudes, velocities, acelerations):
    xp,z,k = kalman.iterate(s,v,a,barometro.lectura(s,v,a), acelerometro.lectura(a))
    kalman_altitud.append(k[0])
    kalman_aceleración.append(k[2])
    kalman_predicción.append(xp[0])
    kalman_medicion.append(z[0])
# Altura
axs[0, 0].plot(tiempos, altitudes)
axs[0, 0].plot(tiempos, kalman_altitud, color="red", linestyle="dotted")
axs[0, 0].plot(tiempos, kalman_predicción, color="green", linestyle="--")
axs[0, 0].plot(tiempos, kalman_medicion, color="orange", linestyle="--")
axs[0, 0].set_title("Tiempo vs Altura")
axs[0, 0].set_ylabel("Altura [m]")

errores = np.array(kalman_altitud) - np.array(altitudes)

axs[0, 1].plot(tiempos, errores)
axs[0, 1].set_title("Errores barometro")
axs[0, 1].set_ylabel("Error de medicion [m]")

# Aceleración
axs[1, 0].plot(tiempos, acelerations)
axs[1, 0].plot(tiempos, kalman_aceleración, color="red", linestyle="dotted")
axs[1, 0].set_title("Tiempo vs Aceleración")
axs[1, 0].set_ylabel("Aceleración [m/s²]")
axs[1, 0].set_xlabel("Tiempo [s]")

errores_acel = np.array(kalman_aceleración) - np.array(acelerations)
axs[1, 1].plot(tiempos, errores_acel)
axs[1, 1].set_title("Errores aceleracion")
axs[1, 1].set_ylabel("Aceleracion [m/s²")

# Ajuste automático de espacios
plt.tight_layout()
plt.show()



