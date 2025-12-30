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