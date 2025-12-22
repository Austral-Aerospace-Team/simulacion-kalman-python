import numpy as np

class Acelerometro:
    def __init__(self,
                 sigma_g=0.02,
                 bias_g=0.02):
        g = 9.81
        self.sigma = sigma_g * g   # m/s²
        self.bias  = bias_g  * g   # m/s²

    def lectura(self, real_ms2):
        return real_ms2 + self.bias + np.random.normal(0, self.sigma)
