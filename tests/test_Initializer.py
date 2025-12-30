from Initializer import Initializer
from sensors.barometro import Barometro
from sensors.acelerometro import Acelerometro
from kalman import Kalman

def test_initializer():
    initializer = Initializer(desvio_baro=10, desvio_modelo=1, desvio_acel=2, iniciales=[0,0,0])
    b,a,k = initializer.instances()
    assert isinstance(b, Barometro)
    assert isinstance(a, Acelerometro)
    assert isinstance(k, Kalman)


