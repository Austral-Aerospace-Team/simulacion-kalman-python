import pandas as pd
from DataReader import DataReader # Asumiendo que tu clase está en data_reader.py

def test_extraer_intervalo_debe_devolver_indices_correctos():
    reader = DataReader()
    # Preparamos datos de prueba (tiempos con deltas variables)
    tiempos = pd.Series([0.0, 0.12, 0.25, 0.38, 0.52, 0.70])


    inicio, fin = reader.extraer_intervalo(tiempos, 0.2, 0.6)

    assert inicio == 2
    assert fin == 4

    inicio2, fin2 = reader.extraer_intervalo(tiempos, 0.1, 0.65)

    assert inicio2 == 1
    assert fin2 == 5

    inicio3, fin3 = reader.extraer_intervalo(tiempos, 0, 0.7)

    assert inicio3 == 0
    assert fin3 == 5

def test_read_file():
    reader = DataReader()
    tiempos, altitudes, velocidades, aceleraciones, iniciales = reader.read(0, 92)
    assert tiempos[0]==0
    assert altitudes[0]==0
    assert velocidades[0] == 0
    assert aceleraciones[0] == 0
    assert iniciales[0] == 0
    assert tiempos[1]==0.005

    tiempos2, altitudes2, velocidades2, aceleraciones2, iniciales2 = reader.read(5, 11)
    assert iniciales2[0]==358.999
    assert iniciales2[1]==50.99





