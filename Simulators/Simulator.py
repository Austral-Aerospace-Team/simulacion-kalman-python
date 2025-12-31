from abc import ABC, abstractmethod

class Simulator(ABC):
    @abstractmethod
    def simulate(self, baro, acel, kal, tiempo, altitudes, velocidades, aceleraciones):
        pass
