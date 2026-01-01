from src.Simulators.Simulator import Simulator
import matplotlib.pyplot as plt

class NoiseSimulator(Simulator):
    def simulate(self, baro, acel, kal, tiempos, altitudes, velocidades, aceleraciones):
        figures = []
        bar_prueba = []
        acel_prueba = []
        for s, v, a in zip(altitudes, velocidades, aceleraciones):
            bar_prueba.append(baro.lectura(s, v, a))
            acel_prueba.append(acel.lectura(a))

        altFig, alt = plt.subplots()
        alt.plot(tiempos, altitudes, label="Trayectoria Real")
        alt.plot(tiempos, bar_prueba, label="Trayectoria Sensada", color="red", linestyle="dotted")
        alt.set_xlabel("Tiempo (s)")
        alt.set_ylabel("Altitud (m)")
        alt.legend()
        alt.grid(True)
        figures.append(altFig)
        #st.pyplot(altFig)

        accFig, acc = plt.subplots()
        acc.plot(tiempos, aceleraciones, label="Aceleraciones Reales")
        acc.plot(tiempos, acel_prueba, label="Aceleraciones Sensadas")
        acc.set_xlabel("Tiempo (s)")
        acc.set_ylabel("Aceleración (m/s^2)")
        acc.legend()
        acc.grid(True)
        figures.append(accFig)
        #st.pyplot(accFig)
        return figures