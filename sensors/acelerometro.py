import numpy as np


class Acelerometro:
    def __init__(self, sigma_g=0.02, bias_g=0.02):
        g = 9.81
        self.sigma = sigma_g * g
        self.bias = bias_g * g
        self.g = g
        # El MPU6050 se puede setear en 2, 4, 8 o 16g.
        # Como el cohete llega a 140 m/s2 (14.3g), HAY usar el de 16g.
        self.rango_mpu = 16 * g

    def lectura(self, real_ms2):
        # Ruido dinámico (vibración)
        sigma_dinamico = self.sigma + (abs(real_ms2) * 0.1)
        ruido = np.random.normal(0, sigma_dinamico)

        medicion = real_ms2 + self.bias + ruido

        # el límite físico del MPU6050 en modo 16g
        # Si la aceleracion se pasa de los 16g el MPU devuelve uns señal plana, ya que paso su maximo de lectura
        return np.clip(medicion, -self.rango_mpu, self.rango_mpu)