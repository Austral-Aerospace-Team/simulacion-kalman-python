from src.sensors.barometro import Barometro
from src.sensors.acelerometro import Acelerometro
from src.kalman import Kalman
class Initializer:
    def __init__(self, iniciales=None, desvio_baro = 2, desvio_acel = 1, desvio_modelo = 1):
        if iniciales is None:
            iniciales = [0, 0, 0]
        self.desvio_baro = desvio_baro
        self.desvio_acel = desvio_acel
        self.desvio_modelo = desvio_modelo
        self.iniciales = iniciales
    def instances(self):
        return Barometro(self.desvio_baro), Acelerometro(self.desvio_acel), Kalman(self.desvio_modelo, self.desvio_baro, self.desvio_acel, self.iniciales)

