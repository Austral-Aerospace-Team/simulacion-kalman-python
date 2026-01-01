from src.Simulators.Simulator import Simulator
import matplotlib.pyplot as plt

class KalmanSimulator(Simulator):
    def simulate(self, baro, acel, kal, tiempo, altitudes, velocidades, aceleraciones):
        figures = []
        # debug
        altFig, axs = plt.subplots()

        kalman_altitud = []
        kalman_aceleración = []
        kalman_predicción = []
        kalman_medicion = []
        for s, v, a in zip(altitudes, velocidades, aceleraciones):
            xp, z, k = kal.iterate(s, v, a, baro.lectura(s, v, a), acel.lectura(a))
            kalman_altitud.append(k[0])
            kalman_aceleración.append(k[2])
            kalman_predicción.append(xp[0])
            kalman_medicion.append(z[0])
        # Altura
        axs.plot(tiempo, altitudes, label="Altura Real")
        axs.plot(tiempo, kalman_altitud, color="red", linestyle="dotted", label="Altura Kalman")
        axs.plot(tiempo, kalman_predicción, color="green", linestyle="--", label="Altura Predicha")
        axs.plot(tiempo, kalman_medicion, color="orange", linestyle="--", label="Altura Sensada")
        axs.set_title("Tiempo vs Altura")
        axs.set_xlabel("Tiempo [s]")
        axs.set_ylabel("Altura [m]")
        axs.legend()
        axs.grid(True)
        figures.append(altFig)

        """errores = np.array(kalman_altitud) - np.array(altitudes)

        axs[0, 1].plot(tiempo, errores)
        axs[0, 1].set_title("Errores barometro")
        axs[0, 1].set_ylabel("Error de medicion [m])"""


        acelFig, axs2 = plt.subplots()

        # Aceleración
        axs2.plot(tiempo, aceleraciones, label= "Aceleracion Real")
        axs2.plot(tiempo, kalman_aceleración, color="red", linestyle="dotted", label= "Aceleración Kalman")
        axs2.set_title("Tiempo vs Aceleración")
        axs2.set_ylabel("Aceleración [m/s²]")
        axs2.set_xlabel("Tiempo [s]")
        axs2.legend()
        axs2.grid(True)
        figures.append(acelFig)

        """errores_acel = np.array(kalman_aceleración) - np.array(acelerations)
        axs[1, 1].plot(tiempos, errores_acel)
        axs[1, 1].set_title("Errores aceleracion")
        axs[1, 1].set_ylabel("Aceleracion [m/s²")"""

        return figures