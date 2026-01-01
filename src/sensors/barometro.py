import numpy as np


class Barometro():
    def __init__(self, sigma=3, bias=0.5):
        self.sigma = sigma  # Ruido aleatorio (metros)
        self.bias = bias  # Error sistemático constante (offset)
        self.velocidad_sonido = 343.0  # m/s (ajustable según temperatura)

    def lectura(self, altitud, velocidad, aceleracion):
        # 1. Número de Mach
        mach = abs(velocidad) / self.velocidad_sonido

        # 2. Aumentamos el ruido Gaussiano
        # Multiplicamos el sigma por un factor para que el "serrucho" sea visible
        # También hacemos que la vibración (aceleración) afecte más
        sigma_dinamico = self.sigma + (abs(aceleracion) * 0.5)
        ruido = np.random.normal(0, sigma_dinamico)

        # 3. Error de Venturi (Succión) - EXAGERADO para visualización
        # Si quieres que la línea roja se separe de la azul, sube este número (ej. 80 o 100)
        error_succion = 40.0 * (mach ** 2)

        # 4. Picos transónicos
        # Simulamos "glitches" de presión cuando el aire es inestable
        pico_aleatorio = 0
        if 0.7 < mach < 1.1:
            pico_aleatorio = np.random.uniform(-15, 15)

        # Resultado final
        medicion = altitud + self.bias + ruido + error_succion + pico_aleatorio

        return medicion