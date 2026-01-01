import numpy as np

class Kalman:

    def __init__(self, desvio_modelo, desvio_baro, desvio_acel, iniciales = None,  delta = 0.005):
        if iniciales is None:
            iniciales = [0,0,0]
        self.T = delta
        self.x = np.array(iniciales)
        self.z = np.array([0,0])
        self.model = np.array([[1,self.T, self.T**2/2],
                        [0,1,self.T],
                        [0,0,1]])
        self.H = np.array([[1,0,0],
                    [0,0,1]])
        self.R = np.array([[desvio_baro**2,0],
                           [0,desvio_acel**2]])
        self.Q = np.array([[desvio_modelo**2,0,0],
                           [0,desvio_modelo**2,0],
                           [0,0,desvio_modelo**2]])
        self.P = np.array([[0,0,0],
                           [0,0,0],
                           [0,0,10]])




    def iterate(self, s,v,a,zs,za):
        #PASO 1: PREDICT
        #predigo el estado
        xp = self.model @ self.x
        #predigo la covarianza
        Pp = self.model @ self.P @ self.model.T + self.Q

        #PASO 2: MEDICION
        self.z = np.array([zs,za])

        ##PASO 3:INNOVACION (Error)
        y = self.z - self.H @ xp

        ##PASO 4: GANANCIA DE KALMAN
        K = Pp @ self.H.T @ np.linalg.inv(self.H @ Pp @ self.H.T + self.R)

        ##PASO 5: CORRIJO ESTADOS
        self.x = xp + K @ y
        self.P = (np.identity(3) - K @ self.H) @ Pp
        result = (self.x[0], self.x[1], self.x[2])
        return xp, self.z, result


