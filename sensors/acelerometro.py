import numpy as np


class Acelerometro:
    def __init__(self, sigma_ms2=0.5, bias_ms2=0.2):
        self.sigma = sigma_ms2  # Usar el valor directo
        self.bias = bias_ms2
        self.g = 9.81
        self.rango_mpu = 16 * self.g

    def lectura(self, real_ms2):
        # Ruido dinámico (vibración)
        sigma_dinamico = self.sigma + (abs(real_ms2) * 0.1)
        ruido = np.random.normal(0, sigma_dinamico)

        medicion = real_ms2 + self.bias + ruido

        # el límite físico del MPU6050 en modo 16g
        # Si la aceleracion se pasa de los 16g el MPU devuelve uns señal plana, ya que paso su maximo de lectura
        return np.clip(medicion, -self.rango_mpu, self.rango_mpu)