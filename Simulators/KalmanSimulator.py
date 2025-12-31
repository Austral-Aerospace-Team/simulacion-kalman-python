from Simulators.Simulator import Simulator
import matplotlib.pyplot as plt

class KalmanSimulator(Simulator):
    def simulate(self, baro, acel, kal, tiempo, altitudes, velocidades, aceleraciones):
        figures = []
        fig,axs = plt.subplots()
        axs.plot(tiempo,altitudes)
        axs.text(0.5, 0.5, 'NO HAY KALMAN',
                 fontsize=15,
                 color='red',
                 fontweight='bold',
                 ha='center', va='center',  # Centra el texto en el punto
                 transform=axs.transAxes,  # Coordenadas relativas al cuadro (0 a 1)
                 zorder=10,  # Asegura que esté por encima de las líneas
                 bbox=dict(facecolor='white',  # Color de fondo para "tapar" lo de atrás
                           edgecolor='black',
                           boxstyle='round,pad=1',
                           alpha=0.9))  # Opacidad (1.0 tapa t0do)
        figures.append(fig)

        fig2,axs2 = plt.subplots()
        axs2.plot(tiempo,aceleraciones)
        axs2.text(0.5, 0.5, 'NO HAY KALMAN',
                 fontsize=15,
                 color='red',
                 fontweight='bold',
                 ha='center', va='center',  # Centra el texto en el punto
                 transform=axs2.transAxes,  # Coordenadas relativas al cuadro (0 a 1)
                 zorder=10,  # Asegura que esté por encima de las líneas
                 bbox=dict(facecolor='white',  # Color de fondo para "tapar" lo de atrás
                           edgecolor='black',
                           boxstyle='round,pad=1',
                           alpha=0.9))  # Opacidad (1.0 tapa t0do)
        figures.append(fig2)

        return figures