import pandas as pan
import numpy as np
class DataReader:
    def __init__(self, filePath = "resources/prueba_simu.csv"):
        self.filePath = filePath



    def read(self, startTime = 0, endTime= 91.897):
        """
        Lee los datos que le pedis de la simulacion
        :param startTime: momento donde queres empezar a leer
        :param endTime: momento donde queres que termine de leer
        :return: (tiempos, altitudes, velocities, accelerations, iniciales)
        """
        datos = pan.read_csv("resources/prueba_simu.csv", comment="#", decimal=',')
        tiempos_totales = datos["Tiempo (s)"]
        a,b = self.extraer_intervalo(tiempos_totales, startTime, endTime)
        tiempos = tiempos_totales[a,b]
        altitudes = datos["Altitud (m)"][a,b]
        velocities = datos["Velocidad total (m/s)"][a,b]
        accelerations = datos["AceleraciÃ³n total (m/sÂ²)"][a,b]
        iniciales = []
        if a == 0:
            iniciales = [0,0,0]
        else:
            iniciales.append(datos["Altitud (m)"][a-1])
            iniciales.append(datos["Velocidad total (m/s)"][a-1])
            iniciales.append(datos["AceleraciÃ³n total (m/sÂ²)"][a-1])
        return tiempos, altitudes, velocities, accelerations, iniciales


    def extraer_intervalo(self, tiempos, startTime, endTime):
        # 1. Encontrar el índice del valor más cercano al inicio
        idx_inicio = np.abs(tiempos - startTime).argmin()

        # 2. Encontrar el índice del valor más cercano al fin
        idx_fin = np.abs(tiempos - endTime).argmin()

        return idx_inicio, idx_fin
