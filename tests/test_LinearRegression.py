import numpy as np
import time

from src.LinearRegression import LinearRegression
import matplotlib.pyplot as plt

def test_linear_regression():
    tiempos = np.array([0,0.005,0.01,0.015,0.02])
    alturas = np.array([300,315,302,400,305])
    a11 = tiempos @ tiempos
    a12 = np.sum(tiempos)
    a22 = len(tiempos)
    coeficientes = np.array([[a11,a12],[a12,a22]])
    start_time = time.time()
    m,b = LinearRegression(tiempos, alturas, coeficientes)
    total_time = time.time()-start_time

    print(f"Total time: {total_time}")

    plot_tiempos = np.linspace(0,0.02)
    x = m*plot_tiempos + b

    plt.scatter(tiempos, alturas, color='red', label='Datos reales')
    plt.plot(plot_tiempos, x, color='blue', label=f'Ajuste: y={m:.2f}x + {b:.2f}')

    # 4. Personalizar (etiquetas y título)
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Altura (m)')
    plt.title('Regresión Lineal: Altura vs Tiempo')
    plt.legend()  # Muestra el cuadrito de referencias
    plt.grid(True)  # Agrega una cuadrícula de fondo

    # 5. Mostrar
    plt.show()