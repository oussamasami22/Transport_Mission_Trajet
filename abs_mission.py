from abc import ABC, abstractmethod

class AbsMission(ABC):
    @abstractmethod
    def calculerCout(self):
        pass

    @abstractmethod
    def view(self, level=0):
        pass
