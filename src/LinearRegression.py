import numpy as np

def LinearRegression(tiempos, alturas, coeficientes):
    d = len(tiempos) - len(alturas)
    print(f"{tiempos}vs{alturas}")
    if d > 0:
        tiempos = tiempos[0:len(tiempos)-d]
    b1 = alturas @ tiempos
    b2 = np.sum(alturas)

    B = [b1,b2]

    return np.linalg.solve(coeficientes, B)

