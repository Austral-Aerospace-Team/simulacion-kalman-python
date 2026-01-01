from src.Initializer import Initializer
from src.sensors.barometro import Barometro
from src.sensors.acelerometro import Acelerometro
from src.kalman import Kalman

def test_initializer():
    initializer = Initializer(desvio_baro=10, desvio_modelo=1, desvio_acel=2, iniciales=[0,0,0])
    b,a,k = initializer.instances()
    assert isinstance(b, Barometro)
    assert isinstance(a, Acelerometro)
    assert isinstance(k, Kalman)


